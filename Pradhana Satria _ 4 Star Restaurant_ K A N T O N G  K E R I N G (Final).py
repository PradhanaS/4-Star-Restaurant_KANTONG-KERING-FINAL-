import os
import sys
def mypass():                                                                                          # Password
	global password
	password = "admin123"
mypass()
def delete_last_lines(n):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)
        
def format_currency(amount):
    return 'Rp.{:,.2f},-'.format(amount)

app_idx_int = []
main_idx_int = []
dessert_idx_int = []
drinks_idx_int = []
wine_idx_int = []
snacks_idx_int = []
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

appetizer = {"name" : ["King Crab Salad", "Marsala Risotto", "Portobello Pot Roast"],
                "stock" : [1, 1, 2]}
main_course =  {"name" : ["Japanese Kobe Steak", "Beef Wellington", "Double-Smoked Salmon"],
                "stock" : [15, 15, 15]}
dessert = {"name" : ["Cheese Cake", "Apple Pie", "Fruit Cake"],
                "stock" : [15, 15, 15]}
drinks = {"name" : ["Coca-cola", "Sprite", "Ice Tea", "Lychee Tea", "Lemon Tea", "Mineral Water 600ml", "Mineral Water 300ml"],
                "stock" : [100, 100, 50, 50, 50, 150, 150],
                "price" : [75000, 75000, 65000, 65000, 65000, 35500, 35500]}
wine_list = {"name" : ["Grattamacco", "Tenuta San Guido", "Graci"],
                 "year" : [2014, 2014, 2018],
                 "stock" : [10, 1, 8],
                 "price": [2750000, 3200000, 1575000]}
snacks = {"name" : ["Stroopwaffle", "Prawn Crackers with Caviar","cheese waffle"],
          "stock" : [20,20,20]}
namaCustomer = {"name" : ["Test 1", "Test 2"],
               "age" : [40,45],
               "gender" : ["Male","Female"]}
ppp = [750000]

for x in range(len(appetizer['name'])):
    for y in range (len(dessert['name'])):
        print(f'{appetizer['name'][x]} with {dessert['name'][y]}')

print(f'{appetizer['name'][0]} with {dessert['name'][0]}')
print(f'{appetizer['name'][1]} with {dessert['name'][1]}')
print(f'{appetizer['name'][2]} with {dessert['name'][2]}')

print(f'{appetizer['name'][1]}')

# # ======================================= FUNCTION ============================================
# ## Main Menu
# def main_page():                                                                                           # Main Page
#     os.system('cls')
#     print("\n\n           W E L C O M E ")
#     print("                T O\n")
#     print("    K A N T O N G  K E R I N G !")
#     print(" \n             * * * *\n")
#     print("  THE MOST Over rated restaurant :p \n\n")

# def UserInput():        # Tested (OK)
#     global totalPerson
#     global TripleP
#     TripleP = totalPerson*(ppp[0])                                                                         # TripleP (Price Per Person)
#     for i in range(1,totalPerson+1):
#         nameInput = input(f"Person {i} name: ").title()
#         if nameInput.strip() == "":
#             namaCustomer["name"].append("NaN")
#         else:
#             namaCustomer["name"].append(nameInput)

#         while True:     # Tested (OK)
#             try:
#                 ageInput = int(input(f"Person {i} age: "))
#                 namaCustomer["age"].append(ageInput)
#                 break
#             except ValueError:
#                 input("Input Invalid press \"ENTER\" to re-input")
#                 delete_last_lines(2)

#         while True:     # Tested (OK)     
#             genderInput = input(f"Person {i} gender [M/F] or \"ENTER\" to skip: ").title()        
#             if genderInput.strip() == "":
#                 namaCustomer["gender"].append("NaN")
#             elif genderInput.strip().lower() == "woman" or genderInput.strip().lower() == "f" :
#                 namaCustomer["gender"].append("Female")
#             elif genderInput.strip().lower() == "man" or genderInput.strip().lower() == "m"  :
#                 namaCustomer["gender"].append("Male")
#             else:
#                 input("Please input gender")
#                 delete_last_lines(2)
#                 continue
#             break

