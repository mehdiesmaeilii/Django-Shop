from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,unique=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home:category_filter',args=[self.slug,])
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name= models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,unique=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d/')
    description=models.TextField()
    price=models.IntegerField()
    available=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home:product_detail',args=[self.slug,])
