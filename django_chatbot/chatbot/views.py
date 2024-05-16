from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from .models import Chat

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

openai_api_key = "your_api_key_here"
openai.api_key = openai_api_key


def generate_image_url(image_prompt):
    response = openai.Image.create(prompt=image_prompt, n=1, size="1024x1024")
    url = response["data"][0]["url"]
    return url


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    answer = response.choices[0].message.content.strip()
    return answer


# Create your views here.
@login_required(login_url="/login")
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == "POST":
        message = request.POST.get("message")
        response = ask_openai(message)

        chat = Chat(
            user=request.user,
            message=message,
            response=response,
            created_at=timezone.now(),
        )
        chat.save()
        return JsonResponse({"message": message, "response": response})

    return render(request, "chatbot.html", {"chats": chats})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chatbot")

        else:
            error_message = "Invalid Credentials"
            return render(request, "login.html", {"error_message": error_message})

    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect("chatbot")
            except:
                error_message = "Username or Email already exists"
                return render(
                    request, "register.html", {"error_message": error_message}
                )
        else:
            error_message = "Passwords do not match"
            return render(request, "register.html", {"error_message": error_message})

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
