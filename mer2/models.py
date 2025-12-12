from django.db import models
from django.db.models.enums import Choices


class student(models.Model):
    LANGUAGES = [
        ('java', 'Javascript'),
        ('Python', 'Python'),
    ]
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    English = models.CharField(
        max_length=100,
        choices=LANGUAGES,
        verbose_name='Изучаемый язык',
    )
    start_date = models.DateField(verbose_name='Дата обучения')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания обучения')
    paid = models.BooleanField(default=False, verbose_name='Оплатил или нет')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.first_name



class work(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    position = models.CharField(max_length=150, verbose_name='Кем работает')
    salary = models.CharField(verbose_name='Сколько получает')
    start_working_date = models.DateField(verbose_name='Дата работы')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Рабочии'

    def __str__(self):
        return self.first_name



class Companymy(models.Model):
    company = models.CharField(max_length=200, verbose_name='Название компании')
    number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.TextField(verbose_name='Адрес')
    logo = models.ImageField(null=True, blank=True, verbose_name='Логотип', upload_to='company_logos/')

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компания'

    def __str__(self):
        return self.company





class rabota(models.Model):
    Human_klass = [
        ('worker', 'учитель'),
        ('work2', 'програмист'),
        ('work3', 'менеджер'),
        ('work4', 'продовец'),
        ('work5', 'Агент'),
    ]
    number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='почта')
    Human = models.CharField(
        max_length=200,
        choices=Human_klass,
        verbose_name='Кем хотите устроиться',
    )
    test = models.BooleanField(default=False, verbose_name='опыт работы')
    money = models.IntegerField(verbose_name='Сколько хотите получать?')
    interest = models.TextField(null=True, blank=True, verbose_name='Что интересует')

    class Meta:
        verbose_name = 'работа'
        verbose_name_plural = 'работы'

    def __str__(self):
        return self.number


class zaiavka(models.Model):
    number = models.CharField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Гмайл почта')
    text = models.TextField(null=True, blank=True, verbose_name='что вас интересует')


    class Meta:
        verbose_name='заявка'
        verbose_name_plural='оставить заявку'


    def __str__(self):
        return self.number


class sertificat(models.Model):
    chat = models.CharField(max_length=100, verbose_name='Дарим серфтификат после оканчания курса')
    text = models.TextField(verbose_name='описание')
    oplata = models.BooleanField(default=False, verbose_name='Сертификат лицензирован')
    oplatas = models.BooleanField(default=False, verbose_name='Международное признание')
    img = models.ImageField(null=True, blank=True, verbose_name='Логотип', upload_to='Certificate')

    class Meta:
        verbose_name='Сертификат'
        verbose_name_plural='Секртификат'

class onas(models.Model):
    name = models.CharField(max_length=100, verbose_name='Что делат нас лучшим')
    text = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'о нас'
        verbose_name_plural = 'о нас'

class curs(models.Model):
    LANGUAGES = [
        ('java', 'Javascript'),
        ('Python', 'Python'),
    ]

    English = models.CharField(max_length=100, choices=LANGUAGES, verbose_name='Изучаемый язык',)
    text = models.TextField(verbose_name='Описание')
    data = models.DateField(verbose_name='запуск курса')
    date = models.DateField(null=True, blank=True, verbose_name='длитильность')


    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'