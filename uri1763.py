while True:
    try:
        pais = input()
        if(pais=='brasil' or pais=='portugal'):
            print('Feliz Natal!')
        elif(pais=='alemanha'):
            print('Frohliche Weihnachten!')
        elif(pais=='austria'):
            print('Frohe Weihnacht!')
        elif(pais=='coreia'):
            print('Chuk Sung Tan!')
        elif(pais=='espanha' or pais=='argentina' or pais=='chile' or pais=='mexico'):
            print('Feliz Navidad!')
        elif(pais=='grecia'):
            print('Kala Christougena!')
        elif(pais=='estados-unidos' or pais=='inglaterra' or pais=='australia' or pais=='antardida' or pais=='canada'):
            print('Merry Christmas!')
        elif(pais=='suecia'):
            print('God Jul!')
        elif(pais=='turquia'):
            print('Mutlu Noeller')
        elif(pais=='irlanda'):
            print('Nollaig Shona Dhuit!')
        elif(pais=='belgica'):
            print('Zalig Kerstfeest!')
        elif(pais=='italia' or pais=='libia'):
            print('Buon Natale!')
        elif(pais=='siria' or pais=='marrocos'):
            print('Milad Mubarak!')
        elif(pais=='japao'):
            print('Merii Kurisumasu!')
        else:
            print('--- NOT FOUND ---')
    except EOFError:
        break
