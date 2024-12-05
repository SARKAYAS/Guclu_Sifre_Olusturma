import random
import string

def generate_strong_password(length: int, use_uppercase: bool, use_digits: bool, use_special_chars: bool) -> str:
    """
    Rastgele güçlü bir şifre oluşturur.
    
    Args:
        length (int): Şifrenin uzunluğu.
        use_uppercase (bool): Büyük harf kullanımı.
        use_digits (bool): Rakam kullanımı.
        use_special_chars (bool): Özel karakter kullanımı.
    
    Returns:
        str: Rastgele oluşturulan güçlü şifre.
    """
    if length < 4:
        raise ValueError("Şifre uzunluğu en az 4 olmalıdır.")

    # Kullanılacak karakter havuzunu oluştur
    char_pool = list(string.ascii_lowercase)  # Küçük harfler
    if use_uppercase:
        char_pool.extend(string.ascii_uppercase)  # Büyük harfler
    if use_digits:
        char_pool.extend(string.digits)  # Rakamlar
    if use_special_chars:
        char_pool.extend(string.punctuation)  # Özel karakterler

    if len(char_pool) == 0:
        raise ValueError("En az bir karakter seti seçilmelidir.")

    # Garanti edilen karakterler
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    # Geri kalan karakterler
    password += random.choices(char_pool, k=length - len(password))

    # Karakterleri karıştır
    random.shuffle(password)

    return ''.join(password)

def get_user_input() -> dict:
    """
    Kullanıcıdan şifre özellikleri için giriş alır.
    
    Returns:
        dict: Kullanıcının seçtiği özellikler.
    """
    print("Güçlü şifre oluşturucuya hoş geldiniz!")
    
    while True:
        try:
            length = int(input("Şifre uzunluğunu girin (en az 4): "))
            if length < 4:
                raise ValueError("Uzunluk en az 4 olmalıdır.")
            break
        except ValueError as e:
            print(f"Hata: {e}. Tekrar deneyin.")

    use_uppercase = input("Büyük harf kullanılsın mı? (Evet/Hayır): ").strip().lower() in ['evet', 'e']
    use_digits = input("Rakam kullanılsın mı? (Evet/Hayır): ").strip().lower() in ['evet', 'e']
    use_special_chars = input("Özel karakter kullanılsın mı? (Evet/Hayır): ").strip().lower() in ['evet', 'e']

    if not (use_uppercase or use_digits or use_special_chars):
        print("Uyarı: Hiçbir opsiyon seçmediniz, sadece küçük harfler kullanılacak.")

    return {
        "length": length,
        "use_uppercase": use_uppercase,
        "use_digits": use_digits,
        "use_special_chars": use_special_chars
    }

if __name__ == "__main__":
    try:
        user_options = get_user_input()
        password = generate_strong_password(**user_options)
        print(f"Oluşturulan güçlü şifre: {password}")
    except Exception as e:
        print(f"Hata: {e}")
