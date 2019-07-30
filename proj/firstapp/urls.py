from django.urls import path
from . import views
from .views import FirstappListView,FirstappCreateView,FirstappDetailView,FirstappUpdateView,FirstappDeleteView

urlpatterns = [
    path('',FirstappListView.as_view(),name="home"),
    path('firstapp/new',FirstappCreateView.as_view(),name="create"),    
    path('firstapp/<int:pk>/',FirstappDetailView.as_view(),name="detail"),
    path('firstapp/<int:pk>/update',FirstappUpdateView.as_view(),name="update"),
    path('firstapp/<int:pk>/delete',FirstappDeleteView.as_view(),name="delete"),
    path("about/",views.about,name="about"),
    path("login/",views.login,name="login"),
    path("add",views.add,name="add"),
    path("register/",views.register,name='register'),
    path("logout/",views.logout,name="logout")
]
