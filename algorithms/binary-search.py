def binarySearch (arr,findIt,start,end):
    if( start == end or start > end):
        return -1
    # print("binary Search find %d",findIt,start,end)
    middle_idx = start + (int)((end - start)/2)
    # print(arr[ middle_idx] == findIt)
    if arr[ middle_idx] == findIt:
        return middle_idx
    elif findIt > arr[middle_idx]:
        return binarySearch(arr,findIt,middle_idx, end )
    elif findIt < arr[middle_idx]:
        return binarySearch(arr,findIt,0,middle_idx)
       
       
arr = [3,4,5,6,7]
print(binarySearch(arr,7,0,len(arr)))
print(binarySearch(arr,6,0,len(arr)))
print(binarySearch(arr,5,0,len(arr)))
print(binarySearch(arr,4,0,len(arr)))
print(binarySearch(arr,3,0,len(arr)))
