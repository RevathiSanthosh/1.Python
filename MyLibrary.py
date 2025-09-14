class MathLibrary:
    def triangle():
                Height = int(input('Height:'))
                Breadth = int(input('Breadth:'))
                print('Area formula:  (Height*Breadth)/2')
                Area = (Height*Breadth)/2
                print('Area of Triangle: ',Area)
                Height1= int(input('Height1:'))
                Height2= int(input('Height2:'))
                Breadth = int(input('Breadth:'))
                print('Perimeter formula: Height1+Height2+Breadth')
                Perimeter = Height1+Height2+Breadth
                print("Perimeter of Triangle: ",Perimeter)
    def percentage():
                 Subject1 = int(input("Subject1 =")) 
                 Subject2 = int(input("Subject2 =")) 
                 Subject3 = int(input("Subject3 =")) 
                 Subject4 = int(input("Subject4 =")) 
                 Subject5 = int(input("Subject5 =")) 
                 Total= Subject1+Subject2+Subject3+Subject4+Subject5
                 Percentage = ((Total/500)* 100)
                 print("Total : ",Total)
                 print("Percentage : ",Percentage)
    
    def OddEven():
            num=int(input("Enter a number: "))
            if(num % 2 == 0):
                print(str(num)+ " is Even number")
            else:
                print(str(num)+ " is Odd number")
    
    def Subfields():
                List = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
                print("Sub-fields in AI are: ")
                for i in List:
                    print(i)
                                
    def Elegible():
                Gender = input("Your Gender :")
                Age =  int(input("Your Age :"))
                if(Gender == 'Male'):
                    if(Age < 21):
                        print("NOT ELIGIBLE")
                    else:
                        print("ELIGIBLE")
                elif(Gender == 'Female'):
                    if(Age < 18):
                         print("NOT ELIGIBLE")
                    else:
                        print("ELIGIBLE")
                else:
                        print("Enter a valid gender")