import random
randomCislo1 = random.randint(0,100)
print("Zadaj cisla tak aby sa ich sucet rovnal ", randomCislo1)
cislo1 = int(input())
cislo2 = int(input())
vysledok = cislo1+cislo2
string = "Nice Debil netrafil si o"
if vysledok == randomCislo1:
    print(string[0:4])
else:
    print(string[5:], abs(randomCislo1-vysledok))

string = "If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways."
user_input = input("Vloz hladany znak: ")
print("V stringu je", user_input, string.count(user_input), "krat")

