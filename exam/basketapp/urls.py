from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:pk>/', basketapp.add_to_card, name='add_to_card'),
]
