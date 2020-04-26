from dbms import *
from admin import *


dbfile = "db.sqlite"
conn = create_connection(dbfile)
create_all_tables(conn)
# insert_instance(conn)
# run_login_register_window()

menu()

# edit_healt_care_center_work_hour(conn, "bf123h", "09:45", "12:30")
# view_table(conn, 'work_hour')

conn.commit()
conn.close()


