Hosts = []

#Manu Option1
Manu_option1=True
while Manu_option1:
    #first screen - users options & get user choise
    print(f"""
          1 - Enter/Add physical servers info
          2 - Edit physical servers info (for types you already entered before)
          3 - Delete physical servers info
          4 - Exit

""")
    try : 
        User_choice = int(input("What do you want to do ? (enter number) "))
        
        #exit if user chose 4
        if User_choice == 4 :
            print("Returning to main manu\n")
            Manu_option1 = False
        
        #adding info to list using user's data
        elif User_choice == 1 :
            try:
                Servers_types=int(input("How many server's types do you want to add ? "))
                if Servers_types <= 0:
                    print(f"Invalid number of server's types, please enter a whole number starting from 1. Re-enter and try again")
                elif Servers_types >= 1 :
                    Servers_type = 0
                    while Servers_type < Servers_types :
                        try:
                            Type_name=str(input(f"Please enter server type {Servers_type+1} name - "))
                            CPU = int(input(f"Please enter how many cpu each server of this type have (Whole number only) - "))
                            Memory = int(input(f"Please enter how much memory each server of this type have (in GB, Whole number only) - "))
                            Storage = int(input(f"Please enter how much storage each server of this type have (in GB, Whole number only) - "))
                            Count = int(input(f"Please enter how many servers of this type you have (Whole number only) - "))
                            print("\n")
                            if CPU < 0 or Memory < 0 or Storage < 0 or Count < 0 :
                                print("Invalid parameters, please start over")
                                Servers_type = Servers_type
                            elif any(h['Name'] == Type_name for h in Hosts) :
                                 print("Name Already Exists, please start over")
                                 Servers_type = Servers_type
                            else :
                                Hosts.append({"Name":Type_name,"CPU":CPU,"Memory":Memory,"Storage":Storage,"Count":Count})
                                Servers_type += 1                            
                        except ValueError:
                            print("Invalid parameters, please start over")
                            Servers_type = Servers_type
                    #Print server's information -
                    print("#### Physical Servers Info ####") 
                    for i in Hosts :
                        print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}

""")
            except ValueError:
                print("Invalid number of server's types, please enter a whole number starting from 1. Re-enter and try again")
        
        #Edit existing server type info
        elif User_choice == 2 :
            print(f"""\n#### Physical Servers Info ####""")
            for i in Hosts :
                        print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}

""")
            if not Hosts : 
                 print("\nEnter data before trying to edit. Re-enter and try again\n")
            else :
                Type_Change = str(input("Enter the name of the server type you want to change - "))
                if any(h['Name'] == Type_Change for h in Hosts) :
                    for i in Hosts : 
                        if i['Name'] == Type_Change :
                            try:
                                Type_name=str(input(f"Please enter new server type name - "))
                                CPU = int(input(f"Please enter how many cpu each server of this type have (Whole number only) - "))
                                Memory = int(input(f"Please enter how much memory each server of this type have (in GB, Whole number only) - "))
                                Storage = int(input(f"Please enter how much storage each server of this type have (in GB, Whole number only) - "))
                                Count = int(input(f"Please enter how many servers of this type you have (Whole number only) - "))
                                print("\n")
                                if CPU < 0 or Memory < 0 or Storage < 0 or Count < 0 :
                                    print("Invalid parameters, please start over")
                                    break
                                else :
                                    Hosts.remove(i)
                                    Hosts.append({"Name":Type_name,"CPU":CPU,"Memory":Memory,"Storage":Storage,"Count":Count})                           
                            except ValueError:
                                print("Invalid parameters, please start over")
                else : 
                    print("\nThe type name you entered to change doesn't exist. Re-enter and try again\n")
                
            print("#### NEW Physical Servers Info ####")
            for i in Hosts :
                        print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}

""")

        #Delete existing server type info
        elif User_choice == 3 :
            print(f"""\n#### Physical Servers Info ####""")
            for i in Hosts :
                        print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}

""")
            if not Hosts : 
                 print("\nEnter data before trying to delete. Re-enter and try again\n")
            else :
                Type_Delete = str(input("Enter the name of the server type you want to delete - THIS IS NOT REVERTABLE ! - "))
                for i in Hosts : 
                    if i['Name'] == Type_Delete :
                        Hosts.remove(i)
                        print(f"Removing {Type_Delete}... Please wait .... ")
            
                print("\n#### NEW Physical Servers Info ####")
                for i in Hosts :
                            print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}

""")

        else : 
             print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")

    except ValueError :
        print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")