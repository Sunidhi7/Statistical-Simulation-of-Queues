# GI/M/1 queue 

import random
import numpy as np
import matplotlib.pyplot as plt

#Input parameters
simulation_time = input("Total simulation time: ")
lambd = float(input("Arrival rate: "))
mu = input("Service rate: ")
k = input("Order of Erlang random variable:")
rho = lambd/mu

#Initialize parameters
arrival_times = []
service_times = []
departure_times = []
waiting_times = []

#Generating arrival times
t = 0  #Initialize clock
while t < simulation_time: 
    erl = 1.0
    for i in range(k):
        erl = erl * np.random.random()
    t_interval = -np.log(erl) / (k*lambd)
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

y = [Q(s) for s in arrival_times]
print('Average  number  of customers in the system seen by arriving customers is', np.mean(y)-1)

x1 = np.arange(0.0, simulation_time, 0.01)
y1 = [Q(e) for e in x1]
print('Time average of the number of customers in the system is', np.mean(y1))







