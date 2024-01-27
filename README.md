categorii=['haine','mancare','electronice']
obiecte={
    'haine':{'tricou':50, 'geaca':200, 'vesta':100, 'pantaloni':70},
    'mancare':{'cartofi':20, 'mazare':10, 'brocoli':13, 'rosii':9},
    'electronice':{'Iphone':2000, 'Airpods':1000, 'Incarcator':100,'Mouse':150}
}

INPUT=input("Ce categorii alegeti?")
categorii_alese=INPUT.split()
input_lenght=len(categorii_alese)-1

lista_preturi=[]
combinatie_finala=[]
budget=300

def find_combination(budget, categories, items):
    
    def backtracking(current_budget,current_combination, remaining_categories):
        nonlocal best_combination,buget_final
        
        if current_budget <=0 or len(remaining_categories)==0:
            best_combination.append(current_combination[:])
            print('alta',best_combination)    #here i have a problem with the final list, because it puts my final answer into an another list
            buget_final=current_budget
            return best_combination,buget_final
        
        for con in categories:
            for item in items[con]:
                if(len(remaining_categories)!=0):
                    price=items[con][item]
                    if price<=current_budget :
                        current_combination.append(item)
                        print('index',current_combination)
                        remaining_categories.remove(con)
                        backtracking(current_budget-price,current_combination,remaining_categories)
                else:
                    break
                    
    best_combination = []
    buget_final=0
    remaining_categories = categorii_alese
    backtracking(budget, [], remaining_categories)
    print("asta",best_combination)
    return best_combination,buget_final

def main():
    result,buget_final=find_combination(budget, categorii_alese, obiecte)
    #print(result[1])
    print("Cea mai buna combinatie:",result)
    print("Buget ramas:",buget_final)
        
main()





#print(input_lenght)
#print(categorii_alese)

#print(obiecte[categorii_alese[input_lenght]])

#print(haine[1][1]) -> asa folosesti tuple    
