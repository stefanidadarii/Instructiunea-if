#Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?

n=int(input('Ionel a sosit al '))
if n%4==0:
    print('Ionel se va caza in casuta cu nr. ', n//4)
else:
    print('Ionel se va caza in casuta cu nr. ', n//4+1)