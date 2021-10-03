"""

Bu dastur yangi oshhonalar uchun elektron menyu vazifasini bajaradi

Yasadi = Q_M

Yasalgan Kuni 3\10\2021

"""

ism = input("Ismingiz nima janob yoki honim: ")
print(f"{ism} bizda 'Milliy taom(1)' va 'Fast Food(2)' bor (iltimos raqmlar bilan kiritsangiz)")
buyurtma = input(f"{ism} janoblari qanday turdagi taom tanavvul etmoqchilar?: ")
"""
1 == Milliy taom
"""
if buyurtma == "1":
    print(f"{ism} Menuni qarshi oling: \n"
          f"1. Ko'za sho'rva = 30000\n"
          f"2. Norin(1 porsiya uchun) = 35000\n"
          f"3. Shashlik(qiyma(1), jaz(2), jigar(3) = 9000, 12000, 14000\n"
          f"4. Somsa(go'shtlik(1), kartoshka(2) = 9500, 5500\n"
          f"5. Tabaka (1 porsiya) = 45000\n"
          f"6. Qozonkabob(1 porsiya) = 55000\n"
          f"7. Mangal (1 porsiya) = 45000\n"
          f"8. Assorti = 60000\n")
    taom_turi = input(f"Qanday taom tanlaysiz janob {ism}(raqam bilan kiriting)")
    if taom_turi == "1":
        shorva = (f"Ko'za sho'rva ajoyib tanlo'v {ism}")
        print(shorva)
        shorva_soni = int(input(f"Necha ko'za sho'rva buyurtma qilmoqchisiz janob: "))

        if shorva_soni == shorva_soni:
            print(f"To'lov {30000 * shorva_soni}")
            print("Choy va non bepul")
    if taom_turi == "2":
        norin = int(input(f"Ajoyib tanlo'v Nehcha porsiya norin buyurtma qilmqchisiz: "))
        if norin == norin:
            print(f"To'lo'vingiz {35000 * norin}")
        print("Choy va non bepul")
    if taom_turi == "3":
        shashlik = input("Qanday turdagi shashlik tanovvul qilmoqchisiz(sonlarda yozing): ")
        if shashlik == ("1"):
            shashlik_soni = int(input("Nechta qiyma shashlik tanovvul qilmoqchisiz: "))
            if shashlik_soni == shashlik_soni:
                print(f"To'lo'v {9000 * shashlik_soni}")
            print("Choy va non bepul")
        if shashlik == ("2"):
            shashlik_soni = int(input("Nechta jaz shashlik tanovvul qilmoqchisiz: "))
            if shashlik_soni == shashlik_soni:
                print(f"To'lo'v {12000 * shashlik_soni}")
            print("Choy va non bepul")
        if shashlik == ("3"):
            shashlik_soni = int(input("Nechta jigar shashlik tanovvul qilmoqchisiz: "))
            if shashlik_soni == shashlik_soni:
                print(f"To'lo'v {14000 * shashlik_soni}")
            print("Choy va non bepul")
    if taom_turi == "4":
        somsa_turi = input("Qanday turdagi somsa xarid qilmoqchisiz(sonlarda yozing): ")
        if somsa_turi == "1":
            somsa_soni = int(input("Nechta go'shtli somsa harid qilmoqchisiz: "))
            if somsa_soni == somsa_soni:
                print(f"To'lo'v {9500 * somsa_soni}")
            print("Choy va non bepul")
        if somsa_turi == "2":
            somsa_soni = int(input("Nechta kartoshkali somsa harid qilmoqchisiz: "))
            if somsa_soni == somsa_soni:
                print(f"To'lo'v {5500 * somsa_soni}")
            print("Choy va non bepul")
    if taom_turi == "5":
        tabaka_porsiya = int(input("Necha po'rsiya tabaka xarid qilmoqchisiz: "))
        if tabaka_porsiya == tabaka_porsiya:
            print(f"To'lo'v {45000 * tabaka_porsiya}")
        print("Choy va non bepul")
    if taom_turi == "6":
        qozonkabob_porsiya = int(input("Necha porsiya qozonkabob xarid qilmoqchisiz: "))
        if qozonkabob_porsiya == qozonkabob_porsiya:
            print(f"To'lo'v {55000 * qozonkabob_porsiya}")
        print("Choy va non bepul")
    if taom_turi == "7":
        mangal_porsiya = int(input("Necha porsiya mangal xarid qilmoqchisiz: "))
        if mangal_porsiya == mangal_porsiya:
            print(f"To'lo'v {45000 * mangal_porsiya}")
        print("Choy va non bepul")
    if taom_turi == "8":
        assorti = int(input("Nech aporsiya Assarti xarid qilmoqchisiz: "))
        if assorti == assorti:
            print(f"To'lo'v {60000 * assorti}")
        print("Choy va non bepul")
    suv = input("Ichishga suv ham buyurasizmi: ")
    if suv == "Ha":
        print("1.Pepsi\n"
              "2.CocaCola\n"
              "3.Fanta\n"
              "4.AysTea\n"
              "5.ArkTea\n"
              "6.FuseTea")
        tanla = input("Qay birini tanladigiz: ")
        if tanla == "1":
            nechaLitr = input("Nechi litirlik pepsi harid qilmoqchisiz(Namuna: 1,5): ")
            if nechaLitr == "1":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {7000 * nechta}")
            if nechaLitr == "1,5":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {12000 * nechta}")
            if nechaLitr == "2":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {16000 * nechta}")
        if tanla == "2":
            nechaLitr_cola = input("Necha litr CocaCola harid qilmoqchisiz:")
            if nechaLitr_cola == "1":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {8000 * nechta_cola}")
            if nechaLitr_cola == "1,5":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {10000 * nechta_cola}")
            if nechaLitr_cola == "2":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {14000 * nechta_cola}")
        if tanla == "3":
            nechaLitr_fanta = input("Necha litrlik fanta sotib olmoqchisiz")
            if nechaLitr_fanta == "1":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {8000 * nechtaFantf}")
            if nechaLitr_fanta == "1,5":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {13000 * nechtaFantf}")
            if nechaLitr_fanta == "2":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {17000 * nechtaFantf}")
        if tanla == "4":
            nechtaAys = int(input("Nechta AysTea sotib olmoqchisiz: "))
            if nechtaAys == nechtaAys:
                print(f"Sotib olgan suvingiz narhi: {8000 * nechtaAys}")
        if tanla == "5":
            nechtaArk = int(input("Nechta ArkTea xarid qilmoqchisiz: "))
            if nechtaArk == nechtaArk:
                print(f"oladigan suvingiz summasi: {6000 * nechtaArk}")
        if tanla == "6":
            nechtaFuse = int(input("Nechta FuseTea xarid qilmoqchisiz: "))
            if nechtaFuse == nechtaFuse:
                print(f"Oladigan suvingiz summasi {10000 * nechtaFuse}")
