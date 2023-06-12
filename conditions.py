import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("ce message ne s'affichera jamais")

number1 = random.randint(0 ,10)
number2 = random.randint(0 ,10)
print(f'{number1 =}')
print(f'{number2 =}')

#blocif1
if number1 < number2:
    print("la variable number1 est plus petite que number2")

#blocif2
if number1 < number2:
    print("la variable number1 est plus petite que number2")
else:
    print("la premiére condition n'est pas vérifiée")


 
if number1 < number2:
    print("la variable number1 est plus petite que number2")
else: #number1 >= number2
    print("la variable number1 est plus grande au egale à number2")

#blocif3
if number1 < number2:
    print("la variable number1 est plus petite que number2")
elif number1 > number2:
    print("la variable number1 est plus grande que number2")
else :
    print("les 2 variables number1 et number2 sont egales")

    #elif == else if

    #bloc if4
    #réécriture du bloc if 3 avec des if imbriqués
if number1 < number2:
    print("la variable number1 est plus petite que number2")
else:
    if number1>number2:
        print("la variable number1 est plus grande que number2")
    else:
        print("les 2 variables number1 et number2 sont egales")

#opérateurs booléens
print(True)
print(False)
#négation
print(not True)
print(not False)

#table de vérité de l'opérateur de négation
#A    not A
#True False
#False True

# OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#table e vérité de l'opérateur ou logique 
# A     B        A or B
#true   true        True 
#True   False       True
#False  True        True
#False  False       False

#pour retrouver la table,remplacer:
#-A par "j'ai du cash"
#-B par "j'ai ma cb"
#-" A OR B" par "puis-je faire mes courses ?"

# ET logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#table e vérité de l'opérateur ET logique 
# A     B        A or B
#true   true       True  
#True   False      False 
#False  True       False 
#False  False      False

#pour retrouver la table,remplacez:
#-A par "j'ai coupé l'electricité"
#-B par "j'ai coupé l'eau"
#-"A or B" par "puis je partir 3 mois à l'etranger?"


#table e vérité de l'opérateur NAND (not and)
# A     B        A or B     not(A and B)
#true   true       True     False
#True   False      False    True
#False  True       False    True
#False  False      False    True

#utilisation de l'opérateur and pour voir si une variable est dans un interval de valeurs



