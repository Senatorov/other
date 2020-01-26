import sqlite3

#--------------------------------CREATING DATABASE-----------------------------#

# sqliteConnection = sqlite3.connect('test_DataBase.db')
# cursor = sqliteConnection.cursor()                            #Conncets to the database
# print("Database created and Successfully Connected to SQLite")

#-------------------------------------------------------------------------------#


#------------------------------CREATING TABLE IN DATABASE-----------------------#

# con = sqlite3.connect('test_DataBase.db')
#
# cursorObj = con.cursor()
#
# cursorObj.execute("CREATE TABLE UsersInfo(Name TEXT,"
#                   "Password TEXT)")
#
# con.commit()

#-------------------------------------------------------------------------------#


#----------------------------ADD NEW INFO IN DATABASE----------------------------#

# con = sqlite3.connect('test_DataBase.db')
# cursorObj = con.cursor()
#
# cursorObj.execute('INSERT INTO UsersInfo VALUES("Nikolay","qwerty123")')
#
# con.commit()

# cursorObj.close()

#-------------------------------------------------------------------------------#


#----------------------------PRINT INFO FROM DATABASE----------------------------#
