from django.urls import path, re_path

from .views import (
    ArtikelListView,
    ArtikelDetailView,
    KategoriListView,
    ArtikelCreateView,
    ArtikelManageView,
    ArtikelDeteleView,
    ArtikelUpdateView,
)

app_name = 'artikel'
urlpatterns = [
    re_path(r'manage/update/(?P<pk>\d+)$',
            ArtikelUpdateView.as_view(), name='update'),
    re_path(r'manage/delete/(?P<pk>\d+)$',
            ArtikelDeteleView.as_view(), name='delete'),
    path('manage/', ArtikelManageView.as_view(), name='manage'),
    re_path(r'kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$',
            KategoriListView.as_view(), name='category'),
    re_path(r'detail/(?P<slug>[\w-]+)$',
            ArtikelDetailView.as_view(), name='detail'),
    re_path(r'(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
    path('create/', ArtikelCreateView.as_view(), name='create'),

]
