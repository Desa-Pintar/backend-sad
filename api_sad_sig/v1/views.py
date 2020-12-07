from django.contrib.auth.models import User, Group
from rest_framework import permissions
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import action
from rest_framework.response import Response
import pandas
import json
from io import BytesIO
from django.http import HttpResponse

from .serializers import (
  UserSerializer,
  GroupSerializer,
  PegawaiSerializer,
  SadProvinsiSerializer,
  SadKabKotaSerializer,
  SadKecamatanSerializer,
  SadDesaSerializer,
  SadDusunDukuhSerializer,
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
  KategoriPotensiSerializer,
  PotensiSerializer,
  KategoriInformasiSerializer,
  InformasiSerializer,
  PotensiSerializer,
  KategoriPotensiSerializer,
)

from .models import (
  Pegawai,
  SadProvinsi,
  SadKabKota,
  SadKecamatan,
  SadDesa,
  SadDusunDukuh,
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
)


class UserViewSet(DynamicModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['get'])
  def me (self, request):
    data = UserSerializer(request.user)
    return Response(data.data)

class GroupViewSet(DynamicModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['get'])
  def me (self, request):
    data = GroupSerializer(request.user)
    return Response(data.data)

class PegawaiViewSet(DynamicModelViewSet):
  queryset = Pegawai.objects.all().order_by('id')
  serializer_class = PegawaiSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadProvinsiViewSet(DynamicModelViewSet):
  queryset = SadProvinsi.objects.all().order_by('id')
  serializer_class = SadProvinsiSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadKabKotaViewSet(DynamicModelViewSet):
  queryset = SadKabKota.objects.all().order_by('id')
  serializer_class = SadKabKotaSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadKecamatanViewSet(DynamicModelViewSet):
  queryset = SadKecamatan.objects.all().order_by('id')
  serializer_class = SadKecamatanSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadDesaViewSet(DynamicModelViewSet):
  queryset = SadDesa.objects.all().order_by('id')
  serializer_class = SadDesaSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadDusunDukuhViewSet(DynamicModelViewSet):
  queryset = SadDusunDukuh.objects.all().order_by('id')
  serializer_class = SadDusunDukuhSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadRwViewSet(DynamicModelViewSet):
  queryset = SadRw.objects.all().order_by('id')
  serializer_class = SadRwSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadRtViewSet(DynamicModelViewSet):
  queryset = SadRt.objects.all().order_by('id')
  serializer_class = SadRtSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadKeluargaViewSet(DynamicModelViewSet):
  queryset = SadKeluarga.objects.all().order_by('id')
  serializer_class = SadKeluargaSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
      file = request.FILES['file']
      data = pandas.read_excel(file)
      for item in data.to_dict('records'):
        item['rt'] = SadRt.objects.get(id=item['rt'])
        SadKeluarga.objects.create(**item)
      return Response()

  @action(detail=False, methods=['get'])
  def ekspor (self, request):
    with BytesIO() as b:
      writer = pandas.ExcelWriter(b)
      item = SadKeluarga.objects.all()
      serializer = SadKeluargaSerializer(item, many=True)
      df = pandas.DataFrame(serializer.data)
      df.to_excel(writer, sheet_name='Sheet1')
      writer.save()
      return HttpResponse(b.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

class SadPendudukViewSet(DynamicModelViewSet):
  queryset = SadPenduduk.objects.all().order_by('id')
  serializer_class = SadPendudukSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = pandas.read_excel(file)
    for item in data.dropna(axis=1).to_dict('records'):
      item['keluarga'] = SadKeluarga.objects.get(id=item['keluarga'])

      SadPenduduk.objects.create(**item)

    return Response()

  @action(detail=False, methods=['get'])
  def ekspor (self, request):
    with BytesIO() as b:
      writer = pandas.ExcelWriter(b)
      item = SadPenduduk.objects.all()
      serializer = SadPendudukSerializer(item, many=True)
      df = pandas.DataFrame(serializer.data)
      df.to_excel(writer, sheet_name='Sheet1')
      writer.save()
      return HttpResponse(b.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

class SadKelahiranViewSet(DynamicModelViewSet):
  queryset = SadKelahiran.objects.all().order_by('id')
  serializer_class = SadKelahiranSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadKematianViewSet(DynamicModelViewSet):
  queryset = SadKematian.objects.all().order_by('id')
  serializer_class = SadKematianSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadLahirmatiViewSet(DynamicModelViewSet):
  queryset = SadLahirmati.objects.all().order_by('id')
  serializer_class = SadLahirmatiSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadPindahKeluarViewSet(DynamicModelViewSet):
  queryset = SadPindahKeluar.objects.all().order_by('id')
  serializer_class = SadPindahKeluarSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadPindahMasukViewSet(DynamicModelViewSet):
  queryset = SadPindahMasuk.objects.all().order_by('id')
  serializer_class = SadPindahMasukSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadSarprasViewSet(DynamicModelViewSet):
  queryset = SadSarpras.objects.all().order_by('id')
  serializer_class = SadSarprasSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadInventarisViewSet(DynamicModelViewSet):
  queryset = SadInventaris.objects.all().order_by('id')
  serializer_class = SadInventarisSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadSuratViewSet(DynamicModelViewSet):
  queryset = SadSurat.objects.all().order_by('id')
  serializer_class = SadSuratSerializer
  permission_classes = [permissions.IsAuthenticated]

class SadDetailSuratViewSet(DynamicModelViewSet):
  queryset = SadDetailSurat.objects.all().order_by('id')
  serializer_class = SadDetailSuratSerializer
  permission_classes = [permissions.IsAuthenticated]

class SigBidangViewSet(DynamicModelViewSet):
  queryset = SigBidang.objects.all().order_by('id')
  serializer_class = SigBidangSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = pandas.read_excel(file)
    for item in data.dropna(axis=1).to_dict('records'):

      SigBidang.objects.create(**item)

    return Response()

class SigDesaViewSet(DynamicModelViewSet):
  queryset = SigDesa.objects.all().order_by('id')
  serializer_class = SigDesaSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      item = {
        'nama_desa': item['properties']['topo_desa'],
        'luas': item['properties']['Luas'],
        'keliling': item['properties']['Keliling'],
        'geometry': item['geometry'],
      }
      SigDesa.objects.create(**item)
    
    return Response()

class SigDusunViewSet(DynamicModelViewSet):
  queryset = SigDusun.objects.all().order_by('id')
  serializer_class = SigDusunSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      desa = SigDesa.objects.get (nama_desa=item['properties']['topo_desa'])
      item = {
        'sig_desa': desa,
        'nama_dusun': item['properties']['topo_dusun'],
        'luas': item['properties']['Luas'],
        'keliling': item['properties']['Keliling'],
        'geometry': item['geometry'],
      }
      SigDusun.objects.create(**item)
    return Response()

class SigDukuhViewSet(DynamicModelViewSet):
  queryset = SigDukuh.objects.all().order_by('id')
  serializer_class = SigDukuhSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      dusun = SigDusun.objects.get (nama_dusun=item['properties']['topo_dusun'])
      item = {
        'sig_dusun': dusun,
        'nama_dukuh': item['properties']['topo_dukuh'],
        'luas': item['properties']['Luas'],
        'keliling': item['properties']['Keliling'],
        'geometry': item['geometry'],
      }
      SigDukuh.objects.create(**item)
    return Response()

class SigDukuh2ViewSet(DynamicModelViewSet):
  queryset = SigDukuh2.objects.all().order_by('id')
  serializer_class = SigDukuh2Serializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      desa = SigDesa.objects.get (nama_desa=item['properties']['topo_desa'])
      item = {
        'sig_desa': desa,
        'nama_dukuh': item['properties']['topo_dukuh'],
        'luas': item['properties']['Luas'],
        'keliling': item['properties']['Keliling'],
        'geometry': item['geometry'],
      }
      SigDukuh2.objects.create(**item)
    return Response()

class SigRwViewSet(DynamicModelViewSet):
  queryset = SigRw.objects.all().order_by('id')
  serializer_class = SigRwSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      dukuh = SigDukuh.objects.get (nama_dukuh=item['properties']['topo_dukuh'])
      item = {
        'sig_dukuh': dukuh,
        'rw': item['properties']['RW'],
        'geometry': item['geometry'],
      }
      SigRw.objects.create(**item)
    return Response()

class SigRw2ViewSet(DynamicModelViewSet):
  queryset = SigRw2.objects.all().order_by('id')
  serializer_class = SigRw2Serializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      dukuh2 = SigDukuh2.objects.get (nama_dukuh=item['properties']['topo_dukuh'])
      item = {
        'sig_dukuh2': dukuh2,
        'rw': item['properties']['RW'],
        'geometry': item['geometry'],
      }
      SigRw2.objects.create(**item)
    return Response()

class SigRtViewSet(DynamicModelViewSet):
  queryset = SigRt.objects.all().order_by('id')
  serializer_class = SigRtSerializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      rw = SigRw.objects.get (rw=item['properties']['RW'])
      item = {
        'sig_rw': rw,
        'rt': item['properties']['RT'],
        'geometry': item['geometry'],
      }
      SigRt.objects.create(**item)
    return Response()

class SigRt2ViewSet(DynamicModelViewSet):
  queryset = SigRt2.objects.all().order_by('id')
  serializer_class = SigRt2Serializer
  permission_classes = [permissions.IsAuthenticated]
  @action(detail=False, methods=['post'])
  def upload (self, request):
    file = request.FILES['file']
    data = json.load(file)

    for item in data['features']:
      rw2 = SigRw2.objects.get (rw=item['properties']['RW'])
      item = {
        'sig_rw2': rw2,
        'rt': item['properties']['RT'],
        'geometry': item['geometry'],
      }
      SigRt2.objects.create(**item)
    return Response()

class KategoriArtikelViewSet(DynamicModelViewSet):
  queryset = KategoriArtikel.objects.all().order_by('id')
  serializer_class = KategoriArtikelSerializer
  permission_classes = [permissions.IsAuthenticated]

class ArtikelViewSet(DynamicModelViewSet):
  queryset = Artikel.objects.all().order_by('id')
  serializer_class = ArtikelSerializer
  permission_classes = [permissions.IsAuthenticated]

class KategoriLaporViewSet(DynamicModelViewSet):
  queryset = KategoriLapor.objects.all().order_by('id')
  serializer_class = KategoriLaporSerializer
  permission_classes = [permissions.IsAuthenticated]

class LaporViewSet(DynamicModelViewSet):
  queryset = Lapor.objects.all().order_by('id')
  serializer_class = LaporSerializer
  permission_classes = [permissions.IsAuthenticated]

class KategoriInformasiViewSet(DynamicModelViewSet):
  queryset = KategoriInformasi.objects.all().order_by('id')
  serializer_class = KategoriInformasiSerializer
  permission_classes = [permissions.IsAuthenticated]

class InformasiViewSet(DynamicModelViewSet):
  queryset = Informasi.objects.all().order_by('id')
  serializer_class = InformasiSerializer
  permission_classes = [permissions.IsAuthenticated]

class KategoriPotensiViewSet(DynamicModelViewSet):
  queryset = KategoriPotensi.objects.all().order_by('id')
  serializer_class = KategoriPotensiSerializer
  permission_classes = [permissions.IsAuthenticated]

class PotensiViewSet(DynamicModelViewSet):
  queryset = Potensi.objects.all().order_by('id')
  serializer_class = PotensiSerializer
  permission_classes = [permissions.IsAuthenticated]