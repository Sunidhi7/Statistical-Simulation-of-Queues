#M/M/1 queue from the point of view of workload for FIFO and LCFS under a preemptive priority serving schedule

import random
import numpy as np
import matplotlib.pyplot as plt

#Input parameters
simulation_time = input("Total simulation time: ")
lambd = float(input("Arrival rate: "))
mu = input("Service rate: ")
c = input("Server speed: ")
rho = lambd/mu

#Initialize parameters
arrival_times = []
interarrival_times = []
incoming_workload = []
rem_workload = []
departure_timesfifo = [] 
departure_times = []
waiting_timesfifo = []
waiting_times = []

#Generating arrival times and inter-arrival times
t = 0  #Initialize clock
while t <= simulation_time: 
    t_interval = -np.log(np.random.random()) / lambd
    t = t + t_interval
    arrival_times.append(t)
    interarrival_times.append(t_interval)

#Generating incoming workload
for j in range(len(arrival_times)):
    incoming_workload.append(-np.log(np.random.random()) / mu)

#Departure times for FIFO
departure_timesfifo.append(arrival_times[0] + incoming_workload[0])
for k in range(1,len(arrival_times)): 
    departure_timesfifo.append(max(arrival_times[k], departure_timesfifo[k-1]) + incoming_workload[k])

#Departure times for LCFS under a preemptive priority serving schedule
departure_times.append(arrival_times[len(arrival_times)-1] + incoming_workload[len(arrival_times)-1])
for k in range(len(arrival_times)-1):
    if incoming_workload[len(arrival_times)-k-2] <= interarrival_times[len(arrival_times)-k-2]:
         departure_times.insert(0, arrival_times[len(arrival_times)-k-2] + incoming_workload[len(arrival_times)-k-2])
    else: 
         departure_times.insert(0, departure_times[0] + incoming_workload[len(arrival_times)-k-2] - interarrival_times[len(arrival_times)-k-2])

#Waiting times for FIFO 
for u in range(len(arrival_times)):
   waiting_times.append(departure_timesfifo[u]- arrival_times[u])

#Waiting times for LCFS under a preemptive priority serving schedule
for v in range(len(arrival_times)):
   waiting_times.append(departure_times[v]- arrival_times[v]) 

#Amount of work arriving in (0, t]
def X(t): 
    x = 0.0
    for m in range(len(arrival_times)):
        if arrival_times[m] <= t:
            x = x + incoming_workload[m]
    return x

#Remaining workload
#Assuming there was no workload in the queue at time 0
rem_workload.append(X(0.01))
a = 0.02
i = 1
while a < simulation_time:  
    m = 0
    for v in range(i):
        if rem_workload[v] > 0:
             m = m + 0.01
    rem_workload.append(X(a) - m * c)    
    i = i+1
    a = a + 0.01
																									
z = np.arange(0.01, simulation_time, 0.01)
y = [rem_workload[int((i-0.01)/0.01)] for i in z]

plt.plot(z, y)
plt.xlabel('Time') 
plt.ylabel('Workload') 
plt.title('Workload vs time in M/M/1 queue')
plt.ylim(ymin = 0)
plt.show()

print('Average workload in the system for FIFO as well as LCFS under a preemptive priority serving schedule is', np.mean(y))


##################################################

#Average number in the queue

#Number of customers in the queue at time t denoted by Q(t)
#Assuming Q(0) is 0, i.e., the number of customers in the queue at time 0 is 0. 

#Number of customers in the queue for FIFO
def Q(t1):
    def A(t1):  #Number of arrivals in time (0, t1]
        n = 0
        for m in range(len(arrival_times)): 
            if arrival_times[m] <= t1:
                 n = n+1
        return n

    def D(t1):  #Number of departures in time (0, t1]
        q=0
        for p in range(len(arrival_times)): 
            if departure_timesfifo[p] <= t1:
                 q = q+1
        return q

    return A(t1)-D(t1)   

x1 = np.arange(0.0, simulation_time, 0.01)
y1 = [Q(s) for s in x1]
print('Expected number of customers in the queue for FIFO is', np.mean(y1))


#Number of customers in the queue for LCFS under a preemptive priority serving schedule
def Qlcfs(t2):
    def Alcfs(t2):  #Number of arrivals in time (0, t2]
        f = 0
        for g in range(len(arrival_times)): 
            if arrival_times[g] <= t2:
                 f = f+1
        return f

    def Dlcfs(t2):  #Number of departures in time (0, t2]
        p=0
        for h in range(len(arrival_times)): 
            if departure_times[h] <= t2:
                 p = p+1
        return p

    return Alcfs(t2)-Dlcfs(t2)   

x2 = np.arange(0.0, simulation_time, 0.01)
y2 = [Qlcfs(e) for e in x2]
print('Expected number of customers in the queue for LCFS under a preemptive priority serving schedule is', np.mean(y2))
print('Number of customers obtained from Little formula using average workload obtained from simulation is ', lambd * np.mean(y))

