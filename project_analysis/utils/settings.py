import utils.fileprocessing as fp
import utils.masterData as md


def initializeData():
    f = open("../dataset/udemy_courses.csv", "r", encoding = "utf8")

    headers = fp.processHeader(f.readline())

    dataset = []

    for line in f:
        dataset.append(fp.processRowData(headers, line))

    md.tableData = dataset;  
