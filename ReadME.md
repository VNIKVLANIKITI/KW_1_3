В данном репозитории содержится Курсовой проект на тему сераиса рассылок
Требования:
1) список рассылок, отчет проведенных рассылок отдельно, создание рассылки, удаление рассылки,
2) создание пользователя, удаление пользователя, редактирование пользователя.
3) логика работы системы:
- После создания новой рассылки, если текущие дата и время больше даты и времени начала и меньше даты и времени окончания, должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
- Если создается рассылка с временем старта в будущем, отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя сервиса.
- По ходу отправки рассылки должна собираться статистика (см. описание сущностей «Рассылка» и «Попытка» выше) по каждой рассылке для последующего формирования отчетов. Попытка создается одна для одной рассылки. Формировать попытки рассылки для всех клиентов отдельно не нужно.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.
4) Интерфейс понятен и соответствует базовым требованиям системы.
5) Все интерфейсы для изменения и создания сущностей, не относящиеся к стандартной админке, реализовали с помощью Django-форм.
6) Все настройки прав доступа реализовали верно.
7) Приложены фикстуры или созданы команды для заполнения базы данных

!!!!!!Отработка замечаний (2 итерация) !!!!!:
+ 1) Корректно собран шаблон файла .env. = - [x] Добавил файл шаблона
+ 2) На главной странице выводится необходимая информация по ТЗ. = - [x] Добавил URL и Шаблон 
3) В шаблон главной страницы передается контекст с необходимыми данными по ТЗ.
4) Шаблон главной страницы отображает данные корректно.
+ 5) Создана команда для наполнения базы данных группой «Менеджеры». = - [x] Добавил команду "create_managers"
+ 6) Каждый пользователь имеет доступ только к своим рассылкам. = - [x] Учел в запросе объектов фильтрацию по создателю "поле creater" ```*.objects.filter(creator=request.user)```
+ 7) Каждый пользователь имеет доступ только к своим получателям рассылки. = - [x] Учел в запросе объектов фильтрацию по создателю "поле creater" ```*.objects.filter(creator=request.user)```
+ 8) Реализованы проверки в шаблонах для ограничения доступа к сущностям. = - [x] Применил условие аутентификации в шаблонах Сообщений и Получателей ```{% if user.is_authenticated %}```
+ 9) В контроллерах переопределены QuerySet’ы для фильтрации по владельцам. = - [x] Учел в запросе объектов фильтрацию по создателю "поле creater" ```*.objects.filter(creator=request.user)```
+ 10) Настроено серверное кеширование = - [x] Добавил возможности кэширования при запросе списка рассылок
+ 11) Реализована отправка рассылки через командную строку (кастомной командой). = - [x] Создал функцию send_yandex_email в "tasks.py"

Рекомендации по улучшению:

+ Сейчас у тебя в репозитории расположен .env с чувствительными данными, необходимо создать шаблон .env.sample, с переменными окружения без значений.
+ В данный момент не скрыта навигация по сайту для неавторизованных пользователей.
Отправку сообщений рассылок необходимо осуществлять через smtp сервер, например yandex. У вас были домашние работы с его использованием.