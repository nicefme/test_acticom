from django.db import models
from django.core.validators import MinValueValidator


class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_parser/csv/')
    name = models.CharField(verbose_name='Код', max_length=1000)

    class Meta:
        verbose_name = 'Файл .csv'
        verbose_name_plural = 'Файлы .csv'


class Table(models.Model):
    class Options(models.TextChoices):
        NO = '0', 'Нет'
        YES = '1', 'Да'

    code = models.CharField(verbose_name='Код', max_length=200)
    name = models.CharField(verbose_name='Наименование', max_length=1000)
    level_one = models.CharField(verbose_name='Уровень1', max_length=1000)
    level_two = models.CharField(verbose_name='Уровень2', max_length=1000,
                                 blank=True, null=True)
    level_three = models.CharField(verbose_name='Уровень3', max_length=1000,
                                   blank=True, null=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена', blank=True,
                                             null=True)
    sp_price = models.PositiveSmallIntegerField(verbose_name='Цена СП',
                                                blank=True, null=True)
    quantity = models.DecimalField(verbose_name='Количество', max_digits=12,
                                   decimal_places=3, null=True,
                                   validators=[MinValueValidator(0), ])
    property_fields = models.CharField(verbose_name='Поля свойств',
                                       max_length=1000, blank=True, null=True)
    joint_purchases = models.CharField(verbose_name='Совместные покупки',
                                       max_length=100, choices=Options.choices,
                                       blank=True, null=True)
    measurement_unit = models.CharField(verbose_name='Единица измерения',
                                        max_length=200)
    picture = models.ImageField(verbose_name='Картинка',
                                upload_to='csv_parser/pictures/',
                                blank=True,
                                null=True)
    is_display = models.CharField(verbose_name='Выводить на главной',
                                  max_length=100,
                                  choices=Options.choices,
                                  blank=True, null=True)
    description = models.CharField(verbose_name='Описание', max_length=2000,
                                   blank=True, null=True)
    file_id = models.PositiveIntegerField(verbose_name='ID загруженного файла')

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'

    def __str__(self):
        return self.name
