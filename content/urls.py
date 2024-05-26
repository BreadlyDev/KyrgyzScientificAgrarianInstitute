from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.main, name='home'),
    path('about', v.about, name='about'),
    path('institute', v.institute, name='institute'),
]
