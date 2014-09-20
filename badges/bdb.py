import re
import urllib2
import MySQLdb
import xml.etree.ElementTree as xml

def keep_log(str):
        str = str.encode('utf-8')
        file = open("badges_log.txt","a")
        file.write(str)
        file.write("\n")
        file.close()

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

try:


        #Parse XML directly from the file path
        tree = xml.parse("badges05")

        #Get the root node
        row = tree.findall("row")

        for i in row:
                b_id = i.attrib.get("Id")
                u_id = i.attrib.get("UserId")
                name = i.attrib.get("Name")
                date = i.attrib.get("Date")

                query = """INSERT IGNORE INTO sof_badges 
                        (sof_users_id, name, date, badge_id) 
                        VALUES ('%s', '%s', '%s', '%s')
                        """ % (u_id, name, date, b_id)


                try:

                        cursor.execute(query)
                        db.commit()
                        print "Insert Successful"

                except:
                        pass

except (ValueError) as e:
        print e
