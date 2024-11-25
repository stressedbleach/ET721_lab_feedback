from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),  # Item detail page
    path('item/<int:item_id>/feedback/', views.submit_feedback, name='submit_feedback'),  # Feedback submission page
]
