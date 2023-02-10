from django.http import HttpResponse
from django.shortcuts import render
# from .models import User
# from .forms import MyForm

# def reg_form(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = MyForm()
#         return render(request, 'register.html', {'form': form})

def reg_form(request):
    return HttpResponse('<h1>hi<h1>')

