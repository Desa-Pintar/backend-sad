from datetime import datetime

from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField


from api_sad_sig.util import (
    CustomSerializer,
)
from v1.models import SadPenduduk
from v1.serializers import SadPendudukMiniSerializer
from .models import LayananSurat, SadKematian
from .serializers import SadKematianSuratSerializer


class ListSuratSerializer(CustomSerializer):
    pemohon = DynamicRelationField(
        "v1.serializers.SadPendudukMiniSerializer", source="penduduk"
    )

    class Meta:
        model = LayananSurat
        name = "data"
        exclude = [
            "atribut",
            "jenis",
            "created_by",
            "created_at",
            "deleted_by",
            "deleted_at",
            "updated_by",
            "updated_at",
        ]


class BaseAdminSuratSerializer(CustomSerializer):
    pemohon = DynamicRelationField(
        "v1.serializers.SadPendudukMiniSerializer", source="penduduk"
    )

    def create(self, data):
        surat = LayananSurat(jenis=self.Meta.jenis_surat, **data)
        if not data.get("atribut"):
            surat.atribut = {}
        surat.save()
        return surat

    class Meta:
        model = LayananSurat
        name = "data"
        exclude = [
            "penduduk",
            "desa",
            "jenis",
            "created_by",
            "created_at",
            "deleted_by",
            "deleted_at",
            "updated_by",
            "updated_at",
        ]


class BasePendudukSuratSerializer(CustomSerializer):
    def create(self, data):
        print(data)
        surat = LayananSurat(jenis=self.Meta.jenis_surat, **data)
        surat.save()
        return surat

    class Meta:
        model = LayananSurat
        name = "data"
        exclude = [
            "pegawai",
            "penduduk",
            "jenis",
            "created_by",
            "created_at",
            "deleted_by",
            "deleted_at",
            "updated_by",
            "updated_at",
        ]


class AtributSKCK(serializers.Serializer):
    keperluan = serializers.CharField(required=False)
    keterangan = serializers.CharField(required=False)


class AdminSKCKSerializer(BaseAdminSuratSerializer):
    atribut = AtributSKCK()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "skck"


class PendudukSKCKSerializer(BasePendudukSuratSerializer):
    atribut = AtributSKCK()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "skck"


class AtributDomisili(serializers.Serializer):
    keperluan = serializers.CharField()


class AdminDomisiliSerializer(BaseAdminSuratSerializer):
    atribut = AtributDomisili()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "domisili"


class PendudukDomisiliSerializer(BasePendudukSuratSerializer):
    atribut = AtributDomisili()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "domisili"


class AtributUsaha(serializers.Serializer):
    nama_usaha = serializers.CharField()


class AdminUsahaSerializer(BaseAdminSuratSerializer):
    atribut = AtributUsaha()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "usaha"


class PendudukUsahaSerializer(BasePendudukSuratSerializer):
    atribut = AtributUsaha()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "usaha"


class AtributRapidTest(serializers.Serializer):
    tempat_rapid_test = serializers.CharField()


class AdminRapidTestSerializer(BaseAdminSuratSerializer):
    atribut = AtributRapidTest()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class PendudukRapidTestSerializer(BasePendudukSuratSerializer):
    atribut = AtributRapidTest()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class AdminKetPendudukSerializer(BaseAdminSuratSerializer):
    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class PendudukKetPendudukSerializer(BasePendudukSuratSerializer):
    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class AdminTempatTinggalSerializer(BaseAdminSuratSerializer):
    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "ktt"
        exclude = BaseAdminSuratSerializer.Meta.exclude + ["atribut"]


class PendudukTempatTinggalSerializer(BasePendudukSuratSerializer):
    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "ktt"
        exclude = BaseAdminSuratSerializer.Meta.exclude + ["atribut"]


class AtributLuarDaerah(serializers.Serializer):
    nama_daerah = serializers.CharField()
    jenis_perjalanan = serializers.CharField()
    jenis_rangka_perjalanan = serializers.CharField()


class AdminLuarDaerahSerializer(BaseAdminSuratSerializer):
    atribut = AtributLuarDaerah()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "kld"


class PendudukLuarDaerahSerializer(BasePendudukSuratSerializer):
    atribut = AtributLuarDaerah()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "kld"


class AtributKetSiswaTidakMampu(serializers.Serializer):
    orangtua_id = serializers.IntegerField()
    orangtua = serializers.SerializerMethodField()

    def get_orangtua(self, obj):
        penduduk = SadPenduduk.objects.get(pk=obj["orangtua_id"])
        return SadPendudukMiniSerializer(penduduk).data


class AdminKetSiswaTidakMampuSerializer(BaseAdminSuratSerializer):
    atribut = AtributKetSiswaTidakMampu()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "sktm"


class PendudukKetSiswaTidakMampuSerializer(BasePendudukSuratSerializer):
    atribut = AtributKetSiswaTidakMampu()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "sktm"


