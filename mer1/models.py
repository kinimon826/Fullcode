from django.db import models

class bidzaiavka(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.CharField(max_length=20, verbose_name='номер')
    paid = models.BooleanField(default=False, verbose_name='нажмите на кнопку отправить')
    class Meta:
        verbose_name = 'fullcode'
        verbose_name_plural = 'fullcodes'

class Logo(models.Model):
    img = models.ImageField(upload_to="Логотип", verbose_name="Логотипы")
    description = models.CharField(max_length=35, verbose_name="Название логотип")
    class Meta:
        verbose_name = 'Логотипы'
        verbose_name_plural = 'Логотип'


class Uslugi(models.Model):
    usluga = models.CharField(max_length=100, verbose_name='товар')
    text = models.TextField(verbose_name='подробнее описание')
    img = models.ImageField(upload_to='услуга', verbose_name='фото')
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

class project(models.Model):
    img = models.ImageField(upload_to='проекты', verbose_name='фото проекта')
    title = models.TextField(verbose_name='описание')
    class Meta:
        verbose_name = 'наш проект'
        verbose_name_plural = 'наши проекты'

class Osavatel(models.Model):
    fro = models.CharField(max_length=120, verbose_name='оснаватели компании')
    text = models.TextField(verbose_name='подробнее')
    img = models.ImageField(upload_to='загрузить', verbose_name='Оснаватели')
    title = models.CharField(max_length=100, verbose_name='имия оснавателя')
    class Meta:
        verbose_name = 'оснаветель'
        verbose_name_plural = 'оснаватели'

class Comanda(models.Model):
    img = models.ImageField(upload_to='загрузка фото', verbose_name='фото')
    name = models.CharField(max_length=100, verbose_name='имия')
    text = models.TextField(verbose_name='описание')
    class Meta:
        verbose_name = 'команды'
        verbose_name_plural = 'команды'

class News(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название компании")
    descriptions = models.TextField(verbose_name="Описание")
    name1 = models.CharField(max_length=100, verbose_name="Все прова защишены")
    name2 = models.CharField(max_length=100, verbose_name="Услуги")
    name3 = models.CharField(max_length=100, verbose_name="АЙти Школа")
    name4 = models.CharField(max_length=100, verbose_name="Проекты")
    name5 = models.CharField(max_length=100, verbose_name="Команда")
    img = models.ImageField(upload_to='Иконки',verbose_name="Иконки")
    img2 = models.ImageField(upload_to='Иконки',verbose_name="Иконки")
    img3 = models.ImageField(upload_to='Иконки',verbose_name="Иконки")
    img4 = models.ImageField(upload_to='Иконки',verbose_name="Иконки")



