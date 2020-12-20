from rest_framework import permissions, status
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User, Group

import pandas
import json
from io import BytesIO
import numpy as np

from users.permissions import IsAdminUserOrReadOnly
from .utils import render_mail
from .serializers import (
    PegawaiSerializer,
    SadProvinsiSerializer,
    SadKabKotaSerializer,
    SadKecamatanSerializer,
    SadDesaSerializer,
    BatasDesaSerializer,
    SadDusunSerializer,
    SadRwSerializer,
    SadRtSerializer,
    SadKeluargaSerializer,
    SadPendudukSerializer,
    SadKelahiranSerializer,
    SadKematianSerializer,
    SadLahirmatiSerializer,
    SadPindahMasukSerializer,
    SadPindahKeluarSerializer,
    SadSarprasSerializer,
    SadInventarisSerializer,
    SadSuratSerializer,
    SadDetailSuratSerializer,
    SigBidangSerializer,
    SigPemilikSerializer,
    SigSadBidangSerializer,
    SigSadBidang2Serializer,
    SigDesaSerializer,
    SigRtSerializer,
    SigRwSerializer,
    SigDusunSerializer,
    SigDukuhSerializer,
    SigDukuh2Serializer,
    SigRt2Serializer,
    SigRw2Serializer,
    KategoriLaporSerializer,
    LaporSerializer,
    KategoriArtikelSerializer,
    ArtikelSerializer,
    SliderSerializer,
    KategoriPotensiSerializer,
    PotensiSerializer,
    KategoriInformasiSerializer,
    InformasiSerializer,
    SuratKelahiranSerializer,
    AdminSuratKelahiranSerializer,
    SuratSkckSerializer,
    AdminSuratSkckSerializer,
    SuratDomisiliSerializer,
    AdminSuratDomisiliSerializer,
    JenisPindahSerializer,
    AlasanPindahSerializer,
    KlasifikasiPindahSerializer,
    StatusKKTinggalSerializer,
    StatusKKPindahSerializer,
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
    SigBidang,
    SigPemilik,
    SigSadBidang,
    SigSadBidang2,
    SigDesa,
    SigRt,
    SigRw,
    SigDusun,
    SigDukuh,
    SigDukuh2,
    SigRt2,
    SigRw2,
    KategoriLapor,
    Lapor,
    Artikel,
    KategoriArtikel,
    Informasi,
    KategoriInformasi,
    Potensi,
    KategoriPotensi,
    SuratKelahiran,
    SuratSkck,
    SuratDomisili,
    JenisPindah,
    KlasifikasiPindah,
    AlasanPindah,
    StatusKKTinggal,
    StatusKKPindah,
    Slider,
)


def format_data_penduduk(data):
    cols = [
        "tgl_lahir",
        "tgl_exp_paspor",
        "tgl_kawin",
        "tgl_cerai",
    ]
    for col in cols:
        if type(data[col]) == pandas.Timestamp:
            data[col] = str(data[col]).split(" ")[0]
        else:
            data.pop(col)


def create_or_reactivate(model, filter_param, data):
    print(data)
    instance = model.all_objects.filter(**filter_param).dead().first()

    if instance:
        instance.deleted_by = None
        instance.deleted_at = None
        instance.save()

        model.objects.filter(pk=instance.pk).update(**data)
        instance.refresh_from_db()
    else:
        print(data)
        instance = model.objects.create(**data)
    instance.save()
    return instance


def create_or_reactivate_user(username, password):
    user = User.objects.filter(username=username).first()
    group = Group.objects.get(name="penduduk")

    if not user:
        user = User.objects.create(username=username)
        user.set_password(password)
        user.groups.add(group)
        user.save()
    elif not user.is_active:
        user.is_active = True
        user.set_password(password)
        user.save()
    return user


class CustomView(DynamicModelViewSet):
    def destroy(self, request, pk, format=None):
        data = self.get_object()
        data.deleted_by = request.user
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SadProvinsiViewSet(CustomView):
    queryset = SadProvinsi.objects.all()
    serializer_class = SadProvinsiSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PegawaiViewSet(CustomView):
    queryset = Pegawai.objects.all().order_by("id")
    serializer_class = PegawaiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BatasDesaViewSet(CustomView):
    queryset = BatasDesa.objects.all().order_by("id")
    serializer_class = BatasDesaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SadKabKotaViewSet(CustomView):
    queryset = SadKabKota.objects.all().order_by("id")
    serializer_class = SadKabKotaSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        provinsi = self.request.query_params.get("provinsi")
        if provinsi:
            return (
                SadKabKota.objects.all()
                .filter(provinsi_id=provinsi)
                .order_by("nama_kab_kota")
            )
        return SadKabKota.objects.all()


