import sys
import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="root", # your password
db="push",
cursorclass=MySQLdb.cursors.DictCursor) # name of the data base

part1    = str(sys.argv[1])
split    = part1.split('@')
sender   = split[0]

message1 = str(sys.argv[2:]).replace("', '"," ")
message2 = message1.replace("['","")
message  = message2.replace("']","")

cur = db.cursor()
cur.execute("""
INSERT INTO messages (sender, content, created_at) VALUES (%s,%s, NOW())""", (sender, message, ))
cur.execute("COMMIT")
