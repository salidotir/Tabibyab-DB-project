import sqlite3
from sqlite3 import Error


def create_connection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Error as e:
        print(e)
    return conn


def close_connection(conn):
    conn.commit()
    conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_all_tables(conn):
    # tables
    gender = "create table if not exists gender (gender_id int not null primary key, title  nvarchar(50) not null);"
    insurance = "create table if not exists insurance ( insurance_id int not null primary key, name  nvarchar(50) not null);"
    user = "create table if not exists user (phone_number nvarchar(50) not null primary key,first_name nvarchar(50) not null, last_name nvarchar(50) not null, password nvarchar(50) not null, birth_day nvarchar(50), gender_id int not null references gender(gender_id),insurance_id int references insurance(insurance_id));"
    disease = "create table if not exists disease (disease_id int not null primary key, title nvarchar(50) not null);"
    address = "create table if not exists address (address_id int not null primary key, city nvarchar(50), street nvarchar(50), alley nvarchar(50), plaque nvarchar(50));"
    support = "create table if not exists support ( insurance_id int not null references insurance(insurance_id), disease_id int not null references disease(disease_id), discount_percent float default 0 not null);"
    specialty = "create table if not exists specialty (name nvarchar(50) not null, specialty_id int not null primary key );"
    appointment = "create table if not exists appointment (appointment_id int not null primary key, doh_id int references doh (doh_id), dhh_id int references dhh (dhh_id), payment_id int not null references payment(payment_id), medical_council_code int not null references doctor (medical_council_code), username nvarchar(50) not null references doctor (username), patient_phone_number nvarchar(50) not null references user (phone_number),getter_phone_number nvarchar(50) not null references user(phone_number),start_hour nvarchar(50) not null);"
    payment = "create table if not exists payment (payment_code int not null, payment_id int not null primary key); --cost will be computed later"
    doctor = "create table if not exists doctor (medical_council_code int not null, username nvarchar(50) not null, first_name nvarchar(50) not null, last_name nvarchar(50) not null, password nvarchar(50) not null, visit_price int not null, specialty_id int not null references specialty(specialty_id), primary key (medical_council_code,username));"
    doh = "create table if not exists doh (medical_council_code int not null references doctor(medical_council_code), username nvarchar(50) not null references doctor (username), doctor_office_id int not null references doctor_office(doctor_office_id), doh_id int not null primary key);"
    doctor_office = "create table if not exists doctor_office (phone_number nvarchar(50), doctor_office_id int not null primary key, address_id int not null references address(address_id));"
    is_family_of = "create table if not exists is_family_of( user_phone_number  nvarchar(50) not null references user(phone_number), family_phone_number nvarchar(50) not null references user(phone_number), primary key(family_phone_number,user_phone_number));"
    saved = "create table if not exists saved (phone_number nvarchar(50) not null references user(phone_number), medical_council_code int not null references doctor (medical_council_code), username nvarchar(50) not null references doctor (username), primary key (medical_council_code,username, phone_number));"
    in_contract_with = "create table if not exists in_contract_with (insurance_id int not null references insurance(insurance_id), medical_council_code int not null references doctor (medical_council_code), username nvarchar(50) not null references doctor (username), primary key(medical_council_code, username, insurance_id));"
    dhh = "create table if not exists dhh( medical_council_code  int not null references doctor (medical_council_code), username nvarchar(50) not null references doctor (username), health_care_center_id int not null references health_care_center (health_care_center_id) ,dhh_id  int not null primary key);"
    work_hour = "create table if not exists work_hour (work_hour_id int not null primary key, start_hour nvarchar(50) not null, end_hour nvarchar(50) not null, wh_year int, wh_month int, wh_day int, doh_id int references doh (doh_id), dhh_id int references dhh (dhh_id));"
    health_care_center = "create table if not exists health_care_center (phone_number nvarchar(50) not null, health_care_center_id int not null primary key, address_id int not null references address(address_id));"

    execute = [gender, insurance, user, disease, address, support, specialty, appointment, payment, doctor, doh,
               doctor_office, is_family_of, saved, in_contract_with, dhh, work_hour, health_care_center]

    for table in execute:
        create_table(conn, table)


