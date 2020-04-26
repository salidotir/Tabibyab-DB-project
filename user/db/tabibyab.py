from db.dbms import *
from ui.login_register import *
from ui.user_register_window import  *
from ui.main_window import *


dbfile = "db.sqlite"
conn = create_connection(dbfile)
create_all_tables(conn)
insert_instance(conn)

run_login_register_window()

conn.commit()
conn.close()


