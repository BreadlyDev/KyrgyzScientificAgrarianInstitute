from django import forms as f
from django.forms import Textarea
from django.forms.widgets import Input

from . import models as m


class MessageForm(f.ModelForm):
    class Meta:
        model = m.Message
        fields = '__all__'
        labels = {
            'firstname': 'Ваше имя',
            'lastname': 'Ваша фамилия',
            'text': 'Текст сообщения',
        }
        widgets = {
            'text': Textarea(attrs={
                'class': 'message-form-body',
                'placeholder': 'Введите текст',
            }),
            'firstname': Input(attrs={
                'class': 'message-form-body',
                'placeholder': 'Введите ваше имя',
            }),
            'lastname': Input(attrs={
                'class': 'message-form-body',
                'placeholder': 'Введите вашу фамилию',
            })
        }
