from django.urls import path, include
from rest_framework import routers

from videos.views import VideoViewset

router = routers.SimpleRouter()
router.register(r'videos', VideoViewset)
urlpatterns = router.urls
