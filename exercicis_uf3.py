#Crea una script que llegeixi un fitxer fruites.txt i n’escrigui el contingut, linea a linea pel terminal.

"""
fitxer = open('fruites.txt')

for linia in fitxer.readlines():
    print(linia)

fitxer.close()

#Imagina que la llista de fruites ara ve en format csv, o sigui tot en una línea separada per ‘;’. 
# Procesa el fitxer per tal que la sortida pel terminal imprimeix una fruita per línia.
fitxer = open('fruites.txt', encoding="utf-8")

for linia in fitxer.readlines():
    fruity=linia.split(";")
    for fruit in fruity:
        print(fruit.strip())
        

print(linia)

fitxer.close()

#Crea un script que llegeixi un fitxer anomenat números i que en faci la suma i ho mostri pel terminal.
fitxer = open('numeros.txt')
suma = 0
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


for linia in fitxer.readlines():
    try:
        suma += int(linia)
        print(suma)
    except :
        print("Introdueix numeros")
    <
fitxer.close()
"""
#ACTIVITAT agenda de telèfons, crea un fitxer amb un contingut similar a aquest:Llegeix el fitxer i converteix-lo en un diccionari que utilitzi com a clau el número de 
# telèfon i com  a valor el nom  Mostra tota l'agenda demana a l'usuari que esculli  un telèfon i mostra una línia que digui: Trucant a XXX al número NNNN
#Pepe 666666666
#Paco 777777777
#Pere 888888888

#x=(input("Quin fitxer de text vols obrir?"))
#g=open(input("nom del fitexer:")+".txt")
"""agenda={}

fitxer = open(input("nom del fitexer:")+".txt")
for linia in fitxer:
    cont=linia.split()
    agenda[cont[1].rstrip()]=cont[0] #strip borra espais en blanc  deban amb r de detras 
    print(linia)
"""
#print("No es pot obrir el fitxer")


"""
#modifica el codic para que es mostre el  correus que surten de uct.ac.za
man_a = open("mbox-short.txt")
for linia in man_a:
    if linia.find("uct.ac.za") and linia.find("From")!= -1:
        print(linia.rstrip())

"""
#modifica l'agenda la possibilitat de cercar al fitxer amb el telefon d'un contacte !
#Modifiqueu u l’aplicació per a que a partir de diferents txt (família, laboral,
#amics) es mostri a l’usuari un menú on pugui escollir la categoria que vol
#obrir
agenda={}

fitxer = open(input("nom del fitexer:")+".txt")
for linia in fitxer:
    cont=linia.split()
    agenda[cont[1].rstrip()]=cont[0] #strip borra espais en blanc  deban amb r de detras 
    print(linia)