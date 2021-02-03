### EMS APP

Python 3.8

### Install
- pip install -r requirements.txt

### Run
- Add ".env" config file to "ems_django" directory.
- Run: 
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


### Get API Token
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}' \
  http://localhost:8000/api/token/
```

### Refresh token

```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<REFRESH-TOKEN>"}' \
  http://localhost:8000/api/token/refresh/

```
### Get some data

```
curl \
  -H "Authorization: Bearer <TOKEN>" \
  http://127.0.0.1:8000/api/entrance_exit/
```