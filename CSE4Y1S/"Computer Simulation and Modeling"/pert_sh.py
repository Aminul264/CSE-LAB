import sys
sys.stdin=open('pert_sh.txt','r')

class Activity:
    def __init__(self,id,start,end,dur) -> None:
        self.id=id
        self.start=start
        self.end=end
        self.dur=dur
        self.es=0
        self.ef=0
        self.ls=0
        self.lf=0
        

activities={}   
forward_f=[0]*100 #updated earliest_finish time of end_node of a activity
backward_f=[10000]*100 #updated latest_finish time of start node of an activity

 

edge,node=map(int,input().split(' '))
# print(type (e))

# taking input from file
def take_input():
    for i in range(1,edge+1):
        id,start,dur,end=map(int,input().split(' '))
        activities[i]=Activity(id,start,end,dur)
        # print(f'id : {id}')

def forward_pass():
    for i in range(1,edge+1):
        activities[i].es=forward_f[activities[i].start]
        activities[i].ef=activities[i].es+activities[i].dur
        forward_f[activities[i].end]=max(forward_f[activities[i].end],activities[i].ef)

def backward_pass():
    # assign the lastest_finish_time of end_node of an activity (forward pass) to the backward_pass as the lastest_finish time
    backward_f[node]=forward_f[node]
    
    for i in range(edge,0,-1):
        activities[i].lf=backward_f[activities[i].end]
        activities[i].ls=activities[i].lf-activities[i].dur
        backward_f[activities[i].start]=min(backward_f[activities[i].start],activities[i].ls)
        
def display_path():
    for i in range(1,edge+1):
        if activities[i].es==activities[i].ls:
            print(chr(i+64), end=' > ')
            # print character(id)
            
def main():
    take_input()
    forward_pass()
    backward_pass()
    display_path()
    
if __name__=='__main__':
    main()       
