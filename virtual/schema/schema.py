def individual_serial(thing)->dict:
    return{
        "id": str(thing["_id"]),
        "house":str(thing["house"]),
        "price": str(thing["price"]),
        "year": str(thing["year"]),
        "area": str(thing["area"]),
    }

def list_serial(things)->list:
    return[individual_serial(thing)for thing in things]
