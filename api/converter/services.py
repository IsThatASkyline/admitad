import uuid

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile

from api.converter import tasks


def process_html(file: InMemoryUploadedFile) -> str:
    if not file.name.endswith(".html"):
        raise TypeError

    name = uuid.uuid4()
    pdf_path = f"{settings.MEDIA_ROOT}/{name}.pdf"
    byte_str = file.file.getvalue()
    text_obj = byte_str.decode("UTF-8")
    tasks.process_html.delay(text_obj, pdf_path)
    return f"{settings.MEDIA_URL}{name}.pdf"


def process_url(url: str) -> str:
    name = uuid.uuid4()
    pdf_path = f"{settings.MEDIA_ROOT}/{name}.pdf"
    tasks.process_url.delay(url, pdf_path)
    return f"{settings.MEDIA_URL}{name}.pdf"
