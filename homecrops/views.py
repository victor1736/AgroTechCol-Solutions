from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render(request, 'homecrops/index.html')

def nosotros(request):
    return render(request, 'homecrops/nosotros.html')

def portafolio(request):
    return render(request, 'homecrops/portafolio.html')

def ceo(request):
    return render(request, 'homecrops/ceo.html')

def contacto(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        affair = request.POST.get('affair')
        message = request.POST.get('message')

        # Lógica para enviar el correo electrónico
        subject = f"Nuevo mensaje de contacto de {name}"
        message = f"""
            Nombre: {name}
            Correo Electrónico: {email}
            Número de Teléfono: {phone}
            Asunto: {affair}
            Mensaje: {message}
        """
        send_mail(subject, message, email, ['cropsfernandez@gmail.com'])

        return render(request, 'homecrops/index.html', {'mensaje_enviado': True})

    return render(request, 'homecrops/contacto.html')
    

