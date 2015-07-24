import sqlite3 as lite
import sys

con = None
dump = None

try:
    con = lite.connect('main.db')
    name ='duarteLines.txt'  # Name of text file coerced with +.txt
    dump = open(name,'w')   # Trying to create a new file or open one
    cur = con.cursor()
    for row in cur.execute("SELECT name  FROM Chats WHERE posters LIKE '%duarte.m.godinho%' AND posters LIKE '%bot.duarte%';"):
    	print row
    	for row2 in cur.execute("SELECT timestamp, author, from_dispname, chatmsg_type, identities, body_xml FROM Messages WHERE chatname = '" + str(row[0]) + "' AND author like '%duarte.m.godinho%';"):
    		print row2
    		if row2[5] is not None:
    			dump.write(((row2[5])).encode('utf-8').strip()+'\n')
    		# dump.write(row2[5]+'\n')
    # for row in cur.execute("SELECT identity, displayname FROM Conversations"):
    	# print row
    # data = cur.fetchone()
    
    # print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
    if dump:
    	dump.close()
