#GRAPHICS FOR RESPONSE TIME TESTS
#Description: as the first ex, the code below show how to plot
# graphics using mathplotlib

import requests
import matplotlib.pyplot as plt

response_times = []
for i in range(10):
    response = requests.get('http://www.google.com')
    response_times.append(response.elapsed.microseconds/1000)

print('Minimum response time: ', min(response_times))
print('Maximum response time: ', max(response_times))
print('Average response time: ', sum(response_times)/len(response_times))

plt.figure()
plt.plot(response_times)
plt.ylim([0, 1.1*max(response_times)])
plt.grid()
plt.xlabel('Request ID')
plt.ylabel('[ms]')
plt.title('Response Times for http://www.google.com')
plt.show()