"""My_test_server_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = []

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', views.reviews, name = 'reviews'),
    path('reverse/', views.reverse, name = 'reverse'),
    path('', views.main),
    path('first_quest/', views.first_quest, name = 'first_quest'),
    path('log_in/', views.login, name = 'login'),
    path('registration_check/', views.registration_check, name = 'registration_check'),
    path('profile_user/', views.profile_user, name = 'profile_user'),
    path('login_check/', views.login_check, name = 'login_check'),
    path('quit_profile/', views.quit_profile, name = 'quit_profile'),
    path('start_game/', views.start_game, name = 'start_game'),
    path('quest2/', views.quest_number_two, name = 'quest_number_two'),
    path('exactly_the_end/', views.exactly_the_end, name = 'exactly_the_end'),
    path('end_game/', views.end_game, name = 'end_game'),
    path('last_warning/', views.last_warning, name = 'last_warning'),
    path('happy_end/', views.happy_end, name = 'happy_end')


]
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)