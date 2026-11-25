from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=15)

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class Request(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий')
    status = models.IntegerField(
        choices=[
            (0, 'Новая'),
            (1, 'Принята'),
            (2, 'Выполнена')
        ],
        default=0
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'Заявка №{self.pk} от {self.user.username}'