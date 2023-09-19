import sqlite3
from sqlite3 import Error
from datetime import datetime

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec']


def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
      
    except Error as e:
        print(e)

    return con


def Insert_Update_Delete(cur, insert_update_check):
    try:
        c = cur.cursor()
        c.execute(insert_update_check)
      
    except Error as e:
        print(e)
      

def Check_Table(cur, check_table):
    try:
        c = cur.cursor()
        c.execute(check_table)
        items = c.fetchall()
        for item in items[0:1]:
            for i in item:
                return i
    except Error as e:
        print(e)

      
def Check_Tables(cur, check_tables):
    try:
        c = cur.cursor()
        c.execute(check_tables)
        items = c.fetchall()
        # print("\n")
        for item in items[1::2]:
            for i in item:
                print(f"> {i}")
              
    except Error as e:
        print(e)


def Check_ID(cur, check_id):
    try:
        c = cur.cursor()
        for ID in c.execute(check_id):
            for id in ID:
                return id
           
    except Error as e:
        print(e)


def Check(cur, check):
    try:
        c = cur.cursor()
        for row in c.execute(check):
            r = []
            for i in row:
                c = i.replace(",", "")
                r.append(c)    
            print(f"> Name: {r[0]}")
            print(f"> {months_list[month-1]}: {r[1]}")
            print(f"> {months_list[month-2]}: {r[2]}")
            print(f"> {months_list[month-3]}: {r[3]}")
            print(f"> {months_list[month-4]}: {r[4]}")
            print(f"> {months_list[month-5]}: {r[5]}")
            print(f"> {months_list[month-6]}: {r[6]}")
            print("--------------------")
    except Error as e:
        print(e)


def Check_Record(cur, check_record):
    try:
        c = cur.cursor()
        for row in c.execute(check_record):
            r = []
            for i in row:
                c = i.replace(",", "")
                r.append(c)    
            print(f"> Name: {r[0]}")
            print(f"> {months_list[month-1]}: {r[1]}")
            print(f"> {months_list[month-2]}: {r[2]}")
            print(f"> {months_list[month-3]}: {r[3]}")
            print(f"> {months_list[month-4]}: {r[4]}")
            print(f"> {months_list[month-5]}: {r[5]}")
            print(f"> {months_list[month-6]}: {r[6]}")
            print(f"> {months_list[month-7]}: {r[7]}")
            print(f"> {months_list[month-8]}: {r[8]}")
            print(f"> {months_list[month-9]}: {r[9]}")
            print(f"> {months_list[month-10]}: {r[10]}")
            print(f"> {months_list[month-11]}: {r[11]}")
            print(f"> {months_list[month-12]}: {r[12]}")
            print(f"> L_{months_list[month-13]}: {r[13]}")
            print(f"> L_{months_list[month-14]}: {r[14]}")
            print(f"> L_{months_list[month-15]}: {r[15]}")
            print(f"> L_{months_list[month-16]}: {r[16]}")
            print(f"> L_{months_list[month-17]}: {r[17]}")
            print(f"> L_{months_list[month-18]}: {r[18]}")
            print(f"> L_{months_list[month-19]}: {r[19]}")
            print(f"> L_{months_list[month-20]}: {r[20]}")
            print(f"> L_{months_list[month-21]}: {r[21]}")
            print(f"> L_{months_list[month-22]}: {r[22]}")
            print(f"> L_{months_list[month-23]}: {r[23]}")
            print(f"> L_{months_list[month-24]}: {r[24]}")
            print("--------------------")
    except Error as e:
        print(e)


