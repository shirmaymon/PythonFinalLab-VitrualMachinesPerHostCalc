# #Docstring:
#     """
#     Check CPU status and return status level
    
#     Parameters:
#         cpu_precent (int): CPU usage percentage
    
#     Returns:
#         str: "OK", "WARNING", or "CRITICAL"
#     """

Machines = {}
Users = [{'name':"dev",'count':300},{'name':"office",'count':900},{'name':"mangers",'count':30},{'name':"IT",'count':100}]

#Manu Option3
Manu_option3=True
while Manu_option3:
    #first screen - users options & get user choise
    print(f"""
          1 - Enter/Add machine's types
          2 - Edit machine type (for data you already entered before)
          3 - Delete machine type
          4 - Add user's populations to each machine type
          5 - Exit

""")
    try : 
        User_choice = int(input("What do you want to do ? (enter number) "))
        
        #exit if user chose 5
        if User_choice == 5 :
            print("Returning to main manu\n")
            Manu_option3 = False
        
        #adding info to list using user's data
        elif User_choice == 1 :
            try:
                Machines_types=int(input("How many machine's types do you want to add ? "))
                if Machines_types <= 0:
                    print(f"Invalid number of machine's types, please enter a whole number starting from 1. Re-enter and try again")
                elif Machines_types >= 1 :
                    Machines_type = 0
                    while Machines_type < Machines_types :
                        try:
                            Type_name=str(input(f"Please enter machine type {Machines_type+1} name - "))
                            CPU = int(input(f"Please enter how many cpu each virtual machine of this type have (Whole number only) - "))
                            Memory = int(input(f"Please enter how much memory each virtual machine of this type have (in GB, Whole number only) - "))
                            Storage = int(input(f"Please enter how much storage each virtual machine of this type have (in GB, Whole number only) - "))
                            print("\n")
                            if CPU < 0 or Memory < 0 or Storage < 0 :
                                print("Invalid parameters, please start over")
                                Machines_type = Machines_type
                            elif any(h == Type_name for h in Machines ) :
                                 print("Name Already Exists, please start over")
                                 Machines_type = Machines_type
                            else :
                                Machines[Type_name] = {'CPU':CPU,'Memory':Memory,'Storage':Storage} 
                                Machines_type += 1                            
                        except ValueError:
                            print("Invalid parameters, please start over")
                            Machines_type = Machines_type
                    #Print user's information -
                    print("\n#### Virtual Machines Types Info ####")
                    for i in Machines :
                        i2 = Machines[i]
                        print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")
            except ValueError:
                print("Invalid number of machine's types, please enter a whole number starting from 1. Re-enter and try again")
        
        #Edit existing machine type info
        elif User_choice == 2 :
            print("\n#### Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")
            if not Machines : 
                 print("\nEnter data before trying to edit. Re-enter and try again\n")
            else :
                Type_Change = str(input("Enter the name of the Type you want to change - "))
                if any(h == Type_Change for h in Machines) :
                    for i in list(Machines) :
                        if i == Type_Change :
                            try:
                                Type_name=str(input(f"Please enter new machine type name - "))
                                CPU = int(input(f"Please enter how many cpu each virtual machine of this type have (Whole number only) - "))
                                Memory = int(input(f"Please enter how much memory each virtual machine of this type have (in GB, Whole number only) - "))
                                Storage = int(input(f"Please enter how much storage each virtual machine of this type have (in GB, Whole number only) - "))
                                print("\n")
                                if CPU < 0 or Memory < 0 or Storage < 0 :
                                    print("Invalid parameters, please start over")
                                    break
                                else :
                                    del Machines[i]
                                    Machines[Type_name] = {'CPU':CPU,'Memory':Memory,'Storage':Storage}                           
                            except ValueError:
                                print("Invalid parameters, please start over")
                else : 
                    print("\nThe type name you entered to change doesn't exist. Re-enter and try again\n")
                
            print("\n#### NEW Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")

        #Delete existing machine type info
        elif User_choice == 3 :
            print("\n#### Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")
            if not Machines : 
                 print("\nEnter data before trying to delete. Re-enter and try again\n")
            else :
                Type_Delete = str(input("Enter the name of the Machines Type you want to delete - THIS IS NOT REVERTABLE ! - "))
                if Type_Delete in Machines :
                    del Machines[Type_Delete]
                    print(f"Removing {Type_Delete}... Please wait .... ")
                else :
                    print("The type name you entered to delete doesn't exist. Re-enter and try again")
            
            print("\n#### NEW Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")
        
        #Add user types to each machine info
        elif User_choice == 4 :
            print("\n#### Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")
            print("\n#### Users Populations Info ####") 
            for i in Users :
                print(f"""
Users Population name : {i['name']}
Users count in this population : {i['count']}

""")
            if not Machines : 
                 print("\nNo machine types found. please enter data first and then try again.\n")
            elif not Users :
                print("\nNo users populations found. please return to the main manu, enter data and then try again.\n")
            else :
                Machines_type = str(input("Please choose a machine type to add users population/s - "))
                if Machines_type in Machines :
                    try : 
                        Users_types_count = int(input("How many users populations you want to add ? "))
                        if Users_types_count < 0 :
                            print(f"Invalid number of users populations, please try again")
                        elif Users_types_count >=1 :
                            # Users_set = {}
                            # for u in range(Users_types_count) :
                            #     Users_type = str(input(f"Enter {u+1}st users population -"))
                            # >    if Users_type in Users['name'] :
                            #         Users_set.add(Users_type)
                            #         Machines[Machines_type]['Users'] = Users_set
                            #     else :
                            #         print("Users population not fount. please try again")
                            print("TO BE CONTINUED")
                    except ValueError:
                        print("Invalid number of users populations, please try again")
                else : 
                    print("Machine type not found. please try again or add machine type in the previous manu")    


            
            print("\n#### NEW Virtual Machines Types Info ####") 
            for i in Machines :
                i2 = Machines[i]
                print(f"""
Type name : {i}
CPU for this type - {i2['CPU']}
Memory for this type - {i2['Memory']}
Storage for this type - {i2['Storage']}

""")

        else : 
             print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")

    except ValueError :
        print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")