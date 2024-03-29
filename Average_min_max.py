#MINIMUM, MAXIMUM, AVERAGE RESPONSE TIME TEST
#This file is used to test the response time of the google.com website
#The response time is calculated in milliseconds and printed in stdout

import requests

response_times = []
for i in range(10):
    r = requests.get('http://www.google.com')
    response_times.append(r.elapsed.microseconds / 1000)

print('Minimum response time: ', min(response_times), ' [ms]')
print('Maximum response time: ', max(response_times), ' [ms]')
print('Average response time: ', sum(response_times) / len(response_times), ' [ms]')
