from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Employee(models.Model):
    """Модель сотрудника"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, verbose_name='Сотрудник')
    patronymic = models.CharField(max_length=200,
                                  verbose_name='Отчество')
    position = models.ForeignKey('Position',
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 verbose_name='Должность',
                                 related_name='positions')
    date_of_employment = models.DateField(verbose_name='Дата трудоустройства')
    salary = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Зарплата')
    department = TreeForeignKey('Department',
                                on_delete=models.PROTECT,
                                related_name='department',
                                verbose_name='Отдел/Подразделение')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.user}'


class Department(MPTTModel):
    """Модель отделов"""
    title = models.CharField(verbose_name='Название отдела',
                             max_length=100,
                             unique=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(verbose_name='Описание отдела',
                                   blank=True)
    head = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name='departments_headed',
                             verbose_name='Руководитель')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title


class Position(models.Model):
    """Модель должности"""
    title = models.CharField(verbose_name='Должность',
                             unique=True)
    department = models.ForeignKey('Department',
                                  verbose_name='Отдел',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title