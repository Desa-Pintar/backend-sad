# Generated by Django 2.2.16 on 2020-11-07 07:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(blank=True, max_length=18, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('jabatan', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('golongan', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pegawai',
            },
        ),
        migrations.CreateModel(
            name='SadDesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_desa', models.CharField(blank=True, max_length=5, null=True)),
                ('nama_desa', models.CharField(blank=True, max_length=250, null=True)),
                ('alamat', models.CharField(blank=True, max_length=150, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=12, null=True)),
                ('kode_pos', models.CharField(blank=True, max_length=5, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('visi_misi', models.TextField(blank=True, null=True)),
                ('sejarah', models.TextField(blank=True, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sad_desa',
            },
        ),
        migrations.CreateModel(
            name='SadDusunDukuh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desa_id', models.IntegerField(blank=True, null=True)),
                ('tipe', models.CharField(blank=True, max_length=5, null=True)),
                ('nama', models.CharField(blank=True, max_length=70, null=True)),
                ('dusun_dukuh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDusunDukuh')),
            ],
            options={
                'db_table': 'sad_dusun_dukuh',
            },
        ),
        migrations.CreateModel(
            name='SadInventaris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_inventaris', models.CharField(blank=True, max_length=100, null=True)),
                ('asal', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_awal', models.DateField(blank=True, null=True)),
                ('keadaan_awal', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_hapus', models.DateField(blank=True, null=True)),
                ('ket_hapus', models.CharField(blank=True, max_length=50, null=True)),
                ('keadaan_akhir', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('tahun', models.CharField(blank=True, max_length=4, null=True)),
                ('foto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'sad_inventaris',
            },
        ),
        migrations.CreateModel(
            name='SadKabKota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_kab_kota', models.CharField(blank=True, max_length=5, null=True)),
                ('nama_kab_kota', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sad_kab_kota',
            },
        ),
        migrations.CreateModel(
            name='SadKelahiran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis_kelamin', models.CharField(blank=True, max_length=20, null=True)),
                ('tempat_dilahirkan', models.CharField(blank=True, max_length=20, null=True)),
                ('tempat_kelahiran', models.CharField(blank=True, max_length=20, null=True)),
                ('waktu_kelahiran', models.DateField(blank=True, null=True)),
                ('jenis_kelahiran', models.CharField(blank=True, max_length=20, null=True)),
                ('kelahiran_ke', models.CharField(blank=True, max_length=5, null=True)),
                ('penolong_kelahiran', models.CharField(blank=True, max_length=30, null=True)),
                ('berat_bayi', models.CharField(blank=True, max_length=10, null=True)),
                ('panjang_bayi', models.CharField(blank=True, max_length=10, null=True)),
                ('nik_ayah', models.CharField(blank=True, max_length=16, null=True)),
                ('nik_ibu', models.CharField(blank=True, max_length=16, null=True)),
                ('nama_ayah', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_ibu', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_pelapor', models.CharField(blank=True, max_length=50, null=True)),
                ('nik_saksi_satu', models.CharField(blank=True, max_length=16, null=True)),
                ('nik_saksi_dua', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'sad_kelahiran',
            },
        ),
        migrations.CreateModel(
            name='SadKeluarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kk', models.CharField(blank=True, max_length=16, null=True)),
                ('alamat', models.CharField(blank=True, max_length=100, null=True)),
                ('kode_pos', models.CharField(blank=True, max_length=5, null=True)),
                ('status_kesejahteraan', models.CharField(blank=True, max_length=30, null=True)),
                ('penghasil', models.IntegerField(blank=True, null=True)),
                ('status_kk', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'sad_keluarga',
            },
        ),
        migrations.CreateModel(
            name='SadLahirmati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lama_kandungan', models.CharField(blank=True, max_length=20, null=True)),
                ('jenis_kelamin', models.CharField(blank=True, max_length=20, null=True)),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('jenis_kelahiran', models.CharField(blank=True, max_length=20, null=True)),
                ('kelahiran_ke', models.CharField(blank=True, max_length=5, null=True)),
                ('tempat_dilahirkan', models.CharField(blank=True, max_length=50, null=True)),
                ('penolong_kelahiran', models.CharField(blank=True, max_length=50, null=True)),
                ('sebab_lahirmati', models.CharField(blank=True, max_length=50, null=True)),
                ('yang_menentukan', models.CharField(blank=True, max_length=50, null=True)),
                ('tempat_kelahiran', models.CharField(blank=True, max_length=50, null=True)),
                ('nik_ayah', models.CharField(blank=True, max_length=16, null=True)),
                ('nik_ibu', models.CharField(blank=True, max_length=16, null=True)),
                ('nama_ayah', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_ibu', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_pelapor', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sad_lahirmati',
            },
        ),
        migrations.CreateModel(
            name='SadPindahMasuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kk', models.CharField(blank=True, max_length=18, null=True)),
                ('status_no_kk_pindah', models.CharField(blank=True, max_length=20, null=True)),
                ('tanggal_kedatangan', models.DateField(blank=True, null=True)),
                ('alamat', models.CharField(blank=True, max_length=100, null=True)),
                ('rt_id', models.IntegerField(blank=True, null=True)),
                ('yang_datang', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sad_pindah_masuk',
            },
        ),
        migrations.CreateModel(
            name='SadProvinsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_provinsi', models.CharField(blank=True, max_length=5, null=True)),
                ('nama_provinsi', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sad_provinsi',
            },
        ),
        migrations.CreateModel(
            name='SadRt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rt', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'sad_rt',
            },
        ),
        migrations.CreateModel(
            name='SadRw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desa_id', models.IntegerField(blank=True, null=True)),
                ('rw', models.CharField(blank=True, max_length=10, null=True)),
                ('dusun_dukuh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDusunDukuh')),
            ],
            options={
                'db_table': 'sad_rw',
            },
        ),
        migrations.CreateModel(
            name='SadSarpras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sarpras', models.CharField(blank=True, max_length=100, null=True)),
                ('asal', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_awal', models.DateField(blank=True, null=True)),
                ('keadaan_awal', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_hapus', models.DateField(blank=True, null=True)),
                ('ket_hapus', models.CharField(blank=True, max_length=50, null=True)),
                ('keadaan_akhir', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('tahun', models.CharField(blank=True, max_length=4, null=True)),
                ('foto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'sad_sarpras',
            },
        ),
        migrations.CreateModel(
            name='SadSurat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=100, null=True)),
                ('sifat', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sad_surat',
            },
        ),
        migrations.CreateModel(
            name='SigDesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_desa', models.CharField(blank=True, max_length=250, null=True)),
                ('luas', models.CharField(blank=True, max_length=10, null=True)),
                ('keliling', models.CharField(blank=True, max_length=10, null=True)),
                ('geometry', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sig_desa',
            },
        ),
        migrations.CreateModel(
            name='SigDusunDukuh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dusun', models.CharField(blank=True, max_length=70, null=True)),
                ('nama_dukuh', models.CharField(blank=True, max_length=70, null=True)),
                ('sig_desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDesa')),
            ],
            options={
                'db_table': 'sig_dusun_dukuh',
            },
        ),
        migrations.CreateModel(
            name='SigRt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rt', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'sig_rt',
            },
        ),
        migrations.CreateModel(
            name='SigRw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rw', models.CharField(blank=True, max_length=10, null=True)),
                ('desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDesa')),
                ('dusun_dukuh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDusunDukuh')),
            ],
            options={
                'db_table': 'sig_rw',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=100, null=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('gambar', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'slider',
            },
        ),
        migrations.CreateModel(
            name='SigSadRw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sad_rw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadRw')),
                ('sig_rw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigRw')),
            ],
            options={
                'db_table': 'sig_sad_rw',
            },
        ),
        migrations.CreateModel(
            name='SigSadRt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sad_rt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadRt')),
                ('sig_rt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigRt')),
            ],
            options={
                'db_table': 'sig_sad_rt',
            },
        ),
        migrations.CreateModel(
            name='SigSadDusunDukuh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sad_dusun_dukuh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDusunDukuh')),
                ('sig_dusun_dukuh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDusunDukuh')),
            ],
            options={
                'db_table': 'sig_sad_dusun_dukuh',
            },
        ),
        migrations.CreateModel(
            name='SigSadDesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sad_desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDesa')),
                ('sig_desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDesa')),
            ],
            options={
                'db_table': 'sig_sad_desa',
            },
        ),
        migrations.AddField(
            model_name='sigrt',
            name='rw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigRw'),
        ),
        migrations.CreateModel(
            name='SigBidang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbt', models.IntegerField(blank=True, null=True)),
                ('desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigDesa')),
            ],
            options={
                'db_table': 'sig_bidang',
            },
        ),
        migrations.CreateModel(
            name='SettingDesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=20, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDesa')),
            ],
            options={
                'db_table': 'setting_desa',
            },
        ),
        migrations.AddField(
            model_name='sadrt',
            name='rw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadRw'),
        ),
        migrations.CreateModel(
            name='SadPindahKeluar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemohon', models.CharField(blank=True, max_length=30, null=True)),
                ('alasan', models.CharField(blank=True, max_length=100, null=True)),
                ('provinsi_tujuan', models.CharField(blank=True, max_length=20, null=True)),
                ('kota_tujuan', models.CharField(blank=True, max_length=20, null=True)),
                ('kecamatan_tujuan', models.CharField(blank=True, max_length=20, null=True)),
                ('kelurahan_tujuan', models.CharField(blank=True, max_length=20, null=True)),
                ('dusun_tujuan', models.CharField(blank=True, max_length=20, null=True)),
                ('rt_tujuan', models.CharField(blank=True, max_length=5, null=True)),
                ('rw_tujuan', models.CharField(blank=True, max_length=5, null=True)),
                ('kodepos_tujuan', models.CharField(blank=True, max_length=5, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=13, null=True)),
                ('klarifikasi_pindah', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis_kepindahan', models.CharField(blank=True, max_length=50, null=True)),
                ('status_no_kk_pindah', models.CharField(blank=True, max_length=50, null=True)),
                ('rencana_tgl_pindah', models.DateField(blank=True, null=True)),
                ('keluarga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadKeluarga')),
            ],
            options={
                'db_table': 'sad_pindah_keluar',
            },
        ),
        migrations.CreateModel(
            name='SadPenduduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(blank=True, max_length=16, null=True)),
                ('chip_ektp', models.CharField(blank=True, max_length=10, null=True)),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_lahir', models.DateField(blank=True, null=True)),
                ('tempat_lahir', models.CharField(blank=True, max_length=50, null=True)),
                ('jk', models.CharField(blank=True, max_length=12, null=True)),
                ('agama', models.CharField(blank=True, max_length=20, null=True)),
                ('pendidikan', models.CharField(blank=True, max_length=20, null=True)),
                ('pekerjaan', models.CharField(blank=True, max_length=50, null=True)),
                ('status_kawin', models.CharField(blank=True, max_length=20, null=True)),
                ('status_penduduk', models.CharField(blank=True, max_length=20, null=True)),
                ('kewarganegaraan', models.CharField(blank=True, max_length=5, null=True)),
                ('anak_ke', models.CharField(blank=True, max_length=5, null=True)),
                ('golongan_darah', models.CharField(blank=True, max_length=5, null=True)),
                ('status_dalam_keluarga', models.CharField(blank=True, max_length=20, null=True)),
                ('no_paspor', models.CharField(blank=True, max_length=20, null=True)),
                ('suku', models.CharField(blank=True, max_length=20, null=True)),
                ('potensi_diri', models.CharField(blank=True, max_length=50, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=13, null=True)),
                ('nik_ayah', models.CharField(blank=True, max_length=18, null=True)),
                ('nik_ibu', models.CharField(blank=True, max_length=18, null=True)),
                ('nama_ayah', models.CharField(blank=True, max_length=45, null=True)),
                ('nama_ibu', models.CharField(blank=True, max_length=45, null=True)),
                ('tgl_exp_paspor', models.DateField(blank=True, null=True)),
                ('akta_lahir', models.CharField(blank=True, max_length=18, null=True)),
                ('akta_kawin', models.CharField(blank=True, max_length=18, null=True)),
                ('tgl_kawin', models.DateField(blank=True, null=True)),
                ('akta_cerai', models.CharField(blank=True, max_length=18, null=True)),
                ('tgl_cerai', models.DateField(blank=True, null=True)),
                ('kelainan_fisik', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=20, null=True)),
                ('keluarga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='anggota', to='v1.SadKeluarga')),
            ],
            options={
                'db_table': 'sad_penduduk',
            },
        ),
        migrations.CreateModel(
            name='SadKematian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_kematian', models.DateField(blank=True, null=True)),
                ('sebab_kematian', models.CharField(blank=True, max_length=50, null=True)),
                ('tempat_kematian', models.CharField(blank=True, max_length=50, null=True)),
                ('yang_menerangkan', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_pelapor', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_saksi_satu', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_saksi_dua', models.CharField(blank=True, max_length=50, null=True)),
                ('penduduk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadPenduduk')),
            ],
            options={
                'db_table': 'sad_kematian',
            },
        ),
        migrations.AddField(
            model_name='sadkeluarga',
            name='rt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadRt'),
        ),
        migrations.CreateModel(
            name='SadKecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_kecamatan', models.CharField(blank=True, max_length=5, null=True)),
                ('nama_kecamatan', models.CharField(blank=True, max_length=250, null=True)),
                ('kab_kota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadKabKota')),
            ],
            options={
                'db_table': 'sad_kecamatan',
            },
        ),
        migrations.AddField(
            model_name='sadkabkota',
            name='provinsi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadProvinsi'),
        ),
        migrations.CreateModel(
            name='SadDetailSurat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('lampiran', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=50, null=True)),
                ('tempat_tujuan', models.CharField(blank=True, max_length=50, null=True)),
                ('pengikut_pindah', models.CharField(blank=True, max_length=50, null=True)),
                ('asal', models.CharField(blank=True, max_length=50, null=True)),
                ('barang_yg_hilang', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_jam_kehilangan', models.CharField(blank=True, max_length=50, null=True)),
                ('pelapor', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_yg_sama', models.CharField(blank=True, max_length=50, null=True)),
                ('keperluan', models.CharField(blank=True, max_length=50, null=True)),
                ('berlaku_mulai', models.DateField(blank=True, null=True)),
                ('sampai_dengan', models.DateField(blank=True, null=True)),
                ('nama_acara', models.CharField(blank=True, max_length=50, null=True)),
                ('tgl_acara', models.DateField(blank=True, null=True)),
                ('tempat_acara', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis_hiburan', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_grup', models.CharField(blank=True, max_length=50, null=True)),
                ('pimpinan_acara', models.CharField(blank=True, max_length=50, null=True)),
                ('jumlah_keluarga_yg_pindah', models.CharField(blank=True, max_length=50, null=True)),
                ('hubungan', models.CharField(blank=True, max_length=50, null=True)),
                ('data_penduduk_luar_desa', models.CharField(blank=True, max_length=50, null=True)),
                ('pegawai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.Pegawai')),
                ('surat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadSurat')),
            ],
            options={
                'db_table': 'sad_detail_surat',
            },
        ),
        migrations.AddField(
            model_name='saddesa',
            name='kecamatan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadKecamatan'),
        ),
    ]
