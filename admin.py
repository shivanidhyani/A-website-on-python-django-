from django.contrib import admin
from catalog.models import Product, Pencil, Ruraltourism, EcoSystem, Blog, Subscriber, Slideshow, Calender, Pen, Paper, Notepad, Farmermarket, Evolvinglives, Ruralshiksha, Ruralshikshagal, Womenempowerment, Virasat, Testimonial
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name','full_address']
    list_per_page = 10

class SlideshowAdmin(admin.ModelAdmin):
    list_display = ['id','caption','simg','slide']
    list_per_page = 10

class CalendarAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class PenAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class PaperAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class NotepadAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class PencilAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class RuraltourismAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class TestimonialAdmin(admin.ModelAdmin):
 list_display = ['id','image','credit','context']
 list_per_page = 10

class VirasatAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class EvolvinglivesAdmin(admin.ModelAdmin):
    list_display = ['id','Title','image','Description']
    list_per_page = 10

class FarmermarketAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class RuralshikshaAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class RuralshikshagalAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class WomenempowermentAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','Description']
    list_per_page = 10

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','Title','banner', 'created','blink']
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
admin.site.register(EcoSystem)
admin.site.register(Blog)
admin.site.register(Subscriber)
admin.site.register(Slideshow, SlideshowAdmin)
admin.site.register(Calender, CalendarAdmin)
admin.site.register(Pen, PenAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Pencil, PencilAdmin)
admin.site.register(Notepad, NotepadAdmin)
admin.site.register(Farmermarket, FarmermarketAdmin)
admin.site.register(Evolvinglives, EvolvinglivesAdmin)
admin.site.register(Ruralshiksha, RuralshikshaAdmin)
admin.site.register(Ruralshikshagal, RuralshikshagalAdmin)
admin.site.register(Womenempowerment, WomenempowermentAdmin)
admin.site.register(Virasat, VirasatAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Ruraltourism, RuraltourismAdmin)
# Register your models here.