class SadKecamatanViewSet(CustomView):
    queryset = SadKecamatan.objects.all().order_by("id")
    serializer_class = SadKecamatanSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        kabkota = self.request.query_params.get("kabkota")
        if kabkota:
            return SadKecamatan.objects.filter(kab_kota_id=kabkota).all()
        return SadKecamatan.objects.all()


class SadDesaViewSet(CustomView):
    queryset = SadDesa.objects.all().order_by("id")
    serializer_class = SadDesaSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        kecamatan = self.request.query_params.get("kecamatan")
        if kecamatan:
            return SadDesa.objects.filter(kecamatan_id=kecamatan).all()
        return SadDesa.objects.all()

    @action(detail=False, permission_classes=[permissions.AllowAny])
    def me(self, request):
        desa = SadDesa.objects.get(pk=settings.DESA_ID)
        data = SadDesaSerializer(desa)
        return Response(data.data)


class SadDusunViewSet(CustomView):
    queryset = SadDusun.objects.all().order_by("id")
    serializer_class = SadDusunSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        desa = self.request.query_params.get("desa")
        if desa:
            return SadDusun.objects.filter(desa_id=desa).all()
        return SadDusun.objects.all()


class SadRwViewSet(CustomView):
    queryset = SadRw.objects.all().order_by("id")
    serializer_class = SadRwSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        dusun = self.request.query_params.get("dusun")
        if dusun:
            return SadRw.objects.filter(dusun=dusun).all()
        return SadRw.objects.all()


class SadRtViewSet(CustomView):
    queryset = SadRt.objects.all().order_by("id")
    serializer_class = SadRtSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        rw = self.request.query_params.get("rw")
        if rw:
            return SadRt.objects.filter(rw_id=rw).all()
        return SadRt.objects.all()


class SadKeluargaViewSet(DynamicModelViewSet):
    queryset = SadKeluarga.objects.all().order_by("id")
    serializer_class = SadKeluargaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        status = {
            "status": "success",
            "data_diinput": 0,
            "data_gagal": 0,
            "data_redundan": 0,
            "rt_tidak_ditemukan": 0,
        }

        file = request.FILES["file"]
        data = pandas.read_excel(file)
        if data[["no_kk", "rt"]].isna().values.any():
            message = "Silahkan lengkapi data no_kk dan rt"
            return Response({"message": message}, status=400)

        for item in data.to_dict("records"):

            rt = SadRt.objects.filter(rt=item["rt"]).first()
            item["rt"] = rt
            if not item["rt"]:
                status["rt_tidak_ditemukan"] += 1
                continue

            param_filter = {"no_kk": item["no_kk"]}
            try:
                create_or_reactivate(SadKeluarga, param_filter, item)
            except IntegrityError:
                status["data_redundan"] += 1
                continue
            except Exception:

                status["data_gagal"] += 1
                continue
            status["data_diinput"] += 1
        if not status["data_diinput"]:
            status["status"] = "failed"
        return Response(status)

    @action(detail=False, methods=["get"])
    def ekspor(self, request):
        with BytesIO() as b:
            writer = pandas.ExcelWriter(b)
            item = SadKeluarga.objects.all()
            serializer = SadKeluargaSerializer(item, many=True)
            df = pandas.DataFrame(serializer.data)
            df.reset_index(drop=True, inplace=True)
            df.to_excel(writer, sheet_name="Sheet1", index=0)
            writer.save()
            return HttpResponse(
                b.getvalue(),
                content_type=(
                    "application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet"
                ),
            )


