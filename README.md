# Library 
## back-end

### Установка [docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru) и [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru)

### Запуск docker-compose

```shell
docker-compose build
docker-compose up
```

### Отключение docker-compose

```shell
docker-compose kill
```

### Порты
***ВНИМАНИЕ!*** освободите следующие порты перед запуском **docker**
- redis: 6379:6379
- database: 5432:5432
- database_admin: 8080:8080
- django: 8000:8000
- celery: 5555:5555
- celery flower: 5556:5556
