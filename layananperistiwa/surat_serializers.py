from datetime import datetime

from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField


from api_sad_sig.util import (
    CustomSerializer,
)
from v1.models import SadPenduduk, SadDusun, Pegawai
from v1.serializers import SadPendudukMiniSerializer, SadDusunSerializer
from .models import LayananSurat, SadKematian, SadKelahiran
from .serializers import SadKematianSuratSerializer, SadKelahiranSerializer


class PendudukListSurat(CustomSerializer):
    class Meta:
        model = SadPenduduk
        fields = ["id", "nik", "nama"]


class PegawaiListSurat(CustomSerializer):
    class Meta:
        model = Pegawai
        fields = ["id", "nip", "nama", "jabatan"]


class ListSuratSerializer(CustomSerializer):
    pemohon = DynamicRelationField(
        "PendudukListSurat", source="penduduk", deferred=False, embed=True
    )
    pegawai = DynamicRelationField(
        "PegawaiListSurat", deferred=False, embed=True
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
        "PendudukListSurat", source="penduduk", deferred=False, embed=True
    )
    pegawai = DynamicRelationField(
        "PegawaiListSurat", deferred=False, embed=True
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
    atribut = serializers.DictField(required=False)

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class PendudukKetPendudukSerializer(BasePendudukSuratSerializer):
    atribut = serializers.DictField(required=False)

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "rapidtest"


class AdminTempatTinggalSerializer(BaseAdminSuratSerializer):
    atribut = serializers.DictField(required=False)

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "ktt"


class PendudukTempatTinggalSerializer(BasePendudukSuratSerializer):
    atribut = serializers.DictField(required=False)

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "ktt"


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
    tanggal_penguburan = serializers.CharField()
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
    kelahiran = serializers.SerializerMethodField()

    def get_kelahiran(self, obj):
        inst = SadKelahiran.objects.get(pk=obj["kelahiran_id"])
        return SadKelahiranSerializer(inst).data


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


class AtributIzinPesta(serializers.Serializer):
    tanggal = serializers.CharField()
    waktu_mulai = serializers.CharField()
    tempat = serializers.CharField()
    jenis_pesta = serializers.ListField(
        child=serializers.CharField(max_length=64)
    )

    tanggal_pesta = serializers.SerializerMethodField()

    def get_tanggal_pesta(self, obj):
        return datetime.strptime(obj["tanggal"], "%Y-%m-%d")


class AdminIzinPestaSerializer(BaseAdminSuratSerializer):
    atribut = AtributIzinPesta()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "izinpesta"


class PendudukIzinPestaSerializer(BasePendudukSuratSerializer):
    atribut = AtributIzinPesta()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "izinpesta"


class AtributIzinKeramaian(serializers.Serializer):
    tanggal = serializers.CharField()
    waktu_mulai = serializers.CharField()
    tempat = serializers.CharField()
    jenis_pesta = serializers.CharField()

    tanggal_pesta = serializers.SerializerMethodField()

    def get_tanggal_pesta(self, obj):
        return datetime.strptime(obj["tanggal"], "%Y-%m-%d")


class AdminIzinKeramaianSerializer(BaseAdminSuratSerializer):
    atribut = AtributIzinKeramaian()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "izinkeramaian"


class PendudukIzinKeramaianSerializer(BasePendudukSuratSerializer):
    atribut = AtributIzinKeramaian()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "izinkeramaian"


class AtributKehilangan(serializers.Serializer):
    nama_barang = serializers.CharField()
    detail_barang = serializers.CharField()


class AdminKehilanganSerializer(BaseAdminSuratSerializer):
    atribut = AtributKehilangan()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "kehilangan"


class PendudukKehilanganSerializer(BasePendudukSuratSerializer):
    atribut = AtributKehilangan()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "kehilangan"


class AtributDudaJanda(serializers.Serializer):
    nama_mantan_pasangan = serializers.CharField()
    tahun_berpisah = serializers.CharField()


class AdminDudaJandaSerializer(BaseAdminSuratSerializer):
    atribut = AtributDudaJanda()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "dudajanda"


class PendudukDudaJandaSerializer(BasePendudukSuratSerializer):
    atribut = AtributDudaJanda()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "dudajanda"


class AtributKeteranganPisah(serializers.Serializer):
    nama_pasangan = serializers.CharField()
    nama_instansi_pengadilan = serializers.CharField()
    keperluan = serializers.CharField()


class AdminKetPisahSerializer(BaseAdminSuratSerializer):
    atribut = AtributKeteranganPisah()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "ket_pisah"


class PendudukKetPisahSerializer(BasePendudukSuratSerializer):
    atribut = AtributKeteranganPisah()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "ket_pisah"


class DaftarKayu(serializers.Serializer):
    jenis = serializers.CharField()
    panjang = serializers.FloatField(required=False)
    lebar = serializers.FloatField(required=False)
    tebal = serializers.FloatField(required=False)
    jumlah = serializers.IntegerField()
    volume = serializers.SerializerMethodField()

    def get_volume(self, obj):
        if (
            obj.get("panjang", None)
            and obj.get("lebar", None)
            and obj.get("tebal", None)
        ):
            return obj["panjang"] * obj["lebar"] * obj["tebal"]
        return None


class AtributAsalUsulKayu(serializers.Serializer):
    nama = serializers.CharField()
    umur = serializers.IntegerField()
    pekerjaan = serializers.CharField()
    alamat = serializers.CharField()
    kota_tujuan = serializers.CharField()
    daftar_kayu = DaftarKayu(many=True)
    total_jumlah_kayu = serializers.SerializerMethodField()

    def get_total_jumlah_kayu(self, obj):
        total = 0
        for item in obj["daftar_kayu"]:
            total += item["jumlah"]
        return int(total)


class AdminSKAUSerializer(BaseAdminSuratSerializer):
    atribut = AtributAsalUsulKayu()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "skau"


class PendudukSKAUSerializer(BasePendudukSuratSerializer):
    atribut = AtributAsalUsulKayu()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "skau"


class AtributHakMilikTanah(serializers.Serializer):
    luas_tanah_angka = serializers.IntegerField()
    luas_tanah_kalimat = serializers.CharField()
    dusun_id = serializers.IntegerField()
    batas_utara = serializers.CharField()
    batas_selatan = serializers.CharField()
    batas_timur = serializers.CharField()
    batas_barat = serializers.CharField()
    nama_saksi1 = serializers.CharField()
    nama_saksi2 = serializers.CharField()
    nama_saksi3 = serializers.CharField()
    dusun = serializers.SerializerMethodField()

    def get_dusun(self, obj):
        if not obj.get("dusun_id", None):
            return {}
        inst = SadDusun.objects.get(pk=obj["dusun_id"])
        return SadDusunSerializer(inst).data


class AdminHakMilikTanahSerializer(BaseAdminSuratSerializer):
    atribut = AtributHakMilikTanah()

    class Meta(BaseAdminSuratSerializer.Meta):
        jenis_surat = "shm"


class PendudukHakMilikTanahSerializer(BasePendudukSuratSerializer):
    atribut = AtributHakMilikTanah()

    class Meta(BasePendudukSuratSerializer.Meta):
        jenis_surat = "shm"


serializer_list = {
    "shm": (
        AdminHakMilikTanahSerializer,
        PendudukHakMilikTanahSerializer,
        "Surat Keterangan Hak Milik",
    ),
    "skau": (
        AdminSKAUSerializer,
        PendudukSKAUSerializer,
        "Surat Keterangan Asal Usul Kayu",
    ),
    "kelahiran": (
        AdminSuratKelahiranSerializer,
        PendudukSuratKelahiranSerializer,
        "Surat Keterangan Kelahiran",
    ),
    "ket_pisah": (
        AdminKetPisahSerializer,
        PendudukKetPisahSerializer,
        "Surat Keterangan Pisah (Belum Cerai)",
    ),
    "dudajanda": (
        AdminDudaJandaSerializer,
        PendudukDudaJandaSerializer,
        "Surat Keterangan Duda / Janda",
    ),
    "kehilangan": (
        AdminKehilanganSerializer,
        PendudukKehilanganSerializer,
        "Surat Kehilangan",
    ),
    "izinkeramaian": (
        AdminIzinKeramaianSerializer,
        PendudukIzinKeramaianSerializer,
        "Surat Izin Keramaian",
    ),
    "izinpesta": (
        AdminIzinPestaSerializer,
        PendudukIzinPestaSerializer,
        "Surat Izin Pesta",
    ),
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