def insert_instance(conn):
    # insurance instance
    # insurance_id, name
    conn.execute("insert into insurance values(1, 'Iran')")
    conn.execute("insert into insurance values(2, 'Moallem')")
    conn.execute("insert into insurance values(3, 'Tamin e ejtemaei')")
    conn.execute("insert into insurance values(4, 'Dana')")

    # disease instance
    # disease_id, title
    conn.execute("insert into disease values(1, 'Cancer')")
    conn.execute("insert into disease values(2, 'Liver Disease')")
    conn.execute("insert into disease values(3, 'Heart Disease')")
    conn.execute("insert into disease values(4, 'Diabetes mellitus')")

    # support instance
    # insurance_id, disease_is, discount
    conn.execute("insert into support values(1, 1, 0.1)")
    conn.execute("insert into support values(1, 2, 0.3)")
    conn.execute("insert into support values(1, 3, 0.2)")
    conn.execute("insert into support values(1, 4, 0.4)")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into support values(1, 1, 0.1)")
    conn.execute("insert into support values(1, 2, 0.3)")
    conn.execute("insert into support values(1, 3, 0.2)")
    conn.execute("insert into support values(1, 4, 0.4)")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into support values(1, 1, 0.1)")
    conn.execute("insert into support values(1, 3, 0.2)")
    conn.execute("insert into support values(1, 4, 0.4)")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into support values(1, 1, 0.1)")
    conn.execute("insert into support values(1, 2, 0.3)")
    conn.execute("insert into support values(1, 3, 0.2)")

    # gender instance
    # gender_id, title
    conn.execute("insert into gender values(0, 'female')")
    conn.execute("insert into gender values(1, 'male')")
    conn.execute("insert into gender values(2, 'other')")

    # user instance
    # phone_number, first_name, last_name, password, birthday, gender_id, insurance_id
    user_register(conn, '09170888747', 'sara', 'limooee', '4444', '1999-07-10', 0, 1)
    user_register(conn, '09364533444', 'golnaz', 'mesbahi', '1234h', '1999-07-19', 0, 1)
    user_register(conn, '09217220654', 'sana', 'sami', 'abcd', '1998-05-05', 1, 2)
    user_register(conn, '09171118747', 'Mohammad', 'Saberi', '445d', '1969-12-25', 1, 3)

    # specialty instance
    # name, specialty_id
    conn.execute("insert into specialty values('Cardiology',1)")
    conn.execute("insert into specialty values('Neurosurgery',2)")
    conn.execute("insert into specialty values('nutritionist',3)")
    conn.execute("insert into specialty values('pediatrician',4)")

    # doctor instance
    # medical_council_code, username, first_name, last_name, password, visit_price, specialty_id
    doctor_register(conn, 'bf123h', 'aliahmadi', 'Ali', 'Ahmadi', 'al1234', 10000, 1)
    doctor_register(conn, 'cd5t3h', 'akbarakbari', 'Akbar', 'Akbari', 'kb4321', 12000, 2)
    doctor_register(conn, 'fk5t64', 'fatemeketabi', 'Fateme', 'Ketabi', 'fkl1234', 6000, 1)
    doctor_register(conn, 'rnm644', 'reyhanenikooee', 'Reyhane', 'Nikooee', 'mn123', 35000, 3)
    doctor_register(conn, 'hs5rt7', 'alirezahosseini', 'Alireza', 'Hosseini', 'df5621', 40000, 4)

    # in_contract_with
    # insurance_id, medical_council_code, username
    conn.execute("insert into in_contract_with values(1, 'bf123h', 'aliahmadi')")
    conn.execute("insert into in_contract_with values(2, 'bf123h', 'aliahmadi')")
    conn.execute("insert into in_contract_with values(4, 'bf123h', 'aliahmadi')")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into in_contract_with values(1, 'cd5t3h', 'akbarakbari')")
    conn.execute("insert into in_contract_with values(2, 'cd5t3h', 'akbarakbari')")
    conn.execute("insert into in_contract_with values(3, 'cd5t3h', 'akbarakbari')")
    conn.execute("insert into in_contract_with values(4, 'cd5t3h', 'akbarakbari')")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into in_contract_with values(4, 'rnm644', 'reyhanenikooee')")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    conn.execute("insert into in_contract_with values(1, 'hs5rt7', 'alirezahosseini')")
    conn.execute("insert into in_contract_with values(2, 'hs5rt7', 'alirezahosseini')")
    conn.execute("insert into in_contract_with values(3, 'hs5rt7', 'alirezahosseini')")
    conn.execute("insert into in_contract_with values(4, 'hs5rt7', 'alirezahosseini')")

    # address
    # address_id, city, stree, alley, plaque
    conn.execute("insert into address values(1, 'Shiraz', 'Khalili', 'Golha', '23')")
    conn.execute("insert into address values(2, 'Esfahan', '33 pol', '4', '45')")
    conn.execute("insert into address values(3, 'Shiraz', 'Eram', '14', '13')")
    conn.execute("insert into address values(4, 'Tehran', 'Khalili', 'Golha', '3')")
    conn.execute("insert into address values(5, 'Shiraz', 'ghasroddasht', '72', '4')")
    conn.execute("insert into address values(6, 'Shiraz', 'Tachara', '8', '23')")

    # doctor_offic
    # phone_number, doctor_offic_id, address_id
    conn.execute("insert into doctor_office values('07136248970', 1, 2)")
    conn.execute("insert into doctor_office values('07137250547', 2, 5)")

    # health_care_center
    # phone_number, health_care_center_id, address_id
    conn.execute("insert into health_care_center values('07136253118', 1, 1)")
    conn.execute("insert into health_care_center values('07136246633', 2, 3)")
    conn.execute("insert into health_care_center values('07132345604', 3, 4)")
    conn.execute("insert into health_care_center values('07136253548', 4, 6)")

    # work_hour
    # work_hour_id, start_hour, end_hour, wh_year, wh_month, wh_day, doh_id, dhh_id
    conn.execute(
        "insert into work_hour(work_hour_id, start_hour, end_hour, wh_year, wh_month, wh_day, doh_id) values(1, '08:00', '12:00', 2020, 1, 23, 1)")
    conn.execute(
        "insert into work_hour(work_hour_id, start_hour, end_hour, wh_year, wh_month, wh_day, dhh_id) values(2, '12:00', '17:30', 2020, 1, 25, 1)")
    conn.execute(
        "insert into work_hour(work_hour_id, start_hour, end_hour, wh_year, wh_month, wh_day, doh_id) values(3, '10:45', '14:00', 2020, 1, 23, 2)")
    conn.execute(
        "insert into work_hour(work_hour_id, start_hour, end_hour, wh_year, wh_month, wh_day, dhh_id) values(4, '16:00', '20:00', 2020, 1, 24, 2)")

    # payment
    # payment_code, payment_id
    conn.execute("insert into payment values(1, 1)")

    # is_family_of
    # user_phone_number, family_phone_number
    add_family(conn, '09364533444', '09170888747', 'sara', 'limooee', '1999-07-10', 0, 1)

    # saved
    # phone_number, medical_council_code, username
    conn.execute("insert into saved values('09170888747', 'bf123h', 'aliahmadi')")

    # appointment
    # appointment_id, doh_id, dhh_id, payment_id, medical_council_code, username, patient_phone_number, getter_phone_number,start_hour
    conn.execute(
        "insert into appointment(appointment_id, doh_id, payment_id, medical_council_code, username, patient_phone_number, getter_phone_number,start_hour) values(1, 1, 1, 'bf123h', 'aliahmadi', '09170888747', '09364533444','08:00')")
    conn.execute(
        "insert into appointment(appointment_id, dhh_id, payment_id, medical_council_code, username, patient_phone_number, getter_phone_number,start_hour) values(2, 1, 1, 'bf123h', 'aliahmadi', '09170888747', '09170888747','12:30')")

    # doh
    # medical_council_code, username, doctor_office_id, doh_id
    conn.execute("insert into doh values('bf123h', 'aliahmadi', 1, 1)")
    conn.execute("insert into doh values('cd5t3h', 'akbarakbari', 2, 2)")

    # dhh
    # medical_council_code, username, health_care_center_id, dhh_id
    conn.execute("insert into dhh values('bf123h', 'aliahmadi', 1, 1)")
    conn.execute("insert into dhh values('cd5t3h', 'akbarakbari', 2, 2)")


