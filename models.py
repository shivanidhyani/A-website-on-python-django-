from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.core.validators import URLValidator
import uuid # Required for unique book instances

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Product(models.Model):
    """Model representing an author."""
    Product_Category = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Img = models.ImageField()
    Price = models.IntegerField()
    Created = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Product-detail', args=[str(self.id)])

    def full_address(self):
        return format_html('%s - <b>%s,%s</b>,%s</b>,%s</b>,%s</b>,' % (self.id,self.Product_Category,self.Name,self.Img,self.Price,self.Created))

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}, {self.Product_Category}, {self.Name}, {self.Img}, {self.Price}, {self.Created}'               

class EcoSystem(models.Model):
    """Model representing an author."""
    EcoSystem_Type = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Img = models.ImageField()
    Created = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('EcoSystem-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}, {self.EcoSystem_Type}, {self.Title}, {self.Img}, {self.Created}'           

class Blog(models.Model):
    """Model representing an author."""
    Title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='blogs')
    created = models.DateField(null=True, blank=True)
    blink = models.URLField(max_length=100,blank=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Blog-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.banner, self.Title, self.created, self.blink}' 

class Subscriber(models.Model):
    """Model representing an author."""
    Email = models.EmailField(max_length=70,blank=True)
    Subscribed_on = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Subscriber-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}, {self.Email}, {self.Subscribed_on}'        

class Slideshow(models.Model):
    """docstring for Slideshow"""
    simg = models.ImageField(upload_to='slideshow')
    caption = models.CharField(max_length=100)
    slide = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f'{self.id,self.caption,self.simg,self.slide}'
        
class Calender(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='calender')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Pen(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='pen')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Paper(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='paper')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Pencil(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='pencil')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'
        
class Notepad(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='notepad')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Farmermarket(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='farmermarket')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Evolvinglives(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='evolvinglives')
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.Title, self.Description, self.image}'

class Ruralshiksha(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='ruralshiksha')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Ruralshikshagal(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='ruralshikshagal')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Ruraltourism(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='ruralshiksha')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Womenempowerment(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='womenempowerment')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'


class Gallery(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='gallery')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Virasat(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='virasat')
    caption = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return f'{self.id,self.caption,self.image,self.Description}'

class Testimonial(models.Model):
    """docstring for Slideshow"""
    image = models.ImageField(upload_to='testimonials')
    context = models.CharField(max_length=1000)
    credit = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.image, self.context, self.credit}'
