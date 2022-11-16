from django.urls import path
from .views import HompageView

urlpatterns = [
    
    path("",HompageView,name="home"),
]
