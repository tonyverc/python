# nombre entier, integer
number1 = 123
number1 = 42
print(number1)

#nombre à virgule flottante, float
number2 = 3.14
number2 = 2.71
print(number2)

#chaine de caractéres, string
text1='foo bar baz'
print(text1)

text2="foo bar bar"
print(text2)

# booléen, boolean
python_is_cool = True
print(python_is_cool)


python_is_boring = False
print(python_is_boring)

# null, valeur nulle,null value
user_accepted_terms= None
print(None)

#types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

#verification du type de données
print(type(number1)is int)
print(type(number1)is str)
print(type(text1)is int)
print(type(text1)is str)

#todo: interroger le type des autres variables...

#transtypage int -> str
print(type(str(number1)))
print(str(number1))

#transtypageint ->bool
print(type(bool(number1)))
print(bool(number1))

#convertie en booléén,la valeur 0 donne false
number3 = 0
print(bool(number3))

#trantypage str -> int
#génére l'erreur: ValueError:invalid litteral for print
print(type(int(text1)))

#il ne peut pas y avoir autre chose qu un nombre dans la chaine de caractére
#si on veut la convertir en int

text3 = "123456789"
print(type(int(text3)))

#les fonctions de transtypage
#str() convertie vers string
#int() convertie vers integer
#float() convertie vers float
#bool() convertie vers boolean

#chaine de caractéres,string
#cette notation permet d'utiliser des sauts de ligne
text4= """<div>
    <h1>titre de premier niveau</h1>
    </div>
    """
#\n est equivalent à un saut de ligne
#\t est equivalent à une tabulation
text5= "<div>\n\<h1>titre de premier niveau</h1>\n</div>\n"

print(text5)


#la backslash seul est le caractére d'echappement
#\"equivalent à une guillemet"
#\\ est equivalent à un back slash \


text6="Foo \"Bar\" Baz"

text7="c:\\Programm Files\\foo"

#permutez les deux variables a et b en utilisant 
#l'operation d'affectation et le nom des variables
a=123
b=42
c=165

#permutation des valeurs à l'aide de la methode pythonique
#destructured assignment
b, a = a, b

#permutation des valeurs à l'aide d'une variable temporaire
c=b
b=a
a=c

print(a)
print(b)

#permutation des valeurs à l'aie d'operations arithmétiques
a= a+b
b= a-b
a= a-b

print(a)
print(b)

#addition de float
#affiche 0.300000000004 au lieu de 0.3
print(0.1+0.1+0.1)

import decimal
from decimal import decimal

#affiche correctement 0.3
print(Decimal("0.1")+("0.1")+("0.1"))

#affiche correctement 0.3
print(Decimal("0.3"))

#ne fonctionne pas pour additionner des floats

#arrondi des floats
decimal.getcontext().rounding = decimal.
ROUND_HALF_up
print(Decimal("0.05").quantize(Decimal("1")))
print(Decimal("0.15").quantize(Decimal("0.1")))





