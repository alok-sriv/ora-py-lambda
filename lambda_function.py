import boto3
import json
import logging
import os
import cx_Oracle

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
   con = cx_Oracle.connect('user/pwd@endpoint-of-rds:port/dbname')
   print con.version
   con.close()
