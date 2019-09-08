from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'flights', views.FlightViewSet)
router.register(r'planes', views.PlaneViewSet)
router.register(r'tickets', views.TicketViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
