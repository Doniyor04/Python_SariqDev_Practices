# Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_ism(self):
        return self.ism

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def get_fanlar(self):
        if self.fanlar:
            return [fan.get_info() for fan in self.fanlar]
        else:
            return f"{self.ism} fanga yozilmagan"

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"Siz {fan.get_info()} faniga yozilmagansiz"


talaba1 = Talaba("Doniyor", "Abdusattarov", "AD2272477", 2004, 46856)
talaba2 = Talaba("Davron", "Olimov", "AB6125489", 2005, 56453)


# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        """Professor xusisiiyatlari"""
        super().__init__(ism, familiya, passport, tyil)

        self.lavozim = "Professor"

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan, Lavozimi:{self.lavozim}"
        return info

    def get_lavozim(self):
        return self.lavozim


professor1 = Professor("Otabek", "Mahmudjonov", "FW34543", 1995)


# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def get_info(self):
        return self.nomi.title()


fan1 = Fan("matematika")
fan2 = Fan("ingliz tili")
fan3 = Fan("geografiya")


# Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

# Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
