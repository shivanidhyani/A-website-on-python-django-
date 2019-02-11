from django.urls import path
from . import views


urlpatterns = [
				path('', views.index, name='index'),
				path('gfa',views.gfa, name='gfa'),
				path('evcal',views.evcal, name='evcal'),
				path('evpen',views.evpen, name='evpen'),
				path('evpaper',views.evpaper, name='evpaper'),
				path('evpencil',views.evpencil, name='evpencil'),
				path('evnote',views.evnote, name='evnote'),
				path('evrtm',views.evrtm, name='evrtm'),
				path('eco',views.eco, name='eco'),
				path('ecoel',views.ecoel, name='ecoel'),
				path('ecowe',views.ecowe, name='ecowe'),
				path('ecors',views.ecors, name='ecors'),
				path('blogs',views.blogs, name='blogs'),
				path('evrs',views.evrs, name='evrs'),
				path('evus',views.evus, name='evus'),
				path('ewed',views.ewed, name='ewed'),
				path('vir',views.vir, name='vir'),
				path('evfm',views.evfm, name='evfm'),
				path('us',views.us, name='us'),
				path('lg',views.lg, name='login'),
				path('login/', views.login, name='login'),
    			path('logout/', views.logout, name='logout'),
    			path('userdetails/', views.user_details, name='user_details'),
    			path('eys/', views.eys, name='eys'),
    			path('privacy/', views.privacy, name='privacy'),
    			#path('story/', views.story, name='story'),
]

