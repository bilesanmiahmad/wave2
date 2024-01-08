from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from people.views import PeopleView


router = routers.DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path("contact/", PeopleView.as_view()),
    path('admin/', admin.site.urls),
    path('docs/', SpectacularAPIView.as_view(), name='schema'), # To download the yaml schema for the api documentation
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # To view the API documentation in swagger interface
]
