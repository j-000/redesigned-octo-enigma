from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, template_name='home.html')


def view_list(request):
    return render(request,
                  template_name='list.html',
                  context={'items': Item.objects.all()}
                  )