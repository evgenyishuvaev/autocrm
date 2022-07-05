Запуск прокета

    docker compose up web

Заполнить базу
    
    docker compose up filldb

В результате будут применены миграции, база будет заполнена
тестовыми данными, будет создан суперпользователь и пользователь с правами менеджера

Супер пользователь:

    login: serv
    password: serv

Менеджер:
    
    login: john
    password: 5DJpsdQJsRhdyS4