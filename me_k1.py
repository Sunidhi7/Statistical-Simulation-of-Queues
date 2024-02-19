#M/E_k/1 queue from congestion point of view
import random
import numpy as np
import matplotlib.pyplot as plt

def mek1(k, simulation_time, lambd, mu): # variable k denotes the order of Erlang random variable
    
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
        uni = 1.0
        for i in range(k):
            uni = uni * np.random.random()
        service_times.append(-np.log(uni) / (k*mu))

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
        def A(t1):  #Number of arrivals in time (0,t1]
            n = 0
            for m in range(len(arrival_times)): 
                if arrival_times[m] <= t1:
                     n = n+1
            return n

        def D(t1):  #Number of departures in time (0,t1]
            q=0
            for p in range(len(arrival_times)): 
                if departure_times[p] <= t1:
                     q = q+1
            return q

        return A(t1)-D(t1)   

    x = np.arange(0.0, simulation_time, 0.01)
    y = [Q(s) for s in x]
    
    return y
    
    
    
########################################################
#Part(b)
# lambd = 4, mu = 5

N = 500

def pi1(x):
  count1 = 0.0
  l1 = len(mek1(1, N, 4, 5))
  for z in range(l1):
      if mek1(1, N, 4, 5)[z] == x:
          count1 = count1 + 1
  return(count1/l1)


def pi2(x):
  count2 = 0.0
  l2 = len(mek1(2, N, 4, 5))
  for j in range(l2):
      if mek1(2, N, 4, 5)[j] == x:
          count2 = count2 + 1
  return(count2/l2)


def pi3(x):
  count3 = 0.0
  l3 = len(mek1(3, N, 4, 5))
  for e in range(l3):
      if mek1(3, N, 4, 5)[e] == x:
          count3 = count3 + 1
  return(count3/l3)

x1 = np.arange(0, np.amax(mek1(1, N, 4, 5))+1 , 1)
y1 = [pi1(t) for t in x1]
print('Expected number of customers in the queue for k=1 is', np.mean(mek1(1, N, 4, 5)))

x2 = np.arange(0, np.amax(mek1(2, N, 4, 5))+1 , 1)
y2 = [pi2(t) for t in x2]
print('Expected number of customers in the queue for k=2 is', np.mean(mek1(2, N, 4, 5)))

x3 = np.arange(0, np.amax(mek1(3, N, 4, 5))+1 , 1)
y3 = [pi3(t) for t in x3]
print('Expected number of customers in the queue for k=3 is', np.mean(mek1(3, N, 4, 5)))

plt.plot(x1, y1, 'b', marker='o', label='k=1')
plt.plot(x2, y2, 'r', marker='o', label='k=2')
plt.plot(x3, y3, 'g', marker='o', label='k=3')
plt.xlabel('n') 
plt.ylabel('Probability of n customers in the queue') 
plt.title('pi_n vs n in M/E_k/1 queue')
plt.legend(loc="upper right")
plt.show()	

#######################################################
#M/D/1 queue
def md1(simulation_time, lambd, mu): 
    
    rho = lambd/mu

    #Initialize parameters
    service_timesd = []
    departure_timesd = []
    waiting_timesd = []
    arrival_timesd = []    

    #Generating arrival times
    t = 0  #Initialize clock
    while t < simulation_time: 
        t_interval = -np.log(np.random.random()) / lambd
        t = t + t_interval
        arrival_timesd.append(t)

    #Generating service times
    for j in range(len(arrival_timesd)):
        service_timesd.append(1/mu)

    #Departure times
    departure_timesd.append(arrival_timesd[0] + service_timesd[0])
    for k in range(1,len(arrival_timesd)):
        departure_timesd.append(max(arrival_timesd[k], departure_timesd[k-1]) + service_timesd[k])

    #Waiting times
    for v in range(len(arrival_timesd)):
       waiting_timesd.append(departure_timesd[v]- arrival_timesd[v]) 

    #Number of customers in the queue at time t denoted by Q(t)
    #Assuming Q(0) is 0, i.e., the number of customers in the queue at time 0 is 0. 
    def Q(t1):
        def A(t1):  #Number of arrivals in time (0,t1]
            n = 0
            for m in range(len(arrival_timesd)): 
                if arrival_timesd[m] <= t1:
                     n = n+1
            return n

        def D(t1):  #Number of departures in time (0,t1]
            q=0
            for p in range(len(arrival_timesd)): 
                if departure_timesd[p] <= t1:
                     q = q+1
            return q

        return A(t1)-D(t1)   

    x = np.arange(0.0, simulation_time, 0.01)
    y = [Q(s) for s in x]
    
    return y


x_axis = np.arange(0.1, 0.9 , 0.1)
y_axis = [np.mean(md1(N, i, 1)) for i in x_axis]
y_axis1 = [np.mean(mek1(1, N, i, 1)) for i in x_axis]
y_axis5 = [np.mean(mek1(5, N, i, 1)) for i in x_axis]
y_axis10 = [np.mean(mek1(10, N, i, 1)) for i in x_axis]
plt.plot(x_axis, y_axis, 'g', marker='o', label='Deterministic')
plt.plot(x_axis, y_axis1, 'b', marker='o', label='k=1')
plt.plot(x_axis, y_axis5, 'r', marker='o', label='k=5')
plt.plot(x_axis, y_axis10, 'y', marker='o', label='k=10')
plt.xlabel('Utilization') 
plt.ylabel('Expected number of customers in the queue') 
plt.title('Expected number of customers in the queue vs Utilization')
plt.legend(loc="upper right")
plt.show()




























#
