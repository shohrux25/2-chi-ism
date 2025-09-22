def kalkulyator():
    print("🧮 Oddiy Kalkulyator 🧮")
    print("Amallar: +, -, *, /")

    while True:
        a = float(input("\nBirinchi sonni kiriting: "))
        amal = input("Amalni tanlang (+, -, *, /): ")
        b = float(input("Ikkinchi sonni kiriting: "))

        if amal == "+":
            print(f"Natija: {a + b}")
        elif amal == "-":
            print(f"Natija: {a - b}")
        elif amal == "*":
            print(f"Natija: {a * b}")
        elif amal == "/":
            if b != 0:
                print(f"Natija: {a / b}")
            else:
                print("0 ga bo‘lish mumkin emas!")
        else:
            print("❌ Noto‘g‘ri amal tanlandingiz.")

        yana = input("Yana hisoblashni xohlaysizmi? (ha/yo'q): ").lower()
        if yana != "ha":
            print("👋 Dastur tugadi.")
            break


if __name__ == "__main__":
    kalkulyator()
