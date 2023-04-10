def hesap_makinesi():
    while True:
        print("Lütfen yapmak istediğiniz işlemi seçin: ")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Mod alma")
        print("6. Çıkış yap")

        secim = input("Seçiminiz (1/2/3/4/5/6): ")

        if secim in ('1', '2', '3', '4', '5'):
            sayi1 = float(input("İlk sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            if secim == '1':
                print(sayi1, "+", sayi2, "=", (sayi1 + sayi2))

            elif secim == '2':
                print(sayi1, "-", sayi2, "=", (sayi1 - sayi2))

            elif secim == '3':
                print(sayi1, "*", sayi2, "=", (sayi1 * sayi2))

            elif secim == '4':
                if sayi2 == 0:
                    print("Sıfıra bölme hatası!")
                else:
                    print(sayi1, "/", sayi2, "=", (sayi1 / sayi2))

            elif secim == '5':
                print(sayi1, "%", sayi2, "=", (sayi1 % sayi2))

        elif secim == '6':
            break

        else:
            print("Geçersiz giriş!")

hesap_makinesi()
