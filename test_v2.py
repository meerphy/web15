from requests import get, post, delete


# print(get('http://localhost:8080/api/v2/news').json())
# print(get('http://localhost:8080/api/v2/news&999').json())
# print(get('http://localhost:8080/api/v2/news&2').json())
# новости с id = 999 нет в базе
# print(get('http://localhost:8080/api/v2/news&q').json())
# print(post('http://localhost:8080/api/v2/news',
#             json={'title': 'Заголовок_22',
#                   'content': 'Текст новости, добавленной через API_v2',
#                   'user_id': 2,
#                   'is_private': False}).json())
# print(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Заголовок_не_сущ',
#                  'content': 'Пользователь не существует',
#                  'user_id': 1,
#                  'is_private': False}).json())
# print(delete('http://localhost:8080/api/v2/news&999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:8080/api/news&1').json())
