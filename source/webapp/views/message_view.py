# if self.request.user.is_authenticated:
#     context = super().get_context_data(**kwargs)
#     user = self.request.user
#     myuser = MyUser.objects.filter(user=user)
#     context['user'] = myuser
#     return context
