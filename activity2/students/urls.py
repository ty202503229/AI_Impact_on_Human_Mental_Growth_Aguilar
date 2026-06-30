from django.urls import path
from . import views

app_name = 'activity2'

urlpatterns = [
    # The main prediction form (e.g., http://127.0.0.1:8000/)
    path('', views.predict_view, name='predict'),
    
    # The history page (e.g., http://127.0.0.1:8000/history/)
    path('history/', views.history_view, name='history'),
]