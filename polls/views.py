from django.http import HttpRespose


def index(request):
    return HttpRespose("Hello,world. You're at the polls index.")
