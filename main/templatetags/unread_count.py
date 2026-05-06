from django import template
from main.models import Notification

register = template.Library()

@register.simple_tag
def get_unread_count(user):
    """Return the number of unread notifications for the given user."""
    if not user or not user.is_authenticated:
        return 0
    return Notification.objects.filter(user=user, is_read=False).count()
