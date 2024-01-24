import numpy as np
import matplotlib.pyplot as plt

def pure_persuit(v,min_dist,max_dist):
    xb,yb=np.random.randint(1,1000,2)
    x_bomber=[xb]
    y_bomber=[yb]
    
    xf,yf=50,50
    x_fighter=[xf]
    y_fighter=[yf]
    
    count=0
    plt.title('pure persuit')
    while True:
        count+=1
        distance=np.sqrt( (xb-xf)**2+(yb-yf)**2 )
        print(distance)
        if distance<=min_dist:
            plt.plot([xb,xf],[yb,yf])
            plt.text(50,45,f'Bomber caught at :{count} sec')
            print(f'Bomber caught at step {count}')
            plt.pause(5)
            break
        elif distance>=max_dist:
            plt.plot([xb,xf],[yb,yf])
            plt.text(50,45,f'Bomber escaped at :{count} sec')
            print(f'Bomber escaped at step {count}')
            plt.pause(5)
            break
        else:
            xb,yb=np.random.randint(max(1,xb-100),min(1000,yb+100),2)
            x_bomber.append(xb)
            y_bomber.append(yb)
            
            cosA,sinA=(xb-xf)/distance,(yb-yf)/distance
            xf,yf=(xf+v*cosA),(yf+v*sinA)            
            x_fighter.append(xf)
            y_fighter.append(yf)
            
            # display
            plt.plot(x_bomber,y_bomber,'r',marker='o',label='bomber')
            plt.plot(x_fighter,y_fighter,'g',marker='o',label='fighter')
            
            plt.pause(0.5)
        if count==1:
            plt.legend()

    plt.show()
def main():
    speed=20
    min_dist=100
    max_dist=900
    pure_persuit(speed,min_dist,max_dist)
    
if __name__=='__main__':
    main()
