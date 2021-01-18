from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    data = response.json()
    kasus = []
    for x in data:
        datanya = {}
        datanya['provinsi'] = x['attributes']['Provinsi']
        datanya['kasus_positif'] = x['attributes']['Kasus_Posi']
        datanya['kasus_sembuh'] = x['attributes']['Kasus_Semb']
        datanya['kasus_meninggal'] = x['attributes']['Kasus_Meni']
        kasus.append(datanya)
    return render(request, 'home.html', {
        'data': kasus,
    })