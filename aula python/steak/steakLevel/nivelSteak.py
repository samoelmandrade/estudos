def steak (temperatura):
    if temperatura < 48 :
        print("cozinhar por mais alguns minutos: ")
    elif temperatura in range(48,53):
        print ('Selada')
    elif temperatura in range(53,59):
        print ('ao ponto para mal')
    elif temperatura in range(59,64):
        print ('ao ponto')
    elif temperatura in range(64,70):
        print ('ao ponto para bem')
    elif temperatura in range(70,99):
        print ('bem passada')
    elif temperatura >= 100:
        print ('coloca fora')