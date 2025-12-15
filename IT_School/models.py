from django.db import models


class Student(models.Model):
    PROGRAMMING_LANGUAGES = [
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    study_language = models.CharField(
        max_length=100,
        choices=PROGRAMMING_LANGUAGES,
        verbose_name='Изучаемый язык',
    )
    start_date = models.DateField(verbose_name='Дата начала обучения')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания обучения')
    is_paid = models.BooleanField(default=False, verbose_name='Оплатил или нет')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Worker(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    position = models.CharField(max_length=150, verbose_name='Кем работает')
    salary = models.IntegerField(verbose_name='Сколько получает')
    start_working_date = models.DateField(verbose_name='Дата начала работы')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return f"{self.first_name} ({self.position})"


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название компании')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.TextField(verbose_name='Адрес')
    logo = models.ImageField(null=True, blank=True, verbose_name='Логотип', upload_to='company_logos/')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    JOB_POSITIONS = [
        ('teacher', 'Учитель'),
        ('programmer', 'Программист'),
        ('manager', 'Менеджер'),
        ('seller', 'Продавец'),
        ('agent', 'Агент'),
    ]

    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    desired_position = models.CharField(
        max_length=200,
        choices=JOB_POSITIONS,
        verbose_name='Кем хотите устроиться',
    )
    has_experience = models.BooleanField(default=False, verbose_name='Опыт работы')
    salary_expectation = models.IntegerField(verbose_name='Сколько хотите получать?')
    interest = models.TextField(null=True, blank=True, verbose_name='Что интересует')

    class Meta:
        verbose_name = 'Заявка на работу'
        verbose_name_plural = 'Заявки на работу'

    def __str__(self):
        return self.phone_number


class Application(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email почта')
    text = models.TextField(null=True, blank=True, verbose_name='Что вас интересует')

    class Meta:
        verbose_name = 'Заявка от клиента'
        verbose_name_plural = 'Заявки от клиентов'

    def __str__(self):
        return self.phone_number


class Certificate(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название сертификата')
    description = models.TextField(verbose_name='Описание')
    is_licensed = models.BooleanField(default=False, verbose_name='Сертификат лицензирован')
    is_internationally_recognized = models.BooleanField(default=False, verbose_name='Международное признание')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение сертификата', upload_to='Certificate')

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class AboutUsItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Пункт "О нас"'
        verbose_name_plural = 'Пункты "О нас"'


class Course(models.Model):
    PROGRAMMING_LANGUAGES = [
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
    ]

    language = models.CharField(max_length=100, choices=PROGRAMMING_LANGUAGES, verbose_name='Изучаемый язык')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата запуска курса')
    duration_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'