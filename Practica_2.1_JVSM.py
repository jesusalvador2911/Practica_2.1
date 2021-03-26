# JESUS SALVADOR VALLES MACIEL
#CARRERA: INFORMATICA
#DESARROLLO DE APLICACIONES WEB
#PRACTICA 2.1 VOTOS

#mostramos las opciones que tienen
print("""
    1) AMARILLO       3) MORADO
    2) ROJO        
    """)
#definimos las variables que usaremos, asi como las librerias
import random
A = (0)
B = (0)
C = (0)
voto = (0)
candi = [1,2,3,4]

#luego definiremos el numero de veces que queremos que se repita la eleccion
while voto <= 2000:
    #usaremos la libreria random para que sea una eleccion impracial
    eleccion = random.choice(candi)
    #definira cual fue la eleccion de la computadora
    if eleccion == 1:
        print ("A votado por PARTIDO AMARILLO")
        #esta varaible contabilizara los votos de cada uno de los candidatos
        A=(A+1)
        #y esta hara avanzar el ciclo
        voto = (voto+1)
    elif eleccion == 2:
        print ("A votado por PARTIDO MORADO") 
        B=(B+1)
        voto = (voto+1)
    elif eleccion == 3:
        print ("A votado por PARTIDO ROJO") 
        C=(C+1)
        voto = (voto+1)
    else:
        print("OPCION NO VALIDA")
#una vez terminado el ciclo se mostraran los resultados
print("""Los resultados son:

""")
print((A)," Votaron por PARTIDO AMARILLO")
print((B)," Votaron por PARTIDO MORADO")
print((C)," Votaron por PARTIDO ROJO")
#luego buscara el resultado que cumpla las dos condiciones para saber quien fue el ganador
if A > B and C:
    print("El ganador es el PARTIDO AMARILLO con: ",(A), " votos")
elif B > C and A:
    print("El ganador es el PARTIDO MORADO con: ",(B), " votos")
elif C > B and A:
    print("El ganador es el PARTIDO ROJO con: ",(C), " votos")
else:
    print("Ha habido un empate")
