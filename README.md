# Admitad
Для генерации PDF-файлов использовал библиотеку [WeasyPrint](https://github.com/Kozea/WeasyPrint?ysclid=lp71uh2cni205206502)
## Задача

Сервис для генерации PDF.
Необходимо разработать сервис, который на вход принимает ссылку на страницу или HTML-файл, а в ответ выдает PDF-файл.


Если на вход приходит ссылка, то сервис идет по ссылке и делает из нее PDF.
Если на вход приходит HTML-файл, то сервис превращает его в PDF.


Обязательный стэк: 
Django, DRF, Docker, Celery


Ожидание по результату: сервис, который легко развернуть и приятно использовать
Фронт вообще не важен.

### Предисловие
В данном случае сгенерированные PDF-файлы хранятся локально, в реальном проекте я бы использовал удаленные хранилища, например Amazon S3.
Также для удобства я не выносил в переменные окружения юзернеймы, пароли к бд и прочее, надеюсь это не будет проблемой

## Установка и запуск
```
git clone https://github.com/IsThatASkyline/admitad.git
cd admitad
docker-compose up --build
```

## Примеры использования
#### (тестировалось через Postman)

### Отправка html-файла
POST-запрос с телом запроса **file: mypage.html** на адрес:
```
http://127.0.0.1:8000/api/v1/converter/html2pdf/
```
в ответ мы получим ссылку на сгенерированный PDF-файл, например:
```
http://127.0.0.1:8000/media/a4e44801-b6e0-4d88-b7ca-b298b003f99f.pdf
```
### Отправка url-ссылки
POST-запрос с телом запроса **url: google.com** на адрес:
```
http://127.0.0.1:8000/api/v1/converter/url2pdf/
```
в ответ мы получим ссылку на сгенерированный PDF-файл, например:
```
http://127.0.0.1:8000/media/a4e44801-b6e0-4d88-b7ca-b298b003f99f.pdf
```
#### Важно:
Так как я использовал Celery для фоновой генерации PDF-файлов, если моментально перейти по сгенерированной ссылке, можно получить 404 ошибку, так как файл просто не успел сгенерироваться, в ответ на такие запросы 
можно отвечать ***'Файл находится в обработке'*** и тому подобное

## Обработка ошибок
Я предусмотрел обработку таких случаев как:
- В теле запроса нет ключа **file** для html-файлов, либо **url** для url-ссылок
- Неверный формат файла (поддерживается только .html)
- Неверно задан url