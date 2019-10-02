import sqlite3

conn = sqlite3.connect('some.db')
c = conn.cursor()
c.execute('''CREATE TABLE files
(filename text, file blob)''')
c.close()
