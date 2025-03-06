from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path("like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path('comment/<int:pk>/', views.CommentView.as_view(), name='comment')

]
