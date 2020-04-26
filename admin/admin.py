from dbms import *
import os

def menu():
    menu_item = "1. register admin\n2. add new doctor\n3. delete a doctor\n4. edit a doctor\n5. add a user\n6. delete a user\n7. edit a user\n8. add new health care center\n9. add new doctor_office\n10. add new insurance\n11. view table\n12. edit a doctor work hour\n13. sign out admin\n"

    choice = 0
    while choice!=11:
        print("\n\n**********Menu**********\n")
        print(menu_item)
        choice = input("\nplease choose what to do: ")

        global conn
        conn = create_connection('db.sqlite')

        if choice == '1':
            dbfile = input("enter datbase file path: ")
            conn = admin_register(dbfile)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '2':
            medical_council_code = input("enter medical_council_code: ")
            user_name = input("enter username: ")
            first_name = input("enter first_name: ")
            last_name = input("enter last_name: ")
            password = input("enter pasword: ")
            visit_price = int(input("enter visit_price: "))
            specialty = input("enter specialty: ")
            add_new_doctor(conn, medical_council_code, user_name, first_name, last_name, password, visit_price, specialty)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '3':
            print("Not completed")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        
        elif choice == '4':
            medical_code = input("enter new_medical_council_code: ")
            username = input("enter new_username: ")
            first_name = input("enter new_first_name: ")
            last_name = input("enter new_last_name: ")
            password = input("enter new_pasword: ")
            visit_price = int(input("enter new_visit_price: "))
            specialty = input("enter new_specialty: ")
            update_doctor_profile(conn, medical_code,username,first_name,last_name,password,visit_price,specialty)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        
        elif choice == '5':
            phone_number = input("enter phone_numer: ")
            first_name = input("enter first_name: ")
            last_name = input("enter last_name: ")
            password = input("enter password: ")
            birth_day = input("enter birthday: ")
            gender = input("enter gender(female, male, other): ")
            insurance = input("enter insurance: ")
            add_new_user(conn, phone_number, first_name, last_name, password, birth_day, gender, insurance)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        
        elif choice == '6':
            phone_number = input("enter user phone number you want to delete: ")
            delete_a_user(conn, phone_number)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        
        elif choice == '7':
            phone_number = input("enter phone_numer you want to change informations: ")
            first_name = input("enter new_first_name: ")
            last_name = input("enter new_last_name: ")
            password = input("enter new_password: ")
            birth_day = input("enter new_birthday: ")
            gender = input("enter new_gender(female, male, other): ")
            insurance = input("enter new_insurance: ")
            gender_id = get_gender_id(conn, gender)
            insurance_id = get_insurance_id(conn, insurance)
            edit_profile(conn, phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id)
            
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '8':
            print("Not completed")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '9':
            print("Not completed")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '10':
            insurance = input("enter insurance name: ")
            add_insurance(conn, insurance)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '11':
            table = input("enter table name:")
            view_table(conn, table)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '12':
            sub_menu_item = "1. edit doctor_office work hour\n2. edit health_care_center work hour\n"
            print(sub_menu_item)
            print("select type of your edit: ")
            choice1 = input()

            medical_code = input("enter medical_council_code: ")
            new_start_hour = input("enter new start_hour: ")
            new_end_hour = input("enter new end_hour: ")

            if choice1 == '1':
                edit_doctor_office_work_hour(conn, medical_code, new_start_hour, new_end_hour)
                
            elif choice1 == '2':
                edit_healt_care_center_work_hour(conn, medical_code, new_start_hour, new_end_hour)

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '13':
            admin_sign_out(conn)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            break
        else:
            print("invalid input!")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue
        

def admin_register(dbfile):     # admin will call it once at first for making the whole database
    print("creating connection...")
    conn = create_connection(dbfile)
    print("creating tables...")
    create_all_tables(conn)
    return conn

def admin_sign_out(conn):
    print("connection is closing...")
    close_connection(conn)

def add_new_doctor(conn, medical_council_code, user_name, first_name, last_name, password, visit_price, specialty):
    specialty_id = get_specialty_id(conn, specialty)
    doctor_register(conn, medical_council_code, user_name, first_name, last_name, password, visit_price, specialty_id)

def update_doctor_profile(conn, medical_code,username,first_name,last_name,password,visit_price,specialty_name):
    edit_doctor_profile(conn, medical_code,username,first_name,last_name,password,visit_price,specialty_name)
    
# def delete_a_doctor(conn, medical_council_code, username):
    # delete all related records from doctor & doh & dhh & working_hour & address & doctor_office & hea;th_care_center

def add_new_user(conn, phone_number, first_name, last_name, password, birth_day, gender, insurance):
    gender_id = get_gender_id(conn, gender)
    insurance_id = get_insurance_id(conn, insurance)
    if if_user_exists(conn, phone_number) == True:
        user_register(conn, phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id)
        print("user added")
    print("current user already exists")

def update_user_profile(conn, phone_number, first_name, last_name, password, birth_day, gender, insurance):
    gender_id = get_gender_id(conn, gender)
    insurance_id = get_insurance_id(conn, insurance)
    edit_profile(conn, phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id)

def delete_a_user(conn, phone_number):
    sql = "delete from user where phone_number = ?"
    conn.execute(sql, [phone_number])
    conn.commit()
    print("user deleted")

def add_new_health_care_center(conn):

    conn.commit()
    pass

def add_new_doctor_office(conn):

    conn.commit()
    pass

def edit_doctor_office_work_hour(conn, medical_code, new_start_hour, new_end_hour):
    sql = "update work_hour set start_hour = ? , end_hour = ? where doh_id in (select doh_id from doh where medical_council_code = ?)"
    conn.execute(sql, [new_start_hour, new_end_hour, medical_code])
    conn.commit()
    pass

def edit_healt_care_center_work_hour(conn, medical_code, new_start_hour, new_end_hour):
    sql = "update work_hour set start_hour = ? , end_hour = ? where dhh_id in (select dhh_id from dhh where medical_council_code = ?)"
    conn.execute(sql, [new_start_hour, new_end_hour, medical_code])
    conn.commit()
    pass

def add_insurance(conn, insurance_name):
    insurance_id = get_last_id_inserted(conn, 'insurance_id', 'insurance') + 1
    sql = "insert into insurance values(?, ?)"
    conn.execute(sql, [insurance_id, insurance_name])
    conn.commit()
    pass