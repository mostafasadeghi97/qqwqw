

a = input().split()
print(' '.join([num for index,num in enumerate(a) if (int(num)%6==0 and ((index+1)%6==0))]))