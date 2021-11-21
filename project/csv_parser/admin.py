from django.contrib import admin

from .models import CSVFile, Table


@admin.register(CSVFile)
class CSVFileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'file'
    ]


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'code',
        'name',
        'level_one',
        'level_two',
        'level_three',
        'price',
        'sp_price',
        'quantity',
        'property_fields',
        'joint_purchases',
        'measurement_unit',
        'picture',
        'is_display',
        'description',
        'file_id'
    ]
