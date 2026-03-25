#Module for option 5 in menu - load dummy data 

def Menu_Option5(Hosts,Users,Machines):

    # #Docstring:
    #     """
    #     adding data to each data structure as an example for the user
        
    #     Parameters:
    #         none
        
    #     Returns:
    #         List - Hosts
    #         List - Users
    #         Directory = Machines
    #     """

    Hosts = [{'Name': 'Esxi', 'CPU': 200, 'Memory': 1000, 'Storage': 3000, 'Count': 5}, {'Name': 'Dell', 'CPU': 400, 'Memory': 1600, 'Storage': 5000, 'Count': 10}, {'Name': 'Lenovo', 'CPU': 500, 'Memory': 2500, 'Storage': 9000, 'Count': 4}]
    Users = [{'Name': 'OfficeUsers', 'Count': 1000}, {'Name': 'Developers', 'Count': 100}, {'Name': 'IT', 'Count': 35}]
    Machines = {'Office': {'CPU': 4, 'Memory': 8, 'Storage': 80, 'Users': {'office'}}, 'Dev': {'CPU': 32, 'Memory': 64, 'Storage': 300, 'Users': {'dev'}}, 'IT': {'CPU': 8, 'Memory': 16, 'Storage': 150, 'Users': {'IT', 'mangers'}}}

    print(f"""\n#### Physical Servers Info ####""")
    for i in Hosts :
        print(f"""
    Type name : {i['Name']}
    CPU of each physical server : {i['CPU']}
    Memory of each physical server : {i['Memory']}
    Storage of each physical server : {i['Storage']}
    physical server count in this type : {i['Count']}

    """)
    
    print("\n#### Users Populations Info ####") 
    for i in Users :
        print(f"""
    Users Population name : {i['Name']}
    Users count in this population : {i['Count']}

    """)
        
    print("\n#### Virtual Machines Types Info ####")
    for i in Machines :
                i2 = Machines[i]
                user_pop_list = i2.get('Users', "No populations assigned")
                print(f"""
    Type name : {i}
    CPU for this type - {i2['CPU']}
    Memory for this type - {i2['Memory']}
    Storage for this type - {i2['Storage']}
    Users Populations for this type - {user_pop_list}
    """)

    return(Hosts,Users,Machines)