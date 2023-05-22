from django.db import models

from ckeditor.fields import RichTextField
# from django.core.validators import FileExtensionValidator

class Bosh_sahifa(models.Model):
   title = models.CharField(max_length=520, unique=True)
   cover = models.ImageField(upload_to='images/', unique=True)
   class Meta:
     verbose_name_plural = "Bosh sahifa"

   def __str__(self):
      return self.title

class Biz_haqimizda(models.Model):
#   cover = models.ImageField(upload_to='images/', unique=True)
  title = models.CharField(max_length=255, unique=True)
  description = models.TextField(unique=True)
  info_1 = models.CharField(max_length=255, null=True, blank=True)
  info_2 = models.CharField(max_length=255, null=True, blank=True)
  info_3 = models.CharField(max_length=255, null=True, blank=True)
  info_4 = models.CharField(max_length=255, null=True, blank=True)
  info_5 = models.CharField(max_length=255, null=True, blank=True)
  info_6 = models.CharField(max_length=255, null=True, blank=True)

  class Meta:
     verbose_name_plural = "Biz haqimizda"

  def __str__(self):
      return self.title
  
class Yangiliklar(models.Model):
   cover = models.ImageField(upload_to='images/', unique=True)
   title = models.CharField(max_length=520, unique=True)
   description = RichTextField(unique=True)
   date = models.DateField(unique=True)
   class Meta:
     verbose_name_plural = "Yangiliklar"

   def __str__(self):
      return self.title

class Shifokorlar(models.Model):
   cover = models.ImageField(upload_to='images/', unique=True)
   name = models.CharField(max_length=255, unique=True)
   title = models.CharField(max_length=255, unique=True)
   class Meta:
     verbose_name_plural = "Shifokorlar"

   def __str__(self):
      return self.name
   
class Kassalliklar(models.Model):
   cover = models.ImageField(upload_to='images/', unique=True)
   title = models.CharField(max_length=520, unique=True)
   description = RichTextField(unique=True)
   date = models.DateField(unique=True)
   class Meta:
     verbose_name_plural = "Kassalliklar"

   def __str__(self):
      return self.title
   
class Tozalik(models.Model):
   title = models.CharField(max_length=520, unique=True)
   cover = models.ImageField(upload_to='images/', unique=True)
   class Meta:
     verbose_name_plural = "Tozalik Qoidalari"

   def __str__(self):
      return self.title
   
class Tavsifnoma(models.Model):
   name = models.CharField(max_length=520, unique=True)
   description = models.TextField(unique=True)
   class Meta:
     verbose_name_plural = "Tavsifnomalar"

   def __str__(self):
      return self.name

class Qarashlarimiz(models.Model):
   title = models.CharField(max_length=520, unique=True)
   description = models.TextField(unique=True)
   class Meta:
     verbose_name_plural = "Qarashlarimiz"

   def __str__(self):
      return self.title