from django.urls import path

from webapp.views import IndexView, AddFriendView, DeleteFriendView, InboxView, SentView, MessageTextView, \
    MessageCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('sent/', SentView.as_view(), name='sent'),
    path('message/<int:pk>/', MessageTextView.as_view(), name='text_message'),
    path('message/add/', MessageCreateView.as_view(), name='message_create'),
    path('friends/<int:pk>/update/', AddFriendView.as_view(), name='add_friend'),
    path('friends/<int:pk>/delete/', DeleteFriendView.as_view(), name='delete_friend'),
]
