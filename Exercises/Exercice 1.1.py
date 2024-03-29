#TODO: write a python script to print the website name that have
# the best response time. Use the following data: http://www.google.com and http://www.youtube.com

import requests

url = ['http://www.google.com', 'http://www.youtube.com']

r1 = requests.get(url[0])
r2 = requests.get(url[1])

if r1.elapsed.microseconds/1000 < r2.elapsed.microseconds/1000:
    print(url[0],' wins with ', r1.elapsed.microseconds/1000)
    print(url[1], ' lost with ', r2.elapsed.microseconds / 1000)
else:
    print(url[1], ' wins with ', r2.elapsed.microseconds/1000)
    print(url[0], ' lost with ', r1.elapsed.microseconds / 1000)