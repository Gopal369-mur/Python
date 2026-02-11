class multiplefunction ():
    def oddeven(): 
        num = int(input("Enter the number: "))
        if num%2 !=0:
            print(num, "is odd  number")
            out="is odd number "
        else:
            print(num, "is even number ")
            out= "is even number "
        return out
        
    def Eligibilityformarriage():
        gender=str(input("Enter the Gender: "))
        age = int (input("Enter the age:"))
        if gender == "male":
            if age >=21:
                print("you are eligible for marriage")
                message = "You are eligible for marriage"
            else:
                print("Not eligible")
                message= "Not eligible"
        elif gender == "female":
            if age >= 18:
                print("you are eligible for marriage")
                message = "You are eligible for marriage"
            else:
                print("Not eligible")
                message= "Not eligible"
            return message
        
