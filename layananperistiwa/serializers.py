from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields import DynamicRelationField

from api_sad_sig.util import CustomSerializer
from v1.serializers import PegawaiSerializer
from .models import SuratDomisili, SuratKelahiran, SuratSkck


class AdminSuratKelahiranSerializer(DynamicModelSerializer):
    pegawai = DynamicRelationField(PegawaiSerializer)

    class Meta:
        model = SuratKelahiran
        name = "data"
        include = ["pegawai"]
        exclude = [
            "created_by",
            "created_at",
            "updated_at",
            "deleted_by",
            "deleted_at",
        ]
        read_only_fields = [
            "ayah",
            "ibu",
            "saksi1",
            "saksi2",
            "nama",
            "jk",
            "tempat_dilahirkan",
            "tempat_kelahiran",
            "tgl",
            "jenis_kelahiran",
            "kelahiran_ke",
            "penolong_kelahiran",
            "berat",
            "panjang",
        ]


class AdminSuratSkckSerializer(DynamicModelSerializer):
    nama = serializers.CharField(source="penduduk.nama", read_only=True)
    tempat_lahir = serializers.CharField(
        source="penduduk.tempat_lahir", read_only=True
    )
    jenis_kelamin = serializers.CharField(source="penduduk.jk", read_only=True)
    kewarganegaraan = serializers.CharField(
        source="penduduk.kewargananegaraan", read_only=True
    )
    agama = serializers.CharField(source="penduduk.agama", read_only=True)
    status_kawin = serializers.CharField(
        source="penduduk.status_kawin", read_only=True
    )
    pekerjaan = serializers.CharField(
        source="penduduk.pekerjaan", read_only=True
    )
    pendidikan = serializers.CharField(
        source="penduduk.pendidikan", read_only=True
    )
    no_ktp = serializers.CharField(source="penduduk.nik", read_only=True)
    no_kk = serializers.CharField(
        source="penduduk.keluarga.no_kk", read_only=True
    )
    alamat = serializers.CharField(source="penduduk.alamat", read_only=True)

    class Meta:
        model = SuratSkck
        name = "data"
        exclude = [
            "penduduk",
            "created_by",
            "created_at",
            "updated_at",
            "updated_by",
            "deleted_by",
            "deleted_at",
        ]
        read_only_fields = ["keperluan", "keterangan"]


class AdminSuratDomisiliSerializer(DynamicModelSerializer):
    nama = serializers.CharField(source="penduduk.nama", read_only=True)
    no_ktp = serializers.CharField(source="penduduk.nik", read_only=True)
    jenis_kelamin = serializers.CharField(source="penduduk.jk", read_only=True)
    status_kawin = serializers.CharField(
        source="penduduk.status_kawin", read_only=True
    )
    pekerjaan = serializers.CharField(
        source="penduduk.pekerjaan", read_only=True
    )
    agama = serializers.CharField(source="penduduk.agama", read_only=True)
    alamat = serializers.CharField(source="penduduk.alamat", read_only=True)

    class Meta:
        model = SuratDomisili
        name = "data"
        exclude = [
            "penduduk",
            "created_by",
            "created_at",
            "updated_at",
            "updated_by",
            "deleted_by",
            "deleted_at",
        ]
        read_only_fields = ["keperluan", "penduduk"]


class SuratMeta:
    name = "data"
    exclude = [
        "pegawai",
        "no_surat",
        "created_by",
        "created_at",
        "deleted_by",
        "deleted_at",
        "updated_by",
        "updated_at",
    ]


jenis_kelahiran = ["Tunggal", "Kembar 2", "Kembar 3", "Kembar 4", "Lainnya"]
tempat_dilahirkan = ["RS/RB", "Puskesmas", "Polindes", "Rumah", "Lainnya"]
jenis_kelamin = ["Laki-laki", "Perempuan"]
penolong_kelahiran = ["Dokter", "Bidan/Perawat", "Dukun", "Lainnya"]


class SuratKelahiranSerializer(CustomSerializer):
    jk = serializers.ChoiceField(jenis_kelamin)
    jenis_kelahiran = serializers.ChoiceField(jenis_kelahiran)
    tempat_dilahirkan = serializers.ChoiceField(tempat_dilahirkan)
    penolong_kelahiran = serializers.ChoiceField(penolong_kelahiran)

    class Meta(SuratMeta):
        model = SuratKelahiran


class SuratSkckSerializer(CustomSerializer):
    class Meta(SuratMeta):
        model = SuratSkck

    def create(self, validated_data):
        surat = SuratSkck(**validated_data)
        surat.created_by = self.context["request"].user
        surat.penduduk = self.context["request"].user.profile
        surat.save()
        return surat


class SuratDomisiliSerializer(CustomSerializer):
    class Meta(SuratMeta):
        model = SuratDomisili

    def create(self, validated_data):
        surat = SuratDomisili(**validated_data)
        surat.created_by = self.context["request"].user
        surat.penduduk = self.context["request"].user.profile
        surat.save()
        return surat
