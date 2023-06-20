import time
import configparser
from telethon.sync import TelegramClient
from telethon import functions, types

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
chat_url = config['Telegram']['chat']

# Создаем клиента Telegram
client = TelegramClient(username, api_id, api_hash)
client.start()

# Словарь для хранения ID последнего пересланного сообщения из каждого исходного чата
last_forwarded_messages = {}

# Ключевые слова для проверки
keywords = ["требуется", "Требуется", "нужно", "Нужно", "Нужен", "нужен", "Нужна", "нужна", "Нужны", "нужны"]

async def forward_new_messages():
    """Пересылает новые сообщения из указанных чатов в целевой чат"""
    target_chat_entity = await client.get_entity(chat_url)  # Целевой чат
    source_chats = [
        ('channel-1', config['Telegram']['channel-1']),
        ('channel-2', config['Telegram']['channel-2']),
        ('channel-3', config['Telegram']['channel-3']),
        ('channel-4', config['Telegram']['channel-4']),
        ('channel-5', config['Telegram']['channel-5'])
    ]

    while True:
        try:
            for source_chat_name, source_chat_url in source_chats:
                source_chat_entity = await client.get_entity(source_chat_url)  # Исходный чат
                messages = await client.get_messages(source_chat_entity, limit=10)

                # Получаем ID последнего пересланного сообщения из текущего исходного чата
                last_forwarded_message_id = last_forwarded_messages.get(source_chat_name)

                for message in reversed(messages):
                    # Проверяем, является ли сообщение новым
                    if last_forwarded_message_id is None or message.id > last_forwarded_message_id:
                        if not isinstance(message, types.MessageService):
                            if any(keyword in message.text for keyword in keywords):
                                await client.forward_messages(target_chat_entity, message, from_peer=source_chat_entity)
                                last_forwarded_messages[source_chat_name] = message.id

            # Ждем 3 минуты перед следующей проверкой
            time.sleep(180)

        except Exception as e:
            print(f"Error: {e}")


async def main():
    await forward_new_messages()


with client:
    client.loop.run_until_complete(main())