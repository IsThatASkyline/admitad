import pathlib

from mysite.celery_app import app
from weasyprint import HTML


@app.task
def process_html(html_path: str, pdf_path: str):
    file = HTML(html_path)
    file.write_pdf(target=pdf_path)
    file = pathlib.Path(html_path)
    file.unlink()


@app.task
def process_url(url: str, path: str):
    file = HTML(url=url)
    file.write_pdf(target=path)
