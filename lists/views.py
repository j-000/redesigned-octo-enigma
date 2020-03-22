from django.shortcuts import render


def home_page(request):
    if request.method == 'POST':
        return render(request, template_name='home.html', context={
            'new_item_text': request.POST.get('item_text', '')
        })
    return render(request, template_name='home.html')
