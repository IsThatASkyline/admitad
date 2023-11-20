import time

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from api.converter import tasks


def process_html(file: InMemoryUploadedFile) -> str:
    if not file.name.endswith('.html'):
        raise TypeError
    name = time.strftime("%Y-%m-%d--%H-%M-%S")
    pdf_path = f'{settings.MEDIA_ROOT}/{name}.pdf'
    html = f'{settings.MEDIA_ROOT}/{name}.html'
    with open(html, 'w') as f:
        f.write(str(file.read().decode('utf-8')))
    tasks.process_html.delay(html, pdf_path)

    return f'{settings.MEDIA_URL}{name}.pdf'


def process_url(url: str) -> str:
    name = time.strftime("%Y-%m-%d--%H-%M-%S")
    path = f'{settings.MEDIA_ROOT}/{name}.pdf'
    tasks.process_url.delay(url, path)
    return f'{settings.MEDIA_URL}{name}.pdf'
