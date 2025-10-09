# son_top() biz
# son_top_pc pc
# yutuq hisoblagich
# while 

import random as r

def son_top(x=10):
    urinish = 0
    son_pc = r.randint(1, x)
    print(f"1 dan {x} gacha son o'yladim. Topa olasizmi?:")
    while True:
        urinish += 1
        taxmin = int(input(""))
        if taxmin > son_pc:
            print("Xato. Men o'ylagan son bundan kichik. Yana xarakat qiling:")
        elif taxmin < son_pc:
            print("Xato. Men o'ylagan son bundan katta. Yana xarakat qiling:")
        else:
            print(f"Topdingiz! {taxmin} sonini o'ylagan edim. {urinish} ta taxmin bilan topdingiz. Tabriklayman!")
            break
    return urinish

def son_top_pc(x=10):
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    urinish=0 
    min = 1
    max = x
    while True:
        urinish += 1
        if min != max:
            taxmin_pc = r.randint(min, max)
            javob = input(f"siz {taxmin_pc} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)")
        else:
            taxmin_pc = min
            break
        if javob == "+":
            min = taxmin_pc + 1
        elif javob == "-":
            max = taxmin_pc - 1
        else:
            break
    print(f"Siz {taxmin_pc} sonini o'yladingiz. {urinish} ta taxminda topdim")
    return urinish

def play(x=10):
    yana = True
    while yana:
        taxmin = son_top(x)
        taxmin_pc = son_top_pc(x)

        if taxmin < taxmin_pc:
            print(f"Siz {taxmin} ta taxmin bilan topdingiz va yutdingiz.")
        elif taxmin > taxmin_pc:
            print(f"Men {taxmin_pc} ta taxmin bilan topdim va yutdim.")
        else:
            print(f"Durrang. Ikkimiz ham {taxmin} ta taxmin bilan topdik.")

        yana = int(input("Yana o'ynaymizmi?: ha(1) / yo'q(0): "))



