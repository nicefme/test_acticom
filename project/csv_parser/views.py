import csv
from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import reverse_lazy


from .models import CSVFile, Table


def upload_csv_file(request):
    file_form = request.FILES.get('file_form')
    all_files = CSVFile.objects.all()
    file_not_csv = None
    if file_form is not None:
        file_permission = file_form.name.split('.')[-1]

        if file_permission != 'csv':
            file_not_csv = True

        elif (request.method == 'POST'
              and file_form is not None
              and file_permission == 'csv'):

            file_new = CSVFile.objects.create(
                file=file_form,
                name=file_form.name
            )

            with open(file_new.file.path, 'r', encoding='cp1251') as file:
                reader = csv.reader(file)
                print(reader)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        row = ''.join(row)
                        row = row.split(';')
                        try:
                            Table.objects.create(
                                code=row[0],
                                name=row[1],
                                level_one=row[2],
                                level_two=row[3],
                                level_three=row[4],
                                price=row[5] if row[5] else None,
                                sp_price=row[6] if row[6] else None,
                                quantity=row[7],
                                property_fields=row[8],
                                joint_purchases=row[9],
                                measurement_unit=row[10],
                                picture=(f'csv_parser/pictures/{row[11]}.png'
                                         if row[11] else None),
                                is_display=row[12],
                                description=row[13],
                                file_id=file_new.id
                            )
                        except (ValueError, IndexError):
                            CSVFile.objects.get(id=file_new.id).delete()
                            return render(request, 'upload.html', {
                                'all_files': all_files,
                                'file_form': file_form,
                                'file_del': True,
                            })
            return redirect(
                reverse_lazy('parser:index', kwargs={'file_id': file_new.id})
            )

    return render(request, 'upload.html', {
        'all_files': all_files,
        'file_form': file_form,
        'file_not_csv': file_not_csv,
    })


def index(request, file_id):

    code = request.GET.get('code')
    table = Table.objects.filter(file_id=file_id)

    name = request.GET.get('name')
    level_one = request.GET.get('level_one')
    level_two = request.GET.get('level_two')
    level_three = request.GET.get('level_three')
    measurement_unit = request.GET.get('measurement_unit')

    if code:
        table = table.filter(code__icontains=code)
    if name:
        table = table.filter(name__icontains=name)
    if level_one:
        table = table.filter(level_one__icontains=level_one)
    if level_two:
        table = table.filter(level_two__icontains=level_two)
    if level_three:
        table = table.filter(level_three__icontains=level_three)
    if measurement_unit:
        table = table.filter(measurement_unit__icontains=measurement_unit)

    return render(request, 'index.html', {
        'table': table,
        'file_id': file_id,
        'code': code,
        'name': name,
        'level_one': level_one,
        'level_two': level_two,
        'level_three': level_three,
        'measurement_unit': measurement_unit,
    })
