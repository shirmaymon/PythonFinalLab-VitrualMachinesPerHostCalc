# VM per Host Calculator 🖥️

An interactive command-line tool designed to help infrastructure admins determine the hosting capacity of their physical server fleet based on specific virtual machine workloads.

## 🚀 Features

* **Physical Server Inventory**: Add, edit, and delete hardware specs for various host types, including CPU, Memory (GB), and Storage (GB).
* **User Population Management**: Define different groups of users (e.g., Developers, Office) and their respective counts.
* **Machine Profile Configuration**: Set up technical requirements (CPU, RAM, Storage) for the Virtual Machines that will serve these users.
* **Data Simulation**: Includes a "Dummy Data" loader to quickly see how the application handles multiple data structures simultaneously.

---

## 📂 Project Structure

The project is highly modular to keep logic clean and manageable:

| File | Role |
| :--- | :--- |
| `main.py` | The "Brain" – manages the main loop and user interaction. |
| `Menu_Option_1_Servers.py` | Handles the `Hosts` list (List of Dictionaries). |
| `Menu_option_2_Users.py` | Handles the `Users` list (List of Dictionaries). |
| `Menu_option_3_Machines.py` | Handles the `Machines` dictionary. |
| `Menu_Option_4_TheCalculator.py` | Makes the calcultaion based on the data. |
| `Menu_Option_5_DummyData.py` | Provides pre-set testing data. |
| `Menu_Option_6_ShowDelete.py` | Shows or deletes all data Hosts, Users and Machines |
| `Menu_User_massages.py` | Stores all UI headers and instructional text. |

---

## 🛠️ How to Use

1. **Run the script**: `python main.py`
2. **Setup Infrastructure**: Use Option 1 to input your physical servers.
3. **Define Demand**: Use Option 2 to define your user base.
4. **Configure VMs**: Use Option 3 to set the specs for the virtual machines.
5. **Calculate**: Use Option 4 to make the final calculation and get the results - which machines should be provsioned on which hosts.
6. **Test**: Use Option 5 to auto-populate data if you want to skip manual entry.


---

## ⚠️ Important Notes

* **Case Sensitivity**: Please be careful! The system is **kEy SeNsiTive**. Ensure names match exactly when editing or deleting.
* **Input Validation**: The script currently checks for basic value errors and negative numbers to prevent "impossible" hardware specs.
