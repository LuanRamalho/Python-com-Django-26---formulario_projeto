from django.shortcuts import render, redirect
from .forms import FormularioForm

def enviar_formulario(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = FormularioForm()
    return render(request, 'formulario/formulario.html', {'form': form})

def sucesso(request):
    return render(request, 'formulario/sucesso.html')
