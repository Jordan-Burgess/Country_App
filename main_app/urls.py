from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('countries/', views.Countries.as_view(), name="countries"),
    path('countries/new', views.CountriesCreate.as_view(), name="countries_create"),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name="country_detail"),
    path('countries/<int:pk>/update', views.CountryUpdate.as_view(), name="country_update"),
    path('countries/<int:pk>/delete', views.CountryDelete.as_view(), name="country_delete"),
    path('continents/', views.Continents.as_view(), name="continents"),
    path('continents/<int:pk>/', views.ContinentDetail.as_view(), name="continent_detail"),
    path('countries/<int:pk>/languages/<int:language_pk>/', views.CountryLanguageAssoc.as_view(), name="country_language_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]