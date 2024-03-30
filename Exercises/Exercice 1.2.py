# TODO: Write a script that prints the name of the webpage with the best average response time among 6 websites.
#  For the calculation of the average time, define the function average(list) that returns the average
#  of the values contained in list.


import requests

websites = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi.it', 'http://www.pornhub.com',
            'http://www.univpm.it', 'http://www.facebook.com']

avg_response_times = []


def average(response_times):
    return sum(response_times) / len(response_times)


k = 0
for url in websites:
    response_times = []
    for i in range(10):
        response_times.append(requests.get(url).elapsed.microseconds / 1000)
    avg_response_times.append(average(response_times))

print(websites[avg_response_times.index(min(avg_response_times))], 'has the best response time: ', min(avg_response_times), '[ms]')
