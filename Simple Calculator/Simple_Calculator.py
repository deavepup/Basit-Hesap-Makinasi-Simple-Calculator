# Bu Fonksiyon iki sayı ekler
def add(x, y):
    return x + y

# Bu Fonksiyon iki sayıyı çıkarır
def subtract(x, y):
    return x - y

# Bu Fonksiyon iki sayıyı çarpar
def multiply(x, y):
    return x * y

# Bu Fonksiyon iki sayıyı böler
def divide(x, y):
    return x / y


print("İşlemi seçin.")
print("1.Topla")
print("2.Çıkar")
print("3.Çarp")
print("4.Böl")

while True:
    # Kullanıcıdan alınan girdi
    choice = input("Seçimi girin(1/2/3/4): ")

    # Seçimin dört seçenekten biri olup olmadığını kontrol etmek
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("İlk numarayı girin: "))
        num2 = float(input("İkinci numarayı girin: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Geçersiz Giriş")
