from requests import get, post, delete


# print(get('http://localhost:8080/api/news').json())
# print(get('http://localhost:8080/api/news&1').json())
# print(get('http://localhost:8080/api/news&999').json())
# новости с id = 999 нет в базе
# print(get('http://localhost:8080/api/news&q').json())
# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости, добавленной через API',
#                  'user_id': 2,
#                  'is_private': False}).json())
# print(post('http://localhost:8080/api/news',
#            json={'title': 'Заголовок_не_сущ',
#                  'content': 'Пользователь не существует',
#                  'user_id': 1,
#                  'is_private': False}).json())

# print(delete('http://localhost:8080/api/news&999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:8080/api/news&1').json())
