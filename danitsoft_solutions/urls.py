from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'incentives', views.IncentivesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
