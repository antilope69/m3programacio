from subprocess import run
import sys
#Fem un ip a i guardem la informació separada per línies.
result=run(["ip","a"],capture_output=True, text=True)
linies=result.stdout.split("\n")
#Guardem sols les línies que comencen per inet
lxarxes=[]
for i in range(len(linies)):
    linies[i]=linies[i].strip()
    if (linies[i][:5]=="inet "):
        lxarxes.append(linies[i])
#Creem un diccionari
diccionari1={}  
#Guardem la posició -1 (última posicó) com a camp del diccionari i la posició 1 com a valor.
for i in lxarxes:
    i=i.split()
    diccionari1[i[-1]]=i[1]
#Imprimim en pantalla les interfícies    
print("S'han trobat aquestes interfícies:\n")
for camp, valor in diccionari1.items():
    print(camp+": "+valor)
#Bucle per a demanar a quina interfície es vol fer el Ping Sweap.
while True:
    try:
        interficie=input("\nEscriu el nom exacte de la interfície que vols fer un Ping Sweap: ")
        pregunta=input("Estas segur que vols fer un Ping Sweap a aquesta ip: "+diccionari1[interficie]+"? Escriu Si o No\n")
    except: continue
    if pregunta.upper() != "SI":
        continue
    elif pregunta.upper() =="SI":
        break
#Creem 2 llistes per a guardar la informació del ping sweap.
ips=[]
ipstemporal=[]
#Fem el ping sweap i guardem el resultat en la variable linies.
result=run(["nmap","-sP",diccionari1[interficie]],capture_output=True, text=True)
linies=result.stdout.split("\n")
#Creem un bucle per a guardar la informació de linies separada per linies.
for i in range(len(linies)):
        linies[i]=linies[i].split()
        ips.append(linies[i])
#Creem un bucle per a guardar en una altra llista sols la última paraula de cada linia de la llista ips.
for i in ips:
    try:
        ipstemporal.append(i[-1])
    except: continue
#Tornem a crear la llista ips buida.
ips=[]
#Fem un bucle per a guardar les paraules en ips però sols si aquestes es troben en posició impar.
#Fem això ja que a les posicions pars es troba text i a les impars es troben les ips.
for i in range(len(ipstemporal)):
    if i % 2 ==1:
        ips.append(ipstemporal[i])
#Eliminem l'última paraula de la llista ips, ja que l'última paraula es "seconds" i no ens interesa guardar-la.
ips.pop()
#Si la llista està buida (No ha trobat cap equip) el programa no es seguirà executant.
if ips:
    print("S'han trobat les següents ips:")
else:
    print("No s'ha trobat cap equip")
    sys.exit()
#Imprimim en pantalla les ips dels equips que ha trobat.
num=1
for i in ips:
    i=str(i).replace('(','')
    i=str(i).replace(')','')
    print(str(num)+".",i)
    num+=1
#Fem un bucle per a que l'usuari indique a quina ip vol fer l'escaneig.
while True:
    escaneig=input("Escolleix a quina IP vols fer l'escaneig dels ports ")
    if escaneig.isnumeric()==False or int(escaneig)<=0 or int(escaneig)>len(ips):
        print("Introdueix un número entre 1 i",len(ips))
    else:break
#guardem la ip a una variable anomenada escaneig.
escaneig=ips[int(escaneig)-1]
escaneig=str(escaneig).replace('(','')
escaneig=str(escaneig).replace(')','')
#fem un nmap per a fer un escaneig dels serveis actius.
result=run(["nmap","-sV",escaneig],capture_output=True, text=True)
linies=result.stdout.split("\n")

portversio=[]
escaneigpv=[]
#Fem un bucle per a guardar la informació de les linies separada per linies a la variable portversio.
for i in range(len(linies)):
        linies[i]=linies[i].split()
        portversio.append(linies[i])
#Fem un bucle per a guardar sols les linies que comencen amb un número.
for i in portversio:
    try:
        if int(i[0][0])>=0 or int(i[0][0])<=9:
            escaneigpv.append(i)
    except: continue

diccionari2={}
#Fem diversos bucles per a guardar els numeros dels ports a la variable portversio.
for i in range(len(escaneigpv)):
    portversio=[]
    for o in escaneigpv[i][0]:
        for p in str(o):
            if p.isnumeric()==True:
                portversio.append(p)
#Unim per un espai les versions dels serveis.
    versio=(" ".join(escaneigpv[i][2::]))    
#Unim els numeros de la llista portversio
    port=("".join(portversio))
#Afegim al diccionari el port i la versió.
    diccionari2[port]=[versio]
#Si el diccionari està buit el programa es pararà.
if diccionari2:
    print("S'han trobat els següents serveis:\n")
else:
    print("No s'ha trobat cap servei actiu")
    sys.exit()
#Imprimim en pantalla els ports i versions.
for camp, valor in diccionari2.items():
    valor=str(valor).replace('[','')
    valor=str(valor).replace("'",'')
    valor=str(valor).replace(']','')
    print(str(camp)+": "+str(valor))
#Fem un bucle per a que l'usuari indique a quin port vol fer l'escaneig, també pot fer l'escaneig sobre un port tancat.
while True:
    port = str(input("\nA quin port vols fer un escaneig de vulnearibilitats? "))
    if port.isnumeric()==False:
        continue
    else:break
#Per últim fem un escaneig de les vulnerabilitats del servei.
result=run(["nmap",escaneig,"-sV","-p"+port,"--script=vuln"])
print("Codi Retorn:\n",result.returncode)
print("Tipus error:\n",result.stderr)