from django.db import models


class ContactRequest(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    is_submitted = models.BooleanField(default=False, verbose_name='Соглащение условиями')

    class Meta:
        verbose_name = 'Заявка на контакт'
        verbose_name_plural = 'Заявки на контакт'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Logo(models.Model):
    image = models.ImageField(upload_to="logos/", verbose_name="Логотип")
    name = models.CharField(max_length=35, verbose_name="Название логотипа")

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Подробное описание')
    image = models.ImageField(upload_to='services/', verbose_name='Фото услуги')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to='projects/', verbose_name='Фото проекта')
    description = models.TextField(verbose_name='Описание проекта')

    class Meta:
        verbose_name = 'Наш проект'
        verbose_name_plural = 'Наши проекты'


class Founder(models.Model):
    full_name = models.CharField(max_length=120, verbose_name='Имя основателя')
    bio = models.TextField(verbose_name='Подробная биография')
    image = models.ImageField(upload_to='founders/', verbose_name='Фото основателя')
    position = models.CharField(max_length=100, verbose_name='Должность')

    class Meta:
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.full_name



class TeamMember(models.Model):
    image = models.ImageField(upload_to='team_photos/', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание / Должность')

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Команда'

    def __str__(self):
        return self.name



class SiteSettings(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Название компании")
    footer_text = models.TextField(verbose_name="Описание/Слоган")
    copyright_text = models.CharField(max_length=100, verbose_name="Все права защищены")
    menu_services = models.CharField(max_length=100, verbose_name="Название ссылки 'Услуги'")
    menu_it_school = models.CharField(max_length=100, verbose_name="Название ссылки 'Айти Школа'")
    menu_projects = models.CharField(max_length=100, verbose_name="Название ссылки 'Проекты'")
    menu_team = models.CharField(max_length=100, verbose_name="Название ссылки 'Команда'")
    icon_1 = models.ImageField(upload_to='icons/', verbose_name="Иконка 1")
    icon_2 = models.ImageField(upload_to='icons/', verbose_name="Иконка 2")
    icon_3 = models.ImageField(upload_to='icons/', verbose_name="Иконка 3")
    icon_4 = models.ImageField(upload_to='icons/', verbose_name="Иконка 4")

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'