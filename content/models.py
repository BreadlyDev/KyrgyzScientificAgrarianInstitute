from django.core.files.storage import default_storage
from django.core.validators import FileExtensionValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/books', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    file = models.FileField(upload_to='books/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'Книга {self.title}'

    def delete(self, using=None, keep_parents=False):
        try:
            default_storage.delete(self.photo.name)
            default_storage.delete(self.file.name)
        except FileNotFoundError as e:
            print('Ошибка при удалении файла', e)
        super().delete(using=using, keep_parents=keep_parents)


class Module(models.Model):
    PAGES = (
        ('Главная', 'Главная'),
        ('Об институте', 'Об институте'),
    )
    module_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=f'photos/modules',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    page = models.CharField(max_length=200, choices=PAGES)

    class Meta:
        db_table = 'modules'
        verbose_name = f'Модуль страницы'
        verbose_name_plural = 'Модули страницы'

    def __str__(self):
        return f'Модуль {self.module_title} страницы "{self.page}"'

    def delete(self, using=None, keep_parents=False):
        try:
            default_storage.delete(self.image.name)
        except FileNotFoundError as e:
            print('Ошибка при удалении файла', e)
        super().delete(using=using, keep_parents=keep_parents)


class Slider(models.Model):
    PAGES = (
        ('Главная', 'Главная'),
        ('Об институте', 'Об институте')
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    page = models.CharField(max_length=200, choices=PAGES)

    class Meta:
        db_table = 'slider'
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return f'Слайдер {self.title} страницы'


class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=f'photos/slides/',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    class Meta:
        db_table = 'slide'
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return f'Слайд страницы "{self.slider.page}"'

    def delete(self, using=None, keep_parents=False):
        try:
            default_storage.delete(self.image.name)
        except FileNotFoundError as e:
            print('Ошибка при удалении файла', e)
        super().delete(using=using, keep_parents=keep_parents)


class Message(models.Model):
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

    class Meta:
        db_table = 'messages'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение от {self.firstname} {self.lastname}'