class SadPendudukViewSet(CustomView):
    queryset = SadPenduduk.objects.all().order_by("id")
    serializer_class = SadPendudukSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        keluarga = self.request.query_params.get("keluarga")
        if keluarga:
            return SadPenduduk.objects.filter(keluarga_id=keluarga).all()
        return SadPenduduk.objects.all()

    @action(detail=False, methods=["post"])
    def upload(self, request):
        status = {
            "status": "success",
            "data_diinput": 0,
            "data_gagal": 0,
            "data_redundan": 0,
            "keluarga_tidak_ditemukan": 0,
        }

        file = request.FILES["file"]
        data = pandas.read_excel(file)
        if data[["nik", "keluarga", "nama"]].isna().values.any():
            message = "Silahkan lengkapi data nik, keluarga dan nama"
            return Response({"message": message}, status=400)
        data = data.replace({np.nan: None})

        for item in data.to_dict("record"):
            item["keluarga"] = SadKeluarga.objects.filter(
                no_kk=item["keluarga"]
            ).first()
            if not item["keluarga"]:
                status["keluarga_tidak_ditemukan"] += 1
                continue

            format_data_penduduk(item)
            param_filter = {"nik": item["nik"]}
            penduduk = create_or_reactivate(SadPenduduk, param_filter, item)
            try:
                penduduk = create_or_reactivate(
                    SadPenduduk, param_filter, item
                )

            except IntegrityError:
                status["data_redundan"] += 1
                continue
            except Exception as e:
                print(str(e))
                status["data_gagal"] += 1
                continue
            status["data_diinput"] += 1

            user = create_or_reactivate_user(
                item["nik"], item["tgl_lahir"].replace("-", "")
            )
            penduduk.user = user
            penduduk.save()

        if not status["data_diinput"]:
            status["status"] = "failed"
        return Response(status)

    @action(detail=False, methods=["get"])
    def ekspor(self, request):
        with BytesIO() as b:
            writer = pandas.ExcelWriter(b)
            item = SadPenduduk.objects.all()
            serializer = SadPendudukSerializer(item, many=True)
            df = pandas.DataFrame(serializer.data)
            df.reset_index(drop=True, inplace=True)
            df.to_excel(writer, sheet_name="Sheet1", index=0)
            writer.save()
            return HttpResponse(
                b.getvalue(),
                content_type=(
                    "application/vnd.openxmlformats-"
                    "officedocument.spreadsheetml.sheet"
                ),
            )


class SadKelahiranViewSet(CustomView):
    queryset = SadKelahiran.objects.all().order_by("id")
    serializer_class = SadKelahiranSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadKematianViewSet(CustomView):
    queryset = SadKematian.objects.all().order_by("id")
    serializer_class = SadKematianSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadLahirmatiViewSet(CustomView):
    queryset = SadLahirmati.objects.all().order_by("id")
    serializer_class = SadLahirmatiSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class JenisPindahViewSet(CustomView):
    queryset = JenisPindah.objects.all()
    serializer_class = JenisPindahSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class AlasanPindahViewSet(CustomView):
    queryset = AlasanPindah.objects.all()
    serializer_class = AlasanPindahSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class KlasifikasiPindahViewSet(CustomView):
    queryset = KlasifikasiPindah.objects.all()
    serializer_class = KlasifikasiPindahSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class StatusKKTinggalViewSet(CustomView):
    queryset = StatusKKTinggal.objects.all()
    serializer_class = StatusKKTinggalSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class StatusKKPindahViewSet(CustomView):
    queryset = StatusKKPindah.objects.all()
    serializer_class = StatusKKPindahSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadPindahKeluarViewSet(CustomView):
    queryset = SadPindahKeluar.objects.all().order_by("id")
    serializer_class = SadPindahKeluarSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=None):
        queryset = SadPindahKeluar.objects.all()
        sad_pindah = get_object_or_404(queryset, pk=pk)
        serializer = SadPindahKeluarSerializer(sad_pindah)
        data = serializer.data

        penduduk_s = sad_pindah.anggota_keluar()
        penduduk_data = []
        for item in penduduk_s:
            temp_data = {"nik": item.nik, "nama": item.nama}
            penduduk_data.append(temp_data)

        data["anggota_keluar"] = penduduk_data
        return Response(data)


class SadPindahMasukViewSet(CustomView):
    queryset = SadPindahMasuk.objects.all().order_by("id")
    serializer_class = SadPindahMasukSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadSarprasViewSet(CustomView):
    queryset = SadSarpras.objects.all().order_by("id")
    serializer_class = SadSarprasSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadInventarisViewSet(CustomView):
    queryset = SadInventaris.objects.all().order_by("id")
    serializer_class = SadInventarisSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadSuratViewSet(CustomView):
    queryset = SadSurat.objects.all().order_by("id")
    serializer_class = SadSuratSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SadDetailSuratViewSet(CustomView):
    queryset = SadDetailSurat.objects.all().order_by("id")
    serializer_class = SadDetailSuratSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SigSadBidangViewSet(CustomView):
    queryset = SigSadBidang.objects.all().order_by("id")
    serializer_class = SigSadBidangSerializer
    permission_classes = [permissions.IsAuthenticated]


