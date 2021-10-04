# import utils.fileprocessing as fp 
# import utils.masterData as md
import utils.settings as settings
import processings.numericAnalysis as numaly


settings.initializeData()


while True:
    selection = input(
       '''Choose the operation
1. Analyse a variable
2. Analyse by category using dictionary
3. Analyse  by Date  using  Regular  Expressions''')
          
    if selection == '1':
        numaly.analyse()

    
    if input('''Do you wish to Continue(Y/N)''') == 'N':
        break

          










