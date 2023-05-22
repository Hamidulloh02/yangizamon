from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("biz-haqimizda", views.AboutPageView.as_view(), name='about'),
    path("yangiliklar", views.BlogListView.as_view(), name='blog'),
    path("yangilik/<str:pk>", views.BlogDetailView.as_view(), name='single_blog'),
    path("shifokorlar", views.DoctorListView.as_view(), name='doctors'),
    path("kassalliklar", views.DiseaseListView.as_view(), name='disease'),
    path("kassallik/<str:pk>", views.DiseaseDetailView.as_view(), name='single_disease'),

]