# def order_input(x,cartData,judul):          # Tested (OK)
#     tableView(judul,x)
#     momAmo = []
#     if totalPerson < 2:
#         print("Press \"ENTER\" for next input")
#     else:
#         print("Press \"ENTER\" for next person")
#     print(f"*caution replacing item will remove all input in this {judul} menu")
#     for i in range(1,totalPerson+1):
#         while True:             # Tested (OK)
#             y = input(f"\nWhich one do you want [Person {i}]? [1-{len(x['name'])}]: ").lower()
#             if y == "":
#                 break
#             elif not y.isdigit():
#                 input("Input Invalid press \"ENTER\" to re-input")
#                 delete_last_lines(3)
#                 continue
#             z = int(y)
#             if z > len(x['name']):
#                 print("\nInvalid input!")
#                 input("Press ENTER to Re-Input Choice")
#                 delete_last_lines(5)
#                 continue
#             if x in [drinks, wine_list]:        # Tested (OK)
#                 while True:
#                     value1 = input(f"How much do you want: ")
#                     if value1 == "":
#                         break
#                     elif not value1.isdigit():
#                         input("Input Invalid press \"ENTER\" to re-input")
#                         delete_last_lines(2)
#                         continue
#                     value2 = int(value1)
#                     if value2 > x["stock"][z-1]:
#                         print(f"We are sorry, unfortunately {x["name"][z-1]} only {x["stock"][z-1]} left ")
#                         input()
#                         delete_last_lines(3)
#                         continue
#                     else:
#                         cartData.append({"name" : z, "amount" : value2})
#                         momAmo.append({"name" : z, "amount" : value2})
#                         for d in momAmo:
#                             x["stock"][d["name"]-1] -= d["amount"]
#                             momAmo.clear()
#                         break
#             else:                       # Tested (OK)
#                 value3 = int(1)
#                 if value3 > x["stock"][z-1]:
#                     print(f"We are sorry, unfortunately {x["name"][z-1]} out of stock")
#                     input()
#                     delete_last_lines(4)
#                     continue
#                 else:
#                     cartData.append({"name" : z, "amount" : value3})
#                     momAmo.append({"name" : z, "amount" : value3})
#                     for d in momAmo:
#                         x["stock"][d["name"]-1] -= d["amount"]
#                         momAmo.clear()
#                         break
#             break

#     while True:         # Tested (OK)
#         request = input("\nAre You Sure of it [y/n]? ").lower()
#         if request == "n":
#             for d in cartData:
#                 x["stock"][d["name"]-1] += d["amount"]           
#             cartData.clear()
#             order_input(x,cartData,judul)
#             return False
#         elif request == "y":
#             return True
#         else:
#             input("Input Invalid press \"ENTER\" to re-input")
#             delete_last_lines(3)
#             continue

# ## MAIN COURSE MENU
# def tableView(judul,tablesource):       # Tested (OK)                                                    # Main Menu (DONE)
#     os.system('cls')
#     print(f"\n{judul} \n")
#     if tablesource in [appetizer,main_course,dessert,snacks]:
#         print("------------------------------------------------------------")
#         print(f"|  INDEX  | {judul:<20}                 |  Stock  |")
#         print("------------------------------------------------------------")
#         for idx, item in enumerate(tablesource["name"]):
#             print(f"|    {idx+1:<5}| {item:<30}       |{tablesource["stock"][idx]:>6}   |")
#         print("------------------------------------------------------------")
#     elif tablesource == drinks:
#         print("---------------------------------------------------------------------")
#         print(f"|Index  | {judul:<20}        |  Stock  |  Price            |")
#         print("--------------------------------------------------------------------")
#         for idx, item in enumerate(tablesource["name"]):
#             print(f"|{idx+1:<5}  | {item:<22}      |{tablesource["stock"][idx]:>6}   |{format_currency(tablesource["price"][idx]):>16}   |")
#         print("---------------------------------------------------------------------")
#     elif tablesource == wine_list:
#         print("--------------------------------------------------------------------------------")
#         print(f"|Index  | {judul:<20}  |    Year    |  Stock  |  Price                |")
#         print("--------------------------------------------------------------------------------")
#         for idx, item in enumerate(tablesource["name"]):
#             print(f"|{idx+1:<5}  | {item:<16}      |{tablesource["year"][idx]:>8}    |{tablesource["stock"][idx]:>5}    |{format_currency(tablesource["price"][idx]):>20}   |")
#         print("--------------------------------------------------------------------------------")

