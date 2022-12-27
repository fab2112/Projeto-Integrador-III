# paginas/urls.py
from django.urls import path
from .views import HomePageView, sobrenosView, dashboardView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sobrenos', sobrenosView.as_view(), name='sobrenos'),
    path('dashboard', dashboardView.as_view(), name='dashboard'),
]

