obiecte=['electronice','mancare','haine']

lista_obiecte={
    'haine':{'tricou':50, 'pantaloni':70 ,'vesta':100 , 'geaca':200},
    'mancare':{'rosii':9 , 'mazare':10, 'brocoli':13 , 'cartofi':20},
    'electronice':{'Incarcator':100 , 'Mouse':150 , 'Airpods':1000 , 'Iphone':2000}
}


'''
def preturi():

    lista_e=tuple(zip(electronice,pret_electronice))  TUPLE
    lista_h=tuple(zip(haine,pret_haine))
    lista_m=tuple(zip(mancare,pret_mancare_per_kg))
    return lista_h,lista_e,lista_m

'''


    
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
            print(lista_obiecte)
            return lista_obiecte

def backtracking(current_budget,current_combination, remaining_categories):

    best_combination=[]
    buget_final=0

    if current_budget <= 0 or len(remaining_categories)==0 :
#   6print('alta',best_combination)    #DE CE IMI PUNE COMBINATIA INTR O LISTA INCA O DATA?
        buget_final=current_budget
        return current_combination,buget_final
    index = ""

    while current_budget > 0 or len(remaining_categories) != 0 :
        for con in remaining_categories:
            '''for item in lista_obiecte[con]:'''
            if current_budget>=lista_obiecte[con][index]:
                """
                if len(remaining_categories)==0:
                        return"""
                price=lista_obiecte[con][index]
                if price<=current_budget :
                    current_combination.append(index)  # NICI MACAR NU REUSESTE SA IASA DIN FOR, SE TOT INTOARCE FARA SA TREACA PRIN PRIMUL IF
                    remaining_categories.remove(con)
                    backtracking(current_budget-price,current_combination,remaining_categories)
                else:
                    return 

        
                    



def find_combination(budget, categories, items):
    best_combination = []
    buget_final=0

    
    backtracking(budget, best_combination, categories)
    return best_combination,buget_final


print(lista_obiecte['haine'])
lista_final=intreaba()

combinatie_finala, BUGETUL = find_combination(300,lista_final,lista_obiecte)
print(combinatie_finala, BUGETUL)