def user_login(conn, password, phone_number):
    global current_logged_in
    current_logged_in = phone_number
    cursor = conn.execute("select * from user where phone_number = ? and password = ?", [phone_number, password])
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    return True


def user_register(conn, phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id):
    if if_user_exists(conn, phone_number) == False:
        conn.execute("insert into user values(?, ?, ?, ?, ?, ?, ?) ",
                    [phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id])
        conn.commit()
        print("user registered")
        return True
    print("user already exists")
    return False

def view_table(conn, table):
    cursor = conn.execute("select * from " + table)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows


def get_insurance_name(conn, insurance_id):
    cursor = conn.execute("select name from insurance where insurance_id = ? ", [insurance_id])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def get_gender_title(conn, gender_id):
    cursor = conn.execute("select title from gender where gender_id = ? ", [gender_id])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def get_specialty_name(conn, specialty_id):
    cursor = conn.execute("select name from specialty where specialty_id = ?", [specialty_id])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def show_profile(conn, phone_number):
    res = []
    sql = "select * from user where phone_number = ?"
    cursor = conn.execute(sql, [phone_number])
    data = cursor.fetchall()
    record = data[0]
    # get insurance name
    insurance_name = get_insurance_name(conn, record[6])
    # get gender title
    gender_title = get_gender_title(conn, record[5])
    res = res + [record[0], record[1], record[2], record[4], record[3], gender_title, insurance_name]
    return res


def edit_profile(conn, phone_number, first_name, last_name, password, birth_day, gender_id, insurance_id):
    conn.execute(
        "update user set first_name = ? ,last_name = ? , password = ? , birth_day =? , insurance_id = ? ,gender_id = ? where phone_number = ? ",
        [first_name, last_name, password, birth_day, insurance_id, gender_id, phone_number])
    print("edit done")
    conn.commit()
    return True


def add_family(conn, user_phone_number, family_phone_number, family_first_name, family_last_name, family_birth_day,
               family_gender_id, family_insurance_id):
    cursor = conn.execute("select * from user where phone_number = ?", [family_phone_number])
    data = cursor.fetchall()
    if len(data) == 0:
        forbidden_password = "@@@@"
        user_register(conn, family_phone_number, family_first_name, family_last_name, forbidden_password,
                      family_birth_day, family_gender_id, family_insurance_id)
        conn.execute("insert into is_family_of values(?,?)", [user_phone_number, family_phone_number])
    else:
        conn.execute("insert into is_family_of values(?,?)", [user_phone_number, family_phone_number])


