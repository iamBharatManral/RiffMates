from django.http import HttpResponse, JsonResponse


def credits(request):
    content = "Bharat\nYour Name"
    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = r"<html><body><h1>About</h1></body></html>"
    return HttpResponse(content, content_type="text/html")


def version_info(request):
    version_info = {
       "version": "0.1.0"
    }
    return JsonResponse(version_info)