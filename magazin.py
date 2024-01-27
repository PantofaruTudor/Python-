#fac un magazin unde introduci bugetul si spui ce ai nevoie, in schimb primesti variante de cumparaturi
#preturile obiectelor vor fi puse intr o matrice
obiecte=['electronice','mancare','haine']

denumiri_obiecte={
    'haine':['tricou', 'pantaloni', 'geaca', 'vesta'],
    'mancare':['mazare','rosii','cartofi','pizza'],
    'electronice':['Incarcator','Mouse', 'Airpods', 'Iphone']
}
lista_obiecte = {
    'haine':[50,70,100,200],
    'mancare':[9,10,13,20],
    'electronice':[100,150,1000,2000]
}

def F_buget(): # terminat
    while True:
        buget=input("Buna ziua si bine v-am gasit la magazinul nostru. Ce buget aveti?")
        print()
        if(buget.isdigit()):
            print("Bugetul tau este de:",buget,"lei")
            print()
            break
        else:
            print("Introduceti un numar!")
            print()
    return int(buget)

    
def intreaba():  # terminat
    lista_obiecte=[]
    i=0
    ok=1
    while True:
        ok=1
        sortare=input("Ce categorii alegeti?")
        print()
        input_values=sortare.split()
        for i in range(len(input_values)):
            if isinstance(input_values[i],str) and input_values[i] in obiecte:
                lista_obiecte.append(input_values[i])
            else:
                print("Trebuie sa alegeti doar din selectia noastra!")
                print()
                ok=0
                input_values=[]
                lista_obiecte=[]
        if(ok==1):
            print("Multumim pentru alegerea facuta")
            print()
            return lista_obiecte
                


def find_combination(budget, categories, items, best_combination):
    zippedList=[]

    nrCtg=len(categories)-1
    for categorii in categories:
        zippedList.append(tuple(zip(denumiri_obiecte[categorii], lista_obiecte[categorii])))

    #print(zippedList)
    '''print(best_combination[0])
    print(best_combination[0][0])
    print(best_combination[0][0][0])'''
    index = 0 
    hIndex = 0

    while budget>0 and hIndex < len(zippedList[index]):        

        price = zippedList[index][hIndex][1]
        if price <= budget:
            best_combination.append(zippedList[index][hIndex][0])
            budget -= price
            index += 1
            if index > nrCtg:
                index = 0
                hIndex += 1
        else:
            break

    return best_combination,budget


def main():
    buget=F_buget()
    lista_magazin=intreaba()
    listaZip=[]

    result,BugetF=find_combination(buget, lista_magazin,lista_obiecte, listaZip)
    
    if len(result)==0:
        print("Ne pare rau, nu puteti achizitiona nimic ):")
    else:
        print("Obiectele disponibile pentru dumneavoastra sunt:", end=" ")
        print(" ")
        for final_combination in result:    #prin asta pun raspunsul separat
            print(final_combination, end=" ")
        print(" ")
        print("Bugetul ramas este:", BugetF, 'lei')


main()

