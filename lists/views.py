from django.http import HttpResponse


def home_page(request):
    html = """<html>
                <title>To-do lists</title>
            </html>"""
    return HttpResponse(html)
