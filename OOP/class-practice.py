# Biror matnni katta harflarda qaytaradi
# class Tekst:
#     def __init__(self, text):
#         self.text = text
    
#     def katta(self):
#         return self.text.upper()
    
# ism = "Doniyor"
# matn1 = Tekst(ism)
# print(matn1.katta())


# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

class User:
    def __init__(self, ism, username, email, password):
        self.ism = ism
        self.username = username
        self.email = email
        self.password = password

# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, \nismi: {self.ism}, \nemail: {self.email}"

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

user1 = User("Doniyor", "spidey_9393", "doniyorabdusattorov4@gmail.com", 132465789)
user2 = User("Olim", "olim3076", "olimbek3076@gmail.com", 3435613)  
user3 = User("Davron", "dav0n12", "davron1298@gmail.com", 654328)

def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

# print(see_methods(User))