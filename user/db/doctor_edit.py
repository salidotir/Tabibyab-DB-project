from db.dbms import *
import os


def menu():
    menu_item = "1.register doctor\n2.edit doctor\n3.add insurance\n4.delete insurace\n5.edit work hour"
    choice = 0
    while choice != 11:
        print("\n\n**********Menu**********\n")
        print(menu_item)
        choice = input("\nplease choose what to do: ")

        global conn
        conn = create_connection("db.sqlite")

        if choice == '1':
            medical_council_code =input("medical_counicl_code")
            user_name= input("user_name")
            first_name = input("first_name")
            last_name = input("last_name")
            password = input("password")
            visit_price = input("visit_price")
            specialty =input("specialty1")
            specialty_id = get_specialty_id(conn,specialty)
            print(doctor_register(conn, medical_council_code, user_name, first_name, last_name, password, visit_price,specialty_id))
            conn.commit()
            view_table(conn,'doctor')
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '2':
            medical_code = input("medical_counicl_code")
            username = input("user_name")
            first_name = input("first_name")
            last_name = input("last_name")
            password = input("password")
            visit_price = input("visit_price")
            specialty_name = input("specialty1")
            print(edit_doctor_profile(conn, medical_code, username, first_name, last_name, password, visit_price,specialty_name))
            conn.commit()
            view_table(conn, 'doctor')
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '3':
            medical_council_code = input("medical_counicl_code")
            insurance_name= input("insurance name")
            print( doctor_add_insurance(conn, medical_council_code, insurance_name))
            conn.commit()
            view_table(conn, 'in_contract_with')
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '4':
            medical_council_code = input("medical_counicl_code")
            insurance_name = input("insurance name")
            print(doctor_delete_insurance(conn, medical_council_code, insurance_name))
            conn.commit()
            view_table(conn, 'in_contract_with')
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        elif choice == '5':
            medical_council_code = input("medical_counicl_code")
            start_hour =input("start h")
            end_hour = input("end_hour")
            place = input("place'")
            wh_year =input("y")
            wh_month =input("m")
            wh_day =input("day")


            print(doctor_edit_work_hour(conn, medical_council_code, start_hour, end_hour, place, wh_year, wh_month, wh_day))
            conn.commit()

            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            continue

        else:
            print("invalid input!")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
menu()