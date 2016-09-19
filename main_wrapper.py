#!/usr/bin/python
import psycopg2
import sys
import os
import csv
import MySQLdb
import os.path

# MR PARAMETERS
tenant = sys.argv[1]
script_path = sys.argv[2]
mysql_username = sys.argv[3]
mysql_password = sys.argv[4]
mysql_host = sys.argv[5]
mysql_db = sys.argv[6]
mysql_workdb = sys.argv[7]
redshift_username = sys.argv[8]
redshift_password = sys.argv[9]
redshift_host = sys.argv[10]
redshift_db = sys.argv[11]
redshift_schema = sys.argv[12]
s3_access_key = sys.argv[13]
s3_secret_key = sys.argv[14]
s3_bucket = sys.argv[15]
s3_folder = sys.argv[16]
db_type = sys.argv[17]
isTraining = sys.argv[18]



#os.system("python dataoutput1.py mysql mysqloutput.csv")
print "Advanced Analytics for "+tenant+" started"
os.chdir(script_path)

print "Downloading all the predictive analytics scripts from s3"

downloadCmd = "python s3folderdownload.py " + s3_bucket + " " + s3_folder + " " + script_path
os.system(downloadCmd)

trainingCmd = "python training_wrapper.py " + tenant + " " + script_path + " " + mysql_username + " " + mysql_password + " " + mysql_host + " " + mysql_db + " " + mysql_workdb + " " + redshift_username + " " + redshift_password + " " + redshift_host + " " + redshift_db + " " + redshift_schema + " " + s3_access_key + " " + s3_secret_key + " " + s3_bucket + " " + s3_folder + " " + db_type

scoringCmd = "python scoring_wrapper.py " + tenant + " " + script_path + " " + mysql_username + " " + mysql_password + " " + mysql_host + " " + mysql_db + " " + mysql_workdb + " " + redshift_username + " " + redshift_password + " " + redshift_host + " " + redshift_db + " " + redshift_schema + " " + s3_access_key + " " + s3_secret_key + " " + s3_bucket + " " + s3_folder + " " + db_type

if isTraining == 'Y':
	print "Starting Training for tenant"
	os.system(trainingCmd)
else:
	print "Starting scoring for tenant"
	os.system(scoringCmd)
	