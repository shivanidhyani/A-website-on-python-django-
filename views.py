from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Slideshow, Blog, Pen, Pencil, Paper, Notepad, Calender, Ruralshiksha, Ruralshikshagal, Ruraltourism, Womenempowerment, Evolvinglives, Farmermarket, Virasat, Testimonial
def index(request):
    """View function for home page of site."""
    tests = Testimonial.objects.order_by('id')
    slides = Slideshow.objects.order_by('id')
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', {'slides' : slides, 'tests':tests})
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('user_details')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'login.html')
 
 
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return render(request,'logout.html')
 
 
def user_details(request):    
    user = get_object_or_404(User, id=request.user.id)    
    return render(request, 'user_details.html', {'user': user})

#Authentication View end
def privacy(request):
  return render(request, 'privacy.html')

def eys(request):
  return render(request, 'eys.html')

def home(request):
  return render(request, 'home.html')

def gfa(request):

    return render(request, 'gift-for-all.html')

def evcal(request):
        cal = Calender.objects.order_by('id')
        return render(request, 'evolve_calendar.html', {'cal': cal } )    

def evpen(request):
  pens = Pen.objects.order_by('id')
  return render(request, 'evolve_pen.html', {'pens' : pens} )

def evpaper(request):
  papers = Paper.objects.order_by('id')
  return render(request, 'evolve_paper.html', { 'papers': papers} )    

def evpencil(request):
  pencils = Pencil.objects.order_by('id')
  return render(request, 'evolve_pencil.html',{ 'pencils': pencils} ) 
def evnote(request):
  notepads = Notepad.objects.order_by('id')
  return render(request, 'evolve_notepad.html' , {'notepads' : notepads} )  
def evfm(request):
  fms = Farmermarket.objects.order_by('id')
  return render(request, 'Farmer%27s+Market+2017.html', { 'fms':fms})
def evrtm(request):
  rts = Ruraltourism.objects.order_by('id')
  return render(request, 'Evolve+Rural+Tourism.html', {'rts':rts})   
def eco(request):
  return render(request, 'eco-systems.html')
def ecoel(request):
  els = Evolvinglives.objects.order_by('id')
  return render(request, 'eco-systemsevolvingLives.html', { 'els': els} )    
def ecowe(request):
  wes = Womenempowerment.objects.order_by('id')
  return render(request, 'eco-systemswomenEmpowerment.html', { 'wes': wes})  
def ecors(request):
  rss = Ruralshiksha.objects.order_by('id')
  return render(request, 'eco-systemsruralShiksha.html', { 'rss': rss} )  
def blogs(request):
  blogs = Blog.objects.order_by('id')
  return render(request, 'blogs.html', { 'blogs': blogs} )  
   
def evrs(request):
  rssg = Ruralshikshagal.objects.order_by('id')
  return render(request, 'Evolve+Rural+Shiksha.html', { 'rssg' : rssg}) 
def evus(request):
          return render(request, 'Evolve+Urban+Shiksha.html')  
def ewed(request):
          return render(request, 'Evolve+World+Environment+Day.html') 
def vir(request):
  virs = Virasat.objects.order_by('id')
  return render(request, 'Evolve+Virasat.html', { 'virs': virs}) 
def us(request):
  slides = Slideshow.objects.order_by('id')
  return render(request, 'aboutus.html', { 'slides': slides} )   
def lg(request):
          return render(request, 'login.html')  
                                                               

          