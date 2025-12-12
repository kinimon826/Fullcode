from django.db import models
from django.db.models.enums import Choices



class studentu(models.Model):
    LANGUAGES = [
        ('java', 'опаздал'),
        ('Python', 'не опаздал'),
    ]
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    English = models.CharField(
        max_length=100,
        choices=LANGUAGES,
        verbose_name='опаздал или нет',
    )
    start_date = models.DateField(verbose_name='Дата обучения')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания обучения')
    paid = models.BooleanField(default=False, verbose_name='Оплатил или нет')
    paid1 = models.BooleanField(default=False, verbose_name='закончил или нет')



    class Meta:
        verbose_name = 'управление Студент'
        verbose_name_plural = 'управиление Студентов'



class rabotau(models.Model):
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
        verbose_name='Кем работает',
    )
    test = models.BooleanField(default=False, verbose_name='опыт работы')
    money = models.IntegerField(verbose_name='Сколько получет')
    paid = models.BooleanField(default=False, verbose_name='уволить?')


    class Meta:
        verbose_name = 'управление работа'
        verbose_name_plural = 'управление работы'




class cursu(models.Model):
    LANGUAGES = [
        ('java', 'Javascript'),
        ('Python', 'Python'),
    ]
    name = models.CharField(max_length=100, verbose_name='имия')
    fristname = models.CharField(max_length=120, verbose_name='фамилия')
    English = models.CharField(max_length=100, choices=LANGUAGES, verbose_name='закончил',)
    data = models.DateField(verbose_name='запуск курса')
    date = models.DateField(null=True, blank=True, verbose_name='длитильность')
    paid = models.BooleanField(default=False, verbose_name='берем в работу?')

    class Meta:
        verbose_name = 'управление курс'
        verbose_name_plural = 'управление курсы'