def Check_Dues(cur, check_dues):
    try:
        c = cur.cursor()
        for row in c.execute(check_dues):
            r = []
            totlist = []
            total = 0
            for i in row:
                num = i.split(",")
                totlist.append(num[0])
                c = i.replace(",", "")
                r.append(c)    

            if (r[1][0] != "0" or r[2][0] != "0" or r[3][0] != "0" or r[4][0] != "0" or r[5][0] != "0" or r[6][0] != "0" or r[7][0] != "0" or r[8][0] != "0" or r[9][0] != "0" or r[10][0] != "0" or r[11][0] != "0" or r[12][0] != "0" or r[13][0] != "0" or r[14][0] != "0" or r[15][0] != "0" or r[16][0] != "0" or r[17][0] != "0" or r[18][0] != "0" or r[19][0] != "0" or r[20][0] != "0" or r[21][0] != "0" or r[22][0] != "0" or r[23][0] != "0" or r[24][0] != "0"):
                print(f"> Name: {r[0]}")
          
            if ("0" != r[1][0]):
                print(f"> {months_list[month-1]}: {r[1]}")
                total += int(totlist[1])
              
            if ("0" != r[2][0]):
                print(f"> {months_list[month-2]}: {r[2]}")
                total += int(totlist[2])
              
            if ("0" != r[3][0]):
                print(f"> {months_list[month-3]}: {r[3]}")
                total += int(totlist[3])
              
            if ("0" != r[4][0]):            
                print(f"> {months_list[month-4]}: {r[4]}")
                total += int(totlist[4])
                
            if ("0" != r[5][0]):            
                print(f"> {months_list[month-5]}: {r[5]}")  
                total += int(totlist[5])
                
            if ("0" != r[6][0]):            
                print(f"> {months_list[month-6]}: {r[6]}")  
                total += int(totlist[6])
                
            if ("0" != r[7][0]):            
                print(f"> {months_list[month-7]}: {r[7]}") 
                total += int(totlist[7])
                
            if ("0" != r[8][0]):            
                print(f"> {months_list[month-8]}: {r[8]}")  
                total += int(totlist[8])
                
            if ("0" != r[9][0]):            
                print(f"> {months_list[month-9]}: {r[9]}")  
                total += int(totlist[9])
                
            if ("0" != r[10][0]):            
                print(f"> {months_list[month-10]}: {r[10]}")    
                total += int(totlist[10])
                
            if ("0" != r[11][0]):            
                print(f"> {months_list[month-11]}: {r[11]}")   
                total += int(totlist[11])
                
            if ("0" != r[12][0]):            
                print(f"> {months_list[month-12]}: {r[12]}")  
                total += int(totlist[12])
                
            if ("0" != r[13][0]):            
                print(f"> L_{months_list[month-13]}: {r[13]}")    
                total += int(totlist[13])
                
            if ("0" != r[14][0]):            
                print(f"> L_{months_list[month-14]}: {r[14]}")    
                total += int(totlist[14])
                
            if ("0" != r[15][0]):            
                print(f"> L_{months_list[month-15]}: {r[15]}")    
                total += int(totlist[15])
                
            if ("0" != r[16][0]):            
                print(f"> L_{months_list[month-16]}: {r[16]}")    
                total += int(totlist[16])
              
            if ("0" != r[17][0]):            
                print(f"> L_{months_list[month-17]}: {r[17]}")    
                total += int(totlist[17])
              
            if ("0" != r[18][0]):            
                print(f"> L_{months_list[month-18]}: {r[18]}")    
                total += int(totlist[18])
              
            if ("0" != r[19][0]):            
                print(f"> L_{months_list[month-19]}: {r[19]}")  
                total += int(totlist[19])
              
            if ("0" != r[20][0]):            
                print(f"> L_{months_list[month-20]}: {r[20]}")   
                total += int(totlist[20])
              
            if ("0" != r[21][0]):            
                print(f"> L_{months_list[month-21]}: {r[21]}")   
                total += int(totlist[21])
              
            if ("0" != r[22][0]):            
                print(f"> L_{months_list[month-22]}: {r[22]}")   
                total += int(totlist[22])
              
            if ("0" != r[23][0]):            
                print(f"> L_{months_list[month-23]}: {r[23]}")  
                total += int(totlist[23])
              
            if ("0" != r[24][0]):            
                print(f"> L_{months_list[month-24]}: {r[24]}") 
                total += int(totlist[24])
              
            if (r[1][0] != "0" or r[2][0] != "0" or r[3][0] != "0" or r[4][0] != "0" or r[5][0] != "0" or r[6][0] != "0" or r[7][0] != "0" or r[8][0] != "0" or r[9][0] != "0" or r[10][0] != "0" or r[11][0] != "0" or r[12][0] != "0" or r[13][0] != "0" or r[14][0] != "0" or r[15][0] != "0" or r[16][0] != "0" or r[17][0] != "0" or r[18][0] != "0" or r[19][0] != "0" or r[20][0] != "0" or r[21][0] != "0" or r[22][0] != "0" or r[23][0] != "0" or r[24][0] != "0"):  
                print(f"> Total: {total}")
                print("--------------------")
          
    except Error as e:
        print(e)

  
