import re
import urllib2
import MySQLdb
import xml.etree.ElementTree as xml

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

try:


        #Parse XML directly from the file path
        tree = xml.parse("c10")

        #Get the root node
        row = tree.findall("row")

        for i in row:
        	c_id = i.attrib.get("Id")
                p_id = i.attrib.get("PostId")
                score = i.attrib.get("Score")
                text = i.attrib.get("Text")
                c_date = i.attrib.get("CreationDate")
                u_id = i.attrib.get("UserId")
                
                
                query = """INSERT IGNORE INTO sof_comments 
                        (comment_id, post_id, score, text, creation_date, user_id) 
                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
                        """ % (c_id, p_id, score, text, c_date, u_id)

                try:
                        cursor.execute(query)
                        db.commit()
                        print "Insert Successful"

                except:
                        pass

except (ValueError) as e:
        print
