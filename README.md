## **Yatube API**

Реализация API при помощи Django REST Framework (DRF)

_Реализованные возможности при помощи API запросов:_

+ Регистрация нового юзера
+ Смена пароля зарегестрированного юзера
+ Получение спика постов для зарегестрированных пользователей
+ Создание, удаление и редактирование (CRUD) поста (by author)
+ Просмотр списка групп для зарегестрированных пользователей
+ Добавление и редактирование комментариев к конкретному посту
+ Подписки

_Используемые инструменты_

1. Python 3.7
2. djangorestframework==3.12.4
3. 

## Setup
```
$ git clone https://github.com/RBekr/api_final_yatube.git
$ cd api_final_yatube
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ cd yatube_pi
$ python manage.py runserver
```
## Examples

`GET /api/v1/posts/`
`GET /api/v1/posts/{id}/`

[__Автор: Руслан__](https://github.com/RBekr)
_email_: r.bekrenyov@mail.ru