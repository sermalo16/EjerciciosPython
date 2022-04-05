def encriptar3(text):
    
    texto = text.lower().split(" ")

    palabras = [
        'murcielago',
        'hipotenusa',
        'escupitajo',
        'sudorienta',
        'suponieras',
        'riachuelos',
        'autenticos',
        'bisabuelos',
        'bufonerias',
        'questionar'
    ]

    dispo = []
    mayor = 0;
    count = 0;
    word = ""
    enc = ""
    indice = 0
    indexL =0
    for letra in texto:
        word = ""
        enc = ""
        indice = 0
        indexL =0
        mayor = 0;
        for palabra in palabras:
            count = 0
            for i in range(len(letra)):
                if(letra[i] in palabra):
                    count+=1
            if(count>mayor):
                mayor = count
                word = palabra

        for i in range(len(palabras)):
            if(word == palabras[i]):
                indice = i
            
        # logica
        enc= str(indice)
        for l in letra:
            indexL=""
            for i in range(len(word)):
                if(l == word[i]):
                    indexL+=str(i)
            if(l not in word):
                indexL+=l.upper()
            enc+=indexL
        dispo.append(enc)    

    print(" ".join(dispo))


encriptar3("la casa solitaria de la montaÃ±a")


#codigo de desencriptacion
        #    enc= str(indice)
        #     for l in range(len(letra)):
        #         for ca in word:
        #             if(ca == letra[l]):  
        #                 enc += str(ca)
        #             elif(ca not in word):
        #                 enc += word[ca]