# TicketReserv
ендпоинты:

регистрация пользователя
http://127.0.0.1:8000/user/api/v0/registration/ 
POST-запрос и BODY :
{
	"email": "borbaris131@gmail.com", 
	"password": "12345",
	"first_name": "Artem",
	"last_name": "Krutsevich"
}

аутентификация с помощь JWT-токена. В headers ответ и ключ.
http://127.0.0.1:8000/user/api/v0/authenticate_user/
POST-запрос и BODY:
{
	"email": "borbaris131@gmail.com",
	"password": "12345"
}

просмотр билетов и информации пользователя
http://127.0.0.1:8000/user/api/v0/lk/my-tickets/


создание сеанса
http://127.0.0.1:8000/film_session/api/v0/create/
POST-запрос и BODY:
{
	"beginning_session": "20:00",
	"ticket":
		{"price": 120}
		,
	"hall" : "red",
	"film": "Star Wars: Episod 1"
}

просмотр сеансов
http://127.0.0.1:8000/film_session/api/v0/all/
GET-запрос и BODY:
В headers.Authorization хранится токен

создание фильма
http://127.0.0.1:8000/films/api/v0/create/
POST-запрос и BODY:
В headers.Authorization хранится токен
{
 "title": "Star Wars 1",
 "duration": 120
}

просмотро фильмов
http://127.0.0.1:8000/films/api/v0/all/
GET-запрос, просмотреть любой может.


резервирование билета 
http://127.0.0.1:8000/tickets/api/v0/reserv/
PATCH-запрос и BODY:
В headers.Authorization хранится токен
{
	"session": "20:00",
	"row": 4,
	"seat": 9
}

API проверял через POSTMAN. Не сделана система покупки и отмена бронирования.
Администраторы создаются через c помощью запроса
user = User.objects.get(email)
user.is_staff = True
user.save()