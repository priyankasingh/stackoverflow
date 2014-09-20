# this code is based on: http://www.flagonwiththedragon.com/2011/06/08/dead-simple-python-calls-to-open-calais-api/
 
import urllib, urllib2
import MySQLdb

db =  MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="Southampton11",
        db="Test")

cursor = db.cursor()

query = """SELECT body  FROM sof_posts LIMIT 10;"""

cursor.execute(query)
numrows = int(cursor.rowcount)

rows = cursor.fetchall()
post = rows[0]

for i in range (numrows):

	#########################
	##### set API key and REST URL values.
 
	myCalaisAPI_key = '9aguj5vvwhq23gqpuamy9ene' # your Calais API key.
	calaisREST_URL = 'http://api.opencalais.com/enlighten/rest/' # this is the older REST interface.
	# info on the newer one: http://www.opencalais.com/documentation/calais-web-service-api/api-invocation/rest
 
	# alert user and shut down if the API key variable is still null.
	if myCalaisAPI_key == '':
		print "You need to set your Calais API key in the 'myCalaisAPI_key' variable."
  		import sys
  		sys.exit()
 
	#########################
	##### set the text to ask Calais to analyze.
 

	# text from: http://www.usatoday.com/sports/football/nfl/story/2012-03-22/Tim-Tebow-Jets-hoping-to-avoid-controversy/53717542/1
	sampleText = rows[i][0] #'''
	#I have a ~23000 line sql dump containing several databases worth of data. I need to extract a certain section of this file (i.e. the data for a single database) and place it in a new file. I know both the start and end line numbers of the data that I want.
	#Does anyone know a unix command (or series of commands) to extract all lines from a file between say line 16224 and 16482 and then redirect them into a new file?
#'''
 
	#########################
	##### set XML parameters for Calais.
 
	# see "Input Parameters" at: http://www.opencalais.com/documentation/calais-web-service-api/forming-api-calls/input-parameters
	calaisParams = '''
	<c:params xmlns:c="http://s.opencalais.com/1/pred/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
	  <c:processingDirectives c:contentType="text/HTML"
  		c:calculateRelevanceScore="true"
      		c:enableMetadataType="GenericRelations,SocialTags"
      		c:outputFormat="XML/RDF"/>
  	  <c:userDirectives/>
  	  <c:externalMetadata/>
	</c:params>
	'''
 
	#########################
	##### send data to Calais API.
 
	# see: http://www.opencalais.com/APICalls
	dataToSend = urllib.urlencode({
	    'licenseID': myCalaisAPI_key,
	    'content': sampleText,
   	    'paramsXML': calaisParams
	})
 
	#########################
	##### get API results and print them.
 
	results = urllib2.urlopen(calaisREST_URL, dataToSend).read()
	print results
