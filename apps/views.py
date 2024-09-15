from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import activate
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from apps.forms import ContactForm, BookingForm, ClickTransactionForm
from apps.models import Packages, Booking
from .models import ClickTransaction
from .utils import PyClickMerchantAPIView
from django.views.generic import ListView
from .forms import TripSearchForm


class IndexView(ListView):
    model = Packages
    template_name = 'index.html'
    context_object_name = 'package_list'


class AboutView(TemplateView):
    template_name = 'about.html'


class ServicesView(TemplateView):
    template_name = 'service.html'


class PackagesView(ListView):
    template_name = 'blog.html'
    model = Packages
    context_object_name = 'packages'


class PackageDetailView(DetailView):
    template_name = 'single.html'
    model = Packages
    context_object_name = 'package'


def set_language(request):
    next_url = request.GET.get('next', '/')
    lang_code = request.GET.get('language')

    if lang_code and lang_code in dict(settings.LANGUAGES):
        # Strip out the language code from the URL before translating the URL.
        for code, _ in settings.LANGUAGES:
            prefix = f'/{code}/'
            if next_url.startswith(prefix):
                next_url = next_url[len(prefix) - 1:]
                break

        # Activate the selected language
        activate(lang_code)
        # Append the selected language code to the URL
        next_url = f'/{lang_code}{next_url}'

    return HttpResponseRedirect(next_url)


class ContactModelFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('package-ordered')

    def form_valid(self, form):
        form.save()
        # send_to_email.delay([form.data.get('email')], form.data.get('first_name'))
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BookingFormView(FormView):
    model = Booking
    template_name = 'single.html'
    form_class = BookingForm
    success_url = reverse_lazy('package-ordered')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['packages'] = Packages.objects.all()
        return context


class PackageSearchView(ListView):
    model = Packages
    template_name = 'blog.html'
    context_object_name = 'packagings'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TripSearchForm(self.request.GET or None)

        if form.is_valid():
            destination = form.cleaned_data.get('destination')
            departure_time = form.cleaned_data.get('departure_time')
            return_time = form.cleaned_data.get('return_time')
            duration = form.cleaned_data.get('duration')

            if destination:
                queryset = queryset.filter(name__icontains=destination)
            if departure_time:
                queryset = queryset.filter(departure_time__gte=departure_time)
            if return_time:
                queryset = queryset.filter(return_time__lte=return_time)
            if duration:
                queryset = queryset.filter(duration=duration)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TripSearchForm(self.request.GET or None)
        return context


class CreateClickTransactionView(CreateView):
    model = ClickTransaction
    form_class = ClickTransactionForm
    template_name = 'payment.html'  # Replace with your template name

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.object = None

    def form_valid(self, form):
        # Save the form to create the ClickTransaction object
        self.object = form.save()

        # Generate the return URL and redirect URL
        return_url = "https://silkroute.uz"
        url = PyClickMerchantAPIView.generate_url(
            order_id=self.object.id, amount=str(self.object.amount), return_url=return_url
        )

        # Redirect to the generated URL
        return redirect(url)

class OrderedDetailView(TemplateView):
    template_name = 'ordered.html'
    queryset = Booking.objects.all()
    context_object_name = 'packagess'

class ShowView(TemplateView):
    template_name = 'example.html'

class UzbekistanCitiesView(TemplateView):
    template_name = 'uzbekistan_cities.html'

class KazakhstanCitiesView(TemplateView):
    template_name = 'kazakhstan_cities.html'

class TajikistanCitiesView(TemplateView):
    template_name = 'tajikistan_cities.html'

class KyrgyzstanCitiesView(TemplateView):
    template_name = 'kyrgyzstan_cities.html'