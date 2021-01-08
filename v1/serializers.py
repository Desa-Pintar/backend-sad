from django.utils import timezone
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields import DynamicRelationField
from rest_framework import serializers

from api_sad_sig.util import (
    CustomSerializer,
    util_columns,
    create_or_reactivate,
    create_or_reactivate_user,
)
from .models import (
    Pegawai,
    SadProvinsi,
    SadKabKota,
    SadKecamatan,
    SadDesa,
    BatasDesa,
    SadDusun,
    SadRw,
    SadRt,
    SadKeluarga,
    SadPenduduk,
    SadKelahiran,
    SadKematian,
    SadLahirmati,
    SadPindahKeluar,
    SadPindahMasuk,
    SadSarpras,
    SadInventaris,
    SadSurat,
    SadDetailSurat,
    SigSadBidang,
    SigSadBidang2,
    SigPemilik,
    SigBidang,
    SigDesa,
    SigRw,
    SigRt,
    SigRw2,
    SigRt2,
    SigDusun,
    SigDukuh,
    SigDukuh2,
    Slider,
    KategoriArtikel,
    Artikel,
    KategoriInformasi,
    Informasi,
    KategoriPotensi,
    Potensi,
    KategoriLapor,
    StatusLapor,
    Lapor,
    JenisPindah,
    KlasifikasiPindah,
    AlasanPindah,
    StatusKKTinggal,
    StatusKKPindah,
    KategoriPendapatan,
    KategoriTahun,
    KategoriBelanja,
    Pendapatan,
    Belanja,
    SuratMasuk,
    SuratKeluar,
    Pekerjaan,
    Pendidikan,
    Agama,
    KelainanFisik,
    Cacat,
    StatusPerkawinan,
    Kewarganegaraan,
    Goldar,
    StatusDlmKeluarga,
    StatusKesejahteraan,
    StatusWarga,
    StatusDatangMasuk,
    Asal,
    KeadaanAwal,
    Jabatan,
    StatusPns,
    Golongan,
)


status_keluarga = [
    "Kepala Keluarga",
    "Suami",
    "Istri",
    "Anak",
    "Menantu",
    "Cucu",
    "Orang Tua",
    "Famili Lain",
    "Lainnya",
]


class JenisPindahSerializer(CustomSerializer):
    class Meta:
        model = JenisPindah
        name = "data"
        exclude = []


class AlasanPindahSerializer(CustomSerializer):
    class Meta:
        model = AlasanPindah
        name = "data"
        exclude = []


class KlasifikasiPindahSerializer(CustomSerializer):
    class Meta:
        model = KlasifikasiPindah
        name = "data"
        exclude = []


class StatusKKTinggalSerializer(CustomSerializer):
    class Meta:
        model = StatusKKTinggal
        name = "data"
        exclude = []


class StatusKKPindahSerializer(CustomSerializer):
    class Meta:
        model = StatusKKPindah
        name = "data"
        exclude = []


class PegawaiSerializer(CustomSerializer):
    class Meta:
        model = Pegawai
        name = "data"
        exclude = []


class SadProvinsiSerializer(CustomSerializer):
    class Meta:
        model = SadProvinsi
        name = "data"
        exclude = []


class SadKabKotaSerializer(CustomSerializer):
    provinsi = DynamicRelationField(SadProvinsiSerializer)

    class Meta:
        model = SadKabKota
        name = "data"
        exclude = util_columns


class SadKecamatanSerializer(CustomSerializer):
    kab_kota = DynamicRelationField(SadKabKotaSerializer)

    class Meta:
        model = SadKecamatan
        name = "data"
        exclude = util_columns


class SadDesaSerializer(CustomSerializer):
    kecamatan = DynamicRelationField(SadKecamatanSerializer)

    class Meta:
        model = SadDesa
        name = "data"
        exclude = util_columns


