# tree_divisions

Проект Django. 

## Технологии:
Серверная часть: Django: 5.1.2, Python: 3.10, База данных: PostgreSQL Клиентская часть: HTML/CSS/Bootstrap

## Описание функциональности
1. Реализованы древовидные модели отделов компании и 3 сущности (модели). Настроена админ-панель Django. 
   
Пример древовидных моделей(дерево отображается в свернутом виде)
![image](https://github.com/user-attachments/assets/585348a5-110b-41ac-bd88-e2ff79f57f4b)

Пример на клиенте: 
![image](https://github.com/user-attachments/assets/c6bd4c70-c708-4ee2-b6b1-5673b015d61d)

Пример страницы детальной информации об отделе:
![image](https://github.com/user-attachments/assets/e10d9f59-6578-4094-a0e7-5adef71469de)

Пример списка сотрудников с указанием их отдела:
![image](https://github.com/user-attachments/assets/b49509ec-7e57-44e3-b443-6eb2dbb9a2e3)

2. Информация о сотруднике хранится в модели Employee:
   Данные: ФИО, должность (отдельная связь ForeignKey), дата приема на работу, зарплата, отдел (связь через TreeForeignKey)
   Модель Employee имеет связь OneToOneField с базовой моделью User.
Пример:  ![image](https://github.com/user-attachments/assets/532ea935-158e-48d4-89f4-37254f699e3e)

3. Применен Bootstrap для стилей. 

4. В папке fixtures есть файл users_data.json (база на 50 000 тысяч пользователей), сгенерировал юзеров и тестировал возможность заполнения моделей через json.
   Ссылка на доку по теме: https://docs.djangoproject.com/en/5.1/howto/initial-data/#providing-data-with-fixtures
   Добавил несколько иерархий и их подразделений.

5. Подключил к проекту PostgreSQL и настроил python-dotenv.

Все зависимости есть в requirements.txt .
Полезные ссылки по теме проекта: https://django-mptt.readthedocs.io/en/latest/ , https://pypi.org/project/python-dotenv/ , https://docs.djangoproject.com/en/5.1/howto/initial-data/#providing-data-with-fixtures 


## Установка
1. Клонируйте репозиторий. 2. Перейдите в папку проекта. 3. Установите зависимости: pip install -r requirements.txt 4. Настройте базу данных в файле settings.py. 5. Выполните миграции: py manage.py makemigrations > python manage.py migrate 6. Запустите сервер: py manage.py runserver

## Настройка окружения
Убедитесь, что у вас установлен Python версии [3.10].

## Лицензия
Проект распространяется под лицензией MIT.

## Контакты
Разработчик: Артур Сахаров Telegram: grizz_dev
