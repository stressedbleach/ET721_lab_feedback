from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Feedback
from .forms import FeedbackForm

# View for the home page (e.g., a list of items)
def home(request):
    items = Item.objects.all()  # Get all items
    return render(request, 'feedback/home.html', {'items': items})

# View to show item details with feedback
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedback_list = Feedback.objects.filter(item=item)
    return render(request, 'feedback/item_detail.html', {'item': item, 'feedback_list': feedback_list})

# View to handle feedback submission
def submit_feedback(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.item = item  # Associate feedback with the item
            feedback.save()  # Save feedback after associating it with the item
            return redirect('item_detail', item_id=item.id)  # Redirect to item detail page after submission
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/submit_feedback.html', {'form': form, 'item': item})
