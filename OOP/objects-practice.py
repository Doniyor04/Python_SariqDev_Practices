# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)


def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith("__")]


class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = 0

    # Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    def get_info(self):
        return f"Model: {self.model} \nRangi: {self.rang} \nKorobka: {self.korobka} \nNarxi: {self.narh}$ \nYurgani: {self.kilometer}km"

    def get_model(self):
        return self.model

    # Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing. update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    def update_km(self, km):
        if km >= 0:
            self.kilometer += km
        return self.kilometer


# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)


class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []
        self.avtomobillar_soni = 0

    # Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
    def add_avto(self, avto):
        self.avtomobillar.append(avto)
        self.avtomobillar_soni += 1

    # Avtosalonga avtomobilni o'chirish uchun metod
    def remove_avto(self, avto):
        if avto in self.avtomobillar:
            self.avtomobillar.remove(avto)
            self.avtomobillar_soni -= 1

    # Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
    def get_info(self):
        return f"Avtosalon: {self.nomi} \nSalonda: {[avtomobil.get_model() for avtomobil in self.avtomobillar]}"


avto1 = Avto("Jentra", "Qora", "Avtomat", 18000)
avto2 = Avto("Cobalt", "Oq", "Mexanika", 15000)


avtosalon1 = Avtosalon("GM", "Toshkent")

avtosalon1.add_avto(avto1)
avtosalon1.add_avto(avto2)
