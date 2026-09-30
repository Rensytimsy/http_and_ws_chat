from django.shortcuts import render
from rest_framework import response, status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
# from django.http import response

# Create your views here.

# @login_required(login_url="login/")
def chatView(request):
    return render(request, "chat_page.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            
            # response[""]
            response.Response({
                "message": "authenticated"
            }, status=status.HTTP_200_OK)
            
        else:
             return render(request,  "login_form.html", {"form": form})
         
         
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def chat_page(request):
    
    return render(request, "chat/index.html")

def chat_room(request, room_name):
    
    return render(request, "chat/room.html", {"room_name": room_name})


