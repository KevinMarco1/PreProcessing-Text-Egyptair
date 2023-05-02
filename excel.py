from pathlib import Path
import openpyxl 
import os

# template of excel sheet
template = ["Reservation number" ,	"COMPANY NAME" , 	"NM" ,	"MS" ,	"Character" ,
"DATE" ,	"ROUTH" ,	"HK" ,	 "MS" , "ROUTH" ,  "DATE" ,	"APM" ,	"APE" ,]

# files
def fileIsExist(abs_path):
    my_file = Path(abs_path)
    if my_file.exists():
        return True
    else:
        return False

def createFile(abs_path):
    f = open(abs_path , 'w')
    f.write("2")
    f.close()
    

def getCurrentDirectory(name_of_file):
    new_list = __file__.split('\\')
    new_list.pop()
    new_list.append(name_of_file)
    abs_path = "\\".join(new_list)
    return abs_path
    

def getIndexFromFile(name_of_file):
    index = 2
    abs_path = getCurrentDirectory(name_of_file)
    if fileIsExist(abs_path):
        f = open(abs_path , 'r')
        index = f.read()
        f.close()
    else:
        createFile(abs_path)
    return index  

def incrementIndexOfFile(name_of_file , index):
    abs_path = getCurrentDirectory(name_of_file)
    f = open(abs_path , 'w')
    f.write(str(index + 1))
    f.close()

# sheet
def putDataIntoRowInExcel(sheet , index , data ):
    for col , value in enumerate(data):
        sheet.cell(row = index , column = col + 1 , value = value)
        

def createTemplateOfExcel(sheet, template):
    for i in range(0 , len(template)):
        sheet.cell(row = 1 , column = i + 1 , value = template[i])
        sheet.cell(row = 1, column =  i + 1).font = openpyxl.styles.Font(size = 14, bold = True)
    # Set the default row height to 20 and the default column width to 10
    sheet.sheet_format.defaultRowHeight = 25
    sheet.sheet_format.defaultColWidth = 30    

def getExcelSheet(name_of_file):
    sheet = None
    abs_path = getCurrentDirectory(name_of_file)
    # Check if file exists
    if fileIsExist(abs_path):
        # Create new workbook object
        wb = openpyxl.load_workbook(abs_path)
        # active sheet 
        sheet = wb.active
        
    else:
        # Create new workbook object
        wb = openpyxl.Workbook()
        # active sheet 
        sheet = wb.active
        # Set default row height and column width
        
        # create template
        createTemplateOfExcel(sheet , template)
        # Save workbook to file
        wb.save(abs_path)
    
    return wb , sheet
    

        
def fillDataIntoExcelSheet(data):
    name_of_file = "number_of_rows.txt"
    index = int(getIndexFromFile(name_of_file))
    
    name_of_excel_sheet = 'reservations.xlsx'
    
    wb , sheet = getExcelSheet(name_of_excel_sheet)
    
    putDataIntoRowInExcel(sheet , index , data)
    wb.save(getCurrentDirectory(name_of_excel_sheet))
    
    incrementIndexOfFile(name_of_file , index)
    
    






