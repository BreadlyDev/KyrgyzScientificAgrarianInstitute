from django.db.models.signals import post_save
from django.dispatch import receiver
from main import settings
from . models import Message
from telegram import Bot


@receiver(post_save, sender=Message)
async def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
        chat_id = settings.TELEGRAM_CHAT_ID
        message_text = f'Новое сообщение от {instance.firstname} {instance.lastname}: {instance.text}'
        await bot.send_message(chat_id=chat_id, text=message_text)