# def customerTable():        # Tested (OK)
#     os.system('cls')
#     print("\nCUSTOMER HISTORY \n")
#     print("-------------------------------------------------------------")
#     print("|Index  | NAME                        |   AGE   | GENDER    |")
#     print("-------------------------------------------------------------")
#     for idx, item in enumerate(namaCustomer["name"]):
#         print(f"|{idx+1:<5}  | {item:<22}      |{namaCustomer["age"][idx]:>5}    | {namaCustomer["gender"][idx]:<9} |")
#     print("-------------------------------------------------------------")

# def full_table(tbl_1,jdl_1,tbl_2,jdl_2,tbl_3,jdl_3,tbl_4,jdl_4,tbl_5,jdl_5,tbl_6,jdl_6 ):       # Tested (OK)
#         os.system('cls')
#         print("------------------------------------------------------------")
#         print(f"|  INDEX  | NAME                                 |  Stock  |")
#         print("------------------------------------------------------------")
#         print(f"|                        {jdl_1}                         |")
#         print("------------------------------------------------------------")
#         for idx, item in enumerate(tbl_1["name"]):
#             print(f"|    {idx+1:<5}| {item:<30}       |{tbl_1["stock"][idx]:>6}   |")
#         print("------------------------------------------------------------")
#         print(f"|                       {jdl_2}                        |")
#         print("------------------------------------------------------------")
#         for idx, item in enumerate(tbl_2["name"]):
#             print(f"|    {idx+1:<5}| {item:<30}       |{tbl_2["stock"][idx]:>6}   |")
#         print("------------------------------------------------------------")
#         print(f"|                         {jdl_3}                          |")
#         print("------------------------------------------------------------")
#         for idx, item in enumerate(tbl_3["name"]):
#             print(f"|    {idx+1:<5}| {item:<30}       |{tbl_3["stock"][idx]:>6}   |")
#         print("------------------------------------------------------------")
#         print(f"|                         {jdl_4}                           |")
#         print("------------------------------------------------------------")
#         for idx, item in enumerate(tbl_4["name"]):
#             print(f"|    {idx+1:<5}| {item:<30}       |{(tbl_4["stock"][idx]):>6}   |")
#         print("------------------------------------------------------------")

#         print("\n---------------------------------------------------------------------")
#         print(f"|Index  | NAME                        |  Stock  |  Price            |")
#         print("---------------------------------------------------------------------")
#         print(f"|                             {jdl_5}                                |")
#         print("---------------------------------------------------------------------")
#         for idx, item in enumerate(tbl_5["name"]):
#             print(f"|{idx+1:<5}  | {item:<22}      |{tbl_5["stock"][idx]:>6}   |{format_currency(tbl_5["price"][idx]):>16}   |")
#         print("---------------------------------------------------------------------")

#         print("\n-------------------------------------------------------------------------------")
#         print(f"|Index  | NAME                  |    Year    |  Stock  |   Price              |")
#         print("-------------------------------------------------------------------------------")
#         print(f"|                                 {jdl_6}                                   |")
#         print("-------------------------------------------------------------------------------")
#         for idx, item in enumerate(tbl_6["name"]):
#             print(f"|{idx+1:<5}  | {item:<16}      |{tbl_6["year"][idx]:>8}    |{tbl_6["stock"][idx]:>5}    |{format_currency(tbl_6["price"][idx]):>20}  |")
#         print("--------------------------------------------------------------------------------")

# ## Food Update                                                                                          # (Admin Menu)
# def food_update():          # Tested (OK)                                                              # UPDATE SECTION (DONE)
#     os.system('cls')
#     print("\nFood Type Update\n")
#     print("1. Appetizer \n2. Main Course \n3. Dessert \n4. Drinks \n5. Wine \n6. Snacks \n7. Back")
#     fd_up = input("\nEnter number: ")
#     if fd_up == "1":                                                                                    # APPETIZER UPDATE (DONE)
#         fd_up_sub(appetizer, "Appetizer", "APPETIZER LIST")
#     elif fd_up == "2":                                                                                  # MAIN COURSE UPDATE (DONE)                        
#         fd_up_sub(main_course, "Main Course", "MAIN COURSE")
#     elif fd_up == "3":                                                                                  # DESSERT UPDATE (DONE)
#         fd_up_sub(dessert, "Dessert", "DESSERT")
#     elif fd_up == "4":                                                                                  # DRINKS UPDATE (DONE)
#         fd_up_sub(drinks, "Drinks", "DRINKS LIST")
#     elif fd_up == "5":                                                                                  # WINE UPDATE (DONE)
#         fd_up_sub(wine_list, "Wine", "WINE LIST")
#     elif fd_up == "6":                                                                                  # SNACKS UPDATE (DONE)
#         fd_up_sub(snacks, "Snacks", "SNACKS")
#     elif fd_up == "7":                                                                                  # Function from food_update()
#         return False                                                                    
#     else:
#         input("Invalid input! Press 'ENTER' to try again....")
#         food_update() 

