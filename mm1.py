#M/M/1 queue from the congestion point of view
import random
import numpy as np
import matplotlib.pyplot as plt

#Input parameters
simulation_time = input("Total simulation time: ")
lambd = float(input("Arrival rate: "))
mu = input("Service rate: ")
rho = lambd/mu

#Initialize parameters
arrival_times = []
service_times = []
departure_times = []
waiting_times = []

#Generating arrival times
t = 0  #Initialize clock
while t < simulation_time: 
    t_interval = -np.log(np.random.random()) / lambd
    t = t + t_interval
    arrival_times.append(t)

#Generating service times
for j in range(len(arrival_times)):
    service_times.append(-np.log(np.random.random()) / mu)

#Departure times
departure_times.append(arrival_times[0] + service_times[0])
for k in range(1,len(arrival_times)): 
    departure_times.append(max(arrival_times[k], departure_times[k-1]) + service_times[k])

#Waiting times
for v in range(len(arrival_times)):
   waiting_times.append(departure_times[v]- arrival_times[v]) 

#Number of customers in the queue at time t denoted by Q(t)
#Assuming Q(0) is 0, i.e., the number of customers in the queue at time 0 is 0. 
def Q(t1):
    def A(t1):  #Number of arrivals in time t1
        n = 0
        for m in range(len(arrival_times)): 
            if arrival_times[m] <= t1:
                 n = n+1
        return n

    def D(t1):  #Number of departures in time t1
        q=0
        for p in range(len(arrival_times)): 
            if departure_times[p] <= t1:
                 q = q+1
        return q

    return A(t1)-D(t1)   

x = np.arange(0.0, simulation_time, 0.01)
y = [Q(s) for s in x]

plt.plot(x, y)
plt.xlabel('Time') 
plt.ylabel('Number of customers in the queue') 
plt.title('Queue length vs time in M/M/1 queue')
plt.show()

#########################################################

def pi(x):
  count = 0
  for i in range(len(y)):
      if y[i] == x:
          count = count + 1.0
  return(count/len(y))

def pi_con(u):
    return (rho**u) * (1-rho)

x1 = np.arange(0, np.amax(y)+1 , 1)
y1 = [pi(t) for t in x1]
y2 = [pi_con(t) for t in x1]

plt.plot(x1, y1, marker='o')
plt.plot(x1, y2,'r', marker='o', linestyle = '--')
plt.xlabel('n') 
plt.ylabel('Probability of n customers in the queue') 
plt.title('pi_n vs n in M/M/1 queue')
plt.show()

###########################################################

print('Expected number of customers in the queue is', np.mean(y))
print('Expected delay is', np.mean(waiting_times))




       







