#Module for option 6 in menu - Show / Delete data

def Menu_Option6(Hosts, Users, Machines):

    # #Docstring:
    #     """
    #     showing or deleting all data of each data structure
        
    #     Parameters:
    #         none
        
    #     Returns:
    #         only if choose to delete -
    #         List - Hosts
    #         List - Users
    #         Directory = Machines
    #     """
         
    Manu_option6 = True
    while Manu_option6:
        print("""
        1 - Show all data
        2 - Delete all data
        3 - Exit
        """)
    
        try:
            user_choice = int(input("What do you want to do? (1-3): "))
        
            if user_choice == 3:
                print("Returning to main menu\n")
                Manu_option6 = False
            
            elif user_choice == 1:
                print("\n#### Physical Servers Info ####")
                for i in Hosts:
                    print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}
""")

                print("\n#### Users Populations Info ####") 
                for i in Users:
                    print(f"""
Users Population name : {i['Name']}
Users count in this population : {i['Count']}
""")
    
                print("\n#### Virtual Machines Types Info ####")
                for i in Machines:
                    i2 = Machines[i]
                    user_pop_list = i2.get('Users', "No populations assigned")
                    print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}
Users Populations for this type - {user_pop_list}
""")

            elif user_choice == 2:
                print("Deleting Data ......")
                Hosts.clear()
                Users.clear()
                Machines.clear()

            else:
                print("Please enter a number between 1 and 3.")
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    return Hosts, Users, Machines