# def fd_up_sub(x,y,z):       # Tested (OK)
#     tableView(z, x)
#     print("1. Add Item  2. Replace Item  3. Delete Item  4. Back")
#     fd_input = input("\nEnter number: ")
#     if fd_input == "1":
#         item_add(y,x)
#     elif fd_input == "2":
#         replace_value(x)
#     elif fd_input == "3":
#         item_delete(y,x)
#     elif fd_input == "4":
#         food_update()
#     else:
#         input("Invalid input! Press 'ENTER' to try again....")
#         fd_up_sub(x,y,z)

# def sub_rep(x,z,str_inp):   # Tested (OK)
#     while True: 
#         nW_Inp = input(f"Input {str_inp} replacement for {x['name'][z-1]}: ")
#         if nW_Inp.lower() == "cancel":
#             input("Update Canceled, press \"ENTER\" to exit")
#             break
#         if nW_Inp.isdigit():
#             pass
#         else:
#             input("Input invalid! press \"ENTER\" to re-input")
#             delete_last_lines(2)
#             continue
#         while True:
#             validInp = input("Are you sure [y/n]: ")
#             if validInp.lower() == "n":
#                 delete_last_lines(1)
#                 input("Update Canceled, press \"ENTER\" to exit")
#                 break
#             elif validInp.lower() != "y":
#                 input("Input invalid! press \"ENTER\" to re-input")
#                 delete_last_lines(2)
#                 continue
#             x[str_inp][z-1] = int(nW_Inp)
#             input(f"{x['name'][z-1]} {str_inp} has been updated, press \"ENTER\" to continue")
#             break
#         break

# # Replace Value                                                                                         # DONE (Admin Menu - Update)
# def replace_value(x):       # Tested (OK)
#     delete_last_lines(3)
#     print("2. Replace Item")
#     print("\nInput \"CANCEL\" To Go Back\n")
#     if x in [appetizer, main_course, dessert, snacks]:
#         print("A. Replace By Number   B. Replace Name   C. Replace Stock")
#     elif x == drinks:
#         print("A. Replace By Number   B. Replace Name   C. Replace Stock   D. Replace Price")
#     elif x == wine_list:
#         print("A. Replace By Number   B. Replace Name   C. Replace Stock   D. Replace Price   E. Year")

#     choose = input("\nInput which option: ").capitalize()
#     if choose.lower() == "cancel":
#         return
#     if choose not in ["A", "B", "C", "D", "E"]:
#         input("Please Input Correctly")
#         delete_last_lines(5)
#         replace_value(x)
#         return
    
#     while True:     # Tested (OK)
#         c = input(f"\nWhich item do you want to update? Please input index [1-{len(x['name'])}]: ").lower()
#         if c == "cancel":
#             return False
#         elif not c.isdigit():
#             input("Input invalid! Press ENTER to re-input.")
#             delete_last_lines(3)
#             continue
#         z = int(c)
#         if 1 <= z <= len(x['name']):
#             break
#         else:
#             input("Input out of range! Press ENTER to re-input.")
#             delete_last_lines(3)
#             continue

#     while True and choose == "A":       # Tested (OK)
#         inputName = input(f"\nInput new name for item {x['name'][z-1]}: ")
#         if inputName.lower() == "cancel":
#             input("Update Canceled, press \"ENTER\" to exit")
#             break
#         elif inputName.strip() == "":
#             input("Please input name, press \"ENTER\" to re-input")
#             delete_last_lines(3)
#             continue

