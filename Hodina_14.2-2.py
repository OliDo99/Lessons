def Factorial(my_num):
    if my_num == 1:
        return 1
    else:
        return (my_num * Factorial(my_num-1))
Number = int(input("Zadaj cislo: "))
vysledok = Factorial(Number)
print("Factorial cisla", Number, "je:",vysledok)
