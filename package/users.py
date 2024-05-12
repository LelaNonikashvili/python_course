import validator
base=[]
base_users={}
def register():
    name=input("enter name ")
    surname=input("enter surname ")
    iban=input("enter iban ")
    validator.validate_iban(iban)
    base_users["name"]=name
    base_users["surname"]=surname
    base_users["iban"]=iban
    base.append(base_users)
    print("You have successfully registered!")
