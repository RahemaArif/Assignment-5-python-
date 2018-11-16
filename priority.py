import sys
print("Enter the total number of processes: ")
no=int(input())
burst=[]
print("\nEnter the burst time for each process: ")
for index in range(int(no)):
	n=int(input())
	burst.append(int(n))
priorityq=[]
print("\nEnter priority of each process: ")
for ind in range(int(no)):
	h=int(input())
	priorityq.append(int(h))
burst2=[]
for ir in range(int(no)):
	num=int(priorityq[ir])
	burst2.append(burst[num])
for element in burst2:
	print(element)
wait=[]
turnaround=[]
avg_wait=0
avg_turnaround=0
dt=0
for ind in range(len(burst2)):
	if ind==0 :
		wait.append(0)
	else:
		wait.append(wait[ind-1]+burst2[ind-1])
	
	turnaround.append(wait[ind]+burst2[ind])
	avg_wait=avg_wait+wait[ind]
	avg_turnaround=avg_turnaround+turnaround[ind]
avg_wait=avg_wait/no
avg_turnaround=avg_turnaround/no
for i in range (no):
	print("\n No of process: " +str(priorityq[i]) +"\t wait time: " +str(wait[i])+"\tturnaroundtime: "+str(turnaround[i])) 
print("\nAverage wait time: " + str(avg_wait))
print("\nAverage turnaround time: " +str(avg_turnaround))
