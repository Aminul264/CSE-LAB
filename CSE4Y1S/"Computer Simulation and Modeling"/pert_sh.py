import sys

sys.stdin = open('pert_sh.txt', 'r')
MX = 1000

class Activity:
	def __init__(self, id, start, end, dur) -> None:
		self.start = start
		self.id = id
		self.end = end
		self.dur = dur
		self.es = 0
		self.ef = 0
		self.ls = 0
		self.lf = 0

n, m = map(int, input().split(' '))

activities = {}
node_f = [0]*100
node_r = [0]*100

for i in range(1, n + 1): # 1<=n
	id, start, dur, end = map(int, input().split())
	activities[i] = Activity(id, start, end, dur)


for i in range(1, n + 1):
	activities[i].es = node_f[activities[i].start]  # est(k) = ent(s(k))
	activities[i].ef = activities[i].es + activities[i].dur  # eft(k) = est(k) + t(k)
	node_f[activities[i].end] = max(node_f[activities[i].end], activities[i].ef)


# backward pass calculation
for i in range(1,m + 1): #  1<=m
	node_r[i] = 100 # mx value initilize

node_r[m] = node_f[m] 

for i in range(n, 0, -1):
	activities[i].lf = node_r[activities[i].end]  
	activities[i].ls = activities[i].lf - activities[i].dur  
	node_r[activities[i].start] = min(node_r[activities[i].start], activities[i].ls)  

for i in range(1, n + 1):
	if activities[i].es == activities[i].ls and activities[i].lf == activities[i].ef:
		print(i, end=" > ")
