import time
 
'''
Vamos a crear un progrma que ingresen una fecha en formato:

dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s

Asi si nos dan una fecha saldra:

## de Mes del Año
'''

## Leemos el archivo y sustituimos \n con '':
with open('Fecha.txt', 'r') as f:
  datos = f.readlines()
  lista = [i.replace('\n', '') for i in datos]

# Imprimimomos la lista creada anteriormente:
print(lista)


## DEFINIMOS UNA FUNCIÓN PARA RESOLVER EL PROBLEMA ANTERIOR:

def validateDateEs(date):
    """
    Funcion para cambiar una fecha en formato:
        dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
    Output:
    dd de Mes del Año
    """
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return result
        except:
            pass
    return False

# Cremaos otro archivo:
w = open('Fechas_Cambiadas.txt', 'w')


## Definimos un diccionario para los mese del año:
meses={1:"Enero",
       2:"Febrero",
       3:"Marzo",
       4:"Abril",
       5:"Mayo",
       6:"Junio", 
       7:"Julio",
       8:"Agosto",
       9:"Septiembre",
       10:"Octubre",
       11:"Noviembre",
       12:"Diciembre"}

## Definimos un for para itera la lista y guardar los valores en otro archivo:
for x in lista:
  fecha = validateDateEs(x)
  if fecha:
    w.write("%s de %s de %s\n" % (fecha.tm_mday, meses[fecha.tm_mon], fecha.tm_year))
  else:
    w.write('Fecha incorrecta\n')

w.close()

#####################2° Ejercicio#####################

import datetime, calendar

# Si es verdadero entonces imprime el calendario con el año indicado
'''
Esta función recibe un año en formato aaaa (int)
y devuelve si es bisesto o no
'''

def es_bi(a):
  '''
  Esta función recibe un año en formato aaaa (int)
  y devuelve si es bisesto o no
  '''
  if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    return "Es un Año Bisiesto"
  else:
    return "No es una Año Bisisesto"

# txt del año bisiesto remplazando los \n por '':
with open('Año_Bisiesto.txt', 'r') as al:
  lista = [i.replace('\n', '') for i in al.readlines()]
    

## Creamos una nueva lista vacia:
lista_int = list()

## Convertimos los años de la lista a int (Enteros)
for i in lista:
  lista_int.append(int(i))

## Hacemos calendarios para años bisiestos:

for x in lista_int:
  if es_bi(x) == "Es un Año Bisiesto":
    strX = str(x)
    with open(f'{strX}.txt', 'w') as year_bis:
      print(calendar.TextCalendar(calendar.SUNDAY).formatyear(x,2, 1, 1, 2), file= year_bis)
      year_bis.close()
  else:
    strX = str(x)
    with open(f'No_es_Bisiesto_el_año_{strX}.txt', 'w') as year_not:
      print(f'El Año {strX}, No es un Año bisiesto', file= year_not)
      year_not.close()
