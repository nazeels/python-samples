existing = set(['a','b'])
compare_with = set(['a','c'])
print('exisiting ' + str(len(existing)))
print('from_queue ' + str(len(compare_with)))
diff = compare_with - existing
print(diff)
