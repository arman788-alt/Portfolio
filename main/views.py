from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactMessage,Education,Skill,Project


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect("home")

    education=Education.objects.all()
    skill=Skill.objects.all()
    project=Project.objects.all()
    

    return render(request, "main/home.html",
                  {
                      "education":education,
                      "skill":skill,
                      "project":project,

                  })