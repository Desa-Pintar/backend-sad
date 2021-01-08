from rest_framework import routers

from .views import (
    SuratKelahiranViewSet,
    SuratSkckViewSet,
    SuratDomisiliViewSet,
    JenisPindahViewSet,
    KlasifikasiPindahViewSet,
    AlasanPindahViewSet,
    StatusKKTinggalViewSet,
    StatusKKPindahViewSet,
    SadKelahiranViewSet,
    SadKematianViewSet,
    SadLahirmatiViewSet,
    SadPindahKeluarViewSet,
    SadPindahMasukViewSet,
)

router = routers.DefaultRouter()

router.register(r"suratkelahiran", SuratKelahiranViewSet)
router.register(r"suratskck", SuratSkckViewSet)
router.register(r"domisili", SuratDomisiliViewSet)
router.register(r"jenispindah", JenisPindahViewSet)
router.register(r"klasifikasipindah", KlasifikasiPindahViewSet)
router.register(r"alasanpindah", AlasanPindahViewSet)
router.register(r"statuskktinggal", StatusKKTinggalViewSet)
router.register(r"statuskkpindah", StatusKKPindahViewSet)
router.register(r"kelahiran", SadKelahiranViewSet)
router.register(r"kematian", SadKematianViewSet)
router.register(r"lahirmati", SadLahirmatiViewSet)
router.register(r"pindahkeluar", SadPindahKeluarViewSet)
router.register(r"pindahmasuk", SadPindahMasukViewSet)
