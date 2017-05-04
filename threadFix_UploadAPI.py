# apikey = BHxhOwJmo0lyRKRAMPAR85jUHCWPHm0qOHgAaLTSew


import requests
import json
import sys


'''
upload the scan report to threadfix team > application
input para1 file-name, para2 appID
'''
def upload_report(app_name, report_name):
	# Fetch all the team & application ID and Name
	headers = {'Accept': 'application/json'}
	r = requests.get('http://10.112.184.177:8080/threadfix/rest/teams?apiKey=BHxhOwJmo0lyRKRAMPAR85jUHCWPHm0qOHgAaLTSew',headers=headers)
	#print r.status_code
	#print r.text
	data = json.loads(r.text)
	#print data['success']
	team_details = {}
	application_details = {}
	if data['success'] == True:
		for obj in data['object']:
			#print "ID = " + str(obj['id']) +" Name = " + obj['name']
			team_details.update({str(obj['id']):str(obj['name'])})
			for obj2 in obj['applications']:
			 	#print "ID = " + str(obj2['id']) +" Name = " + obj2['name'] 
	 			application_details.update({str(obj2['name']):str(obj2['id'])})
		#print team_details
		#print application_details[app_name]
		if app_name in application_details:
			app_id = application_details[app_name]
			call_upload_api(app_id,report_name)
		else:
			print "Application is not found in Threadfix, exiting"

	#upload the report

def call_upload_api(app_id, report):
	headers = {'Accept': 'application/json'}
	#payload = {'file': report}
	files = {'file': open(report, 'rb')}
	url = "http://10.112.184.177:8080/threadfix/rest/applications/"+app_id+"/upload?apiKey=BHxhOwJmo0lyRKRAMPAR85jUHCWPHm0qOHgAaLTSew"
	r = requests.post(url, headers=headers, files=files)
	data = json.loads(r.text)
	print "Scan report upload status=>" + str(data['success'])





# get the command line parameters


def main(argv):
	#print len(argv)
	if len(argv) == 2:
		app_name = argv[0]
		report_name = argv[1]
		upload_report(app_name, report_name)
	else:
		print "parameter missing 1st arg app_name, 2nd arg report"
#	print argv[1]
#	print argv[2]
   
if __name__ == "__main__":
   main(sys.argv[1:])


