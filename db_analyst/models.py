# Create your models here.
from django.db import models


class User_verification(models.Model):
    """Таблица Аутентификации пользователя"""
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name='ID пользователя из телеграма', null=True)
    name = models.CharField(blank=True, verbose_name='Имя пользователя', max_length=50, )
    activating_bot = models.CharField(max_length=50, verbose_name='Активация бота')
    goal = models.CharField(blank=True, max_length=50, verbose_name='есть цель')
    price = models.IntegerField(verbose_name='Цена', null=True, blank=True)
    income = models.IntegerField(verbose_name='Доход', null=True, blank=True)
    data = models.CharField(max_length=15, verbose_name='Дата покупки')

    class Meta:
        verbose_name = 'Аутентификации пользователя'
        verbose_name_plural = 'Аутентификации пользователя'

    def __str__(self):
        return f'@{self.name}' if self.name is not None else f"{self.user_id}" \
                                                             f" {self.price} {self.goal} {self.income} {self.data}"


class Purposes(models.Model):
    objects = True
    machine = models.CharField(blank=True, max_length=50, verbose_name='купить машину')
    apartment = models.CharField(blank=True, max_length=50, verbose_name='купить квартиру')
    vacation = models.CharField(blank=True, max_length=50, verbose_name='съездить в отпуск')
    another_target = models.CharField(blank=True, max_length=50, verbose_name='другие траты')
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Цели'
        verbose_name_plural = 'Цели'

    # def __str__(self):
    #     return {self.}

