#MULTIPLE WEBSITES RESPONSE TIMES GRAPHICS
#This script will check the response time of multiple websites and will display
# the response time plots of each website.

import requests
import matplotlib.pyplot as plt

m = 0
plt.figure()

#List of websites
websites = ['https://www.google.com', 'https://www.polimi.it', 'https://www.youtube.com', 'https://www.univpm.it']

for url in websites:
    print('Test ', url)
    response_time = []
    for i in range(10):
        r = requests.get(url)
        response_time.append(r.elapsed.microseconds/1000)

    plt.plot(response_time, label=url)
    print('Minimum Response Time: ', min(response_time), '[ms]')
    print('Maximum Response Time: ', max(response_time), '[ms]')
    print('Average Response Time: ', sum(response_time)/len(response_time), '[ms]')
    m = max([m, max(response_time)])

plt.ylim([0, 1.1*m])
plt.xlabel('Request ID')
plt.ylabel('[ms]')
plt.legend(loc='lower right', fontsize='8')
plt.grid()
plt.show()