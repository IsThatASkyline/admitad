from rest_framework.response import Response
from rest_framework.views import APIView
from weasyprint.urls import URLFetchingError
from .services import process_url, process_html


class HtmlToPdfApi(APIView):

    def post(self, request):
        try:
            file = request.FILES['file']
        except KeyError:
            return Response({'detail': 'В теле запроса необходимо указать ключ \'file\' и с ним передать html-файл'})

        try:
            path = process_html(file)
            return Response(
                {'data':
                     {'pdf_url': f'{request.get_host()}{path}'},
                 },
            )
        except TypeError:
            return Response({'detail': 'Ошибка, поддерживаются только html-файлы'})
        except Exception:
            return Response({'detail': 'Ошибка при обработке файла'})


class UrlToPdfApi(APIView):

    def post(self, request):
        try:
            url = request.data['url']
        except KeyError:
            return Response({'detail': 'В теле запроса необходимо указать ключ \'url\' и с ним передать ссылку на страницу'})

        try:
            path = process_url(url)
            return Response(
                {'data':
                     {'pdf_url': f'{request.get_host()}{path}'},
                },
            )
        except URLFetchingError:
            return Response({'detail': 'Ошибка, проверьте указанный url и повторите попытку'})
        except Exception:
            return Response({'detail': 'Ошибка при обработке страницы'})
