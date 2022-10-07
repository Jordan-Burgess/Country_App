from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Country, Continent, Language


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
   template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class Countries(TemplateView):
   template_name = "country_list.html"

   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
        context["countries"] = Country.objects.filter(name__icontains=name)
        context["header"] = f"Searching for {name}"
    else:
        context["countries"] = Country.objects.all()
        context["header"] = "All Countries"
    return context

@method_decorator(login_required, name='dispatch')
class CountriesCreate(CreateView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "countries_create.html"
    
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class CountryDetail(DetailView):
    model = Country
    template_name = "country_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["languages"] = Language.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class CountryUpdate(UpdateView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "country_update.html"
    
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class CountryDelete(DeleteView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "country_delete_confirmation.html"
    success_url = "/countries/"

@method_decorator(login_required, name='dispatch')
class Continents(TemplateView):
   template_name = "continent_list.html"

   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["continents"] = Continent.objects.all()
    context["header"] = "All Continents"
    return context

@method_decorator(login_required, name='dispatch')
class ContinentDetail(DetailView):
    model = Continent
    template_name = "continent_countries.html"

@method_decorator(login_required, name='dispatch')
class CountryLanguageAssoc(View):
    def get(self, request, pk, language_pk):
        assoc = request.GET.get("assoc")
        if assoc == 'remove':
            Country.objects.get(pk=pk).languages.remove(language_pk)
        if assoc == 'add':
            Country.objects.get(pk=pk).languages.add(language_pk)
        return redirect('countries')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("countries")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)