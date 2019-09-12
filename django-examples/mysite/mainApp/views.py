from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainApp/home.html')


def contact(request):
    return render(request, 'mainApp/contact.html', 
    {'values': ['Если у вас остались вопросы, то задавайте их мне по телефону', '(123-123-123)',
    'test@mail.ru']})
