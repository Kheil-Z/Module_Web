from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Article, Contact
from .forms import ContactForm, ArticleForm, NouveauContactForm


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request,'base.html')

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def view_article(request, id_article):
    if id_article > 100:
        raise Http404
    return redirect(view_redirection)

def list_articles(request, year, month=1,):
    return redirect("https.djangoproject.com")#HttpResponse('Articles de %s/%s' % (year, month))

def date_acteulle(request):
    return render(request,'blog/date.html',{'date':datetime.now()})

def addition(request,nombre1,nombre2):
    total = nombre1+nombre2
    return render(request,'blog/addition.html',locals())


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

# def new_article(request):
#     form = ArticleForm(request.POST, instance=article)
#     if form.is_valid():
#         form.save()

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    return render(
        request,
        'blog/voir_contacts.html',
        {'contacts': Contact.objects.all()}
    )