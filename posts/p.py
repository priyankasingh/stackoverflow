from xml.dom.minidom import parse
import xml.dom.minidom
import MySQLdb
import codecs

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

doc = parse("s01")

row = doc.getElementsByTagName('row')

for i in row:

	a = i.attributes["Id"]
	#print a.value
	
	b = i.attributes["PostTypeId"]
	#print b.value
	
	c = i.attributes["CreationDate"]
	#print c.value
	
	d = i.attributes["Score"]
	#print d.value
	
	if i.hasAttribute("OwnerUserId"):
		e1 = i.attributes["OwnerUserId"]
		e = e1.value
		#print e.value
	else:
		e = ""
	
	if i.hasAttribute("Title"):
		f1 = i.attributes["Title"]
		f = f1.value.encode('ascii', 'ignore')
		f = MySQLdb.escape_string(f)
		#print f.value
	else:
		f = ""

	
	if i.hasAttribute("ParentId"):
		g1 = i.attributes["ParentId"]
		g = g1.value
		#print g.value
	else:
		g = ""
	
	if i.hasAttribute("AcceptedAnswerId"):
		h1 = i.attributes["AcceptedAnswerId"]
		h = h1.value
		#print h.value
	else:
		h = ""
	
	if i.hasAttribute("ViewCount"):
		j1 = i.attributes["ViewCount"]
		j = j1.value
		#print j.value
	else:
		j = ""
	
	if i.hasAttribute("Body"):
		k1 = i.attributes["Body"]
		k = k1.value.encode('ascii', 'ignore')
		k = MySQLdb.escape_string(k)
		#print k.value
	else:
		k = ""
	
	if i.hasAttribute("Tags"):
		l1 = i.attributes["Tags"]
		l = l1.value
		#print l.value
	else:
		l = ""
	
	if i.hasAttribute("AnswerCount"):
		m1 = i.attributes["AnswerCount"]
		m = m1.value
		#print m.value
	else: m = ""
	
	if i.hasAttribute("CommentCount"):
		n1 = i.attributes["CommentCount"]
		n = n1.value
		#print n.value
	else:
		n = ""
	
	if i.hasAttribute("FavoriteCount"):
		o1 = i.attributes["FavoriteCount"]
		o = o1.value
		#print o.value
	else:
		o = ""

	query = """INSERT IGNORE INTO sof_posts 
                        (post_id, post_type_id, parent_id, accepted_answer_id, creation_date, score, view_count, body, owner_user_id, title, tags, answer_count, comment_count, favourite_count) 
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                        """% (a.value, b.value, g, h, c.value, d.value, j, k, e, f, l, m, n, o)


	try:
        	cursor.execute(query)
                db.commit()
                #print "Insert Successful"

	except:
        	pass
