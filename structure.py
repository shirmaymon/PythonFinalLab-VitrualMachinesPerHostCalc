this file is to be deleted

project structure is - 

Big loop - 
        specify all variables and data structures - 
        Hosts = [] (List of Dictionaries)
        Users = {}
        Machines = {} (dictionary of dictionaries (with tuple))

    main manu -
        1 - loop 1 - enter server info 
            repeat for as many servers 
            allow changing/adding/removing
        2 - loop 2 - enter users info 
            repeat for as many users types 
            allow changing/adding/removing
        3 - loop 3 - enter machine info 
            repeat for as many machine types 
            allow changing/adding/removing
        4 - calculate
        5 - load dummy data
        6 - exit


***** loop 1 -  physical servers info *****
List of Dictionaries - 
[{name:,memory:,cpu:,storage:,count:},{name:,memory:,cpu:,storage:,count:},...]  
                1                                     2                    ...

how many servers do you have ? 
are they all the same type ? Y/N 
if N - how many types of servers you have ? 

for each type - 
name (string)
memory (float)
cpu (int)
storage (float)
number of servers - (int)


this is the information you typed - 
to -
change - type C
        if more than 1 - type the name of the group you want to change 
        to change name - type N
        to change memory - type M
        to change CPU - type C
        to change storage - type S
        to change number of servers - type A
add - type A 
remove (the whole group) - type R
        "Please notice! this action is not revertable, do you want to continue ? Y/N"
go back to main manu - type B



***** loop 2 - users info *****
dictionary -
{group name: number of users,}

how many users groups you have ? 
for each group - 
    name the group (Key) (string)
    how many users are in that group ? (Value) (int)


this is the information you typed - 
to -
change - type C
        if more than 1 - type the name of the group you want to change 
        to change name - type N
        to change number of users type - U
add - type A 
remove (the whole group) - type R
        "Please notice! this action is not revertable, do you want to continue ? Y/N"
go back to main manu - type B

**remember - if a name already exists - handle - choose diferent name or add to exisiting group ?




***** loop 3 - machines info *****
dictionary of dictionaries (with tuple) - 
{type:{cpu:,memory:,storage:,usergroups:()},type:{cpu:,memory:,storage:,usergroups:()},....}

how many machine types you need to have ? 
for each type - 
        cpu (int)
        memory (float)
        storage (float)
        how many user groups would use this type ? (int) 
            display users group types (unique) 
            enter group name (x number of groups) (string)


this is the information you typed - 
to -
change - type C
        if more than 1 - type the group type you want to change 
        to change cpu - type C
        to change memory type - M
        to change storage - type S
        to change users group - type U
add - type A 
remove (the whole group) - type R
        "Please notice! this action is not revertable, do you want to continue ? Y/N"
go back to main manu - type B

**remember - if a the same type already exists - handle 
             if asks to add but no users groups left - handle 


4 - calculate 

total number of machines and users - 
total need for cpu - 
               memory - 
               storage - 

machines per server - 
    server group name :
    server X/total - 
    machines on that server : 
        machine type - 
        amount of machines - 
        left cpu, memory, storage on that server - 

go back to main manu - type B






















