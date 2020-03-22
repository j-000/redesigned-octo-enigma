from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    return render(request, template_name='home.html')


def view_list(request):
    return render(request,
                  template_name='list.html',
                  context={'items': Item.objects.all()}
                  )


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
