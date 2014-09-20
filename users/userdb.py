import re
import urllib2
import MySQLdb
import xml.etree.ElementTree as xml

def keep_log(str):
        str = str.encode('utf-8')
        file = open("user_log.txt","a")
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
	tree = xml.parse("x10")

	#Get the root node
	row = tree.findall("row")

	for i in row:
		u_id = i.attrib.get("Id")
		rep = i.attrib.get("Reputation")
		cr_dt = i.attrib.get("CreationDate")
		dp_name = i.attrib.get("DisplayName")
		email = i.attrib.get("EmailHash")
		l_dt = i.attrib.get("LastAccessDate")
		wurl = i.attrib.get("WebsiteUrl")
		lct = i.attrib.get("Location")
		age = i.attrib.get("Age")
		abt_me = i.attrib.get("AboutMe")
		views = i.attrib.get("Views")
		uvote = i.attrib.get("UpVotes")
		dvote = i.attrib.get("DownVotes")
      
		query = """INSERT IGNORE INTO sof_users 
                	(user_id, reputation, creation_date, display_name, email_hash, last_access_date, website_url, location, age, about_me, views, upvotes, downvotes) 
                	VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                	""" % (u_id, rep, cr_dt, dp_name, email, l_dt, wurl, lct, age, abt_me, views, uvote, dvote)


        	try:
			
	    		cursor.execute(query)
            		db.commit()
           		print "Insert Successful"

        	except:
            		pass

except (ValueError) as e:
        print e

