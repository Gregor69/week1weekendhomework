# WRITE YOUR FUNCTIONS HERE





def get_pet_shop_name(pet_shop):
   return pet_shop["name"]

# def get_pet_shop_name(self):
#     pet_shop_name = ("Camelot of Pets")
#     return pet_shop_name

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# def get_total_cash(list):
#     total_cash = 1000
#     return total_cash

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop, stock_count):
    stock_count = (len("pets"))
    stock_count = count+1
    return(get_stock_count)
    
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)
    return found_pets

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)

def remove_pet_by_name(pet_shop, name):
    # new_pets_list = []
    # for pets in pet_shop["pets"]:
    #     if pet["name"] != name:
    #         new_pets-list.append(pet)
    # pet_shop["pets"] = new_pets_list
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# def get_customer_cash(customers):
#     customers["cash"]


# def increase_pets_sold(pet_shop, amount):
#     pets_sold = get_pets_sold(pet_shop)
#     pets_sold += amount

# def get_pets_sold(self):
#     pets_sold = (0)
#     return pets_sold

# def get_pets_sold(list):
#     return cc_pet_shop["admin"]["pets_sold"]



# def get_stock_count(self):
#     count = 6
#     return get_stock_count

# def get_stock_count(list):
#     return cc_pet_shop["pets"]

