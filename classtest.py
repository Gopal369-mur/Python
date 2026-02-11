class Alltest():
    def subfield():
        print("Sub-fields in AI are:")

        fields =["machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language processing"]

        for field in fields:
            print(field)

   
    def oddeven ():
        num = int(input("Enter a number:"))
        if num%2 == 0:
            print(num, "is even number ")
        else:
            print(num, "is odd number")
            

    def Eligible():
        gender = str(input("Enter the Gender:"))
        age = int(input("Enter the age:"))
        
        if gender == "male":
            if age >= 21:
                print("you are eligible for marriage")
               
            else:
                print("You are not eligible")
                
                
        elif gender == "female":
            if age >= 18:
                print(" you are eligible for marriage")
                 
            else:
                print("You are not eligible")
                
                

    def percentage():
        sub1 = int(input("Subject 1 = "))
        sub2 = int(input("Subject 2 = "))
        sub3 = int(input("Subject 3 = "))
        sub4 = int(input("Subject 4 = "))
        sub5 = int(input("Subject 5 = "))
        
        Total = sub1+sub2+sub3+sub4+sub5
        print("Total: ", Total)
        percentage = Total/500*100
        print("Percentage", percentage)

    def triangle():
        hei = int(input("height:"))
        bread = int(input("breadth:"))
        
        print("Areaformula = (hei*bread)/2 ")
        Areaformula = (hei*bread)/2
        print("Area of Triangle: ", Areaformula)
        
        hei1 = int(input("Height1:"))
        hei2 = int(input("Height2: "))
        bread1 = int(input("height2:"))

        print("Perimeterformula = hei1+ hei2+bread1")
        Perimeterformula = hei1+ hei2+bread1
        print(" perimieter of triangle:", Perimeterformula)
        


           
    

    