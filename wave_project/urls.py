from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from people.views import PeopleView

router = routers.DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path("contact/", PeopleView.as_view()),
    path('admin/', admin.site.urls),
]
