import utils.masterData as md

def total(selectedColumn):
    total = 0
    for i in md.tableData:
        total = total + float(i.get(selectedColumn))
    
    print('Total of the data is: ' , total)