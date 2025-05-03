Bitcoin'in (BTC) güncel USD cinsinden fiyatını CoinGecko API'si üzerinden alır ve tarih bilgisiyle birlikte bir `.txt` dosyasına kaydeder.

->Otomatik Çalıştırma
Scripti her gün belirli bir saatte otomatik çalıştırmak için aşağıdaki yöntemlerden birini kullanabilirsin:
🪟 Windows (Görev Zamanlayıcı)
"Görev Zamanlayıcı"yı aç.
"Görev Oluştur" → "Tetikleyiciler" sekmesinde → "Yeni" → Günlük/Saat seç.
"Eylemler" sekmesinde: Program/script: python
Argümanlar: "C:\tam\dosya\yolu\btc_fiyat_kaydet.py"

Not: Python yüklü konumu bilmiyorsan where python komutunu kullan.

🐧 Linux/macOS (cron)
Terminalde crontab -e komutunu gir.
Aşağıdaki satırı ekle (örnek: her gün saat 10:00'da):

bash
Kopyala
Düzenle
0 10 * * * /usr/bin/python3 /tam/dosya/yolu/btc_fiyat_kaydet.py
Python yolu için which python3 komutunu kullan.