class AdminBelumMenikahSerializer(BaseAdminSuratSerializer):
    atribut = AtributKetSiswaTidakMampu()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "belummenikah"


class PendudukBelumMenikahSerializer(BasePendudukSuratSerializer):
    atribut = AtributKetSiswaTidakMampu()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "belummenikah"


class AtributSuratPenguburan(serializers.Serializer):
    nama_jenazah = serializers.CharField()
    tanggal_penguburan = serializers.DateField()
    tanggal = serializers.SerializerMethodField()

    def get_tanggal(self, obj):
        return datetime.strptime(obj["tanggal_penguburan"], "%Y-%m-%d")


class AdminSuratPenguburanSerializer(BaseAdminSuratSerializer):
    atribut = AtributSuratPenguburan()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "penguburan"


class PendudukSuratPenguburanSerializer(BasePendudukSuratSerializer):
    atribut = AtributSuratPenguburan()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "penguburan"


class AtributPelakuPerikananSerializer(serializers.Serializer):
    orangtua_id = serializers.IntegerField()
    orangtua = serializers.SerializerMethodField()
    keperluan = serializers.CharField()

    def get_orangtua(self, obj):
        penduduk = SadPenduduk.objects.get(pk=obj["orangtua_id"])
        return SadPendudukMiniSerializer(penduduk).data


class AdminPelakuPerikananSerializer(BaseAdminSuratSerializer):
    atribut = AtributPelakuPerikananSerializer()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "ketnelayan"


class PendudukPelakuPerikananSerializer(BasePendudukSuratSerializer):
    atribut = AtributPelakuPerikananSerializer()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "ketnelayan"


# Template not made yet
class AtributPernyataanKebenaranData(serializers.Serializer):
    keperluan = serializers.CharField(default="Seleksi Perguruan Tinggi")


class AdminPernyataanKebenaranSerializer(BaseAdminSuratSerializer):
    atribut = AtributPernyataanKebenaranData()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "spkd"


class PendudukPernyataanKebenaranSerializer(BasePendudukSuratSerializer):
    atribut = AtributPernyataanKebenaranData()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "spkd"


class AtributKelahiran(serializers.Serializer):
    kelahiran_id = serializers.IntegerField()


class AdminSuratKelahiranSerializer(BaseAdminSuratSerializer):
    atribut = AtributKelahiran()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "kelahiran"


class PendudukSuratKelahiranSerializer(BasePendudukSuratSerializer):
    atribut = AtributKelahiran()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "kelahiran"


class AtributKematian(serializers.Serializer):
    kematian_id = serializers.IntegerField()
    kematian = serializers.SerializerMethodField()

    def get_kematian(self, obj):
        inst = SadKematian.objects.get(pk=obj["kematian_id"])
        return SadKematianSuratSerializer(inst).data


class AdminSuratKematianSerializer(BaseAdminSuratSerializer):
    atribut = AtributKematian()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "kematian"


class PendudukSuratKematianSerializer(BasePendudukSuratSerializer):
    atribut = AtributKematian()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "kematian"


serializer_list = {
    "kematian": (
        AdminSuratKematianSerializer,
        PendudukSuratKematianSerializer,
        "Surat Keterangan Kematian",
    ),
    "ketnelayan": (
        AdminPelakuPerikananSerializer,
        PendudukPelakuPerikananSerializer,
        "Surat Keterangan Pelaku Perikanan",
    ),
    "penguburan": (
        AdminSuratPenguburanSerializer,
        PendudukSuratPenguburanSerializer,
        "Surat Keterangan Penguburan",
    ),
    "skck": (
        AdminSKCKSerializer,
        PendudukSKCKSerializer,
        "Surat Keterangan Kelakuan Baik",
    ),
    "domisili": (
        AdminDomisiliSerializer,
        PendudukDomisiliSerializer,
        "Surat Keterangan Domisili",
    ),
    "rapidtest": (
        AdminRapidTestSerializer,
        PendudukRapidTestSerializer,
        "Surat Pengantar Rapid Test",
    ),
    "ket_penduduk": (
        AdminKetPendudukSerializer,
        PendudukKetPendudukSerializer,
        "Surat Keterangan Penduduk",
    ),
    "ktt": (
        AdminTempatTinggalSerializer,
        PendudukTempatTinggalSerializer,
        "Surat Keterangan Tempat Tinggal",
    ),
    "kld": (
        AdminLuarDaerahSerializer,
        PendudukLuarDaerahSerializer,
        "Surat Keterangan Di Luar Daerah",
    ),
    "sktm": (
        AdminKetSiswaTidakMampuSerializer,
        PendudukKetSiswaTidakMampuSerializer,
        "Surat Keterangan Siswa Tidak Mampu",
    ),
    "belummenikah": (
        AdminBelumMenikahSerializer,
        PendudukBelumMenikahSerializer,
        "Surat Keterangan Belum Menikah",
    ),
    "usaha": (
        AdminUsahaSerializer,
        PendudukUsahaSerializer,
        "Surat Keterangan Usaha",
    ),
}
