beers = [{'name': 'Modelo Especial', 'price': 25.00, 'ap': 4.0},
         {'name': 'Indio','price': 20.00, 'ap': 4.2 },
         {'name': 'Tecate Light','price': 30.00, 'ap': 3.5 },
         {'name': 'Minerva', 'price': 35.00, 'ap': 8.0 },
         {'name': 'Budlight', 'price': 18.00, 'ap': 5.0 }]
# Exercise 3.0
# Output:
# Name  Precio  Porcentaje de Alcohol (%)
# ---   ---     ---
# At the end add a beer of your choice to the dictionary and 
# print the output


print (" Name                    ", " Price          ", " Alcohol Percentage %        ")
beers.append({'name': 'Victoria', 'price': 25.00, 'ap': 5.0})
for dictionary in beers:
    print(dictionary["name"],"              ", dictionary["price"], "                      ",dictionary["ap"])