def Check_Month(cur):
    try:
        c = cur.cursor()
        for row in c.execute(" SELECT num From RaDin where name = 'month' "):
            for i in row:
                return i

    except Error as e:
        print(e)


def OriginalDate(d, m, y):
  
    return f"{d}-{m}-{y}"


def Get_Cls(cur):
    c = cur.cursor()
    c.execute("""SELECT name FROM sqlite_master""")
    tables = c.fetchall()
    LoC = []
    for clas in tables[1::2]:
        for cls in clas:
            LoC.append(cls)
    return LoC         

def MonthToCol(col):
    if (col == months_list[month-1]):
        return "recent"    
    elif (col == months_list[month-2]):
        return "last1"  
    elif (col == months_list[month-3]):
        return "last2"  
    elif (col == months_list[month-4]):
        return "last3"  
    elif (col == months_list[month-5]):
        return "last4"  
    elif (col == months_list[month-6]):
        return "last5"  
    elif (col == months_list[month-7]):
        return "last6"  
    elif (col == months_list[month-8]):
        return "last7"  
    elif (col == months_list[month-9]):
        return "last8"  
    elif (col == months_list[month-10]):
        return "last9"  
    elif (col == months_list[month-11]):
        return "last10"  
    elif (col == months_list[month-12]):
        return "last11"  
    elif (col == f"L_{months_list[month-13]}"):
        return "last12"  
    elif (col == f"L_{months_list[month-14]}"):
        return "last13"  
    elif (col == f"L_{months_list[month-15]}"):
        return "last14"  
    elif (col == f"L_{months_list[month-16]}"):
        return "last15"  
    elif (col == f"L_{months_list[month-17]}"):
        return "last16"  
    elif (col == f"L_{months_list[month-18]}"):
        return "last17"  
    elif (col == f"L_{months_list[month-19]}"):
        return "last18"  
    elif (col == f"L_{months_list[month-20]}"):
        return "last19"  
    elif (col == f"L_{months_list[month-21]}"):
        return "last20"  
    elif (col == f"L_{months_list[month-22]}"):
        return "last21"
    elif (col == f"L_{months_list[month-23]}"):
        return "last22"
    elif (col == f"L_{months_list[month-24]}"):
        return "last23"
          
def Addition_Subtraction(cur, cls, u_i, n, col):
   
    def Get_data(cur, get_data):
        try:
            c = cur.cursor()  
            for item in c.execute(get_data):
                for i in item:
                    return i
                  
        except Error as e:
            print(e)

    values = f""" SELECT {col} From Class_{cls} where name = '{n}' """  
  
    Data = Get_data(cur, values)  
    data = Data.split(",")
  
    plus = int(data[0]) + int(u_i[1::])
    minus = int(data[0]) - int(u_i[1::])

    def Records(u_i, n, col, cur, count):
    
        records = f"| {u_i} / {OriginalDate(day, month, year)} "
        first_words = f"{count},{data[1]}"
      
        m_d = first_words + records
      
        c = cur.cursor()
        c.execute(f""" Update Class_{cls} set {col} = '{m_d}' where name = '{n}' """)
        cur.commit()

    if u_i[0] == "+":  
        Records(u_i, n, col, cur, plus)       
        print(f"  {u_i[1::]} added successfully\n")
      
    elif u_i[0] == "-":
        Records(u_i, n, col, cur, minus)
        print(f"  {u_i[1::]} subtracted successfully\n")
        

