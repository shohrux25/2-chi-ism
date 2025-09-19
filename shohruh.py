
def ism_familiya():
    birinchi = input("Ismingizni kiriting: ").upper()
    ikkinchi = input("Familyangizni kiriting: ").upper()
    tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: ").strip())
    hozirgi_yil = int(input("Hozirgi yilni kiriting: ").strip())

    yosh = hozirgi_yil - tugilgan_yil
    print(f"Salom {birinchi} {ikkinchi}, sizning yoshingiz {yosh} da.")

if __name__ == "__main__":
    ism_familiya()
