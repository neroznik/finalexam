from django.contrib import admin

from webapp.models import MyUser, Message

admin.site.register(MyUser)
admin.site.register(Message)