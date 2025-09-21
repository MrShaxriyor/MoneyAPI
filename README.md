# 💰 Money Control – Finanslarni boshqarish tizimi

Money Control – bu foydalanuvchilarga o‘z daromad va xarajatlarini boshqarish, kuzatish va tahlil qilish imkonini beruvchi **Django REST Framework** asosida yozilgan veb-ilova.  

## ✨ Asosiy imkoniyatlar
- 🔑 **JWT Authentication** – foydalanuvchi xavfsizligini ta’minlaydi  
- 📊 **Kirim va chiqimlarni kuzatish** – real vaqtda balansni ko‘rish  
- 🗂️ **Kategoriyalar** – foydalanuvchi o‘ziga xos kategoriyalar yaratishi mumkin  
- 📈 **Grafiklar va tahlil** – moliyaviy faoliyatni ko‘rish va tahlil qilish imkoniyati  
- 🔒 **Ma’lumotlar xavfsizligi** – barcha foydalanuvchi ma’lumotlari himoyalangan  

## 🛠️ Texnologiyalar
- [Python 3.12+](https://www.python.org/)  
- [Django 5](https://www.djangoproject.com/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [JWT (SimpleJWT)](https://django-rest-framework-simplejwt.readthedocs.io/)  
- SQLite (default) yoki PostgreSQL (production uchun tavsiya etiladi)  

## 🚀 O‘rnatish
```bash
git clone https://github.com/MrShaxriyor/MoneyAPI.git
cd money-control

# Virtual environment yaratish
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver
