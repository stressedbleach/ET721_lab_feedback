# models.py
from django.db import models  # Make sure this import is here

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # Add this field if needed

    def __str__(self):
        return self.name

class Feedback(models.Model):
    item = models.ForeignKey(Item, related_name='feedback', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(null=True, blank=True)  # Add rating field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.item.name}"