def doctor_login(conn, medical_council_code, password):
    global current_logged_in
    current_logged_in = medical_council_code
    cursor = conn.execute("select * from doctor where medical_council_code = ? and password = ?",
                          [medical_council_code, password])
    print(medical_council_code, password)
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        return False
    return True


def doctor_register(conn, medical_council_code, user_name, first_name, last_name, password, visit_price, specialty_id):
    # specialty comes from table specialty
    conn.execute("insert into doctor values(?, ?, ?, ?, ?, ?, ?)",
                 [medical_council_code, user_name, first_name, last_name, password, visit_price, specialty_id])
    conn.commit()
    return True


def view_all_doctors_personal_informations(conn):
    sql = "select * from doctor, specialty where doctor.specialty_id = specialty.specialty_id"
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return data

def get_visit_price(conn, medical_council_code):
    sql = "select visit_price from doctor where medical_council_code = ?"
    cursor = conn.execute(sql, [medical_council_code])
    data = cursor.fetchall()
    return data[0]


def view_doctor_personal_information(conn, medical_council_code):
    sql = "select * from doctor, specialty on doctor.specialty_id = specialty.specialty_id and doctor.medical_council_code = ?"
    cursor = conn.execute(sql, [medical_council_code])
    data = cursor.fetchall()
    res = "medical_code |  first_name |  last_name | visit_price |  specialty\n\n"
    for row in data:
        name = get_doctor_name(conn,str(row[0]))
        cost = get_visit_price(conn,str(row[0]))
        res += str(row[0]) +" "+ name[0]+" "+ name[1]+" " + str(cost[0]) + " " + get_specialty_name(conn, row[6]) + '\n' 

    return res


def search_doctors_based_on_first_name(conn, first_name):
    sql = "select doctor.medical_council_code, doctor.first_name, doctor.last_name, doctor.visit_price, specialty.name from doctor, specialty where doctor.specialty_id = specialty.specialty_id and  first_name like '%" + first_name + "%'"
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    res = "medical_code |  first_name |  last_name | visit_price |  specialty\n\n"
    for row in data:
        res += str(row[0]) + " " + row[1] + " " + row[2] +" " + str(row[3]) + " " + row[4] +'\n'
    return res


def search_doctors_based_on_last_name(conn, last_name):
    sql = "select doctor.medical_council_code, doctor.first_name, doctor.last_name, doctor.visit_price, specialty.name from doctor, specialty where doctor.specialty_id = specialty.specialty_id and  last_name like '%" + last_name + "%'"
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    res = "medical_code |  first_name |  last_name | visit_price |  specialty\n\n"
    for row in data:
        res += str(row[0]) + " " + row[1] + " " + row[2] + " " + str(row[3]) + " " + row[4] + '\n'
    return res


def search_doctors_based_on_specialty_id(conn, specialty_name):
    specialty_id = get_specialty_id(conn,specialty_name)
    sql = "select doctor.medical_council_code, doctor.first_name, doctor.last_name, doctor.visit_price from doctor where specialty_id = ?"
    cursor = conn.execute(sql, [specialty_id])
    data = cursor.fetchall()
    res = "medical_code |  first_name |  last_name | visit_price |  specialty\n\n"
    for row in data:
        res += str(row[0]) + " " + row[1] + " " + row[2] + " " + str(row[3]) + " " + specialty_name+ '\n'
    return res


def search_doctors_based_on_city(conn,city):
    sql = "select doctor.medical_council_code, doctor.first_name, doctor.last_name, doctor.visit_price, specialty.name from doctor, specialty where doctor.specialty_id = specialty.specialty_id and medical_council_code in (select medical_council_code from doh, doctor_office, address where city = ? and address.address_id = doctor_office.address_id and doh.doctor_office_id = doctor_office.doctor_office_id union select medical_council_code from dhh, health_care_center, address where city = ? and address.address_id = health_care_center.address_id and dhh.health_care_center_id= health_care_center.health_care_center_id)"
    cursor = conn.execute(sql, [city,city])
    data = cursor.fetchall()
    res = "medical_code |  first_name |  last_name | visit_price |  specialty\n\n"
    for row in data:
        res += str(row[0]) + " " + row[1] + " " + row[2] + " " + str(row[3]) + " " + row[4] + '\n'
    return res


def docotrs_of_a_medical_center(conn, health_care_center_phone_number):
    sql = "select * from doctor where medical_council_code in( select medical_council_code from dhh where health_care_center_id in" \
          "(select health_care_center_id from health_care_center where phone_number =? ))"
    cursor = conn.execute(sql, [health_care_center_phone_number])
    data = cursor.fetchall()
    for row in data:
        print(row)
    return data


def docotrs_of_all_medical_centers(conn):
    sql = "select * from doctor where medical_council_code in(select medical_council_code from dhh ) "
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    return data


def get_insurance_id(conn, name):
    cursor = conn.execute("select insurance_id from insurance where name = ? ", [name])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def get_gender_id(conn, title):
    cursor = conn.execute("select gender_id from gender where title = ? ", [title])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def get_specialty_id(conn, name):
    cursor = conn.execute("select specialty_id from specialty where name = ? ", [name])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0][0]


