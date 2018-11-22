import sys
count=0
t=0
r=0
flag=0
time_slice=0
wait=0
turnaround=0
arrive=[]
burst=[]
remain=[]
print("Enter total number of processes: ")
no=int(input())
r=int(no)
print("\nEnter  burst time for each process: ")
for count in range(int(no)):
	n=int(input())
	burst.append(int(n))
	remain.append(burst[count])
count=0
n=0
print("\nEnter arrival time for each process:")
for count in range(int(no)):
	n=int(input())
	arrive.append(int(n))
print("\nEnter time slice value:")
time_slice=int(input())
print("\nProcess\t  Turnaround Time\tWaiting Time\n")
count=0
while(r!=0):
	if(remain[count]<=time_slice and remain[count]>0):
		t+=remain[count];
		remain[count]=0
		flag=1
	elif(remain[count]>0):
		remain[count]-=time_slice
		t+=time_slice
	if(remain[count]==0 and flag==1):
		r=r-1
		print("P"+str(count+1)+"\t\t"+str(t-arrive[count])+"\t\t"+str(t-arrive[count]-burst[count]))
		wait+=t-arrive[count]-burst[count]
		turnaround+=t-arrive[count]
		flag=0
	if(count==int(no-1)):
		count=0
	elif(arrive[count+1]<= t):
		count=count+1
	else:
		count=0
print("\nAverage waiting time: " +str(wait*1.0/no))
print("\nAverage turnaround time: " +str(turnaround*1.0/no))

