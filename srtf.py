import sys
print("Enter total no of processes: ")
no=int(input())
burst=[]
print("\nEnter burst time for each process: ")
for index in range(int(no)):
	n=int(input())
	burst.append(int(n))
arrive=[]
count=0
print("\nEnter arrival time for each process: ")
for index in range(int(no)):
	u=int(input())
	arrive.append(int(u))
	if(arrive[index]!=0):
		count=count+1
d=-1
num=[]
for ir in range(int(no)):
	d=d+1;
	num.append(d)
if(count==0):
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
else:
	time=0
	run=[]
	for index in range(int(no)):
		for ir in range(burst[index]):
			if(index!=4 and arrive[index+1]==time and burst[index+1]<burst[index]):
				break
			else:
				burst[index]=burst[index]-1
				time=time+1
				run[index]=time;
				
	for index in range(int(no)):
		if(burst[index]!=0):
			for iu in range(burst[index]):
				burst[index]=burst[index]-1
				time=time+1
				run[index]=time
	for i in range (no):
		print("\n No of process: " +str(num[i]) +"\t wait time: " +str(wait[i]) +"\t 	final time: "+str(run[i])) 


			

			
