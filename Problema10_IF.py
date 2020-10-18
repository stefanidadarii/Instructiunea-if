'''La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
numărul de boabe de porumb.'''

g=int(input('Numărul de găini: '))
b=int(input('Numarul de boabe: '))
if (b%g)==(b//g):
    print('Numarul de boabe primite este', c, ', egalitate')
elif (b%g)>(b//g):
    print('Clapon a primit mai multe boabe cu', r-c, 'boabe')
else:
    print('Gainele au primit mai multe boabe cu', c-r, 'boabe')