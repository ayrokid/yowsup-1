TUTORIAL YOWSUP 2.0
-------------------------

1. download : https://github.com/ayrokid/yowsup
2. wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
3. sudo apt-get install python-pip
4. sudo pip install requests-oauth
5. sudo python setup.py install
6. sudo apt-get install python-mysqldb or # pip install mysql-python

7. registerasi no. HP (dengan nomor axis)
$ yowsup-cli registration --requestcode sms -p 6283808647193 --cc 62 --mcc 510 --mnc 11

8. jika keluar seperti pesan berikut berarti sukses :
INFO:yowsup.common.http.warequest:{"status":"sent","length":6,"method":"sms","retry_after":65,"sms_wait":65,"voice_wait":65}

status: sent
retry_after: 65
length: 6
method: sms

9. daftarkan kode yang dikirim ke sms (498-392) dengan format seperti berikut :
$ yowsup-cli registration --register 498-392 -p 6283808647193 --cc 62 --mcc 510 --mnc 11

10. jika keluar balasan seperti berikut berarti sukses :
INFO:yowsup.common.http.warequest:{"status":"ok","login":"6283808647193","type":"new","pw":"c7AKYNtnxNT5IQWPmyAj9wEiR8o=","expiration":4444444444.0,"kind":"free","price":"Rp9500","cost":"9500.00","currency":"IDR","price_expiration":1458990952}

status: ok
kind: free
pw: c7AKYNtnxNT5IQWPmyAj9wEiR8o=
price: Rp9500
price_expiration: 1458990952
currency: IDR
cost: 9500.00
expiration: 4444444444.0
login: 6283808647193
type: new

11. Buat file : yowsup-cli.config 


12. Test send message :
$ ./yowsup-cli demos -s 6285725523023 "dasda" --config yowsup-cli.config

13. Save Message to database mysql :
 a. edit file : /home/ayrokid/yowsup/yowsup/demos/cli/layer.py :

#save sql
jid = message.getFrom()
messageContent = messageOut.encode('latin-1').decode() if sys.version_info >= (3, 0) else messageOut

self.output(output, tag = None, prompt = not self.sendReceipts)
if self.sendReceipts:
    self.toLower(message.ack(self.sendRead))
    self.output("Sent delivered receipt"+" and Read" if self.sendRead else "", tag = "Message %s" % message.getId())
    os.system("python save.py " + jid + " " + messageContent + " ")

14. create file save.py di /home/ayrokid/yowsup/yowsup/demos/cli/ :

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

15. run apps : ./yowsup-cli demos --yowsup --login 6283808647193:c7AKYNtnxNT5IQWPmyAj9wEiR8o=
-----------------------------------------------------------------------------------


reverensi : http://kennethkinyanjui.info/whatsapp-on-laptop.html

note : 
jika keluar error :
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

install : 
sudo apt-get install python-dev 

sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

sudo easy_install greenlet

sudo easy_install gevent

jika python setup.py install error coba install :
pip install https://pypi.python.org/packages/source/p/python-axolotl/python-axolotl-0.1.7.tar.gz






