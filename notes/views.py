from django.shortcuts import render, redirect
from .models import Note

def note_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(title=title, content=content)
        return redirect('note_list')
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'notes': notes})
