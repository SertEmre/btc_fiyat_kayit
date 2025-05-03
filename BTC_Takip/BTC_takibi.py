import requests
from datetime import datetime

def btc_fiyat_takibi():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies":"usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["bitcoin"]["usd"]

def fiyat_kaydet():
    fiyat = btc_fiyat_takibi()
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    yazi= (f"{tarih} tarihinde BTC fiyatı: ${fiyat}\n")

    with open("btc_günlük_fiyatları.txt","a",encoding="utf-8") as dosya:
        dosya.write(yazi)
    print("Btc fiyatı kaydedildi:", yazi)

fiyat_kaydet()