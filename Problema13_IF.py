#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi?

x=int(input('Ionel este pe locul '))
if x<=100:
    if (x%4)==1:
        print('Ionel va prii tricou de culoare albă')
    elif (x%4)==2:
        print('Ionel va prii tricou de culoare rosie')
    elif (x%4)==3:
        print('Ionel va prii tricou de culoare albastră')
    else:
        print('Ionel va prii tricou de culoare neagra')
else:
    print('Ionel nu va primi niciun tricou')