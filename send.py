from yowsup.demos import sendclient
#import logging #tampilan log khusus centos os
import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="root", # your password
db="push",
cursorclass=MySQLdb.cursors.DictCursor) # name of the data base

credentials = ['6283808647193', 'c7AKYNtnxNT5IQWPmyAj9wEiR8o=']

data = []

try:
    cur = db.cursor()
    cur.execute("select id,content from messages where status='1' limit 1")
    msg = cur.fetchone()
    #print "Message : %s " % msg['content']
    
    cur.execute("select nomor from msisdn")
    results = cur.fetchall()

    i = 0;
    for row in results:
       data.append([ row['nomor'], msg['content'] ])
       i += 1
    
    #stack = sendclient.YowsupSendStack(credentials, [(['6285725523023', 'pesan dari ubuntu'])])
    stack = sendclient.YowsupSendStack(credentials, data)
    stack.start()
    cur.execute("""update messages set status=0 where id=%s """, (msg['id']) )
    db.commit()
    print('\nKirim Sukses..')
except KeyboardInterrupt:
    db.rollback()
    print('\nYowsdown')

#disconnect from server
db.close()
