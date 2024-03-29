#RESPONSE TIME TEST
#This file is used to test the response time of the google.com website
#The response time is calculated in milliseconds and printed in stdout


import requests

for i in range(10):
    r = requests.get('http://www.google.com')
    print('Response time ', i, ': ', r.elapsed.microseconds / 1000, ' [ms]')