class SigSadBidang2ViewSet(CustomView):
    queryset = SigSadBidang2.objects.all().order_by("id")
    serializer_class = SigSadBidang2Serializer
    permission_classes = [permissions.IsAuthenticated]


class SigBidangViewSet(CustomView):
    queryset = SigBidang.objects.all().order_by("id")
    serializer_class = SigBidangSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    @action(detail=False, methods=["get"])
    def me(self, request):
        user = request.user
        payload = {"id": user.id, "username": user.username}

        if hasattr(user.profile, 'pemilik'):
            pemilik = {
                'pemilik_warga': user.profile.pemilik.pemilik_warga,
            }
            payload["pemilik"] = pemilik
        return Response(payload)

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            rt = SigRt.objects.get(rt=item["properties"]["RT"])
            item = {
                "sig_rt": rt,
                "nbt": item["properties"]["NBT"],
                "geometry": item["geometry"],
            }
            SigBidang.objects.create(**item)

        return Response()


class SigPemilikViewSet(CustomView):
    queryset = SigPemilik.objects.all().order_by("id")
    serializer_class = SigPemilikSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SigDesaViewSet(CustomView):
    queryset = SigDesa.objects.all().order_by("id")
    serializer_class = SigDesaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            item = {
                "nama_desa": item["properties"]["topo_desa"],
                "luas": item["properties"]["Luas"],
                "keliling": item["properties"]["Keliling"],
                "geometry": item["geometry"],
            }
            SigDesa.objects.create(**item)

        return Response()


class SigDusunViewSet(CustomView):
    queryset = SigDusun.objects.all().order_by("id")
    serializer_class = SigDusunSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            desa = SigDesa.objects.get(
                nama_desa=item["properties"]["topo_desa"]
            )
            item = {
                "sig_desa": desa,
                "nama_dusun": item["properties"]["topo_dusun"],
                "luas": item["properties"]["Luas"],
                "keliling": item["properties"]["Keliling"],
                "geometry": item["geometry"],
            }
            SigDusun.objects.create(**item)
        return Response()


class SigDukuhViewSet(CustomView):
    queryset = SigDukuh.objects.all().order_by("id")
    serializer_class = SigDukuhSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            dusun = SigDusun.objects.get(
                nama_dusun=item["properties"]["topo_dusun"]
            )
            item = {
                "sig_dusun": dusun,
                "nama_dukuh": item["properties"]["topo_dukuh"],
                "luas": item["properties"]["Luas"],
                "keliling": item["properties"]["Keliling"],
                "geometry": item["geometry"],
            }
            SigDukuh.objects.create(**item)
        return Response()


class SigDukuh2ViewSet(CustomView):
    queryset = SigDukuh2.objects.all().order_by("id")
    serializer_class = SigDukuh2Serializer
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            desa = SigDesa.objects.get(
                nama_desa=item["properties"]["topo_desa"]
            )
            item = {
                "sig_desa": desa,
                "nama_dukuh": item["properties"]["topo_dukuh"],
                "luas": item["properties"]["Luas"],
                "keliling": item["properties"]["Keliling"],
                "geometry": item["geometry"],
            }
            SigDukuh2.objects.create(**item)
        return Response()


class SigRwViewSet(CustomView):
    queryset = SigRw.objects.all().order_by("id")
    serializer_class = SigRwSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            dukuh = SigDukuh.objects.get(
                nama_dukuh=item["properties"]["topo_dukuh"]
            )
            item = {
                "sig_dukuh": dukuh,
                "rw": item["properties"]["RW"],
                "geometry": item["geometry"],
            }
            SigRw.objects.create(**item)
        return Response()


class SigRw2ViewSet(CustomView):
    queryset = SigRw2.objects.all().order_by("id")
    serializer_class = SigRw2Serializer
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            dukuh2 = SigDukuh2.objects.get(
                nama_dukuh=item["properties"]["topo_dukuh"]
            )
            item = {
                "sig_dukuh2": dukuh2,
                "rw": item["properties"]["RW"],
                "geometry": item["geometry"],
            }
            SigRw2.objects.create(**item)
        return Response()


