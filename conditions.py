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

# syntaxe alternative spécifique à Python
#équivalent de : age >= 12 and age <= 25
#print(12 <= age <= 25)

# OU EXCLUSIF
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

#table de vérité de l'operateur XOR
# A     B       A XOR B 
# True  True    False
# True  False   True
# False True    True
# False False   False

# exo course(opérateur OU Logique)
#affichez:
#-"je peux aller faire les courses"si on a au moins un moyen de paiement
#-"je ne peux pas aller faire les courses"si je n'ai aucun moyen de paiement
has_cash = bool(random.randint(0,1))
has_cb = bool(random.randint(0,1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cb or has_cash:
    print("je peux aller faire les courses")
else :
    print("je ne peux pas aller faire les courses")

# exo courses (opérateur ET logique)
#remplissez le meme cahier des charges mais avec l'opérateur ET

if has_cb ==  False and has_cash == False :
    print("je ne peux pas aller faire les courses")
else:
    print("je peux aller faire les courses")

# combinaison d'operateurs AND et OR
user_level = 1
user_xp = 0
user_social = 150
if user_level >= 3 and (user_xp >= 100 or use_social >= 100):
  print("je peux echeter du matériel")
else:
    print("le joueur ne peut pas acheter de matériel")

#version buggée
if user_level >= 2 and user_xp >= 100 or user_social >= 100:
    print("je peux echeter du matériel")
else
    print("le joueur ne peut pas acheter de matériel")

    
#exo carte de réduction
#determinez la carte de réduction auquelle le voyageur a droit:
#-entre 0 et 11 ans (inclus),le voyageur a droit a la gratuité
#-entre 12 et 25 ans (inclus),le voyageur a droit à une reduction de 50%
#-entre 26 et 64 ans (inclus),le voyageur à droit a une reduction de 10%
#-au dela de 65 ans (inclus),le voyageur à droit à une reduction de 50%
age = random.randint(0,99)
if age >= 0 and age <= 11:
    print("le voyageur à droit à la gratuité")
elif age >= 12 and age <= 25:
    print("le voyageur à droit à une reduction de 50%")
elif age >= 26 and age <= 64:
    print("le voyageur à droit à une reduction de 10%")
elif age >= 65 and age <= 99:
    print("le voyageur à droit à une reduction de 50%")