class BatasDesaSerializer(CustomSerializer):
    desa = DynamicRelationField(
        "SadDesaSerializer", deferred=False, embed=True
    )

    class Meta:
        model = BatasDesa
        name = "data"
        exclude = []


class SadDusunSerializer(CustomSerializer):
    desa = DynamicRelationField(SadDesaSerializer)

    class Meta:
        model = SadDusun
        name = "data"
        exclude = util_columns


class SadRwSerializer(CustomSerializer):
    dusun = DynamicRelationField(SadDusunSerializer)

    class Meta:
        model = SadRw
        name = "data"
        exclude = util_columns


class SadRtSerializer(CustomSerializer):
    rw = DynamicRelationField(SadRwSerializer)

    class Meta:
        model = SadRt
        name = "data"
        exclude = util_columns


class MiniSadRtSerializer(CustomSerializer):
    rw = DynamicRelationField("SadRwSerializer", deferred=True, embed=True)

    class Meta:
        model = SadRt
        name = "data"
        fields = ["rw", "id", "rt"]


class SadKeluargaSerializer(CustomSerializer):
    anggota = DynamicRelationField(
        "SadPendudukSerializer", many=True, deferred=True, embed=True
    )
    dusun = serializers.CharField(read_only=True, source="rt.rw.dusun.nama")
    rw = serializers.CharField(read_only=True, source="rt.rw.rw")
    rt = DynamicRelationField("MiniSadRtSerializer", deferred=True, embed=True)
    kepala_keluarga = serializers.DictField(read_only=True)

    class Meta:
        model = SadKeluarga
        name = "data"
        exclude = util_columns
        extra_kwargs = {
            "created_by": {"default": serializers.CurrentUserDefault()}
        }


