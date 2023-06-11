import requests
import json
def hesapla():
    bozulan = input("Lütfen bozdurmak istediğiniz döviz türünü yazınız (USD/TRY): ")
    bozulan = bozulan.strip().upper()
    alinan = input("Lütfen almak istediğiniz döviz türünü yazınız (USD/TRY): ")
    alinan = alinan.strip().upper()
    key = f"https://v6.exchangerate-api.com/v6/704df543d4c455515f7b0694/latest/{bozulan}"
    sorgula = requests.get(key)
    text = json.loads(sorgula.text)
    hedef_kur = float(text["conversion_rates"][f"{alinan}"])
    miktar = float(input(f"Ne kadar {bozulan} bozdurmak istiyorsunuz: "))
    sonuc = miktar * hedef_kur
    print(f"1 {bozulan} = {hedef_kur} {alinan} \n{int(miktar)} {bozulan} = {sonuc} {alinan}")

hesapla()
    