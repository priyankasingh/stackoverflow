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
        tree = xml.parse("vbq")

        #Get the root node
        row = tree.findall("row")

        for i in row:
 
      		v_id = i.attrib.get("Id")
                p_id = i.attrib.get("PostId")
                vt_id = i.attrib.get("VoteTypeId")
                c_date = i.attrib.get("CreationDate")
                u_id = i.attrib.get("UserId")
                b_amt = i.attrib.get("BountyAmount")
                
                
                query = """INSERT IGNORE INTO sof_votes 
                        (vote_id, post_id, vote_type_id, creation_date, user_id, bounty_amount) 
                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
                        """ % (v_id, p_id, vt_id, c_date, u_id, b_amt)

                try:
                        cursor.execute(query)
                        db.commit()
                        #print "Insert Successful"

                except:
                        pass

except (ValueError) as e:
        print e
