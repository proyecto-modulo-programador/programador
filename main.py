from data_persistence.database import Database
from config.db_config import mydb
from data_persistence.menu import Menu

# Instancio una nueva DB con la config correspondiente
new_db = Database(mydb)

# Instancio y ejecuto el menú 
app_menu = Menu(new_db)
app_menu.run()