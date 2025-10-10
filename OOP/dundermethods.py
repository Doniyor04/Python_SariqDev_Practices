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
        Talaba.__num_talaba += 1
        
    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya}"
    
    def __lt__(self, boshqa_talaba):
        if self.bosqich < boshqa_talaba.bosqich:
            return boshqa_talaba
        else:
            return self

    def __eg__(self, boshqa_talaba):
        return self.bosqich == boshqa_talaba.bosqich

    def __getitem__(self, index):
        if type(index) == int:
            if 0<=index<len(self.fanlar):
                return self.fanlar[index]
            else:
                print(f"Iltimos 0 yoki 0 dan katta {len(self.fanlar)} dan kichik index kiriting")
        else:
            print("Iltimos butun son yozing")
    
    def __setitem__(self, index, value):
        if type(index) == int:
            if 0<=index<len(self.fanlar):
                if value in self.fanlar:
                    value = self.fanlar.pop(self.fanlar.index(value))
                    self.fanlar.insert(index, value)
                else:
                    self.fanlar[index] = value
            else:
                print(f"Iltimos 0 yoki 0 dan katta {len(self.fanlar)} dan kichik index kiriting")
        else:
            print("Iltimos butun son yozing")

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
    
    def fanga_yozil(self, *fanlar):
        for fan in fanlar:
            if isinstance(fan, Fan):
                if fan in self.fanlar:
                    print(f"{self} {fan} fanida bor")     
                else:
                    self.fanlar.append(fan)
                    fan.talabalar.append(self)
            else:
                print("Fan obyektini kiriting!")
    
    def remove_fan(self, *fanlar):
        for fan in fanlar:
            if isinstance(fan, Fan):
                if fan in self.fanlar:
                    self.fanlar.remove(fan)
                    fan.talabalar.remove(self)
                else:
                    return f"{self} {fan.get_info()} faniga yozilmagan"
            else:
                print("Fan obyektini kiriting!")
        
    

talaba1 = Talaba("Doniyor", "Abdusattarov", "AD2272477", 2004, 46856)
talaba2 = Talaba("Davron", "Olimov", "AB6125489", 2005, 56453)
talaba3 = Talaba("Ali", "Mahmudov", "AB6125489", 2006, 23156)

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        """ Professor xusisiiyatlari """
        super().__init__(ism, familiya, passport, tyil)
        
        self.lavozim = "Professor"
    def __repr__(self):
        return f"Professor: {self.ism} {self.familiya}"

    def get_info(self):
        info = f"{self.ism} {self.familiya}. " 
        info += f"{self.tyil}-yilda tug`ilgan, Lavozimi:{self.lavozim}"
        return info
    def get_lavozim(self): 
    	return self.lavozim

professor1 = Professor("Otabek", "Mahmudjonov", "FW34543", 1995)

class Fan:
    __num_fan = 0
    fanlar = []
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
        Fan.fanlar.append(self)
        Fan.__num_fan += 1

    def __repr__(self):
        return self.nomi.title()
    
    def __len__(self):
        return len(self.talabalar)

    @classmethod
    def get_num_fan(cls):
        return cls.__num_fan
    @classmethod
    def get_fanlar(cls):
        return cls.fanlar


    def get_info(self):
        return self.nomi.title()
    
    def get_talabalar(self):
        return [talaba for talaba in self.talabalar]
    
    def add_student(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)
                talaba.fanlar.append(self)
            else:
                print("Talaba obyektini kiriting!")

    def remove_student(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar.remove(talaba)
                talaba.fanlar.remove(self)
            else:
                print("Talaba obyektini kiriting!")

fan1 = Fan("matematika")
fan2 = Fan("ingliz tili")
fan3 = Fan("geografiya")
fan4 = Fan("rus tili")
fan5 = Fan("ona tili")

talaba1.fanga_yozil(fan1, fan2, fan3, fan4, fan5)
talaba2.fanga_yozil(fan2, fan3)
talaba3.fanga_yozil(fan2, fan4)

for fan in Fan.get_fanlar():
    print(f"{fan} fanimizda {len(fan.talabalar)} ta bola o'qiydi")

