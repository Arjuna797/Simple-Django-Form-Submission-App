from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the data: display success message or echo values
        response = f"Form submitted successfully!<br>Name: {name}<br>Email: {email}<br>Message: {message}"
        return HttpResponse(response)
    else:
        return render(request, 'index.html')
