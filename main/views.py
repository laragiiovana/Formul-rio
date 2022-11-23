from django.shortcuts import render
from .forms import InscricaoForm

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST) 
        if form.is_valid():
            form.save()
            form = InscricaoForm()
    else:
        form = InscricaoForm()

    return render(request,'form.html', { 'form' : form})