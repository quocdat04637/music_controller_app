from django.urls import path
from .views import main, RoomView

urlpatterns = [
    path('', main),
    path('home', RoomView.as_view()),
]
