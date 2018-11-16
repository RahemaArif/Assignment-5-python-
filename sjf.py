import sys
print("Enter the total number of processes: ")
no=int(input())
num=[]
d=-1
for ir in range(int(no)):
	d=d+1;
	num.append(d)
burst=[]
print("\nEnter the burst time for each process: ")
for index in range(int(no)):
	n=int(input())
	burst.append(int(n))
for ind in range(int(no)):
	for io in range(0,int(no)-ind-1):
		if burst[io+1]<burst[io]:
			temp=burst[io]
			burst[io]=burst[io+1]
			burst[io+1]=temp
			n1=num[io]
			num[io]=num[io+1]
			num[io+1]=n1
wait=[]
turnaround=[]
avg_wait=0
avg_turnaround=0
dt=0
for ind in range(len(burst)):
	if ind==0 :
		wait.append(0)
	else:
		wait.append(wait[ind-1]+burst[ind-1])
	
	turnaround.append(wait[ind]+burst[ind])
	avg_wait=avg_wait+wait[ind]
	avg_turnaround=avg_turnaround+turnaround[ind]
avg_wait=avg_wait/no
avg_turnaround=avg_turnaround/no
for i in range (no):
	print("\n No of process: " +str(num[i]) +"\t wait time: " +str(wait[i]) +"\t turnaround time: "+str(turnaround[i])) 
print("\nAverage wait time: " + str(avg_wait))
print("\nAverage turnaround time: " +str(avg_turnaround))
