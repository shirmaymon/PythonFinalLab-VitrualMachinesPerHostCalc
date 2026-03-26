#This module is for saving user manual massages as functions to call in main.py

def Menu1() : 
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

def Menu2() : 
    print(f"""
######### User's Info #########
In order to calculate how many machines of each type you need, we need to know how many types of users populations you need to serve with those machines.
User's populations examples - Developers, Regular simple users, Managers, etc.
For each population we will ask for a name and number of users .
                  
        ****** Please Notice ! All info is kEy SeNsiTive! ******
""")
    
def Menu3() : 
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

def Menu4() :
    print(f"""
***********************************************************************
                            Final Results
*********************************************************************** 

    ****** For each host - resources available for use are 80% of it's resources (rounded down) ******
          
""")

def Menu5() :
    print(f"""
Loading exaple data...... Please wait......
""")

def Menu6() :
    print(f"""
######### Show/Delete all Data #########
please notice - deleting is not revertable
""")