class SadPendudukSerializer(CustomSerializer):
    keluarga = DynamicRelationField(
        "SadKeluargaSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SadPenduduk
        name = "data"
        exclude = []

    def create(self, data):
        penduduk = create_or_reactivate(
            SadPenduduk, {"nik": data["nik"]}, data
        )
        password = str(data["tgl_lahir"]).replace("-", "")
        penduduk_user = create_or_reactivate_user(data["nik"], password)
        penduduk.user = penduduk_user
        penduduk.save()
        penduduk.user.save()
        return penduduk


class SadKelahiranSerializer(CustomSerializer):
    class Meta:
        model = SadKelahiran
        name = "data"
        exclude = []


class SadKematianSerializer(CustomSerializer):
    penduduk = DynamicRelationField(
        "SadPendudukSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SadKematian
        name = "data"
        exclude = []


class SadLahirmatiSerializer(CustomSerializer):
    class Meta:
        model = SadLahirmati
        name = "data"
        exclude = []


class SadPindahKeluarSerializer(CustomSerializer):
    kelurahan_tujuan = DynamicRelationField(
        SadDesaSerializer, deferred=False, embed=True
    )
    anggota_pindah = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    def create(self, validated_data):
        nik_pindah = validated_data.pop("anggota_pindah")

        validated_data["nik_pindah"] = ",".join(str(i) for i in nik_pindah)
        sad_pindah = SadPindahKeluar.objects.create(**validated_data)

        keluarga_id = validated_data.get("nomor_kk")
        keluarga = SadKeluarga.objects.get(no_kk=keluarga_id)

        if validated_data.get("status_kk_pindah"):
            if validated_data["status_kk_pindah"].nama == "kk_baru":
                penduduk_pindah = keluarga.anggota.filter(pk__in=nik_pindah)
                for penduduk in penduduk_pindah:
                    penduduk.deleted_at = timezone.now()
                    penduduk.deleted_by = self.context["request"].user
                    penduduk.save()
        if validated_data.get("status_kk_tinggal"):
            if validated_data["status_kk_tinggal"].nama == "kk_baru":
                penduduk_tinggal = keluarga.anggota.exclude(pk__in=nik_pindah)
                for penduduk in penduduk_tinggal:
                    penduduk.deleted_at = timezone.now()
                    penduduk.deleted_by = self.context["request"].user
                    penduduk.save()
        keluarga.refresh_from_db()
        if not keluarga.anggota.count():
            keluarga.deleted_at = timezone.now()
            keluarga.deleted_by = self.context["request"].user
            keluarga.save()
        sad_pindah.save()
        return sad_pindah

    class Meta:
        model = SadPindahKeluar
        name = "data"
        exclude = util_columns + ["nik_pindah"]


class MiniUserSerializer(DynamicModelSerializer):
    status_dalam_keluarga = serializers.ChoiceField(status_keluarga)

    class Meta:
        model = SadPenduduk
        fields = ["nik", "nama", "tgl_lahir", "status_dalam_keluarga"]


class SadPindahMasukSerializer(CustomSerializer):
    rt_id = DynamicRelationField(SadRtSerializer)
    anggota = serializers.ListField(
        child=MiniUserSerializer(), write_only=True
    )

    def create(self, validated_data):
        anggota = validated_data.pop("anggota")

        print("This 0")
        if SadKeluarga.objects.filter(no_kk=validated_data["no_kk"]).exists():
            print("This x")
            raise APIException("Nomor KK Sudah terdaftar", 400)

        sad_masuk = SadPindahMasuk.objects.create(**validated_data)

        keluarga_data = validated_data.copy()
        print("This 1")
        print(keluarga_data)
        keluarga_data["status_kk"] = keluarga_data.pop(
            "status_kk_pindah"
        ).label
        keluarga_data["rt"] = keluarga_data.pop("rt_id")
        keluarga_data.pop("tanggal_kedatangan")
        keluarga_filter = {"no_kk": keluarga_data["no_kk"]}
        try:
            keluarga = create_or_reactivate(
                SadKeluarga, keluarga_filter, keluarga_data
            )
        except Exception:
            return Response({"msg": "Gagal menyimpan data keluarga"}, 400)
        keluarga.save()

        for item in anggota:
            penduduk_filter = {"nik": item["nik"]}
            try:
                penduduk = create_or_reactivate(
                    SadPenduduk, penduduk_filter, item
                )
            except Exception:
                keluarga.delete()
                return Response({"msg": "Data Penduduk Gagal"})
            print(str(item["tgl_lahir"]))
            user = create_or_reactivate_user(
                item["nik"], str(item["tgl_lahir"]).replace("-", "")
            )
            penduduk.user = user
            penduduk.keluarga = keluarga
            penduduk.save()
        print("This 2")

        sad_masuk.save()
        return sad_masuk

    class Meta:
        model = SadPindahMasuk
        name = "data"
        exclude = util_columns + ["nik_datang"]


class SadSarprasSerializer(CustomSerializer):
    class Meta:
        model = SadSarpras
        name = "data"
        exclude = []


class SadInventarisSerializer(CustomSerializer):
    class Meta:
        model = SadInventaris
        name = "data"
        exclude = []


class SadSuratSerializer(CustomSerializer):
    class Meta:
        model = SadSurat
        name = "data"
        fields = ["id", "judul", "sifat"]


class SadDetailSuratSerializer(CustomSerializer):
    class Meta:
        model = SadDetailSurat
        name = "data"
        fields = ["id", "no_surat", "keterangan"]


class SigDesaSerializer(CustomSerializer):
    class Meta:
        model = SigDesa
        name = "data"
        exclude = []


class SigDusunSerializer(CustomSerializer):
    sig_desa = DynamicRelationField(
        "SigDesaSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigDusun
        name = "data"
        exclude = []


class SigDukuhSerializer(CustomSerializer):
    sig_dusun = DynamicRelationField(
        "SigDusunSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigDukuh
        name = "data"
        exclude = []


class SigDukuh2Serializer(CustomSerializer):
    sig_desa = DynamicRelationField(
        "SigDesaSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigDukuh2
        name = "data"
        exclude = []


class SigRwSerializer(CustomSerializer):
    sig_dukuh = DynamicRelationField(
        "SigDukuhSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigRw
        name = "data"
        exclude = []


class SigRtSerializer(CustomSerializer):
    sig_rw = DynamicRelationField("SigRwSerializer", deferred=True, embed=True)

    class Meta:
        model = SigRt
        name = "data"
        exclude = []


class SigRw2Serializer(CustomSerializer):
    sig_dukuh2 = DynamicRelationField(
        "SigDukuh2Serializer", deferred=True, embed=True
    )

    class Meta:
        model = SigRw2
        name = "data"
        exclude = []


class SigRt2Serializer(CustomSerializer):
    sig_rw2 = DynamicRelationField(
        "SigRw2Serializer", deferred=True, embed=True
    )

    class Meta:
        model = SigRt2
        name = "data"
        exclude = []


class SigPemilikSerializer(CustomSerializer):
    pemilik = DynamicRelationField(
        "SadPendudukSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigPemilik
        name = "data"
        exclude = []


class PemilikBidangSerializer(serializers.Serializer):
    nik = serializers.CharField()
    nama = serializers.CharField()
    namabidang = serializers.CharField()
    is_warga = serializers.BooleanField(default=False)


class PenguasaBidangSerializer(serializers.Serializer):
    no_kk = serializers.CharField()
    is_warga = serializers.BooleanField(default=False)


class SigBidangSerializerMini(CustomSerializer):
    sig_rt = DynamicRelationField(
        "SigRtSerializer", deferred=False, embed=True
    )

    class Meta:
        model = SigBidang
        name = "data"
        fields = ["id", "nbt", "sig_rt", "gambar_atas", "gambar_depan"]


class SigBidangSerializerFull(CustomSerializer):
    sig_rt = DynamicRelationField(
        "SigRtSerializer", deferred=False, embed=True
    )
    daftar_pemilik = serializers.ListField(
        child=PemilikBidangSerializer(), required=False
    )
    daftar_penguasa = serializers.ListField(
        child=PenguasaBidangSerializer(), required=False
    )

    class Meta:
        model = SigBidang
        name = "data"
        fields = [
            "id",
            "nbt",
            "gambar_atas",
            "gambar_depan",
            "sig_rt",
            "daftar_pemilik",
            "daftar_penguasa",
        ]


class SigSadBidangSerializer(CustomSerializer):
    sad_penduduk = DynamicRelationField(
        "SadPendudukSerializer", deferred=True, embed=True
    )
    sig_bidang = DynamicRelationField(
        "SigBidangSerializer", deferred=True, embed=True
    )

    class Meta:
        model = SigSadBidang
        name = "data"
        exclude = []


class SigSadBidang2Serializer(CustomSerializer):
    sad_penduduk = DynamicRelationField(
        "SadPendudukSerializer", deferred=True, embed=True
    )
    sig_bidang2 = DynamicRelationField(
        "SigBidang2Serializer", deferred=True, embed=True
    )

    class Meta:
        model = SigSadBidang2
        name = "data"
        exclude = []


class SliderSerializer(DynamicModelSerializer):
    class Meta:
        model = Slider
        name = "data"
        exclude = []


class KategoriArtikelSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriArtikel
        name = "data"
        exclude = []


class KategoriInformasiSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriInformasi
        name = "data"
        exclude = []


class KategoriPotensiSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriPotensi
        name = "data"
        exclude = []


class KategoriLaporSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriLapor
        name = "data"
        exclude = []


class StatusLaporSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusLapor
        name = "data"
        exclude = []


class LaporSerializer(CustomSerializer):
    kategori = DynamicRelationField(
        "KategoriLaporSerializer", deferred=True, embed=True
    )
    status = DynamicRelationField(
        "StatusLaporSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Lapor
        name = "data"
        exclude = []


class ArtikelSerializer(DynamicModelSerializer):
    kategori = DynamicRelationField(
        "KategoriArtikelSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Artikel
        name = "data"
        exclude = []


class InformasiSerializer(DynamicModelSerializer):
    kategori = DynamicRelationField(
        "KategoriInformasiSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Informasi
        name = "data"
        exclude = []


class PotensiSerializer(DynamicModelSerializer):
    kategori = DynamicRelationField(
        "KategoriPotensiSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Potensi
        name = "data"
        exclude = []


class KategoriPendapatanSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriPendapatan
        name = "data"
        exclude = []


class KategoriTahunSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriTahun
        name = "data"
        exclude = []


class KategoriBelanjaSerializer(DynamicModelSerializer):
    class Meta:
        model = KategoriBelanja
        name = "data"
        exclude = []


class PendapatanSerializer(DynamicModelSerializer):
    kategori = DynamicRelationField(
        "KategoriPendapatanSerializer", deferred=True, embed=True
    )
    tahun = DynamicRelationField(
        "KategoriTahunSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Pendapatan
        name = "data"
        exclude = []


class BelanjaSerializer(DynamicModelSerializer):
    kategori = DynamicRelationField(
        "KategoriBelanjaSerializer", deferred=True, embed=True
    )
    tahun = DynamicRelationField(
        "KategoriTahunSerializer", deferred=True, embed=True
    )

    class Meta:
        model = Belanja
        name = "data"
        exclude = []


class SuratMasukSerializer(DynamicModelSerializer):
    class Meta:
        model = SuratMasuk
        name = "data"
        exclude = []


class SuratKeluarSerializer(DynamicModelSerializer):
    class Meta:
        model = SuratKeluar
        name = "data"
        exclude = []


class PekerjaanSerializer(DynamicModelSerializer):
    class Meta:
        model = Pekerjaan
        name = "data"
        exclude = []


class PendidikanSerializer(DynamicModelSerializer):
    class Meta:
        model = Pendidikan
        name = "data"
        exclude = []


class AgamaSerializer(DynamicModelSerializer):
    class Meta:
        model = Agama
        name = "data"
        exclude = []


class KelainanFisikSerializer(DynamicModelSerializer):
    class Meta:
        model = KelainanFisik
        name = "data"
        exclude = []


class CacatSerializer(DynamicModelSerializer):
    class Meta:
        model = Cacat
        name = "data"
        exclude = []


class StatusPerkawinanSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusPerkawinan
        name = "data"
        exclude = []


class KewarganegaraanSerializer(DynamicModelSerializer):
    class Meta:
        model = Kewarganegaraan
        name = "data"
        exclude = []


class GoldarSerializer(DynamicModelSerializer):
    class Meta:
        model = Goldar
        name = "data"
        exclude = []


class StatusDlmKeluargaSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusDlmKeluarga
        name = "data"
        exclude = []


class StatusKesejahteraanSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusKesejahteraan
        name = "data"
        exclude = []


class StatusWargaSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusWarga
        name = "data"
        exclude = []


class StatusDatangMasukSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusDatangMasuk
        name = "data"
        exclude = []


class AsalSerializer(DynamicModelSerializer):
    class Meta:
        model = Asal
        name = "data"
        exclude = []


class KeadaanAwalSerializer(DynamicModelSerializer):
    class Meta:
        model = KeadaanAwal
        name = "data"
        exclude = []


class JabatanSerializer(DynamicModelSerializer):
    class Meta:
        model = Jabatan
        name = "data"
        exclude = []


class StatusPnsSerializer(DynamicModelSerializer):
    class Meta:
        model = StatusPns
        name = "data"
        exclude = []


class GolonganSerializer(DynamicModelSerializer):
    class Meta:
        model = Golongan
        name = "data"
        exclude = []
