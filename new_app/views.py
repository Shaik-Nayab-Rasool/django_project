from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    print('Hi iam View')
    return HttpResponse('Welcome Home!')

# backend -> render
# database -> aiven