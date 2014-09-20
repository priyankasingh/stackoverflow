import re
import StringIO
import urllib2
import codecs
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
        #post = open('a.xml', 'r')
	
	#a = post.read()
	#print a

	#tree = xml.parse((a).decode('utf-8'))#, 'replace'))
	#exit()
	tree = xml.parse("a.xml")
        #Get the root node
        row = tree.findall("row")

        for i in row:
                #i=i.encode('utf-8')
		p_id = i.attrib.get("Id")
                t_id = i.attrib.get("PostTypeId")
                par_id = i.attrib.get("ParentId")
                ans_id = i.attrib.get("AcceptedAnswerId")
                c_date = i.attrib.get("CreationDate")
                score = i.attrib.get("Score")
                v_cnt = i.attrib.get("ViewCount")
                body = i.attrib.get("Body")
                u_id = i.attrib.get("OwnerUserId")
                #le_id = i.attrib.get("LastEditorUserId")
                #le_name = i.attrib.get("LastEditorDisplayName")
                #le_date = i.attrib.get("LastEditDate")
                #la_date = i.attrib.get("LastActivityDate")
                #co_date = i.attrib.get("CommunityOwnedDate")
                #c_date = i.attrib.get("ClosedDate")
                title = i.attrib.get("Title")
                tags = i.attrib.get("Tags")
                a_cnt = i.attrib.get("AnswerCount")
                c_cnt = i.attrib.get("CommentCount")
                f_cnt = i.attrib.get("FavoriteCount")
                
		if title is None:
			title = ""
		
		if body is None:
			body = ""
		
		bd = MySQLdb.escape_string(body)
		tt = MySQLdb.escape_string(title)
		
		print tt
			
		#print body
		
                query = """INSERT IGNORE INTO posts 
                        (post_id, post_type_id, parent_id, accepted_answer_id, creation_date, score, view_count, body, owner_user_id, title, tags, answer_count, comment_count, favourite_count) 
                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                        """% (p_id, t_id, par_id, ans_id, c_date, score, v_cnt, bd, u_id, tt, tags, a_cnt, c_cnt, f_cnt)


                try:
                	cursor.execute(query)
                        db.commit()
                        print "Insert Successful"

                except:
                        pass

except (ValueError) as e:
        print e
