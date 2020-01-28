#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import boto3
import uuid
import time
import random
import json

# Client details - To be modified to avoid hardcoding - Write to a file and pickle it.
region_name='us-east-1'
aws_access_key_id='ABCDEFGHIJKLMNOP'
aws_secret_access_key='abcdefghijklmnopqrstuvwxyz'

client = boto3.client('kinesis', region_name=region_name,
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key)
partition_key = str(uuid.uuid4())

while True:
        r = requests.get('https://randomuser.me/api/?exc=login')
        data = json.dumps(r.json())
        client.put_record(
                StreamName='random-user-stream',
                Data=data,
                PartitionKey=partition_key)
        print('Data streamed :{}'.format(data))
        time.sleep(random.uniform(0, 1))

