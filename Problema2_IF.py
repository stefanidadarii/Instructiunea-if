'''La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi
laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici
ca 32000, şi returnează DA sau NU.'''

a=int(input('Primul numar este '))
b=int(input('Al doilea numar este '))
c=int(input('Al treilea numar este '))
if (0<a<32000) and (0<b<32000) and (0<c<32000):
    if (a<b+c) and (b<a+c) and (c<a+b):
        print('Da')
    else:
        print('Nu')
else:
    print('Numerele introduse nu corespund conditiei')