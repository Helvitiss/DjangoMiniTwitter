from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path("like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path('comment/<int:pk>/', views.CommentView.as_view(), name='comment'),
    path("search/", views.search, name="search")

]
