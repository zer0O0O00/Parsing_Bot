# Parsing_Bot
Parsing_Bot - это программа, предназначенная для пересылки новых сообщений из указанных исходных каналов Telegram в целевой чат. Она использует библиотеку Telethon для взаимодействия с Telegram API.

## Установка
Для работы с Parsing_Bot вам понадобится Python 3.x. Если его у вас нет, вы можете установить его, посетив официальный сайт [Python](https://www.python.org/).

Клонируйте репозиторий с помощью следующей команды:
```bash
git clone https://github.com/zer0O0O00/Parsing_Bot.git
```
Перейдите в каталог Parsing_Bot:
```bash
cd Parsing_Bot
```
Установите зависимости, используя pip:
```bash
pip install telethon configparser
```
## Настройка
Создайте Telegram-приложение, чтобы получить необходимые API-данные. Следуйте этим шагам:

Посетите страницу [Telegram API development tools](https://my.telegram.org/auth?to=apps) и войдите в свою учетную запись Telegram.
Заполните необходимую информацию для создания нового приложения.
После создания приложения запишите предоставленные api_id и api_hash для вашего приложения.
Откройте файл config.ini и внесите следующие изменения:

```ini
[Telegram]
api_id = ВАШ_API_ID
api_hash = ВАШ_API_HASH
username = ВАШ_ИМЯ_ПОЛЬЗОВАТЕЛЯ
chat = URL_ЦЕЛЕВОГО_ЧАТА

channel-1 = ВАШ_URL_CHANNEL_1
channel-2 = ВАШ_URL_CHANNEL_2
channel-3 = ВАШ_URL_CHANNEL_3
channel-4 = ВАШ_URL_CHANNEL_4
channel-5 = ВАШ_URL_CHANNEL_5
```
Замените ВАШ_API_ID, ВАШ_API_HASH и ВАШ_ИМЯ_ПОЛЬЗОВАТЕЛЯ на ваши учетные данные API и имя пользователя Telegram соответственно. Также замените URL_ЦЕЛЕВОГО_ЧАТА на URL целевого чата, куда вы хотите пересылать сообщения. Аналогичным образом обновите ВАШ_URL_CHANNEL_X с URL исходных каналов, которые вы хотите отслеживать.

## Запуск
Для запуска Parsing_Bot выполните следующую команду:

```bash
python parsing_bot.py
```


> **ВАЖНО!** При первом запуске программы, она будет запрашивать номер телефона и код подтверждения. Вам будет предложено ввести номер телефона в формате, принятом в вашей стране (например, "1234567890"). Затем, после отправки номера телефона, Telegram отправит вам код подтверждения через SMS или Telegram-сообщение. Введите этот код в программу для завершения авторизации.

Программа сохранит сессию авторизации, чтобы вам не нужно было вводить номер и код каждый раз при запуске. Однако, если вы хотите сменить аккаунт, вам нужно будет удалить файл сессии (session.session) в директории программы перед следующим запуском.

Программа начнет пересылку новых сообщений из указанных исходных каналов в целевой чат. Она будет проверять наличие новых сообщений каждые 3 минуты. Если сообщение в исходном канале содержит ключевые слова (которые можно изменить в коде), оно будет переслано в целевой чат.

Если возникнут ошибки или проблемы, убедитесь, что вы указали правильные API-данные и настроили файл config.ini соответствующим образом.

## Лицензия
This project is licensed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode) license. See the [LICENSE](LICENSE) file for more details.