def if_user_exists(conn, phone_nume):
    cursor = conn.execute("select * from user where phone_number = ?", [phone_nume])
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    return True


def if_saved_exists(conn, phone_number, medical_council_code, username):
    sql = "select * from saved where phone_number = ? and medical_council_code = ? and username = ?"
    cursor = conn.execute(sql, [phone_number, medical_council_code, username])
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    return True


def save_doctor(conn, phone_number, medical_council_code):
    username = get_doctor_name(conn,medical_council_code)[2]
    res = if_saved_exists(conn, phone_number, medical_council_code, username)
    if res == False:
        sql = "insert into saved values(?, ?, ?)"
        conn.execute(sql, [phone_number, medical_council_code, username])
        conn.commit()
        return "Doctor saved."
    else:
        return "Already saved this doctor."


def get_saved_doctors(conn, user_phone_number):
    sql = "select medical_council_code from saved where phone_number = ?"
    cursor = conn.execute(sql, [user_phone_number])
    data = cursor.fetchall()
    if len(data)!=0:
        medical_council_code = data[0][0]
        return view_doctor_personal_information(conn, medical_council_code)
    return "there is no saved doctors"


def get_last_id_inserted(conn, primary_key, table_name):
    sql = "select * from (select " + primary_key + " from " + table_name + " order by " + primary_key + " desc) limit 1"
    print(sql)
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    return data[0][0]


# appointments you got for your family
def view_family_appointments(conn, user_phone_number):
    sql = "select * from appointment where patient_phone_number <> ? and getter_phone_number = ?"
    cursor = conn.execute(sql, [user_phone_number, user_phone_number])
    data = cursor.fetchall()
    res = "id | cost | medical_code | doctor_first_name | doctor_last_name | place | time | patient_first_name | patient_last_name | patient_phone_number  \n\n"
    for row in data:
        cost = get_cost(conn, int(row[3]))
        place = get_place(conn, row[1], row[2])
        patient = show_profile(conn, str(row[6]))
        res += str(row[0]) + " " + str(cost) + " " + row[4] + " " + get_doctor_name(conn, str(row[4]))[0] + " " + \
               get_doctor_name(conn, str(row[4]))[1] + " " + str(place) + " "+ row[8]+ patient[1]+" " + patient[2] +" " + patient[0]+'\n'
    return res


# appointments you got for yourself
def view_your_appointments(conn, user_phone_number):
    sql = "select * from appointment where patient_phone_number = ? and getter_phone_number = ?"
    cursor = conn.execute(sql, [user_phone_number, user_phone_number])
    data = cursor.fetchall()
    res ="id | cost | medical_code | doctor_first_name | doctor_last_name | place | time \n\n"
    for row in data:
        cost = get_cost(conn,int(row[3]))
        place =get_place(conn,row[1],row[2])
        res += str(row[0])+" " +str(cost)+" "+row[4]+" "+get_doctor_name(conn,str(row[4]))[0]+" " +get_doctor_name(conn,str(row[4]))[1]+" " +str(place)+" " + row[8]+'\n'

    return res

def get_cost(conn,payment_id):
    sql = "select visit_price from payment,appointment,doctor where payment.payment_id = appointment.payment_id and appointment.medical_council_code = doctor.medical_council_code and appointment.username = doctor.username and payment.payment_id = ?"
    cursor = conn.execute(sql,[payment_id])
    data = cursor.fetchall()
    return data[0][0]


def get_place(conn,doh_id,dhh_id):
    if dhh_id == None:
        sql = "select city,street,alley,plaque from address,doctor_office,doh where address.address_id = doctor_office.address_id and doh.doctor_office_id = doctor_office.doctor_office_id and doh.doh_id =?"
        cursor = conn.execute(sql,[int(doh_id)])

    elif doh_id == None:
        sql = "select city,street,alley,plaque from address,health_care_center,dhh where address.address_id = health_care_center.address_id and dhh.health_care_center_id = health_care_center.health_care_center_id and dhh.dhh_id =?"
        cursor = conn.execute(sql, [int(dhh_id)])
    data= cursor.fetchall()
    return data[0]


def get_doctor_name(conn,medical_council_code):
    sql = "select first_name,last_name,username from doctor where medical_council_code = ?"
    cursor = conn.execute(sql,[medical_council_code])
    data =cursor.fetchall()
    return data[0]


def get_doctor_specialty(conn,doctor_code):
    sql ="select name from doctor,specialty where doctor.specialty_id = specialty.specialty_id and doctor.medical_council_code = ?"
    cursor = conn.execute(sql,[doctor_code])
    data = cursor.fetchall()
    return data[0][0]

