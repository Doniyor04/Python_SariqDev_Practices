# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya


def textTitle(text=""):
    if text:
        return text.title()
    else:
        return "Matn bo'sh"
