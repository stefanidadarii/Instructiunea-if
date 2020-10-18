#“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă iubeşte …. 

x=int(input('Nr de petale a margaretei este '))
if (x%5)==1:
    print('El (ea) mă iubeşte un pic')
elif (x%5)==2:
    print('El (ea) mă iubeşte mult')
elif (x%5)==3:
    print('El (ea) mă iubeşte cu pasiune')
elif (x%5)==4:
    print('El (ea) mă iubeşte la nebunie')
else: 
    print('El (ea) mă iubeşte de loc')