#         while True:     # Tested (OK)
#             inputStock = input(f"Input new stock: ")
#             if inputStock.lower() == "cancel":
#                 input("Update Canceled, press \"ENTER\" to exit")
#                 return False
#             if inputStock.isdigit():
#                 if x in [appetizer, main_course, dessert, snacks]:
#                     x["name"][z-1] = inputName.title()
#                     x["stock"][z-1] = int(inputStock)
#                 break
#             else:
#                 input("Input invalid! press \"ENTER\" to re-input")
#                 delete_last_lines(2)
#                 continue
        
#         while x in [drinks, wine_list]:     # Tested (OK)
#             inputPrice = input(f"Input Price: ")
#             if inputPrice.lower() == "cancel":
#                 input("Change canceled, press \"ENTER\" to exit")
#                 return False
#             elif not inputPrice.isdigit():
#                 input("Input invalid! Change canceled, press \"ENTER\" to exit")
#                 delete_last_lines(2)
#                 continue
#             elif x == drinks:    # Tested (OK)
#                 valid = input("Are you sure? if sure [y] if not! input anything : ").lower()
#                 if valid == "y":
#                     x["name"][z-1] = inputName.title()
#                     x["stock"][z-1] = int(inputStock)
#                     x["price"][z-1] = int(inputPrice)
#                     break
#                 elif valid == "n":
#                     return False
#                 input("Input invalid! Change canceled, press \"ENTER\" to re-input")
#                 delete_last_lines(3)
#                 continue
#             elif x == wine_list:
#                 break
                
#         while True and x == wine_list:   # Tested (OK)
#             inputYear = input(f"Input Year: ")
#             if inputYear.lower() == "cancel":
#                 input("Change canceled, Press ENTER to exit")
#                 return False
#             elif not inputYear.isdigit():
#                 input("Input invalid! Change canceled, press \"ENTER\" re-input")
#                 delete_last_lines(2)
#                 continue
            
#             while True:     # Tested (OK)
#                 valid = input("Are you sure [y/n]: ").lower()
#                 if valid == "n":
#                     input("Input Canceled")
#                     return False
#                 if valid != "y":
#                     input("Input invalid! Change canceled, press \"ENTER\" to re-input")
#                     delete_last_lines(2)
#                     continue
#                 x["name"][z-1] = inputName.title()
#                 x["stock"][z-1] = int(inputStock)
#                 x["price"][z-1] = int(inputPrice)
#                 x["year"][z-1] = int(inputYear)
#                 break
#             break

#         input(f"Item {z} has been updated!! press \"ENTER\" to proceed")
#         break
    
#     while choose == "B":    # Tested (OK)
#         newName = input(f"\nInput new name for item {x['name'][z-1]}: ")
#         if newName.lower() == "cancel":
#             input("Update Canceled, press \"ENTER\" to exit")
#             break
#         elif newName.strip() == "":
#             delete_last_lines(2)
#             continue
#         x["name"][z-1] = newName.title()
#         input(f"{x['name'][z-1]} has been updated to {newName}, press \"ENTER\" to proceed")
#         break

#     if choose == "C":   # Tested (OK)
#         sub_rep(x,z,"stock")
#         return False

#     if choose == "D" and x in [drinks, wine_list]:  # Tested (OK)
#         sub_rep(x,z,"price")
#         return False

#     if choose == "E" and x == wine_list:    # Tested (OK)
#         sub_rep(x,z,"year")
#         return False
#     return

# # Item Delete                                                                                           # DONE (Admin Menu - Update)
# def item_delete(a,b):   # Tested (OK)
#     delete_last_lines(3)
#     print("3. DELETE ITEM")
#     print("\nInput \"CANCEL\" To Go Back")
#     while True:
#         try:
#             c = input(f"\nDelete {a} item, please input index [1-{len(b["name"])}]: ").lower()
#             if c == "cancel":
#                 food_update()
#             else:
#                 z = int(c)
#                 if z > len(b['name']):
#                     input(f"\nInvalid input! press \"ENTER\" to re-input!")
#                     delete_last_lines(4)
#                     continue
#                 else:
#                     b["name"].pop(z-1)
#                     b["stock"].pop(z-1)
#                     if b == drinks or b == wine_list:
#                         b["price"].pop(z-1)
#                         if b == wine_list:
#                             b["year"].pop(z-1)
#                     break
#         except ValueError:
#             input("Input Invalid press \"ENTER\" to re-input")
#             delete_last_lines(3)
#             continue

