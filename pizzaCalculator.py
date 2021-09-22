#pizzaCalculator.py

Invoer1 = int(input("Hoeveel small Pizza's wilt u? : "))
aantalsmallPizzas = Invoer1
prijssmallpizza = 6
Invoer2 = int(input("Hoeveel medium Pizza's wilt u? : "))
aantalmediumpizzas = Invoer2
prijsmediumpizza = 9
Invoer3 = int(input ("hoeveel large Pizza's wilt u? : "))
aantallargepizzas = Invoer3
prijslargepizza = 13.5
Invoer4 = int(input("hoeveel sictergitlan pizza's wilt u? : "))
aantalsictergitlanpizzas = Invoer4
prijssictergitlanpizza = 20

print(f"{Invoer1}x small pizza's : (€{prijssmallpizza*Invoer1} : ")
print(f"{Invoer2}x medium pizza's : (€{prijsmediumpizza*Invoer2} : ")
print(f"{Invoer3}x large pizza's : (€{prijslargepizza*Invoer3} : ")
print(f"{Invoer4}x sictergitlan pizza's : (€{prijssictergitlanpizza*Invoer4} : ")



totaalprijs = (int(Invoer1) * float(prijssmallpizza)) + (int(Invoer2) * float(prijsmediumpizza)) + (int(Invoer3) * float(prijslargepizza)) + int(Invoer4) * float(prijssictergitlanpizza)

print(" bij de domilan kosten de pizza's " + str(totaalprijs) + " voor de " + str(Invoer1)
      + " small pizza's, " + str(Invoer2) + " medium pizza, " +   str(Invoer3)  + " large pizza's en de " + str(Invoer4) + " sictergitlan pizza ")
