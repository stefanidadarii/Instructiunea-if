'''Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi.'''

z=int(input('Ziua curenta este '))
l=int(input('Luna curenta este '))
a = int(input("Anul curent este "))
zn=(input('Ziua curenta este '))
ln=int(input('Luna curenta este '))
an =int(input('Anul nasterii este '))
if (l<ln) or (l==ln and z<zn):
    print('Numarul de ani impliniti este ', (a-an)-1)
else:
    print('Numarul de ani impliniti este ', a-an)