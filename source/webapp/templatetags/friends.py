from django import template

register = template.Library()

@register.filter()
def add_friend(obj,user):
    return obj.add_friend_by_user(user)