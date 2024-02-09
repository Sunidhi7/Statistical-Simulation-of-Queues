#Generating Erlang Random Variable

import random
import numpy as np

#Generating service times
    for j in range(len(arrival_times)):
        uni = 1.0
        for i in range(k):
            uni = uni * np.random.random()
        service_times.append(-np.log(uni) / (k*mu))

   
