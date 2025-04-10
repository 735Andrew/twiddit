<h2>Twiddit</h2>
<hr>

<b>Twiddit</b> - текстовое веб-приложение, в котором присутствует функционал:
<ul>
    <li>Создания профиля пользователя и его редактура</li>
    <li>Написания публичных постов и личных сообщений</li>
    <li>Взаимных подписок и отписок пользователей</li>
</ul>
<img src="app/static/logo.png" height="230">
<br>
:pushpin: Посетить ресурс: <a href="https://twiddit.ru">twiddit.ru</a>
<br><br>
<hr>
<div>
<h3>Deploy проекта на сервере Linux</h3>

```bash
    sudo apt-get -y update
    sudo apt-get -y install python3 python3-venv git
    
    git clone https://github.com/735Andrew/twiddit 
    cd twiddit 
    python3 -m venv venv 
    source venv/bin/activate 
    (venv) pip install -r requirements.txt
    
    touch .env # Создание файла с необходимыми зависимостями
    sudo nano .env
    # В файле необходимо задать переменную SECRET_KEY=<very-secret-key>,
    # которая позволяет приложению принимать и обрабатывать веб-формы с данными
    
    (venv) flask run # Приложение будет доступно по адресу http://localhost:5000
    
```
</div>
<hr>