def mainfunc():
  
    id = 386598423721096
   
    # database address
    database = r"Manipulator.db"
        
    # create a database connection
    con = create_connection(database)
        
    if con is not None:
        
        if Check_Table(con, """ SELECT name FROM sqlite_master """) != "RaDin":
          
            while True:
              
                prompt = int(input("User Id: "))
              
                if (prompt == id):
                
                    insert_table = """ CREATE TABLE IF NOT EXISTS RaDin (name text, num integer, nToE integer, ninth integer, matric integer, id integer); """           
                    insert_values = f""" INSERT INTO RaDin (name, num, nToE, ninth, matric, id) VALUES ("month", 1, 0, 0, 0, {prompt}) """            
                                
                    Insert_Update_Delete(con, insert_table)
                    Insert_Update_Delete(con, insert_values)
                    con.commit()

                    print("Correct id!")
                    break
              
        elif Check_Table(con, """ SELECT name FROM sqlite_master """) == "RaDin":
        
            if Check_ID(con, """ SELECT id From RaDin where name = 'month' """) == id:
            
                if (OriginalDate(day, month, year) == OriginalDate(1, month, year) and Check_Month(con) == 1):
                  
                    cl = Get_Cls(con)
        
                    def modify_data(cn):
                        c = con.cursor()
                        LoN = []
        
                        for name in c.execute(f""" SELECT name From {cn} """):
                            for n in name:
                                LoN.append(n)
                      
                        def mod(n):
                            con = create_connection(database)
                            c = con.cursor()
                            for row in c.execute(f"""SELECT recent, last1, last2, last3, last4, last5, last6, last7, last8, last9, last10, last11, last12, last13, last14, last15, last16, last17, last18, last19, last20, last21, last22, last23 From {cn} where name = '{n}' """):
                                c.execute(f""" Update {cn} set last23 = '{row[22]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last22 = '{row[21]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last21 = '{row[20]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last20 = '{row[19]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last19 = '{row[18]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last18 = '{row[17]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last17 = '{row[16]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last16 = '{row[15]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last15 = '{row[14]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last14 = '{row[13]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last13 = '{row[12]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last12 = '{row[11]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last11 = '{row[10]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last10 = '{row[9]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last9 = '{row[8]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last8 = '{row[7]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last7 = '{row[6]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last6 = '{row[5]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last5 = '{row[4]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last4 = '{row[3]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last3 = '{row[2]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last2 = '{row[1]}' where name = '{n}' """)
                                c.execute(f""" Update {cn} set last1 = '{row[0]}' where name = '{n}' """)
                              
                                for f in c.execute(""" SELECT nToE, ninth, matric From RaDin where name = 'month' """):
                                    if ("10" in cn):
                                        c.execute(f""" Update {cn} set recent = '{f[2]}, ' where name = '{n}' """)
                              
                                    elif ("9" in cn):
                                        c.execute(f""" Update {cn} set recent = '{f[1]}, ' where name = '{n}' """)
                                        
                                    else:
                                        c.execute(f""" Update {cn} set recent = '{f[0]}, ' where name = '{n}' """)
                                con.commit()
                              
                        list(map(mod, LoN))
                      
                    list(map(modify_data, cl))
                  
                    def oneTimeRun():
                        c = con.cursor()
                        c.execute(" Update RaDin set num = 0 where name = 'month' ")
                        con.commit()
                        print("Month is changed")
                    
                    oneTimeRun()
        
              
                elif (OriginalDate(day, month, year) == OriginalDate(2, month, year)):
                    c = con.cursor()
                    c.execute(" Update RaDin set num = 1 where name = 'month' ")
                    con.commit()
                  
                    print("Preparing resources...")
        
              
                else:
                    print("""Type "intro" for introduction""")
                                          
                    while True:
                        user_input = input("\nWhat you want: ")
            
                        if (user_input == "e"):
                            break

                        elif (user_input == "intro"):
                            print("""\n- Type "e" for exit function. \n- Type "i c" for inserting class. \n- Type "c c" for checking class. \n- Type "r c" for removing class. \n- Type "i" for inserting student in class. \n- Type "c" for checking student. \n- Type "c r" for checking record of student. \n- Type "c d" for checking dues of students. \n- Type "c a" for checking all students. \n- Type "r" for removing student in class. \n- Type "change session" for changing year. \n- Type "fees" for setup feeses.""")
                            print("""\nNote: \n- Always insert class by descending order \n- Inside every check function there is another function for addition and subtraction thats sytax is "+500" or "-500" """)
                                                
                        elif (user_input == "change session"):
                          
                            cls = Get_Cls(con)
                
                            def Cls_Index(cl):
                              l = []
                              for i in range(len(cl)):
                                  l.append(i)
                              return l
                  
                            index = Cls_Index(cls)
                            
                            def modify_data(cl, ind, cur):
                                c = cur.cursor()
                
                                for i in ind:                        
                                    c.execute(f""" ALTER TABLE {cl[i]} RENAME TO C{i} """)  
                
                                c.execute(""" DROP TABLE IF EXISTS C0 """)
                                for i, n in zip(ind[1::], ind):
                                    c.execute(f""" ALTER TABLE C{i} RENAME TO {cl[n]} """)   

                                insert_table = f""" CREATE TABLE IF NOT EXISTS {cl[-1]} (name text unique, recent text, last1 text, last2 text, last3 text, last4 text, last5 text, last6 text, last7 text, last8 text, last9 text, last10 text, last11 text, last12 text, last13 text, last14 text, last15 text, last16 text, last17 text, last18 text, last19 text, last20 text, last21 text, last22 text, last23 text); """
                
                                Insert_Update_Delete(con, insert_table)
                                    
                            modify_data(cls, index, con)
                          
                            print("\nSession successfully changed")
                                                   
                        elif (user_input == "fees"):
                            nTo8 = int(input("\nNursery to Eight fees: "))
                            ninth = int(input("Ninth fees: "))
                            matric = int(input("Matric fees: "))
                          
                            update_fees1 = f""" Update RaDin set nToE = {nTo8} where name = 'month' """
                            update_fees2 = f""" Update RaDin set ninth = {ninth} where name = 'month' """
                            update_fees3 = f""" Update RaDin set matric = {matric} where name = 'month' """
                          
                            Insert_Update_Delete(con, update_fees1)
                            Insert_Update_Delete(con, update_fees2)
                            Insert_Update_Delete(con, update_fees3)
                            con.commit()
            
                        elif (user_input == "i c"):
                            cls = input("\nClass Name: ")
                            insert_table = f""" CREATE TABLE IF NOT EXISTS Class_{cls} (name text unique, recent text, last1 text, last2 text, last3 text, last4 text, last5 text, last6 text, last7 text, last8 text, last9 text, last10 text, last11 text, last12 text, last13 text, last14 text, last15 text, last16 text, last17 text, last18 text, last19 text, last20 text, last21 text, last22 text, last23 text); """
                
                            Insert_Update_Delete(con, insert_table)
                          
                        elif (user_input == "c c"):
                            check_tables = """ SELECT name FROM sqlite_master """    
                          
                            Check_Tables(con, check_tables)
                          
                        elif (user_input == "r c"):
                            cls = input("\nWhich class: ")
                            remove_tables = f""" DROP TABLE IF EXISTS Class_{cls} """
                          
                            Insert_Update_Delete(con, remove_tables)
                            print(f"Class_{cls} removed")
                          
                        elif (user_input == "i"):
                            cls = input("\nWhich class: ")
                            n = input("Student Name: ")
                          
                            lOC = Get_Cls(con)              
                            c = con.cursor()
                          
                            for f in c.execute(""" SELECT nToE, ninth, matric From RaDin where name = 'month' """):
                                if (cls in lOC[0]):
                                    insert_values = f""" INSERT INTO Class_{cls} (name, recent, last1, last2, last3, last4, last5, last6, last7, last8, last9, last10, last11, last12, last13, last14, last15, last16, last17, last18, last19, last20, last21, last22, last23) VALUES ('{n}', '{f[2]}, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, '); """
                                    Insert_Update_Delete(con, insert_values)
                                    con.commit()
                                    print(f"{n} inserted")                             
                           
                                elif (cls in lOC[1]):
                                    insert_values = f""" INSERT INTO Class_{cls} (name, recent, last1, last2, last3, last4, last5, last6, last7, last8, last9, last10, last11, last12, last13, last14, last15, last16, last17, last18, last19, last20, last21, last22, last23) VALUES ('{n}', '{f[1]}, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, '); """
                                    Insert_Update_Delete(con, insert_values)
                                    con.commit()
                                    print(f"{n} inserted")
                                                           
                                else:
                                    insert_values = f""" INSERT INTO Class_{cls} (name, recent, last1, last2, last3, last4, last5, last6, last7, last8, last9, last10, last11, last12, last13, last14, last15, last16, last17, last18, last19, last20, last21, last22, last23) VALUES ('{n}', '{f[0]}, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, ', '0, '); """
                                    Insert_Update_Delete(con, insert_values)
                                    con.commit()
                                    print(f"{n} inserted")                                
                          
                        elif (user_input == "c"):
                            cls = input("\nWhich class: ")
                            n = input("Which student: ")
                            check_values = f""" SELECT * From Class_{cls} where name = '{n}' """
                          
                            Check(con, check_values)
            
                            while True:
                                u_i = input("  Any add or sub: ")
                                if (u_i == "e"):
                                    break
                                  
                                elif (u_i[0] == "-" or u_i[0] == "+"):
                                    co = input("  From: ")                                     
                                    col = MonthToCol(co)
                                  
                                    Addition_Subtraction(con, cls, u_i, n, col)
                              
                        elif (user_input == "c r"):
                            cls = input("\nWhich class: ")
                            n = input("Which student: ")
                            check_record = f""" SELECT * From Class_{cls} where name = '{n}' """
                          
                            Check_Record(con, check_record)
            
                            while True:
                                u_i = input("  Any add or sub: ")   
                                if (u_i == "e"):
                                    break
                                  
                                elif (u_i[0] == "-" or u_i[0] == "+"):  
                                    co = input("  From: ")                                     
                                    col = MonthToCol(co)
                                  
                                    Addition_Subtraction(con, cls, u_i, n, col)
                              
                        elif (user_input == "c d"):
                            cls = input("\nWhich class: ")
                            check_dues = f""" SELECT * From Class_{cls} ORDER BY NAME """
                          
                            Check_Dues(con, check_dues)
            
                            while True:
                                u_i = input("  Any add or sub: ")   
                                if (u_i == "e"):
                                    break
                                  
                                elif (u_i[0] == "-" or u_i[0] == "+"):
                                    n = input("  Which student: ")  
                                    co = input("  From: ")                                     
                                    col = MonthToCol(co)
                                  
                                    Addition_Subtraction(con, cls, u_i, n, col)        
                          
                        elif (user_input == "c a"):
                            cls = input("\nWhich class: ")
                            check_values = f""" SELECT * From Class_{cls} ORDER BY NAME """
                            
                            Check(con, check_values)
                          
                            while True:        
                                u_i = input("  Any add or sub: ")     
                                if (u_i == "e"):
                                    break
                                  
                                elif (u_i[0] == "-" or u_i[0] == "+"):
                                    n = input("  Which student: ")                
                                    co = input("  From: ")                                     
                                    col = MonthToCol(co)
                                  
                                    Addition_Subtraction(con, cls, u_i, n, col)             
                          
                        elif (user_input == "r"):
                            cls = input("\nWhich class: ")
                            n = input("Which student: ")
                            delete_values = f""" DELETE from Class_{cls} where name = '{n}' """
                          
                            Insert_Update_Delete(con, delete_values)
                            con.commit()
                            print(f"{n} removed")
                  
            else:
                print("Error! Id is incorrect.")
              
        else:
            print("Error! RaDin is not found.")
          
    else:
        print("Error! cannot create the database connection.")
    
if __name__ == '__main__':
    mainfunc()