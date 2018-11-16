import sys
print("Input the total no of processes:")
no=int(input())
print("\nInput the burst time for each process:")
burst=[]
for index in range(int(no)):
	n=int(input())
	burst.append(int(n))
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
	print("\n No of process: " +str(i) +"\t wait time: " +str(wait[i]) +"\t turnaround time: "+str(turnaround[i])) 
print("\nAverage wait time: " + str(avg_wait))
print("\nAverage turnaround time: " +str(avg_turnaround))
