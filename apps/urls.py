from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.views import IndexView, AboutView, ServicesView, PackagesView, PackageDetailView, ContactModelFormView, \
    BookingFormView, PackageSearchView, CreateClickTransactionView, OrderedDetailView, ShowView, UzbekistanCitiesView, \
    KazakhstanCitiesView, TajikistanCitiesView, KyrgyzstanCitiesView, Payment

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('uzbekistan-cities/', UzbekistanCitiesView.as_view(), name='uzbekistan_cities'),
    path('kazakhstan-cities/', KazakhstanCitiesView.as_view(), name='kazakhstan_cities'),
    path('tajikistan-cities/', TajikistanCitiesView.as_view(), name='tajikistan_cities'),
    path('kyrgyzstan-cities/', KyrgyzstanCitiesView.as_view(), name='kyrgyzstan_cities'),
    path('services', ServicesView.as_view(), name='services'),
    path('packages', PackagesView.as_view(), name='packages'),
    path('packages/<str:slug>', PackageDetailView.as_view(), name='package-detail'),
    path('ordered', OrderedDetailView.as_view(), name='package-ordered'),
    path('contact', ContactModelFormView.as_view(), name='contact'),
    path('booking', BookingFormView.as_view(), name='booking'),
    path('search', PackageSearchView.as_view(), name='trip-search'),
    path("process/click/transaction/", csrf_exempt(Payment.as_view()), name='payment'),
    path('example', ShowView.as_view(), name='example'),
]


# strukturani o'zgartiramiz
# ruschani o'zgartirish
# language bittalik bo'lsin +
# package tepaga ko'tarilsin +
# about us ni o'rniga dolores ni kiga o'xshagan razdel "" bo'lsin
# email ni pastga qo'yib qoyamiz
# nomer o'zgaradi 90 919 22 20+
# 77 777 78 90 +
# whatsapp 90 919 22 20 +
# text ni orasida bo'shliq qolmasin +
# blog detail kerak emas