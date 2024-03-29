#MULTIPLE WEBSITE RESPONSE TIMES
#This script will check the response time of multiple websites and will display
# the response time of each website in a tabular format.
#The script will also display the average response times of all the websites.

import requests
import matplotlib.pyplot as plt

#List of websites
websites = ['https://www.google.com', 'https://www.pornhub.com', 'https://www.youtube.com', 'https://www.twitter.com']

for url in websites:
    print('Test ', url)
    response_time = []
    for i in range(10):
        r = requests.get(url)
        response_time.append(r.elapsed.microseconds/1000)

    print('Minimum Response Time: ', min(response_time), '[ms]')
    print('Maximum Response Time: ', max(response_time), '[ms]')
    print('Average Response Time: ', sum(response_time)/len(response_time), '[ms]')
