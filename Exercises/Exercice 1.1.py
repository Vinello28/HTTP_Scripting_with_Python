# TODO: write a python script to print the website name that have
# the best response time. Use the following data: http://www.google.com and http://www.youtube.com

import requests

url = ['http://www.google.com', 'http://www.youtube.com']

r1 = requests.get(url[0])
r2 = requests.get(url[1])

response_time = [r1.elapsed.microseconds / 1000, r2.elapsed.microseconds / 1000]

if response_time[0] < response_time[1]:
    print(url[0], ' wins with ', response_time[0])
    print(url[1], ' lost with ', response_time[1])
else:
    print(url[1], ' wins with ', response_time[1])
    print(url[0], ' lost with ', response_time[0])
