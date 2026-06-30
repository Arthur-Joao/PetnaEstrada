from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]