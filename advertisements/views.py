from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementModelForm
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse


def index(request):
    advertisements = Advertisement.objects.all()

    context = {
        "advertisements": advertisements
    }

    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def post_adv(request: WSGIRequest):
    if request.method == 'POST':
        form = AdvertisementModelForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse("main-page")
            )
        else:
            print(form.errors)

    else:
        form = AdvertisementModelForm()
    form = AdvertisementModelForm()
    context = {"form": form}
    return render(request, 'advertisement-post.html', context)