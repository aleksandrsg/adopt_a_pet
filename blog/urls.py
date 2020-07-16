from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments, name="comments"),
    path('comment', views.new_comment, name="new_comment"),
]