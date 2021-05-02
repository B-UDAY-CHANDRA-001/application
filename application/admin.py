from django.contrib import admin
from .models import JsonData
from .models import Upload

admin.site.register(JsonData)
# admin.site.register(Upload)

@admin.register(Upload)
class UploadModelAdmin(admin.ModelAdmin):
    list_display = ['UserName', 'Email', 'my_file']

# @admin.register(JsonData)
# class JsonModelAdmin(admin.ModelAdmin):
#     list_display = ['userId', 'id', 'title', 'body']
#
