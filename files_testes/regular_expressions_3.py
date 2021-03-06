'''
Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''
import re

def stripr(txt, remove):
    inicioRegex = re.compile(r'^([{}]+)(.*)'.format(remove))
    fimRegex = re.compile(r'([{}]+$)'.format(remove))
    inicio = inicioRegex.search(txt)
    print((lambda: txt, lambda: inicio) [inicio != None]())
    if inicio:
        fim = fimRegex.search(inicio.group(2))
        if fim:
            return inicio.group(2)[:fim.span()[0]]
        else:
            return inicio.group(2)
    else:
        fim = fimRegex.search(txt)
        if fim:
            return txt[:fim.span()[0]]
        else:
            return txt





x = stripr('      teste   teste       ', ' ')
print(x)


y = stripr('..........    teste     .. .. . .tes testes.........      ', '.')
print(y)


z = stripr('          ..........    teste     .. .. . .tes testes.........', '.')
print(z)


w = stripr('          ..........    teste     .. .. . .tes testes.........        ', '.')
print(z)
