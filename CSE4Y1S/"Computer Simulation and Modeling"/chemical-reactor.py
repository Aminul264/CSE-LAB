import numpy as np
import matplotlib.pyplot as plt



def chemical_reactor(A,B,C,k1,k2,dt):
    # initialization
    substance_A=[]
    substance_B=[]
    substance_C=[]
    time=0
    time_points=[]
    end_time=10
    
    while(time<=end_time):
        substance_A.append(A)
        substance_B.append(B)
        substance_C.append(C)
        time_points.append(time)
        
        A+=(k2*C-k1*A*B)*dt
        B+=(k2*C-k1*A*B)*dt
        C+=(2*k1*A*B-2*k2*C)*dt
        time+=dt
        
        plt.clf()
        plt.plot(time_points,substance_A,'r',label='Substance A')
        plt.plot(time_points,substance_B,'g',label='Substance B')
        plt.plot(time_points,substance_C,'b',label='Substance C')  
        
        #display 
        plt.title('Simulation of Chemical Reactor')
        plt.xlabel('Time (s)')
        plt.ylabel('Quantity (gm)')
        plt.xlim(0,end_time)
        plt.legend()
        plt.grid()
        
        plt.pause(0.0001)
    plt.show()
    
def main():
    a,b,c=100,50,0
    k1,k2=0.008,0.002
    dt=0.1
    
    chemical_reactor(a,b,c,k1,k2,dt)

if __name__=='__main__':
    main()