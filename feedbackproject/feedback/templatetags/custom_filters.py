# feedback/templatetags/custom_filters.py
from django import template
from feedback.models import Feedback

register = template.Library()

@register.filter
def average(item):
    feedbacks = Feedback.objects.filter(item=item)
    if feedbacks.exists():
        return sum(feedback.rating for feedback in feedbacks) / len(feedbacks)
    return 0  # Return 0 if no feedbacks exist