# # Item Add                                                                                              # DONE (Admin Menu - Update)
# def item_add(a,b):
#     delete_last_lines(3)
#     print("1. UPDATE LIST")
#     print("\nInput \"CANCEL\" To Go Back")
#     while True:                                                 # Tested (OK)
#         c = input(f"\nInsert {a} name: ").title()
#         if c == "Cancel":
#             return False
#         elif c.strip() == "":
#             input("Please input name")
#             delete_last_lines(3)
#             continue
#         break

#     while True:                                                 # Tested (OK)
#         d = input(f"Insert {a} stock: ")
#         if d == "cancel":
#             return False
#         if not d.isdecimal():
#             input("Input Invalid press \"ENTER\" to re-input")
#             delete_last_lines(2)
#             continue
#         stock_int = int(d)
#         break

#     while True and b in [drinks, wine_list]:                    # Tested (OK)
#         e = input(f"Insert {a} price: ")
#         if e.lower() == "cancel":
#             return False
#         if not e.isdecimal():
#             input("Input Invalid press \"ENTER\" to re-input")
#             delete_last_lines(2)
#             continue
#         price_int = int(e)
#         b["price"].append(price_int)
#         break

#     while True and b == wine_list:                              # Tested (OK)
#         f = input(f"Insert {a} year: ")
#         if f.lower() == "cancel":
#             return False
#         if not f.isdecimal():
#             input("Input Invalid press \"ENTER\" to re-input")
#             delete_last_lines(2)
#             continue
#         year_int = int(f)
#         b["year"].append(year_int)
#         break

#     b["name"].append(c)
#     b["stock"].append(stock_int)

# totalHarga = 0

# def sub_bill(tabelU,y_int,joedoel):         # Tested (OK)
#     global totalHarga 
#     if tabelU in [appetizer,main_course,dessert,snacks]:
#         print(f"\n *** {joedoel} ***")
#         for data in y_int:
#             print(f"X {data["amount"]}  {tabelU["name"][data["name"]-1]}")
#         y_int.clear()
#     elif tabelU in [drinks, wine_list]:
#         print(f"\n *** {joedoel} ***")
#         for data in y_int:
#             totalHarga += (data["amount"]*tabelU["price"][data["name"]-1])
#             print(f"X {data["amount"]:<3}  {tabelU["name"][data["name"]-1]:<19}                         {format_currency(data["amount"]*tabelU["price"][data["name"]-1]):>23}")
#         y_int.clear()

# def bill():         # Tested (OK)
#     os.system('cls')
#     # totalHarga = 0
#     print(f"X {totalPerson}  Person                                               {format_currency(TripleP)}")
    
#     sub_bill(appetizer,app_idx_int,"APPETIZER")
#     sub_bill(main_course,main_idx_int,"MAIN COURSE")
#     sub_bill(dessert,dessert_idx_int,"DESSERT")
#     sub_bill(snacks,snacks_idx_int,"SNACKS")
#     sub_bill(drinks,drinks_idx_int,"DRINKS")
#     sub_bill(wine_list,wine_idx_int,"WINE")

#     print("==========================================================================\n") 
#     subTotal = totalHarga + TripleP
#     subTax = int(subTotal/10)
#     global grandTotal
#     grandTotal = subTax + subTotal
#     print(f"                                     sub Total = {format_currency(subTotal):>25}")
#     print(f"                                       TAX 10% = {format_currency(subTax):>25}")
#     print("==========================================================================\n") 
#     print(f"                                   Grand Total = {format_currency(grandTotal):>25}")

