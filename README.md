Проект по бронированию туров
Technologies: Python, FLASK, Bootstrap
Сайт состоит из 3 страниц:
Главная страница

В меню выводится список направлений, при клике на направление мы переходим на страницу направления.
При клике на карточку мы переходим на страницу тура.
Список по направлению

На странице направления выводится заголовок.
В подзаголовке выводится количество найденного, максимальные и минимальные значения.
При клике на карточку мы переходим на страницу тура.
Страница тура

В заголовке выводится название локации и количество звезд.
В подзаголовке выведится страна, длительность.
А также кнопка, которая будет вести на внешний ресурс.
Для запуска приложения локально: открываем терминал, переходим в дерикторию проекта и выполняем следующие команды:

pip install -r requirements.txt

python manage.py migrate --run-syncdb

python manage.py makemigrations

python manage.py runserver

Далее открываем в браузере следующую страницу http://127.0.0.1:8000/.