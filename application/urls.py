from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    # path('login/',auth_view.LoginView.as_view(template_name = 'registration/login.html'),name = 'login'),
    path('accounts/logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('upload/accounts/logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('filedata/', views.filedata),
    path('upload/', views.upload),
    path('application/filedata', views.filedata, name='filedata'),
    path('application/jdata', views.jdata, name='jdata')
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


