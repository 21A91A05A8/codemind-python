def CountingEvenOdd(arr,arr_size):
    even_count=0
    odd_count=0
    for i in range(arr_size):
        if(arr[i] & 1 ==1):
            odd_count+=1
        else:
            even_count+=1
    print(even_count,odd_count) 
n=int(input())
arr=list(map(int,input().split()))
CountingEvenOdd(arr,n)