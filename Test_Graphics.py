#ADD GRAPHICS TO TESTS
# Description: This file contains the graphics for http response time tests

import matplotlib.pyplot as plt
import requests

response_times = []
for i in range(10):
    r = requests.get('http://www.google.com')
    response_times.append(r.elapsed.microseconds / 1000)

print('Minimum response time: ', min(response_times), ' [ms]')
print('Maximum response time: ', max(response_times), ' [ms]')
print('Average response time: ', sum(response_times) / len(response_times), ' [ms]')

plt.figure()
plt.plot(response_times)
plt.ylim([0, max(response_times)])
plt.title('Response times')
plt.ylabel('Time [ms]')
plt.show()