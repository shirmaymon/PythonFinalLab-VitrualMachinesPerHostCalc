#This script calculate how many virtual machines can be hostes on every physical server based on the information reciecved from the user 

#import modules
from Menu_User_massages import *
from Menu_Option_1_Servers import *
from Menu_option_2_Users import *
from Menu_option_3_Machines import *

from Menu_Option_5_DummyData import *


#Define data structures
Hosts = []      #(List of Dictionaries)
Users = []      #(List of Dictionaries)
Machines = {}   #(dictionary of dictionaries (with tuple))

#Print first greeting
print("\n")
print("*"*150+"\n"+" "*57+"VIRTUAL MACHINES per HOST CALCULATOR"+" "*57+"\n"+"*"*150+"\n")
print(f"""This cacluator purpose is to help you manage the number of virtual machines on every host you own or might consider owning.
You will be asked for hosts information, machines information and number of users that are using your virtual machines
Please follow the instructions to get the best results :)

****** Please Notice ! All info is kEy SeNsiTive! ******\n\n""")

#Main Manu
In_manu=True
while In_manu:
    print(f"""
***********************************************************************
                               MAIN MENU
***********************************************************************
          1 - Server's Details
          2 - User's Details 
          3 - Machine's Details
          4 - Calculate
          5 - Load Example Data
          6 - Exit

""")
    
    try : 
        User_choice = int(input("What do you want to do ? (enter number) "))
        if User_choice == 6 :
            print("Bye! See you next time\n")
            In_manu = False
        elif User_choice == 1 :
            Menu1()
            Menu_Option1(Hosts)

        elif User_choice == 2 :
            Menu2()
            Menu_option_2(Users)
            
        elif User_choice == 3 :
            Menu3()
            Menu_option_3(Machines,Users)

        elif User_choice == 4 :
           Menu4()

        elif User_choice == 5 :
            Menu5()
            Menu_Option5(Hosts,Users,Machines)

        else : 
             print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-6 only)***")

    except ValueError :
        print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-6 only)***")