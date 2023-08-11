from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from .forms import ContactForm
from .models import AboutMe, Education, Experience, Skill, Profile


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutme'] = AboutMe.objects.all()
        context['education'] = Education.objects.all()
        context['experience'] = Experience.objects.all()
        context['profile'] = Profile.objects.all()

        return context


class HomePageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutme'] = AboutMe.objects.all()
        context['education'] = Education.objects.all()
        context['experience'] = Experience.objects.all()
        context['skills'] = Skill.objects.all()
        context['profile'] = Profile.objects.all()

        return context


class ContactPageView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }

        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur!</h2>")

        context = {
            "form": form
        }

        return render(request, 'contact.html', context)


