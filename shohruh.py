import datetime
def ism_familiya():
    birinchi = input("Ismingizni kiriting: ").upper()
    ikkinchi = input("Familyangizni kiriting: ").upper()
    tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: ").strip())
    hozirgi_yil = datetime.datetime.now().year - tugilgan_yil

    yosh = hozirgi_yil
    print(f"Salom {birinchi} {ikkinchi}, sizning yoshingiz {yosh} da.")

if __name__ == "__main__":
    ism_familiya()
