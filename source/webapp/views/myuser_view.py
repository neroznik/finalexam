from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View

from webapp.models import MyUser


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'myuser'
    paginate_by = 10
    paginate_orphans = 0
    model = get_user_model()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddFriendView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user= self.request.user
        friend = get_object_or_404 (get_user_model(), pk=kwargs.get('pk'))
        if user != friend:
            user.friends.add(friend)
            return HttpResponse('Пользователь добавлен в друзья')
        else:
            return Http404 ('Нельзя добавить себя')

class DeleteFriendView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        user = self.request.user
        friend = get_object_or_404(get_user_model(), pk=kwargs.get('pk'))
        if user != friend:
            user.friends.remove(friend)
            return HttpResponse('Пользователь удален из друзей')
        else:
            return Http404 ('Нельзя удалить себя')