# appointments your family got for you
def view_other_appointments(conn, user_phone_number):
    sql = "select * from appointment where patient_phone_number = '" + user_phone_number + "' and getter_phone_number <> '" + user_phone_number + "'"
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    res = "id | cost | medical_code | doctor_first_name | doctor_last_name | place| time  | getter_first_name | getter_last_name | getter_phone_number \n\n"
    for row in data:
        cost = get_cost(conn, int(row[3]))
        place = get_place(conn, row[1], row[2])
        patient = show_profile(conn, str(row[7]))
        res += str(row[0]) + " " + str(cost) + " " + row[4] + " " + get_doctor_name(conn, str(row[4]))[0] + " " + \
               get_doctor_name(conn, str(row[4]))[1] + " " + str(place) + " " +row[8]+ ' '+ patient[1] + " " + patient[2] + " " + \
               patient[0] + '\n'

    return res

def get_doctor_office_phone_number(conn, doctor_office_id):
    sql = "select phone_number from doctor_office where doctor_office_id = ?"
    cursor = conn.execute(sql, [doctor_office_id])
    data = cursor.fetchall()
    return data[0][0]

def get_working_hour(conn,doctor_code):
    res = "doctor_office times:\n\n"
    res += "medical_code | first_name | last_name | specialty | start_hour | end_hour | date | address | telephone\n\n"
    sql ="select medical_council_code,start_hour,end_hour,city,street,alley,plaque,phone_number,wh_year,wh_month,wh_day from doh,doctor_office,address,work_hour where doh.medical_council_code = '" + doctor_code + "' and doh.doh_id = work_hour.doh_id and doh.doctor_office_id = doctor_office.doctor_office_id and doctor_office.address_id = address.address_id"
    print(sql)
    cursor = conn.execute(sql)
    data = cursor.fetchall()
    for row in data:
        medical_code = row[0]
        doctor_name=get_doctor_name(conn,medical_code)
        specialty= get_doctor_specialty(conn,medical_code)
        res += row[0] + " " + str(doctor_name[0]) + " "+ str(doctor_name[1])+" " + specialty +" "+ row[1]+ " " + row[2] + " " + str(row[8]) + "-" + str(row[9]) + "-" + str(row[10]) + " " + " (" +row[3]+", "+row[4]+", "+row[5]+", " +row[6] +') ' + row[7] + '\n'

    res += "\nhealth_care_center_times:\n\n"
    res += "medical_code | first_name | last_name | specialty | start_hour | end_hour | date | address | telephone\n\n"
    sql1 = "select medical_council_code,start_hour,end_hour,city,street,alley,plaque,phone_number,wh_year,wh_month,wh_day from dhh,health_care_center,address,work_hour where dhh.medical_council_code = '" + doctor_code + "' and dhh.dhh_id = work_hour.dhh_id and dhh.health_care_center_id = health_care_center.health_care_center_id and health_care_center.address_id = address.address_id"
    cursor = conn.execute(sql1)
    data = cursor.fetchall()
    for row in data:
        medical_code = row[0]
        doctor_name=get_doctor_name(conn,medical_code)
        specialty= get_doctor_specialty(conn,medical_code)
        res += row[0] + " " + str(doctor_name[0]) + " "+ str(doctor_name[1])+" " + specialty +" "+ row[1]+ " " + row[2] + " " + str(row[8]) + "-" + str(row[9]) + "-" + str(row[10]) + " " + " (" +row[3]+", "+row[4]+", "+row[5]+", " +row[6] +') ' + row[7] + '\n'
    
    return res

def show_doctor_profile(conn, medical_council_code):
    res = ["medical_code | user_name | first_name | last-name | password | visit_price | specialty"]
    sql = "select * from doctor where medical_council_code = ?"
    cursor = conn.execute(sql, [medical_council_code])
    data = cursor.fetchall()
    record = data[0]
    # get specialty name
    specialty = get_specialty_name(conn,record[6])
    res = res + [record[0], record[1], record[2], record[3], record[4], record[5],specialty]
    return res


def edit_doctor_profile(conn,medical_code,username,first_name,last_name,password,visit_price,specialty_name):
    sql ="update doctor set username =?, first_name = ? , last_name = ? ,password = ?, visit_price = ? , specialty_id = ? where medical_council_code =? "
    specialty_id = get_specialty_id(conn,specialty_name)
    conn.execute(sql,[username,first_name,last_name,password,visit_price,int(specialty_id),medical_code])
    conn.commit()
    print("edit done")
    return True


def see_patients_of_a_doctor(conn,medical_council_code):
    sql ="select * from user where phone_number in(select phone_number from appointment where appointment.medical_council_code= ?)"
    cursor = conn.execute(sql,[medical_council_code])
    data = cursor.fetchall()
    #TODO:insert the appointment time
    res = "phone_number | first_name  | last_name | birth_day  | gender | insurance \n\n"
    for row in data:
        gender = get_gender_title(conn,row[5])
        insurance=get_insurance_name(conn,row[6])
        res =res + row[0]+" "+ row[1]+" "+row[2]+" "+row[4]+" "+gender +" "+ insurance+'\n'
    if res == "phone_number | first_name  | last_name | birth_day  | gender | insurance \n\n":
        res = "you have no patients"
    return res

