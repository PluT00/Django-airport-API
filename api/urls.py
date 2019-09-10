from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from api import views


router = DefaultRouter()
router.register(r'flights', views.FlightViewSet)
router.register(r'planes', views.PlaneViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'users', views.UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi/', get_schema_view(
        title="Airport CRM",
        description="API for Airport CRM app"
        ), name="openapi-schema"),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name="swagger-ui")
]
