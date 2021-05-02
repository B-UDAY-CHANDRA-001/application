from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UploadForm, JDataForm
from django.contrib import messages
from .models import Upload,JsonData


def home(request):
    return render(request, 'application/home.html')


def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Account created for' + username)
            login(request, user)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
def index(request):
    return render(request, 'application/index.html')





def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Uploaded file Sucessfully!!")
            return render(request, "application/upload.html", {'form': form})


    else:
        form = UploadForm()

        data = Upload.objects.all()
        return render(request, 'application/upload.html', {'form': form, 'data': data})






def filedata(request):
    try:
         data = Upload.objects.all()
         return render(request, "application/filedata.html", {'data': data})
    except:
        pass
def jdata(request):
    with open('media/doc/data_4_3.json') as jfile:

        print(type(jfile))
        jfile = jfile.read()
        values = eval(jfile)
    data = JsonData.objects.all()

    return render(request, "application/jdata.html", {'data': data, 'values': values})



