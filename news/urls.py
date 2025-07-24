from django.urls import path


from .views import new_list

urlpatterns = [
    path("",new_list,name="news_list"),
]