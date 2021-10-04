def processHeader(string):
    arr = string.split(',')
    # print(arr)
    arr[len(arr)-1] = arr[len(arr)-1][:-1]
    return arr

def processRowData(headers, line):
    arr = line.split(',')
    arr[len(arr)-1] = arr[len(arr)-1][:-1]
    data = {}
    for i in range(10):
        data.update({headers[i] : arr[i]})
    
    return data;

