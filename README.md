# Restaurant Table Reservation API

Проект представляет собой REST API-сервис для управления столиками и бронями в ресторане. Реализован на Django с использованием Django REST Framework и разворачивается в Docker-среде с PostgreSQL.

---

## Функциональность

- CRUD для столиков (Table):
    
    - GET /api/tables/ — список всех столиков
        
    - POST /api/tables/ — создать новый столик
        
    - DELETE /api/tables/{id}/ — удалить столик
        
- CRUD для бронирований (Reservation):
    
    - GET /api/reservations/ — список всех броней
        
    - POST /api/reservations/ — создать бронь
        
    - DELETE /api/reservations/{id}/ — удалить бронь
        
- Бизнес-логика:
    
    - Нельзя создать бронь, если указанный стол уже занят в этот временной интервал (реализована проверка пересечений).
        

---

## Запуск проекта

### 1. Клонировать репозиторий:

```bash
git clone https://github.com/M0rnstar/restaurant-reservation-api.git
cd restaurant-reservation-api
```

### 2. Запустить проект через Docker Compose:

```bash
docker-compose up --build
```

### 3. Применить миграции:

```bash
docker-compose exec web python manage.py migrate
```

### 4. Открыть в браузере:

- API: [http://localhost:8000/api/](http://localhost:8000/api/)

---

## Пример запроса (создание брони)

`POST /api/reservations/`

```json
{
  "customer_name": "Иван",
  "table": 1,
  "reservation_time": "2025-04-14T18:00:00Z",
  "duration_minutes": 90
}
```

---

## Тестирование

### Запуск автотестов:

```bash
docker-compose exec web pytest
```

### Покрытые сценарии:

- Успешное создание брони
    
- Блокировка при пересечении по времени
    
- Создание столика через сериализатор
    

---

## Зависимости

Все зависимости перечислены в `requirements.txt`, сформированы внутри Docker-контейнера:

```bash
docker-compose exec web pip freeze > requirements.txt
```

---

## Используемые технологии

- Python 3.11
    
- Django 5.2
    
- Django REST Framework
    
- PostgreSQL
    
- Docker + docker-compose
    
- Pytest
    

---

## Автор

M0rnstar 
github.com/M0rnstar
---