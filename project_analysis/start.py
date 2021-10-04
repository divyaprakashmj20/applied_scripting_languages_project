import utils.fileprocessing as fp 
f = open("../dataset/udemy_courses.csv", "r", encoding = "utf8")

headers = fp.processHeader(f.readline())
dataset = []

for line in f:
    dataset.append(fp.processRowData(headers, line));        

