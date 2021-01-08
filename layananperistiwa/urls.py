from rest_framework import routers

from .views import (
    SuratKelahiranViewSet,
    SuratSkckViewSet,
    SuratDomisiliViewSet,
)

router = routers.DefaultRouter()

router.register(r"suratkelahiran", SuratKelahiranViewSet)
router.register(r"suratskck", SuratSkckViewSet)
router.register(r"domisili", SuratDomisiliViewSet)
