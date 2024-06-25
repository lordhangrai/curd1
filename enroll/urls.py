from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>', views.update_data, name="updatedata"),
    path('home',views.HomeView.as_view(), name='home'),
    path('/<int:pk>/', views.CandidateView.as_view(), name='candidate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)