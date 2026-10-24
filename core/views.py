from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        "home.html",
        {
            "title": "Головна сторінка",
            "text": "Це моя перша сторінка",
        }
    )

def about(request):
    return render(request,
                "about.html",
                {
                    "title": "Про проект",
                    "text": "Проект Django Aesthetic Medicine.",
                }
            )