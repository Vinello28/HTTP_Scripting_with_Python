# TODO: write a python script to print the website name that have
# the best response time. Use the following data: http://www.google.com and http://www.youtube.com

import requests

websites = ['http://www.google.com', 'http://www.youtube.com']

response_times1 = []
response_times2 = []

avg1 = None
avg2 = None

for i in range(10):
    response_times1.append(requests.get(websites[0]).elapsed.microseconds/1000)
    response_times2.append(requests.get(websites[1]).elapsed.microseconds/1000)

avg1 = sum(response_times1)/len(response_times1)
avg2 = sum(response_times2)/len(response_times2)

if avg1 < avg2:
    print(websites[0], 'has the best response time: ', avg1, '[ms]')
else:
    print(websites[1], 'has the best response time', avg2, '[ms]')
