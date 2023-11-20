from django.urls import path, include
from api.converter.views import HtmlToPdfApi, UrlToPdfApi


converter_patterns = [
        path('html2pdf/', HtmlToPdfApi.as_view(), name='html2pdf'),
        path('url2pdf/', UrlToPdfApi.as_view(), name='url2pdf'),
]

urlpatterns = [
    path('converter/', include((converter_patterns, 'converter'))),
]
