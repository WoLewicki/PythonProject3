from django.urls import include, path

urlpatterns = [
    path('home/', include('StackLike.urls'))
]