#!/bin/python3
import json
import sys
try:
  import boto3
except Exception as e:
  print(e)
  print("Please rectify above exception and try again..!")
  sys.exit(1)

def get_hosts(ec2_ob,fv):
   f={"Name":"tag:Env" , "Values": [fv]}
   hosts=[]
   for each_in in ec2_ob.instances.filter(Filters=[f]):
       hosts.append(each_in.private_ip_address)
   return hosts

def main():
   ec2_ob=boto3.resource("ec2","ap-northeast-1")
   db_group= get_hosts(ec2_ob, 'db')
   app_group= get_hosts(ec2_ob, 'app')
   all_groups={ 'db': db_group, 'app': app_group }
   print(json.dumps(all_groups))
   return None
