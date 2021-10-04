import utils.masterData as md
import processings.calculations as calc

def analyse():
    numericHeaders = []
    for i in md.headersAndType:
        if list(i.values())[0] == 'int' or list(i.values())[0] == 'float':
            numericHeaders.append(i)

    count = 0

    print('\n\nSelect column to analyse:')
    for i in numericHeaders:
        print(count+1 , list(i.keys())[0])
        count = count + 1

    selectedColumn = list(numericHeaders[int(input())-1].keys())[0]
    print(selectedColumn)

    print('''\n\n\nSelect what to analyse:
1.All
2.number of values
3.Total
4.Mean''')

    selectedOperation = input()

    if selectedOperation == '1':
        print('number of data is: ',len(md.tableData))
        calc.total(selectedColumn)
        # mean()
    elif selectedOperation == '2':
        print('number of data is: ',len(md.tableData))
    elif selectedOperation == '3':
        calc.total(selectedColumn)
    elif selectedOperation == '4':
        print('test')
        # mean()

    
