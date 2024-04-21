import sqlite3 as sql


def maker() -> None:
     with sql.connect('app.db') as db:
          cursor = db.cursor()
          
          cursor.execute("""CREATE TABLE IF NOT EXISTS reg(
               login STR,
               password INT
               )""")
          db.commit()
     cursor.close()
     
          

def login_check(login: str) -> bool:
     with sql.connect('app.db') as db:
          cursor = db.cursor()
          
          check = cursor.execute("SELECT login FROM reg WHERE login = ?", [login]).fetchone()
         
          if not check:
               return None   
          
          if check:
               return cursor.execute("SELECT password FROM reg WHERE login = ?", [login]).fetchone()[0]    
     cursor.close() 
     


def new_data(login: str, password: int) -> bool:
     with sql.connect('app.db') as db:
          cursor = db.cursor()
          
          cursor.execute("INSERT INTO reg(login) VALUES(?)", [login])
          cursor.execute("UPDATE reg SET password = ? WHERE login = ?", [password, login])
          db.commit()
     cursor.close()

