class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __num_shaxs = 0

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__num_shaxs += 1

    @classmethod

    def get_num_talaba(cls):
        return cls.__num_shaxs


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
    __num_talaba = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
        Talaba.num_talaba += 1
    
    @classmethod
    def get_num_talaba(cls):
        return cls.__num_talaba

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

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        """ Professor xusisiiyatlari """
        super().__init__(ism, familiya, passport, tyil)
        
        self.lavozim = "Professor"

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan, Lavozimi:{self.lavozim}"
        return info
    
    def get_lavozim(self):
        return self.lavozim

professor1 = Professor("Otabek", "Mahmudjonov", "FW34543", 1995)

class Fan:
    __num_fan = 0
    def __init__(self, nomi):
        self.nomi = nomi
        Fan.__num_fan += 1

    @classmethod
    def get_num_fan(cls):
        return cls.__num_fan
    
    def get_info(self):
        return self.nomi.title()
    
fan1 = Fan("matematika")
fan2 = Fan("ingliz tili")
fan3 = Fan("geografiya")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)