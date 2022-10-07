from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Country, Continent, Language


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
   template_name = "about.html"

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

class CountriesCreate(CreateView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "countries_create.html"
    
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})

class CountryDetail(DetailView):
    model = Country
    template_name = "country_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["languages"] = Language.objects.all()
        return context

class CountryUpdate(UpdateView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "country_update.html"
    
    def get_success_url(self):
        return reverse('country_detail', kwargs={'pk': self.object.pk})

class CountryDelete(DeleteView):
    model = Country
    fields = ['name', 'image', 'flag', 'info', 'population', 'continent']
    template_name = "country_delete_confirmation.html"
    success_url = "/countries/"

class Continents(TemplateView):
   template_name = "continent_list.html"

   def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["continents"] = Continent.objects.all()
    context["header"] = "All Continents"
    return context

class ContinentDetail(DetailView):
    model = Continent
    template_name = "continent_countries.html"

class CountryLanguageAssoc(View):
    def get(self, request, pk, language_pk):
        assoc = request.GET.get("assoc")
        if assoc == 'remove':
            Country.objects.get(pk=pk).languages.remove(language_pk)
        if assoc == 'add':
            Country.objects.get(pk=pk).languages.add(language_pk)
        return redirect('countries')