from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
import json

AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"

def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False

class AddView(View):
    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01+num02)

    def get(self, request):
        print(request.headers)
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        print("Num01", num01)
        return HttpResponse(num01 + num02)

class SubView(View):
    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01 - num02)


    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        AddView

        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 - num02)


class DivView(View):
    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)

    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)



class MultiView(View):
    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01 * num01)


    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 * num02)
