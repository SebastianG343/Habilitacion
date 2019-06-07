s=[23,25,18,19,17,25,24,23,18,27,26,25]
g=[15,17,19,23,25,28,24,22,23,19,15,20]
n=[17,18,20,22,23,26,28,30,29,26,22,19]
temas = [ ]
promcalientes=[ ]
n1=0
n2=0
n3=0
conts= 0
contg=0
contn=0
menu = (" ")
while menu != ("000"):
    print("Digite /a/ para ver el promedio de cada departamento")
    print("Digite /b/ para ver el promedio de la temperatura a nivel nacional")
    print("Digite /c/ para ver el mes mas caliente de cada departamento")
    print("Digite /d/ para ver el promedio de los meses mas calientes de cada departamento")
    print("Digite /e/ para ver el promedio con la temperatura mas alta")
    print("Digite /f/ para ver la temperatura mas caliente del año, en que departamento fue y el mes")
    menu = input("Digite una opcion:")
    if menu == "a":
        promcalientes=[]
        
        for i in (s):
            n1+=i
        
        ps= n1/12
        promcalientes.append(ps)
        
        for j in (g):
            n2+=j
        
        pg= n2/12
        promcalientes.append(pg)

        for z in (n):
            n3+=z

        pn= n3/12
        promcalientes.append(pn)
        
        print("Promedio de temperaturas:")
        print("Prom Santander:",ps)
        print("Prom Guajira:",pg)
        print("Prom Nariño:",pn)

        n1 = 0
        n2 = 0
        n3 = 0

    if menu == "b":
        for i in (s):
            n1+=i

        for j in (g):
            n2+=j

        for ñ in (n):
            n3+=ñ

        print("Promedio temperatura nacional:",(((n1/12)+(n2/12)+(n3/12))/3))
        n1 = 0
        n2 = 0
        n3 = 0
    if menu == "c":
        mascalienteS = (s[0])
        for ms in (s):
            if ms > mascalienteS:
                mascalienteS = ms
        mascalienteG = (g[0])
        for mg in (g):
            if mg > mascalienteG:
                mascalienteG = mg
        mascalienteN = (n[0])
        for mn in (n):
            if mn > mascalienteN:
                mascalienteN = mn
        print("Mes mas caliente de Santander:",mascalienteS)
        print("Mes mas caliente de Guajira:",mascalienteG)
        print("Mes mas caliente de Nariño:",mascalienteN)

    if menu == "d":
        mascalienteS = (s[0])
        for ms in (s):
            if ms > mascalienteS:
                mascalienteS = ms
        mascalienteG = (g[0])
        for mg in (g):
            if mg > mascalienteG:
                mascalienteG = mg
        mascalienteN = (n[0])
        for mn in (n):
            if mn > mascalienteN:
                mascalienteN = mn
        print("Promedio de temperatura pico:",((mascalienteS+mascalienteG+mascalienteN)/3))
    if menu == "e":
        promascaliente = promcalientes[0]
        for pmc in (promcalientes):
            if pmc > promascaliente:
                promascaliente = pmc

        print("Promedio de temperatura mas caliente:",(int(promascaliente)))
    if menu == "f":
        mascalienteS = (s[0])
        for ms in (s):
            if ms > mascalienteS:
                mascalienteS = ms
        mascalienteG = (g[0])
        for mg in (g):
            if mg > mascalienteG:
                mascalienteG = mg
        mascalienteN = (n[0])
        for mn in (n):
            x+=1
            if mn > mascalienteN:
                mascalienteN = mn
                mesmasc = x
        if mascalienteS > mascalienteG:
            if mascalienteS > mascalienteN:
                print("Temperatura mayor:", mascalienteS, "en Santander")
                for ññ in (s):
                    conts += 1
                    if mascalienteS == ññ:
                        print("En el mes:", conts)
                conts = 0
            else:
                print("Temperatura mayor:", mascalienteN , "en nariño")
                for ñn in (n):
                    contn += 1
                    if mascalienteN == ñn:
                        print("En el mes:", contn)
                contn = 0
        else:
            if mascalienteG > mascalienteN:
                print("Temperatura mayor:", mascalienteG, "en guajira")
                for ñg in (g):
                    contg += 1
                    if mascalienteG == ñg:
                        print("En el mes:", contg)
                contg = 0
            else:
                print("Temperatura mayor:", mascalienteN, "en nariño") 
                for ñn in (n):
                    contn += 1
                    if mascalienteN == ñn:
                        print("En el mes:", contn)
                contn = 0
      
                      
                    





            

    

