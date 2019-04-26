#rotating an array
arr = [1,2,3,4]
#input
start_from = 3
#solution
index_start = arr.index(3)
# print(index_start)
result_arr = []
it_idx = 0
while(len(result_arr) < len(arr)):
    ref_idx = it_idx + index_start
    if ref_idx > len(arr) - 1:
        ref_idx = ref_idx % len(arr)
    # print(arr[ref_idx])
    result_arr.append(arr[ref_idx])
    index_start +=1

print(result_arr)

