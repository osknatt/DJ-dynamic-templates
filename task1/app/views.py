from django.shortcuts import render
import csv
from .settings import INFLATION
def inflation_view(request):
    template_name = 'inflation.html'
    all_data = []
    with open(INFLATION, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            all_data.append(row[0].split(';'))

    for row in all_data:
        for i, elem in enumerate(row):
            try:
                row[i] = float(elem)
            except:
                pass

    print(all_data[1])
    # чтение csv-файла и заполнение контекста
    context = {
        'all_data': all_data,
    }

    return render(request, template_name, context)