def follow_appointment_info(conn, appointment_id, phone_number):
    sql = "select * from appointment where appointment_id = ? and (appointment.patient_phone_number = ? or appointment.getter_phone_number = ?)"
    cursor = conn.execute(sql, [appointment_id, phone_number, phone_number])
    data = cursor.fetchall()
    res = "id | cost | medical_code | doctor_first_name | doctor_last_name | place| time | getter_phone_number | patient_phone_number\n\n"
    for row in data:
        cost = get_cost(conn, int(row[3]))
        place = get_place(conn, row[1], row[2])
        getter = show_profile(conn, str(row[7]))
        patient = show_profile(conn, str(row[6]))
        res += str(row[0]) + " " + str(cost) + " " + row[4] + " " + get_doctor_name(conn, str(row[4]))[0] + " " + \
               get_doctor_name(conn, str(row[4]))[1] + " " + str(place) + " " +row[8]+ " " + getter[0] + " " + patient[0] + '\n'
    return res

import random
from random import randrange
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# ~~~~~~~~~~~~~~~~~~~~~~ NOT TESTED ~~~~~~~~~~~~~~~~~~~~~~~~

def get_doh_id(conn, medical_council_code):
    sql = "select doh_id from doh where medical_council_code = ?"
    cursor = conn.execute(sql, [medical_council_code])
    return cursor.fetchall()[0][0]


def get_dhh_id(conn, medical_council_code):
    sql = "select dhh_id from dhh where medical_council_code = ?"
    cursor = conn.execute(sql, [medical_council_code])
    return cursor.fetchall()[0][0]


def make_appointment(conn, doh_or_dhh, medical_council_code, patient_phone_number, getter_phone_number, start_hour):
    # cost will be computed whenever it is needed
    username = get_doctor_name(conn, medical_council_code)[2]
    payment_code =randrange(100000)
    new_appointment_id = get_last_id_inserted(conn, 'appointment_id', 'appointment') + 1
    new_payment_id = get_last_id_inserted(conn, 'payment_id', 'payment')

    # add to payment table
    conn.execute("insert into payment values(?, ?)", [new_payment_id, payment_code])

    doh_id = get_doh_id(conn, medical_council_code)
    dhh_id = get_dhh_id(conn, medical_council_code)

    # if appointment reserved from doctor office
    if doh_or_dhh == 'doh':
        conn.execute(
            "insert into appointment(appointment_id, doh_id, payment_id, medical_council_code, username, patient_phone_number, getter_phone_number,start_hour) values(?, ?, ?, ?, ?, ?, ?, ?)",
            [new_appointment_id, doh_id, new_payment_id, medical_council_code, username, patient_phone_number,
             getter_phone_number, start_hour])
    # # if appointment reserved from health care center
    elif doh_or_dhh == 'dhh':
        conn.execute(
            "insert into appointment(appointment_id, dhh_id, payment_id, medical_council_code, username, patient_phone_number, getter_phone_number,start_hour) values(?, ?, ?, ?, ?, ?, ?, ?)",
            [new_appointment_id, dhh_id, new_payment_id, medical_council_code, username, patient_phone_number,
             getter_phone_number, start_hour])

    res = "appointment reserved for:"
    res += follow_appointment_info(conn, new_appointment_id, getter_phone_number)
    res += '\n\nYour appointment id is : ' + str(new_appointment_id)
    conn.commit()
    return res


def is_start_hour_valid(conn, medical_council_code, doh_or_dhh, start_hour):
    if doh_or_dhh == 'doh':
        doctors_available_times = get_docotor_start_end_hour(conn, medical_council_code)
        doh_start = doctors_available_times[0]
        doh_end = doctors_available_times[1]
        lst_all_doh_available = set(make_list_of_available_start_hours(doh_start, doh_end))
        lst_reserved_times = set(make_list_of_reserved_start_hours_doh(conn, medical_council_code))
        doh_empty = list(lst_all_doh_available - lst_reserved_times)

        for i in range(len(doh_empty)):
            if (doh_empty[i] == start_hour):
                return True
        return False

    elif doh_or_dhh == 'dhh':

        doctors_available_times = get_docotor_start_end_hour(conn, medical_council_code)

        dhh_start = doctors_available_times[2]
        dhh_end = doctors_available_times[3]
        lst_all_dhh_available = set(make_list_of_available_start_hours(dhh_start, dhh_end))
        lst_reserved_times = set(make_list_of_reserved_start_hours_dhh(conn, medical_council_code))
        dhh_empty = list(lst_all_dhh_available - lst_reserved_times)

        for i in range(len(dhh_empty)):
            if (dhh_empty[i] == start_hour):
                return True
        return False


def count_digits(num):
    count =0
    while num> 0:
        num = num // 10
        count += 1
    return count

def organize_number(num):
    if count_digits(num)==1 or num==0:
        num = str('0')+str(num)
    else:
        num = str(num)
    return num


def add_15(start_hour):

    start_saat =int(start_hour[0:2])
    start_degh = int(start_hour[3:5])
    if start_degh != 45:
        start_degh +=15
    else:
        start_degh =0
        start_saat += 1
    return organize_number(start_saat)+":"+organize_number(start_degh)


