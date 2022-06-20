quetzales = input('Ingrese cantidad de Quetzales: ')
quetzales = float(quetzales)

valor_dolar = 7.8

dolares = quetzales / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print('Tines $' + dolares)