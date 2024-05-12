def validate_iban(iban):
    while True:
        if iban[0:2]=="TB" and (iban[2:6]).isdigit() and len(iban)==5:
            break
        else:
            print("Invalid iban format! Try again")
            iban=input("enter iban: ")
            
 
