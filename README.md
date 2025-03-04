# 🔐 Caesar Cipher - Basit Şifreleme Algoritması

Bu proje, kullanıcıdan alınan bir metni belirli bir harf kaydırmasıyla şifreleyen **Caesar Cipher** algoritmasını içermektedir. Python kullanarak kolayca uygulanabilen bu yöntem, temel kriptografi mantığını anlamak için harika bir başlangıçtır.

## 📌 Özellikler
- Kullanıcının girdiği metni belirli bir harf kaydırmasıyla şifreler.
- Alfabenin dışına çıkan harfler başa dönerek devam eder.
- Büyük ve küçük harf duyarlılığı korunur.
- Özel karakterler ve sayılar değiştirilmez.

## 🚀 Kullanım
### 1️⃣ Gerekli Kütüphaneleri Yükleyin  
Bu proje için ekstra bir kütüphane yüklemenize gerek yoktur. **Python 3+** yeterlidir.

### 2️⃣ Projeyi Çalıştırın
```python
python caesar_cipher.py 

``` 

### 3️⃣ Örnek Kullanım

Metni girin: HELLO
Kaç harf kaydırılsın?: 3

Şifrelenmiş metin: KHOOR

### 🔑 Algoritma Mantığı
Caesar Cipher, her harfi belirlenen bir sayı kadar kaydırarak şifreleme yapar. Örneğin, 3 harf kaydırma ile:

A → D, B → E, C → F, ..., X → A, Y → B, Z → C
