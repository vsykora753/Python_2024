# prirozeny jazyk 
"""
1. rozvalet testo
2. pridat rajcatovy zaklad
3. pridat syr
4. pridat sunku
5. kdyz chcem cerstvy rajcata, tak je tam pridame
6. upect

"""

# pseudokod
"""
1. rozvalet_testo()
2. add(rajcatovy_zaklad)
3. add(syr)
4. add(ham)
5. if chceme rajcata:
    add(rajcata)
6. upect()

"""

class Pizza:
    def __init__(self):
        print("Valime testo...")
        self.ingredients = []
        #self.status = "raw"
        self.is_baked = False
        #self.has_items

    def add_ingredient(self, ingredient: str) :
        self.ingredients.append(ingredient)

    def bake(self) -> None:
        if self.is_baked:
             print("uz je to upeceno...")    
        else:
            print("Baking...")
            self.is_baked = True
           

    def __repr__(self) -> str:
        ingredience =", ".join(self.ingredients)
        if self.is_baked:
            return
       
       
        return f"Pizza({ingredience})"
    
    #def __str__(self):
    #    pass


pizza = Pizza()
print(pizza)


pizza.add_ingredient("maslo")
pizza.add_ingredient("rajcata")

print(pizza)


def make_my_pizza(chceme_rajcata: bool):
    pizza = Pizza()
    pizza.add_ingredient("rajcatovy zaklad")
    pizza.add_ingredient("syr")
    pizza.add_ingredient("sunka")

    if chceme_rajcata:
        pizza.add_ingredient("rajcata")
    else:
        print("Preskakujeme rajcata, protoze je nechceme..")    

    pizza.bake()
    return pizza

def make_any_pizza(ingredients:list[str]):
    pizza = Pizza()
    
    for ingredient in ingredients:
        pizza.add_ingredient(ingredient)
    pizza.bake()
    return pizza


def make_my_pizza2(chceme_rajcata):
    ingredients = []
    ingredients.add_ingredient("rajcatovy zaklad")
    ingredients.add_ingredient("syr")
    ingredients.add_ingredient("sunka")
    

    if chceme_rajcata:
        pizza.add_ingredient("rajcata")
    else:
           print("Preskakujeme rajcata, protoze je nechceme..")    

    pizza.make_any_pizza(ingredients)
    return pizza