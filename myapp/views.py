from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import SignUpForm
from .tokens import account_activation_token

from .models import *

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Votre inscription sur Esearch'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/account_activation_invalid.html')

# @login_required
def home(request):
    return render(request, 'pages/home.html', {'annonces': Annonces.objects.all()})

def concours1(request):
    return render(request, 'pages/Concours.html', {'Concours': Concours_Services_de_lEtat.objects.all()})

def concours2(request):
    return render(request, 'pages/Concours.html', {'Concours': Concours_Etablissements_Entreprises_publics.objects.all()})

def concours3(request):
    return render(request, 'pages/Concours.html', {'Concours': Concours_Collectivites_territoriales.objects.all()})

def emplois_sup(request):
    return render(request, 'pages/Emplois_superieurs.html', {'Emplois_sup': Emplois_superieurs.objects.all()})

def postes1(request):
    return render(request, 'pages/Postes_Services_de_lEtat.html', {'Postes': Postes_Services_de_lEtat.objects.all()})

def postes2(request):
    return render(request, 'pages/Postes_Etablissements_Entreprises_publics.html', {'Postes': Postes_Etablissements_Entreprises_publics.objects.all()})

def postes3(request):
    return render(request, 'pages/Postes_Provinces_et_prefectures.html', {'Postes': Postes_Provinces_et_prefectures.objects.all()})

def contact(request):
    return render(request, 'pages/contact.html')


def handler404(request):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, 'errors/500.html', {}, status=500)
