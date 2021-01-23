from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, TemplateView, CreateView
from django.urls import reverse

from webapp.forms import MessageForm
from webapp.models import Message

class InboxView(LoginRequiredMixin, ListView):
    template_name = 'inbox.html'
    context_object_name = 'message'
    paginate_by = 10
    paginate_orphans = 0
    model = Message
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=self.request.user
        message = Message.objects.filter(reciever = user.pk)
        context['message']=message
        return context

class SentView(LoginRequiredMixin, ListView):
    template_name = 'sent.html'
    context_object_name = 'message'
    paginate_by = 10
    paginate_orphans = 0
    model = Message
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = Message.objects.filter(sender = self.request.user)
        context['message'] = message
        return context


class MessageTextView (LoginRequiredMixin, TemplateView):
    template_name = 'message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        message = get_object_or_404(Message, pk=pk)
        context['message'] = message
        return context



class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'message_add.html'
    form_class = MessageForm


    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:sent', kwargs={'pk': self.object.pk})


