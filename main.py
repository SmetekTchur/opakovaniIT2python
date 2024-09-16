import random
#Proměnné kde jako proměná je jméno a příjmení
name = ("Martin")
name2 = (" Tchuř")
print (name + name2)

#zadání věku(jen číslo bez písmen)
num = int(input("Zadejte věk "))
print("Váš věk:", num)

#Kolik písmen je v obou proměnných
name = (len("Martin"))
name2 = (len(" Tchuř"))
print (name + name2)

#Proměnná ve které je číslo 6
num2 = 6

#Cyklus který má 5 opakování, už se dokonce vypisuje do konzole i výsledek
cyklus = 0

cislo = 6
for i in range(1,6):
    cislo += 3
print(cislo)

#Uživatel zde může zadat jen celočíselnou hodnotu
vek = input("Zadej věk: ")
if vek.isdigit():
  print("Děkuji")
else:
  print("Zadej jen celočíselnou hodnotu.")

#Náhodné číslo od 1 do 10
nahodne_cislo = random.randint(1, 10)
print(nahodne_cislo)
