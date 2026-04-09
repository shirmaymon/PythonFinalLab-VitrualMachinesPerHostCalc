#Module for option 2 in menu - creates Users data structure 

def Menu_option_2(Users):

    # #Docstring:
    #     """
    #     Infinate loop for menu option 2- enter users data
    #     Allows adding, deleting and editing users info
        
    #     Parameters:
    #         none
        
    #     Returns:
    #         List - Users
    #     """

    #Manu Option2
    Manu_option2=True
    while Manu_option2:
        #first screen - users options & get user choise
        print(f"""
            1 - Enter/Add user populations
            2 - Edit user population (for data you already entered before)
            3 - Delete user population
            4 - Exit

    """)
        try : 
            User_choice = int(input("What do you want to do ? (enter number) "))
            
            #exit if user chose 4
            if User_choice == 4 :
                print("Returning to main manu\n")
                Manu_option2 = False
            
            #adding info to list using user's data
            elif User_choice == 1 :
                try:
                    Users_types=int(input("How many user's populations do you want to add ? "))
                    if Users_types <= 0:
                        print(f"Invalid number of user's types, please enter a whole number starting from 1. Re-enter and try again")
                    elif Users_types >= 1 :
                        Users_type = 0
                        while Users_type < Users_types :
                            try:
                                Type_name=str(input(f"Please enter user populations {Users_type+1} name - "))
                                Count = int(input(f"Please enter how many users are in this population (Whole number only) - "))
                                print("\n")
                                if Count < 0 :
                                    print("Invalid parameters, please start over")
                                    Users_type = Users_type
                                elif any(h['Name'] == Type_name for h in Users) :
                                    print("Name Already Exists, please start over")
                                    Users_type = Users_type
                                else :
                                    Users.append({"Name":Type_name,"Count":Count})
                                    Users_type += 1                            
                            except ValueError:
                                print("Invalid parameters, please start over")
                                Users_type = Users_type
                        #Print user's information -
                        print("\n#### Users Populations Info ####") 
                        for i in Users :
                            print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)
                except ValueError:
                    print("Invalid number of user's types, please enter a whole number starting from 1. Re-enter and try again")
            
            #Edit existing user population info
            elif User_choice == 2 :
                print("\n#### Users Populations Info ####") 
                for i in Users :
                    print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)
                if not Users : 
                    print("\nEnter data before trying to edit. Re-enter and try again\n")
                else :
                    Type_Change = str(input("Enter the name of the population you want to change - "))
                    if any(h['Name'] == Type_Change for h in Users) :
                        for i in Users : 
                            if i['Name'] == Type_Change :
                                try:
                                    Type_name=str(input(f"Please enter new users population name - "))
                                    Count = int(input(f"Please enter how many users are in this population (Whole number only) - "))
                                    print("\n")
                                    if Count < 0 :
                                        print("Invalid parameters, please start over")
                                        break
                                    else :
                                        Users.remove(i)
                                        Users.append({"Name":Type_name,"Count":Count})
                                        break
                                except ValueError:
                                    print("Invalid parameters, please start over")
                                    break
                    else : 
                        print("\nThe type name you entered to change doesn't exist. Re-enter and try again\n")
                    
                print("\n#### NEW Users Populations Info ####") 
                for i in Users :
                    print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)

            #Delete existing user population info
            elif User_choice == 3 :
                print("\n#### Users Populations Info ####") 
                for i in Users :
                    print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)
                if not Users : 
                    print("\nEnter data before trying to delete. Re-enter and try again\n")
                else :
                    Type_Delete = str(input("Enter the name of the users population you want to delete - THIS IS NOT REVERTABLE ! - "))
                    for i in Users : 
                        if i['Name'] == Type_Delete :
                            Users.remove(i)
                            print(f"Removing {Type_Delete}... Please wait .... ")
                            break
                
                print("\n#### NEW Users Populations Info ####") 
                for i in Users :
                    print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)

            else : 
                print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")

        except ValueError :
            print("\n***Notice! you entered an invalid option. Please Enter The number of the action you want to make (1-4 only)***")

    return(Users)
