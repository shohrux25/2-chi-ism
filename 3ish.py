
import random

def oyin():
    print(" Raqam topish o‘yini ")
    sirli_son = random.randint(1, 20)
    taxminlar = 0

    while True:
        try:
            son = int(input("1 dan 20 gacha son kiriting: "))
        except ValueError:
            print(" Iltimos, faqat son kiriting!")
            continue

        taxminlar += 1

        if son < sirli_son:
            print("Kichik! ")
        elif son > sirli_son:
            print("Katta! ")
        else:
            print(f" Tabriklaymiz! {taxminlar} urinishda topdingiz!")
            break

if __name__ == "__main__":
    oyin()
