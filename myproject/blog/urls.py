from django.urls import path
from .views import home, detail
app_name = "blog"
urlpatterns = [
    path('blog', home, name="home"),
    path('detail/<slug:slug>', detail, name="detail")
]
