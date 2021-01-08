from django.db import models

from api_sad_sig.util import CustomModel


class SuratDomisili(CustomModel):
    no_surat = models.CharField(max_length=50, blank=True, null=True)
    pegawai = models.ForeignKey(
        "v1.Pegawai", models.DO_NOTHING, blank=True, null=True
    )
    penduduk = models.ForeignKey(
        "v1.SadPenduduk", models.DO_NOTHING, blank=True, null=True
    )
    keperluan = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "surat_domisili"


class SuratSkck(CustomModel):
    no_surat = models.CharField(max_length=50, blank=True, null=True)
    pegawai = models.ForeignKey(
        "v1.Pegawai", models.DO_NOTHING, blank=True, null=True
    )
    penduduk = models.ForeignKey(
        "v1.SadPenduduk", models.DO_NOTHING, blank=True, null=True
    )
    keterangan = models.TextField(blank=True, null=True)
    keperluan = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "surat_skck"


class SuratKelahiran(CustomModel):
    no_surat = models.CharField(max_length=50, blank=True, null=True)
    pegawai = models.ForeignKey(
        "v1.Pegawai",
        models.DO_NOTHING,
        related_name="acc_surat_kelahiran",
        blank=True,
        null=True,
    )
    ayah = models.ForeignKey(
        "v1.SadPenduduk",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="ayah_surat_lahir",
    )
    ibu = models.ForeignKey(
        "v1.SadPenduduk",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="ibu_surat_lahir",
    )
    saksi1 = models.ForeignKey(
        "v1.Pegawai",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="saksi1_surat_lahir",
    )
    saksi2 = models.ForeignKey(
        "v1.Pegawai",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="saksi2_surat_lahir",
    )
    nama = models.CharField(max_length=100, blank=True, null=True)
    jk = models.CharField(max_length=15, blank=True, null=True)
    tempat_dilahirkan = models.CharField(max_length=50, blank=True, null=True)
    tempat_kelahiran = models.CharField(max_length=50, blank=True, null=True)
    tgl = models.DateField(blank=True, null=True)
    jenis_kelahiran = models.CharField(max_length=15, blank=True, null=True)
    kelahiran_ke = models.CharField(max_length=15, blank=True, null=True)
    penolong_kelahiran = models.CharField(max_length=15, blank=True, null=True)
    berat = models.CharField(max_length=15, blank=True, null=True)
    panjang = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "surat_kelahiran"
