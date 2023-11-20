from weasyprint import HTML

from mysite.celery_app import app


@app.task
def process_html(html: str, pdf_path: str):
    file = HTML(string=str(html))
    file.write_pdf(target=pdf_path)


@app.task
def process_url(url: str, path: str):
    file = HTML(url=url)
    file.write_pdf(target=path)
