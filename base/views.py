from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hitcount.views import HitCountDetailView
#pagination
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Bosh_sahifa.objects.all()
        context["news"] = Yangiliklar.objects.order_by('-id')[:3]
        context["clean"] = Tozalik.objects.all()
        context["tavsifnoma"] = Tavsifnoma.objects.all()
        context["shifokor"] = Shifokorlar.objects.all()

        return context

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Biz_haqimizda.objects.all()
        context["qarashlar"] = Qarashlarimiz.objects.all()
        return context

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise

class BlogListView(ListView):
    model = Yangiliklar
    template_name = "pages/blog.html"
    paginate_by = 4
    paginator_class = MyPaginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        yangiliklar = Yangiliklar.objects.all()
        paginator = self.paginator_class(yangiliklar, self.paginate_by)

        yangiliklar = paginator.page(page)
        context["data"] = yangiliklar
        context["news"] = Yangiliklar.objects.order_by('-id')[:3]

        return context


    

class BlogDetailView(HitCountDetailView):
    model = Yangiliklar
    template_name = "pages/blog-single.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Yangiliklar.objects.get()
        context["news"] = Yangiliklar.objects.order_by('-id')[:3]

        return context

class DoctorListView(ListView):
    model = Shifokorlar
    template_name = "pages/doctors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Shifokorlar.objects.all()

        return context


class DiseaseListView(ListView):
    model = Kassalliklar
    template_name = "pages/disease.html"
    paginate_by = 4
    paginator_class = MyPaginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        kasalliklar = Kassalliklar.objects.all()
        paginator = self.paginator_class(kasalliklar, self.paginate_by)

        yangiliklar = paginator.page(page)
        context["data"] = kasalliklar
        context["news"] = Kassalliklar.objects.order_by('-id')[:3]

        return context


class DiseaseDetailView(HitCountDetailView):
    model = Kassalliklar
    template_name = "pages/disease-single.html"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Kassalliklar.objects.get()
        context["news"] = Kassalliklar.objects.order_by('-id')[:3]

        return context
