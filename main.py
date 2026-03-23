#This script calculate how many virtual machines can be hostes on every physical server based on the information reciecved from the user 

#the structure is - 
    # main manu - keeps running as long as the user keep interacting
    #     1 - loop 1 - server info 
    #         repeat for as many servers 
    #         allow changing/adding/removing
    #     2 - loop 2 - users info 
    #         repeat for as many users types 
    #         allow changing/adding/removing
    #     3 - loop 3 - machine info 
    #         repeat for as many machine types 
    #         allow changing/adding/removing
    #     4 - calculate
    #     5 - load dummy data
    #     6 - exit


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
            print(f"""
######### Physical Servers Info #########
In order to calculate your physical resources we need some information regarding your servers.
First we need to know if all of your servers are of the same type or do you have (or intended to have) multiple types of servers.
For each type we need the following information :
                type name (give it any name you like)
                how much cpu each server have (in numbers only)
                how much memory each server have (in numbers only)
                how much storage each server have (in numbers only)
                and how many servers of this type you have

        ****** Please Notice ! All info is kEy SeNsiTive! ****** 
""")
        elif User_choice == 2 :
            print(f"""
######### User's Info #########
In order to calculate how many machines of each type you need, we need to know how many types of users populations you need to serve with those machines.
User's populations examples - Developers, Regular simple users, Managers, etc.
For each population we will ask for a name and number of users .
                  
        ****** Please Notice ! All info is kEy SeNsiTive! ******
""")
        elif User_choice == 3 :
            print(f"""
######### Virtual Machines Info #########
Last thing we need is the virtual machines information.
Usually, different user's populations need different types of machine for their work.
For each type we need the following information :
                how much cpu you want each machine in that type to have (in numbers only)
                how much memory you want each machine in that type to have (in numbers only)
                how much storage you want each machine in that type to have (in numbers only)
                which of your user's populations are going to use those machines (you can choose more than 1)
                  
        ****** Please Notice ! All info is kEy SeNsiTive! ******
""")
        elif User_choice == 4 :
           print(f"""
***********************************************************************
                            Final Results
*********************************************************************** 
""")
        elif User_choice == 5 :
            print(f"""
Loading exaple data...... Please wait......
""")
        else : 
             print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-6 only)***")

    except ValueError :
        print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-6 only)***")