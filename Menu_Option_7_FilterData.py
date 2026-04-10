


def sort_host_by_cpu(Hosts):

    Sort = sorted(Hosts, key=lambda x: x['CPU'], reverse = True)

    print("\n#### Physical Servers Info ####")
    for i in Sort:
                    print(f"""
Type name : {i['Name']}
CPU of each physical server : {i['CPU']}
Memory of each physical server : {i['Memory']}
Storage of each physical server : {i['Storage']}
physical server count in this type : {i['Count']}
""")

def filter_users_by_count(Users):
     filter_list = []
     while True:
        count = int(input("From which count of users you want to filter the list by: "))
        if count >= 0:
             break
        elif count < 0:
             print("Error: Negative value. Please enter only positive value")
        else:
             print("Invalid value. Please try again")

     for User in Users: 
          if User['Count'] >= count:
               filter_list.append(User)

     print("\n#### Filtered Users Populations Info ####") 
     for i in filter_list :
                            print(f"""
Users Population name : {i['Name']}
Users count in this population : {i['Count']}

    """)
                            
def Menu_Option7(Hosts , Users):
    
    while True: 
        print("""
        1 - Sort Hosts By CPU
        2 - Filter Users By Count
        3 - Exit
        """)

        
        user_choice = int(input("What do you want to do? (1-3): "))
        
        if user_choice == 3:
            print("Returning to main menu\n")
            break
        elif user_choice == 2:
            filter_users_by_count(Users)
        elif user_choice == 1:
            sort_host_by_cpu(Hosts)
        else:
            print("Invalid Value. Please try again")    
    


