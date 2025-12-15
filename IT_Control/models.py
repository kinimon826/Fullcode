from django.db import models



class StudentManagement(models.Model):
    ATTENDANCE_STATUSES = [
        ('late', 'Опоздал'),
        ('on_time', 'Вовремя'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    # English -> attendance_status
    attendance_status = models.CharField(
        max_length=100,
        choices=ATTENDANCE_STATUSES,
        verbose_name='опоздал:',
    )
    start_date = models.DateField(verbose_name='Дата начала обучения')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания обучения')
    is_paid = models.BooleanField(default=False, verbose_name='Оплатил или нет')
    is_graduated = models.BooleanField(default=False, verbose_name='Закончил или нет')

    class Meta:
        verbose_name = 'Управление студентом'
        verbose_name_plural = 'Управление студентами'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class StaffManagement(models.Model):
    JOB_POSITIONS = [
        ('teacher', 'Учитель'),
        ('programmer', 'Программист'),
        ('manager', 'Менеджер'),
        ('seller', 'Продавец'),
        ('agent', 'Агент'),
    ]

    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    position = models.CharField(
        max_length=200,
        choices=JOB_POSITIONS,
        verbose_name='Кем работает',
    )
    has_experience = models.BooleanField(default=False, verbose_name='Опыт работы')
    salary = models.IntegerField(verbose_name='Сколько получает')
    is_terminated = models.BooleanField(default=False, verbose_name='в работе:')

    class Meta:
        verbose_name = 'Управление работ'
        verbose_name_plural = 'Управление работы'

    def __str__(self):
        return f"{self.position} ({self.phone_number})"



class CourseEnrollment(models.Model):
    PROGRAMMING_LANGUAGES = [
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
    ]

    student_name = models.CharField(max_length=100, verbose_name='Имя')
    student_lastname = models.CharField(max_length=120, verbose_name='Фамилия')
    completion_status = models.CharField(
        max_length=100,
        choices=PROGRAMMING_LANGUAGES,
        verbose_name='Закончил курс'
    )
    start_date = models.DateField(verbose_name='Дата запуска курса')
    duration_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    is_hired = models.BooleanField(default=False, verbose_name='Берем в работу:')

    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курсы'

    def __str__(self):
        return f"Запись: {self.student_name} на {self.completion_status}"