def make_list_of_available_start_hours(start_hour,end_hour):
    # start_saat =int(start_hour[0:2])
    # start_degh = int(start_hour[3:5])
    # end_saat = int(end_hour[0:2])
    # end_degh = int(end_hour[3:5])
    lst = []
    # while start_saat<end_saat:
    #     if start_degh<=end_degh:
    #         while start_degh!=60:
    #             added = organize_number(start_saat)+':'+organize_number(start_degh)
    #
    #             lst+=[added]
    #             start_degh+=15
    #         start_saat+=1
    #         start_degh=0

    added = start_hour
    while added!= end_hour:
        added = add_15(added)
        lst+=[added]

    return lst[:len(lst)-1]


def make_list_of_reserved_start_hours_doh(conn,medical_council_code):
    sql = "select start_hour from appointment where appointment.medical_council_code =? and appointment.dhh_id is null"
    cursor = conn.execute(sql,[medical_council_code])
    data = cursor.fetchall()
    if len(data) !=0:
        return data[0]
    return []


def make_list_of_reserved_start_hours_dhh(conn, medical_council_code):
    sql = "select start_hour from appointment where appointment.medical_council_code =? and appointment.doh_id is null"
    cursor = conn.execute(sql, [medical_council_code])
    data = cursor.fetchall()
    if len(data) != 0:
        return data[0]
    return []


def get_docotor_start_end_hour(conn,medical_council_cod):
    sql ="select start_hour, end_hour from work_hour,doh where work_hour.doh_id = doh.doh_id and doh.medical_council_code = ? "
    cursor = conn.execute(sql,[medical_council_cod])
    data1 = cursor.fetchall()
    if len(data1)!=0:
        data = data1[0]
        sql = "select start_hour, end_hour from work_hour,dhh where work_hour.dhh_id = dhh.dhh_id and dhh.medical_council_code = ? "
        cursor = conn.execute(sql, [medical_council_cod])
        data2 = cursor.fetchall()[0]
        # doh start hour, doh end hour, dhh start hour, dhh end hour
        result = [data[0],data[1],data2[0],data2[1]]
        return result
    return []

def get_doctor_office_address(conn,medical_council_code):
    sql= "select city,street,alley,plaque from address,doctor_office,doh where doh.medical_council_code = ? and doh.doctor_office_id= doctor_office.doctor_office_id and doctor_office.address_id = address.address_id"
    cursor = conn.execute(sql,[medical_council_code])
    return str(cursor.fetchall()[0])

def get_doctor_health_care_center_address(conn,medical_council_code):
    sql = "select city,street,alley,plaque from address,health_care_center,dhh where dhh.medical_council_code = ? and dhh.health_care_center_id = health_care_center.health_care_center_id and health_care_center.address_id = address.address_id"
    cursor = conn.execute(sql, [medical_council_code])
    return str(cursor.fetchall()[0])

def show_all_available_empty_times(conn,medical_council_code):
    global doh_empty_first
    global dhh_empty_first
    res = "doctor_office all empty times --> address: "
    res += get_doctor_office_address(conn,medical_council_code)
    res += "\ntimes: \n"
    doctors_available_times = get_docotor_start_end_hour(conn, medical_council_code)
    doh_start = doctors_available_times[0]
    doh_end = doctors_available_times[1]
    lst_all_doh_available =set(make_list_of_available_start_hours(doh_start, doh_end))
    lst_reserved_times =set(make_list_of_reserved_start_hours_doh(conn, medical_council_code))
    doh_empty=list(lst_all_doh_available - lst_reserved_times)
    doh_empty.sort()
    doh_empty_first = doh_empty[0]

    res += str(doh_empty) + '\n\n'

    res += "health_care_center all empty times --> address: "
    res += get_doctor_health_care_center_address(conn,medical_council_code)
    res += "\ntimes:\n"
    doctors_available_times = get_docotor_start_end_hour(conn, medical_council_code)
    dhh_start = doctors_available_times[2]
    dhh_end = doctors_available_times[3]
    lst_all_dhh_available = set(make_list_of_available_start_hours(dhh_start, dhh_end))
    lst_reserved_times = set(make_list_of_reserved_start_hours_dhh(conn, medical_council_code))
    dhh_empty = list(lst_all_dhh_available - lst_reserved_times)
    dhh_empty.sort()
    dhh_empty_first = dhh_empty[0]

    res += str(dhh_empty)

    return res

def show_first_available_empty_time(conn,medical_council_code):
    res = ""
    result= show_all_available_empty_times(conn,medical_council_code)
    if dhh_empty_first < doh_empty_first :
        res += "first available empty time at health care center --> address: "
        res += get_doctor_health_care_center_address(conn,medical_council_code)
        res += "\ntime:  "
        res +=dhh_empty_first
    else:
        res += "first available empty time at doctor office  --> address: "
        res += get_doctor_office_address(conn,medical_council_code)
        res += "\ntime:  "
        res += doh_empty_first
    return res





def main():
    database = "db.sqlite"
    conn = create_connection(database)
    if conn is not None:
        create_all_tables(conn)
    else:
        print("error!")
