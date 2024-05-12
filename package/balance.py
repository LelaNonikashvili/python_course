from validator import validate_iban
from users import base,base_users
def add_balance():
    a=input("enter iban: ")
    validate_iban(a)
    b=input("entter amount of money: ")
    if b.isdigit():
        base_users["balance"]=b
        base.append(base_users)
        print(f"The balance was filled with {b} GEL")
