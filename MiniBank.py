import time
import threading


# Bank Users Details Dictionary
Users_Details = {
'Users_Name' : {1:"Rakesh" , 2:"Parul" , 3:"Ankit" , 4:"Monu" , 5:"Manish" , 6:"Bittu" , 7:"Jeetu" , 8:"Ajay" , 9:"Harsh" , 10:"Khali"},
'Users_ID' :   {1:1 , 2:2 , 3:3 , 4:4 , 5:5 , 6:6 , 7:7 , 8:8 , 9:9 , 10:10},
'Users_Balance' : {1:1000 , 2:4000 , 3:11000 , 4:1020 , 5:1000 , 6:1200 , 7:1860 , 8:1600 , 9:1800 , 10:1000},
'Users_Password' : {1:"Rakesh" , 2:"Parul" , 3:"Ankit" , 4:"Monu" , 5:"Manish" , 6:"Bittu" , 7:"Jeetu" , 8:"Ajay" , 9:"Harsh" , 10:"Khali"} 
}
# --------------------------------------------------------------------------------------------------------------------------------------------
def iAA():
    """Mini bank application with related functionality"""
                         
    try:
        count = 0                                                                                                                   
        Attempt = 3                                                                 
        while count < Attempt:                                                                                                      
            print("******************************************************************************************************")
            print("\t\t\t\t\t IAA BANK")
            print("\t\t\t\\____________________________________________________/\n\n")
            print("Namaskaar ! We are happy to service.")
            AskFirst = input("Are You Ready Y/N ?:   ")
            if AskFirst.lower() == "y":

                input1 = int(input("Please Enter Your Account Number:  "))                                                              
                password = (input("Enter Your Password : "))
                time.sleep(1)    

                timer = threading.Timer(60.0,iAA)  # timerout after 60 seconds (Screen open for 60 seconds)
                timer.start()                                                                        

                
                
            # Users Authentication check  
                if (password == Users_Details['Users_Password'][input1]):                                                               
                    print("\t\t\t\t\t Welcome " + Users_Details['Users_Name'][input1] +" to IAABank !")                                 
                    print("\t\t\t\t\t______________________________")                     
                    print("\t\t\t\t\t 1. User Details > \n\t\t\t\t\t 2. Transaction >\n\t\t\t\t\t 3. Exit >")                           
                    input2 = int(input( '\n\t\t\t\t\t Please choose your Option:   '))                                                  

                    
                    
            # User Details Option
                    if (input2 == 1 ):                                                                                                  
                        print("Welcome " + Users_Details['Users_Name'][input1] + " Your Details are :" )                                
                        print("______________________________")
                        print(". User_ID =  ", Users_Details['Users_ID'][input1])                                                       
                        print(". User_Name =  ",Users_Details['Users_Name'][input1])                                                    
                        print(". User_Balance =  ",Users_Details['Users_Balance'][input1],"\n\n\t")                                     
                        print("\t\t\t\t\t You are in User Details Section !")                                                
                        print("\t\t\t\t\t______________________________")
                        print("\n\t\t\t\t\t Choose Option :- \n\t\t\t\t\t 1. Main Menu \n\t\t\t\t\t 2. Exit")                            
                        input3 = (int(input("\t\t\t\t\t Please Choose your option :  ")))                                          
                
                        if(input3 == 1):                                                                                                
                            return iAA()
                        elif(input3 == 2):
                            time.sleep(2)                                                                                              
                            print("Thank you, to using IAA BANK !")
                            break                                                                                                       
                        else:
                            time.sleep(2)                                                                                                            
                            print("Your Transaction Suspended !")
                            print("Thank you, using to IAA BANK")                                                                       


                            
                            # Transaction option Choose by the user
                    elif(input2 == 2):                                                                                                  
                        print("Welcome in Transaction Option")
                        print("______________________________")
                        input4 = int(input("Choose Option : \n 1. Debit :\n 2. Credit : \n 3. Transfer Money :  "))                      
                        
                        if(input4 == 1):                                                                                                
                            print("\t\t\t\t\t Debit Amount !")                                                                                 
                            print("\t\t\t\t______________________________")
                            print(f"\t\t\t\t > You have {Users_Details['Users_Balance'][input1]},amount balance left !")                      
                            input5 = int(input("\t\t\t\t > Enter Debited Amount:  "))                                                   
                            if(input5 <= Users_Details['Users_Balance'][input1]):                                                       
                                Users_Details['Users_Balance'][input1] = (Users_Details['Users_Balance'][input1]) - input5
                                time.sleep(1)
                                print("Your Transaction is processed . . . . \n Please wait !")
                                time.sleep(2)               
                                print("\n\n\t\t\t\t< You have left ", Users_Details['Users_Balance'][input1] , "in your account >")     
                                break                                                                                                   
                            else:
                                time.sleep(1)                                                                                                       
                                print("\n\n\t\t < You have unsufficient balance in your account to make a debit transaction >")          
                                break                                                                                                    
                        elif(input4 == 2):                                                                                              
                            input6 = int(input("\n\n\t\t\t\t\tCredit Amount: "))                                                        
                            print("\t\t\t\t______________________________")
                            Users_Details['Users_Balance'][input1] = Users_Details['Users_Balance'][input1] + input6
                            time.sleep(1)
                            print("Your Transaction is processed . . . . \n Please wait !")   
                            time.sleep(2)  
                            print(" Your current updated account balance is ", Users_Details['Users_Balance'][input1])   
                            break                                                                                                       

                        elif(input4 == 3):                                                                                              
                            print("\n\n\t\t\t Which account ID, you want to transfer money !")                                  
                            input7 = int(input("\t\t\t\t Enter Receiver Account_ID : "))                                                 
                            print("\nYou are crediting amount to", Users_Details['Users_Name'][input7])                                 
                                                
                            if(input7 == (Users_Details['Users_ID'][input7])):                                                          
                                input8 = int(input("Transfer Credit Amount:  "))                                                        
                                if(input8 < Users_Details['Users_Balance'][input1]):                                                    
                                    Users_Details['Users_Balance'][input7] + input8      
                                    time.sleep(1)      
                                    print("Your Transaction is processed . . . . \n Please wait !") 
                                    time.sleep(2)                                        
                                    print("\nThank you !\n You have", Users_Details['Users_Balance'][input1] - (input8), "Balance Left !") 
                                    break                                                                                                 
                                else:
                                    time.sleep(1)                                                                                                     
                                    print("You have unsufficient balance in your account to transfer money !")
                            else:                                                                                                 
                                print("Wrong Account Number")                                                                             
                                    
                        else:                                                                                                                       
                            print("Wrong Input !")
                            break                                                                                                                   




            # Exit Option Choosen by the user 
                    elif(input2 == 3):                                                                                                              
                        print("Thank you, to using IAA BANK")
                        break
                    else:
                        print("You have press wrong option key !")
                        break
                else:
                    time.sleep(2)
                    print("Maximum time limit over")                                                                                                         
                    count = count + 1                                                                                                               
            else:
                print("Welcome you !")
                break
    except ValueError:
        print("Incorrect user input, Watch your input please.....")
    except KeyError:
        print("Key not matching, Please use after sometime......")
    except ModuleNotFoundError as e:
        print(f"Module Error {e}")
    except NameError as e:
        print(f"Module not found {e}")
        
        
 # ------------------------------***********************--------------------------------------
   
if __name__ == "__main__":
    iAA()
