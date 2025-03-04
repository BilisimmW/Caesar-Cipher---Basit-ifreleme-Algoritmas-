def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  # Sadece harfleri şifrele
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char  # Harf olmayan karakterleri olduğu gibi bırak
    
    return result

# Kullanıcıdan giriş al
text = input("Şifrelenecek metni girin: ")
shift = int(input("Kaydırma miktarını girin: "))

# Şifrelenmiş metni yazdır
encrypted_text = caesar_cipher(text, shift)
print("Şifrelenmiş metin:", encrypted_text)
