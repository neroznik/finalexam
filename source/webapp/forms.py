from django import forms
from webapp.models import MyUser, Message

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = []

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['created_at', 'sender']