# # ================================= LOOPING SEQUENCE ======================================
# while True:
#     main_page()
#     main2 = input("Press ENTER to Proceed ")
#     if main2 == "admin":
#         print("Only authorized personel are allowed to access this option !!")
#         clarification = input("Are you sure you are authorized? [y/n]: ")
#         if clarification == "y":
#             os.system('cls')
#             passRequest = input("\nEnter Admin Password: ")
#             while True:
#                 if passRequest == password:
#                     os.system('cls')
#                     print("\nAdmin Option \n")
#                     print("1. Full Menu List \n2. Food Update \n3. Customer List \n4. Update TripleP \n5. Back To Main Page \n6. Turn Off System ")
#                     ad_target = input("\nwhich menu you wish to do [1-5]: ")                                                                      # Function from food_update()
#                     if ad_target == "1":
#                         full_table(appetizer,"APPETIZER",main_course,"MAIN COURSE",dessert,"DESSERT",snacks,"SNACKS",drinks,"DRINKS",wine_list,"WINE LIST")
#                         input("Press Anything To Go Back")
#                     elif ad_target == "2":
#                         food_update()
#                     elif ad_target == "3":      # customerTable DONE !!!
#                         customerTable()
#                         input("Press Anything To Go Back")
#                     elif ad_target == "4":      # TripleP (Price Per Person) update # DONE!!!
#                         while True:
#                             try:
#                                 delete_last_lines(1)
#                                 print(f"TripleP now is {format_currency(ppp[0])}")
#                                 rep_PPP = int(input("Update Price Per Person: "))
#                                 req3 = input("Are you sure? if sure [y] if not! input anything : ")
#                                 if req3 != "y":
#                                     input("Update canceled, press \"ENTER\" to exit")
#                                     break
#                                 ppp[0] = rep_PPP
#                                 delete_last_lines(3)
#                                 print(f"Updated TripleP {format_currency(ppp[0])}")
#                                 input(f"TripleP Updated to {format_currency(ppp[0])}, press \"ENTER\" to go back")
#                                 break
#                             except ValueError:
#                                 input("Input Invalid press \"ENTER\" to re-input")
#                                 delete_last_lines(2)
#                                 continue
#                     elif ad_target == "5":      # DONE !!!
#                         os.system('cls')
#                         break
#                     elif ad_target == "6":      # DONE !!!
#                         os.system('cls')
#                         sys.exit()
#                     else:
#                         print("Invalid input! Press 'ENTER' to try again....")
#                         input()
#                         continue
#                 elif passRequest.lower() == "back":
#                     break
#                 elif passRequest != password:  
#                     os.system('cls')
#                     print("\nIncorrect Password")
#                     print("\n!!! Press Enter to Re-Try !!!")
#                     input()
#                     os.system('cls')
#                     print("\n!Write \"Back\" to go back to main page!")
#                     passRequest = input("\nEnter Admin Password: ")
#                     continue
#         elif clarification != "n":
#             continue

#     while main2 != "admin":                                                                                                                                         ## Opening Page for USER     
#         main_page()
#         totalPerson = input("How Many Person: ")
#         if totalPerson.lower() == "cancel":
#             break
#         elif not totalPerson.isdigit():
#             input("Input invalid! press \"ENTER\" to re-input")
#             delete_last_lines(2)
#             continue

#         totalPerson = int(totalPerson)             # Tested (OK)
#         UserInput()
#         while True:
#             order_input(appetizer,app_idx_int,"APPETIZER LIST")
#             order_input(main_course,main_idx_int,"MAIN COURSE")
#             order_input(dessert,dessert_idx_int,"DESSERT")
#             order_input(snacks,snacks_idx_int,"SNACKS")
#             order_input(drinks,drinks_idx_int,"DRINKS LIST")
#             order_input(wine_list,wine_idx_int,"WINE LIST")
#             bill()
#             while True:                            # Tested (OK)
#                 try:
#                     print("\nPlease input payment without \"Rp.\" \",\" and \",-\" Thank You.")
#                     payment = int(input("Input your payment: "))
#                     if payment < grandTotal:
#                         print(f"\nSorry, your payment isn't enought {format_currency(grandTotal-payment)} short")
#                         input("press \"ENTER\" to re-pay")
#                         # os.system('cls')
#                         delete_last_lines(6)
#                         # bill()
#                         continue
#                     else:
#                         if payment > grandTotal:
#                             print(f"\nYour change: Rp. {format_currency(payment - grandTotal)},-")
#                         print("\nTHANK YOUR FOR EATING WITH US, WE WILL SEE YOU SOON!")
#                         input()
#                         totalHarga=0
#                         os.system('cls')
#                         break
#                 except ValueError:
#                     input("Input Invalid press \"ENTER\" to re-input")
#                     delete_last_lines(4)
#                     continue
#             break
#         break







