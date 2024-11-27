from django.shortcuts import render
import requests

def KursView(request):
    if request.method == 'POST':
        amount = float(request.POST.get('text', 1))
        base_code = request.POST.get('base_code', 'USD')
        target_code = request.POST.get('target_code', 'UZS')

        url = f'https://v6.exchangerate-api.com/v6/2ee123025e10880a40d7d5c7/pair/{base_code}/{target_code}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                conversion_rate = data['conversion_rate']
                converted_amount = amount * conversion_rate

                context = {
                    'amount': amount,
                    'base_code': base_code,
                    'target_code': target_code,
                    'conversion_rate': conversion_rate,
                    'converted_amount': converted_amount,
                    'last_update': data['time_last_update_utc']
                }
                return render(request, 'index.html', context)
        else:
            context = {'error': 'Не удалось получить данные курса обмена. Пожалуйста, попробуйте позже.'}
            return render(request, 'index.html', context)

