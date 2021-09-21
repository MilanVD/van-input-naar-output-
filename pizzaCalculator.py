#pizzaCalculator.py

Invoer1 = input('Hoeveel small Pizzas wilt u?')
aantalsmalPizzas = Invoer1
prijssmallpizza = 6
Invoer2 = input('Hoeveel medium Pizzas wilt u?')
aantalmediumpizzas = Invoer2
prijsmediumpizza = 9
Invoer3 = input ('hoeveel large Pizzas wilt u?')
aantallargepizzas = Invoer3
prijslargepizza = 13.5
Invoer4 = input('hoeveel sictergitlan pizzas wilt u?')
aantalsictergitlanpizzas = Invoer4
prijssictergitlanpizza = 20

totaalprijs = (int(Invoer1) * float(prijssmallpizza)) + (int(Invoer2) * float(prijsmediumpizza)) + (int(Invoer3) * float(prijslargepizza)) + int(Invoer4) * float(prijssictergitlanpizza)

print(" bij de domilan kosten de pizzas " + str(totaalprijs) + " voor de " + str(Invoer1)
      + " small pizzas, " + str(Invoer2) + " medium pizza, " +   str(Invoer3)  + " large pizzas en de " + str(Invoer4) + " sictergitlan pizza ")