"""
2 == Fast food
"""
if buyurtma == "2":
    print(f"{ism} Fast Food siz uchun muntazir(Son bilan kiriting)\n"
          f"1. Gamburger = 12000\n"
          f"2. ChizBurger = 14000\n"
          f"3. DublleBurger = 17000\n"
          f"4. XotDog = 10000\n"
          f"5. Lavash(sir(1), gosht(2) va garimdorili(3) = 17000, 20000, 23000\n"
          f"6. Haggi = 19000\n")
    fast_food_turi = input(f"{ism} Qanday taom yemoqchisiz buyuring: ")

    if fast_food_turi == "1":
        gam_soni = int(input(f"{ism.title()} nechta gamburger xarid qilmoqchisiz: "))
        if gam_soni == gam_soni:
            print(f"To'lo'v {12000 * gam_soni}")
        print("Choy va non bepul")
    if fast_food_turi == "2":
        chizgam_soni = int(input(f"{ism} nechta ChizBurger xarid qilmoqchisiz: "))
        if chizgam_soni == chizgam_soni:
            print(f"To'lo'v {14000 * chizgam_soni}")
        print("Choy va non bepul")
    if fast_food_turi == "3":
        dll_soni = int(input("Nechta DublleBurger sotib olmoqchisiz: "))
        if dll_soni == dll_soni:
            print(f"To'lo'v {17000 * dll_soni}")
        print("Choy va non bepul")
    if fast_food_turi == "4":
        xotdog = int(input("Nechta XotDog sotib olmoqchisiz: "))
        if xotdog == xotdog:
            print(f"To'lo'v {10000 * xotdog}")
        print("Choy va non bepul")
    if fast_food_turi == "5":
        lavash_turi = input("Qanday turdagi lavash xarid qilmoqchisiz(son bilan kiriting): ")
        if lavash_turi == "1":
            lavash_soni = int(input("Nechta sirli lavash harid qilmoqchisiz"))
            if lavash_soni == lavash_soni:
                print(f"To'lo'v {17000 * lavash_soni}")
            print("Choy va non bepul")
        if lavash_turi == "2":
            lavash_soni = int(input("Nechta go'shtli lavash harid qilmoqchisiz"))
            if lavash_soni == lavash_soni:
                print(f"To'lo'v {20000 * lavash_soni}")
            print("Choy va non bepul")
        if lavash_turi == "3":
            lavash_soni = int(input("Nechta Garimdorili lavash harid qilmoqchisiz"))
            if lavash_soni == lavash_soni:
                print(f"To'lo'v {23000 * lavash_soni}")
            print("Choy va non bepul")
    if fast_food_turi == "6":
        haggi_soni = int(input(f"{ism} nechta haggiga buyurtma bermoqchisiz: "))
        if haggi_soni == haggi_soni:
            print(f"To'lo'v: {19000 * haggi_soni}")
            print("Choy va non bepul")
    suv = input("Ichishga suv ham buyurasizmi: ")
    if suv == "Ha":
        print("1.Pepsi\n"
              "2.CocaCola\n"
              "3.Fanta\n"
              "4.AysTea\n"
              "5.ArkTea\n"
              "6.FuseTea")
        tanla = input("Qay birini tanladigiz: ")
        if tanla == "1":
            nechaLitr = input("Nechi litirlik pepsi harid qilmoqchisiz(Namuna: 1,5): ")
            if nechaLitr == "1":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {7000 * nechta}")
            if nechaLitr == "1,5":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {12000 * nechta}")
            if nechaLitr == "2":
                nechta = int(input(f"Nechta {nechaLitr}lik pepsi harid qilmoqchisiz: "))
                if nechta == nechta:
                    print(f"Olgan suvingizni narhi: {16000 * nechta}")
        if tanla == "2":
            nechaLitr_cola = input("Necha litr CocaCola harid qilmoqchisiz:")
            if nechaLitr_cola == "1":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {8000 * nechta_cola}")
            if nechaLitr_cola == "1,5":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {10000 * nechta_cola}")
            if nechaLitr_cola == "2":
                nechta_cola = int(input(f"Necha {nechaLitr_cola}litirli cola xarid qilmoqchisiz: "))
                if nechta_cola == nechta_cola:
                    print(f"Suvingizni narhi: {14000 * nechta_cola}")
        if tanla == "3":
            nechaLitr_fanta = input("Necha litrlik fanta sotib olmoqchisiz")
            if nechaLitr_fanta == "1":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {8000 * nechtaFantf}")
            if nechaLitr_fanta == "1,5":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {13000 * nechtaFantf}")
            if nechaLitr_fanta == "2":
                nechtaFantf = int(input(f"Nechta {nechaLitr_fanta} sotib olmoqchisiz"))
                if nechtaFantf == nechtaFantf:
                    print(f"Sotib olgan suvingiz summasi: {17000 * nechtaFantf}")
        if tanla == "4":
            nechtaAys = int(input("Nechta AysTea sotib olmoqchisiz: "))
            if nechtaAys == nechtaAys:
                print(f"Sotib olgan suvingiz narhi: {8000 * nechtaAys}")
        if tanla == "5":
            nechtaArk = int(input("Nechta ArkTea xarid qilmoqchisiz: "))
            if nechtaArk == nechtaArk:
                print(f"oladigan suvingiz summasi: {6000 * nechtaArk}")
        if tanla == "6":
            nechtaFuse = int(input("Nechta FuseTea xarid qilmoqchisiz: "))
            if nechtaFuse == nechtaFuse:
                print(f"Oladigan suvingiz summasi {10000 * nechtaFuse}")