class SigRtViewSet(CustomView):
    queryset = SigRt.objects.all().order_by("id")
    serializer_class = SigRtSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            rw = SigRw.objects.get(rw=item["properties"]["RW"])
            item = {
                "sig_rw": rw,
                "rt": item["properties"]["RT"],
                "geometry": item["geometry"],
            }
            SigRt.objects.create(**item)
        return Response()


class SigRt2ViewSet(CustomView):
    queryset = SigRt2.objects.all().order_by("id")
    serializer_class = SigRt2Serializer
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=False, methods=["post"])
    def upload(self, request):
        file = request.FILES["file"]
        data = json.load(file)

        for item in data["features"]:
            rw2 = SigRw2.objects.get(rw=item["properties"]["RW"])
            item = {
                "sig_rw2": rw2,
                "rt": item["properties"]["RT"],
                "geometry": item["geometry"],
            }
            SigRt2.objects.create(**item)
        return Response()


class KategoriArtikelViewSet(DynamicModelViewSet):
    queryset = KategoriArtikel.objects.all().order_by("id")
    serializer_class = KategoriArtikelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArtikelViewSet(DynamicModelViewSet):
    queryset = Artikel.objects.all().order_by("id")
    serializer_class = ArtikelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SliderViewSet(DynamicModelViewSet):
    queryset = Slider.objects.all().order_by("id")
    serializer_class = SliderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SliderViewSet(DynamicModelViewSet):
    queryset = Slider.objects.all().order_by("id")
    serializer_class = SliderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SliderViewSet(DynamicModelViewSet):
    queryset = Slider.objects.all().order_by("id")
    serializer_class = SliderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KategoriLaporViewSet(DynamicModelViewSet):
    queryset = KategoriLapor.objects.all().order_by("id")
    serializer_class = KategoriLaporSerializer
    permission_classes = [permissions.IsAuthenticated]


class LaporViewSet(DynamicModelViewSet):
    queryset = Lapor.objects.all().order_by("id")
    serializer_class = LaporSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kategori = self.request.query_params.get("kategori")
        if kategori:
            return Lapor.objects.filter(kategori=kategori).all()
        return Lapor.objects.all()

class KategoriInformasiViewSet(DynamicModelViewSet):
    queryset = KategoriInformasi.objects.all().order_by("id")
    serializer_class = KategoriInformasiSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class InformasiViewSet(DynamicModelViewSet):
    queryset = Informasi.objects.all().order_by("id")
    serializer_class = InformasiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KategoriPotensiViewSet(DynamicModelViewSet):
    queryset = KategoriPotensi.objects.all().order_by("id")
    serializer_class = KategoriPotensiSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PotensiViewSet(DynamicModelViewSet):
    queryset = Potensi.objects.all().order_by("id")
    serializer_class = PotensiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kategori = self.request.query_params.get("kategori")
        if kategori:
            return Potensi.objects.filter(kategori=kategori).all()
        return Potensi.objects.all()


class SuratKelahiranViewSet(DynamicModelViewSet):
    queryset = SuratKelahiran.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.groups.first().name == "admin":
            return AdminSuratKelahiranSerializer
        return SuratKelahiranSerializer

    @action(detail=True, methods=["get"])
    def print(self, request, pk=None):
        data = self.get_object()
        pdf = render_mail("skl", data)
        return HttpResponse(pdf, content_type="application/pdf")


class SuratSkckViewSet(DynamicModelViewSet):
    queryset = SuratSkck.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.groups.first().name == "admin":
            return AdminSuratSkckSerializer
        return SuratSkckSerializer

    @action(detail=True, methods=["get"])
    def print(self, request, pk=None):
        data = self.get_object()
        pdf = render_mail("skck", data)
        return HttpResponse(pdf, content_type="application/pdf")


class SuratDomisiliViewSet(DynamicModelViewSet):
    queryset = SuratDomisili.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.groups.first().name == "admin":
            return AdminSuratDomisiliSerializer
        return SuratDomisiliSerializer

    @action(detail=True, methods=["get"])
    def print(self, request, pk=None):
        data = self.get_object()
        pdf = render_mail("skd", data)
        return HttpResponse(pdf, content_type="application/pdf")
