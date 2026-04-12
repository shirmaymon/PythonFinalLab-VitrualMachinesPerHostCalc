# #Module for option 4 in menu - calculate

#matanmo - import os and datetime for the export
import datetime
import os


def Menu_Option4(Hosts,Users,Machines):

#     # #Docstring:
#     #     """
#     #     calculating how many machines of each type can be hosted on each physical server
        
#     #     Parameters:
#     #         none
        
#     #     Returns:
#     #         prints calculation results as an inpormative summery
#     #     """

    #matanmo- init a print_list for the export function
    #i make change to your code to make my implment
    print_list = []

    #Add count to each machine type that sums up amount of machines based on users list
    for Machine_type in Machines :
        Count = 0
        for i in (Machines[Machine_type]['Users']) :
            if i == "No populations assigned" :
                count = 0   
            else :
                for u in Users :
                    if u['Name'] == i :
                        Add = u['Count']
                        Count = Count + Add
        Machines[Machine_type]['Count'] = Count

    #Machines = {'Office': {'CPU': 4, 'Memory': 8, 'Storage': 80, 'Users': {'No populations assigned'}, 'Count': 0}, 'Dev': {'CPU': 32, 'Memory': 64, 'Storage': 300, 'Users': {'Developers'}, 'Count': 100}, 'IT': {'CPU': 8, 'Memory': 16, 'Storage': 150, 'Users': {'IT', 'Managers'}, 'Count': 85}}

    #Add 80% of each paramter as a new parameter to each host type in hosts list
    for Host in Hosts:
        Host['CPU_to_use'] = int(0.8*Host['CPU'])
        Host['Memory_to_use'] = int(0.8*Host['Memory'])
        Host['Storage_to_use'] = int(0.8*Host['Storage'])

    #Hosts = [{'Name': 'Esxi', 'CPU': 200, 'Memory': 1000, 'Storage': 3000, 'Count': 5, 'CPU_to_use': 160, 'Memory_to_use': 800, 'Storage_to_use': 2400}, {'Name': 'Dell', 'CPU': 400, 'Memory': 1600, 'Storage': 5000, 'Count': 10, 'CPU_to_use': 320, 'Memory_to_use': 1280, 'Storage_to_use': 4000}, {'Name': 'Lenovo', 'CPU': 500, 'Memory': 2500, 'Storage': 9000, 'Count': 4, 'CPU_to_use': 400, 'Memory_to_use': 2000, 'Storage_to_use': 7200}]

    #create Hosts_seperated list of dictionaries in order to create a list that every entry in it is a single host

    Hosts_seperated = []

    for Host in Hosts :
        for i in range(Host['Count']) :
            Host_seperated = {}
            name = ((Host['Name'])+" server #"+(f"{i+1}"))
            Host_seperated['Name'] = name
            Host_seperated['CPU'] = (Host['CPU_to_use'])
            Host_seperated['Memory'] = (Host['Memory_to_use'])
            Host_seperated['Storage'] = (Host['Storage_to_use'])
            Hosts_seperated.append(Host_seperated)


    # Create dictionary for storing how many machines each host stores
    Host_Dict = {}
    for Host_seperated in Hosts_seperated:
        Host_Dict[Host_seperated['Name']] = {}

    #for each machine type - allocate in a host until host resources run out
    for Machine_type in Machines:
        Total_vms_needed = Machines[Machine_type]['Count']
        
        if Total_vms_needed == 0:
            continue

        for i in range(Total_vms_needed):
            for Host_seperated in Hosts_seperated:
                CPU_New = Host_seperated['CPU'] - Machines[Machine_type]['CPU']
                Mem_New = Host_seperated['Memory'] - Machines[Machine_type]['Memory']
                Strg_New = Host_seperated['Storage'] - Machines[Machine_type]['Storage']

                if CPU_New >= 0 and Mem_New >= 0 and Strg_New >= 0:
                    Host_seperated['CPU'] = CPU_New
                    Host_seperated['Memory'] = Mem_New
                    Host_seperated['Storage'] = Strg_New
                    Current_count = Host_Dict[Host_seperated['Name']].get(Machine_type, 0)
                    Host_Dict[Host_seperated['Name']][Machine_type] = Current_count + 1
                    break 


    #print summery of machine allocation
    for Host in Hosts_seperated:
        Name = Host['Name']
        Allocated_vms = Host_Dict[Name]
        
        print_block = f"""******* {Name} *******
    Remaining Resources: CPU: {Host['CPU']} 
                        RAM: {Host['Memory']}GB
                        Storage: {Host['Storage']}GB
    """

        print_list.append(print_block)
        print(print_block)

        if Allocated_vms:
            print_block = f" Allocated Machines:"
            print_list.append(print_block)
            print(print_block)
            for machine_type, count in Allocated_vms.items():
                print_block = f"      {machine_type}: {count} machines"
                print_list.append(print_block)
                print(print_block)
        else:
            print_block = f" Allocated Machines: NONE"
            print_list.append(print_block)
            print(print_block)
        
        print_block = "-" * 50
        print_list.append(print_block)
        print(print_block)

    #print if there is not enough resources in hosts
    print_block = f"""
     ************************************************
                     Missing Resources
     ************************************************
"""
    print_list.append(print_block)
    print(print_block)

    total_missing_cpu = 0
    total_missing_mem = 0
    total_missing_strg = 0
    missing_found = False

    for Machine_type in Machines:
        requested = Machines[Machine_type]['Count']
        
        total_allocated = 0
        for host_name in Host_Dict:
            inventory = Host_Dict[host_name]
            if Machine_type in inventory:
                total_allocated = total_allocated + inventory[Machine_type]
        
        missing_count = requested - total_allocated

        if missing_count > 0:
            missing_found = True
            
            cpu_needed = Machines[Machine_type]['CPU'] * missing_count
            mem_needed = Machines[Machine_type]['Memory'] * missing_count
            strg_needed = Machines[Machine_type]['Storage'] * missing_count
            
            total_missing_cpu = total_missing_cpu + cpu_needed
            total_missing_mem = total_missing_mem + mem_needed
            total_missing_strg = total_missing_strg + strg_needed
            
            print_block = f"Notice: {missing_count} machines of type '{Machine_type}' could not be allocated."
            print_list.append(print_block)
            print(print_block)

    if missing_found == True:
        print_block = f"""TOTAL RESOURCES MISSING TO FIT ALL VMS:
Total CPU needed:     {total_missing_cpu}
Total Memory needed:  {total_missing_mem} GB
Total Storage needed: {total_missing_strg} GB
{"="*40}
"""
        print_list.append(print_block)
        print(print_block)
    else:
        print_block = "All machines were allocated successfully! No resources missing."
        print_list.append(print_block)
        print(print_block)
        print_list.append("="*40)
        print("="*40)

    #matanmo - call to export function
    #matanmo - after first PR, add an question to user if he wnat to save the report
    save_report = input("Do you want to save the report? (yes/no): ").lower()
    if save_report == 'y' or save_report == 'yes':
        export_result_to_file(print_list)
    
def export_result_to_file(print_list):
        """
        This function export print list to a new txt file with the calculator report
        Parameters:
            print_list (list): The list with the print that build the report
        """
        # for the reports, i make reports folder for the reports
        folder_name = 'reports/' 
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # make uniqe file name
        file_name = 'CalcReport-{date:%Y-%m-%d_%H:%M:%S}.txt'.format(date=datetime.datetime.now())
        file_path = os.path.join(folder_name, file_name) # the only way the path work for me
        with open(file_path, 'w+') as file:
            for print_block in print_list: # loop through every print block and write to the file with new line in end each print block
                file.write(print_block+"\n")
        print(f'SAVED! path to file:')
        print(os.getcwd()+ '/' + file_path)






        



