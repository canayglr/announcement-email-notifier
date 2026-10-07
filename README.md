# 📢 Announcement Email Notifier

**<img src="https://raw.githubusercontent.com/canayglr/canayglr/main/assets/flags/gb.png" height="14" alt="EN"/>** Watches the Erzurum Technical University announcements page and **emails you as soon as a new announcement is posted**.
**<img src="https://raw.githubusercontent.com/canayglr/canayglr/main/assets/flags/tr.png" height="14" alt="TR"/>** Erzurum Teknik Üniversitesi duyuru sayfasını takip eder ve **yeni bir duyuru yayınlandığında e-posta ile haber verir**.

## How it works / Nasıl çalışır
1. Fetches the page every 60 s with `requests` / Sayfayı her 60 saniyede bir `requests` ile çeker
2. Parses the latest announcements with `BeautifulSoup` / En son duyuruları `BeautifulSoup` ile ayrıştırır
3. If the newest date changed, sends a summary email via Outlook SMTP / En yeni tarih değiştiyse Outlook SMTP üzerinden özet e-posta gönderir

## Setup / Kurulum
```bash
pip install -r requirements.txt
# Set credentials as environment variables (see .env.example)
# Kimlik bilgilerini ortam değişkeni olarak tanımlayın (.env.example dosyasına bakın)
export MAIL_SENDER=... MAIL_PASSWORD=... MAIL_RECEIVER=...
python index.py
```

> 🔒 Credentials are read from environment variables and never stored in the code.
> Kimlik bilgileri ortam değişkenlerinden okunur, kodda saklanmaz.
