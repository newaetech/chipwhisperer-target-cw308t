import sexpdata 
import pandas as pd
import numpy as np
import pprint #for testing 
import sys
import func
import copy

'''
Script that imports parts from a spread sheet to a kicad library file 

template part being used must contain data in all of the fields in the spreadsheet 
inorder for all data to be included. 

script call: python KiCAD_Script.py path_to_library template_symbol spreadsheet_name
'''

"""main"""
if __name__ == '__main__':

	file_path = sys.argv[1]
	template_name = sys.argv[2]
	spreadsheet_name = sys.argv[3]
	spreadsheet_path = "spreadsheets/"+ spreadsheet_name

	file_to_write_to = copy.deepcopy(file_path)

	#Read the contents of the file
	with open(file_path, 'r') as file:
	    file_contents = file.read()

	#get first substring of the split string i.e. name of file without type
	file_name = file_path.split(".")[0] 

	file_backup = file_name + ".bak"

	backup = open(file_backup, "a")

	backup.write(file_contents)

	# Load the contents using sexpdata
	lib_list = sexpdata.loads(file_contents)

	lib_length = len(lib_list)

	print("LIB_LENGTH", lib_length)

	template = func.find_template(lib_list, template_name)

	#open excel sheet 
	spreadsheet = pd.read_excel(spreadsheet_path)
	spreadsheet = spreadsheet.replace(np.nan, "no_data")

	sp_length = len(spreadsheet)

	row_index = 0 
	file_row = 0
	last_description = None

	data_format_error = False

	lib_file_count = 1 #keep track of number of library files - if keeping the split library if 250 items reached

	row_limit = 250 - lib_length

	while row_index < sp_length and not data_format_error: 
		#create copy that will not be linked at all to previous changes
		copy_template = copy.deepcopy(template)

		row = spreadsheet.loc[row_index, :] #get data from row 

		row_index += 1

		file_row += 1

		data_row = row.to_dict() 

		#determine if there are any formatting issues in the spreadsheet data 
		error_flag = func.find_formatting_error(data_row) 
		if error_flag == True: 
			raise Exception(f"error in data (row {row_index + 1}). data can not contain commas and can not be blank (other than supplier 2 fields)")

		current_description = data_row["Description"]

		if current_description != last_description:
			#call function to store data in template
			part = func.store_in_template(copy_template, data_row, template_name)

		last_description = current_description
		
		#kicad libraries should contain no more than 250 parts
		#if this limit is reached open a second library file 
		if file_row == row_limit:
			#dump current lib
			s_exp_library = sexpdata.dumps(lib_list)
			
			#append s expressions to original file 
			with open(file_to_write_to, 'w') as file:
				file.seek(0)
				file.write(s_exp_library)

			total_length = 0 #reset for new lib file
			file_to_write_to = file_name + f"{lib_file_count}" + ".kicad_sym"

			lib_file_count += 1 
			
			lib_list.clear()#clear lib list 

			row_limit = 250 
			file_row = 0 #set to beginning of file

		#append template to library obj
		lib_list.append(part)

	s_exp_library = sexpdata.dumps(lib_list)

	with open(file_to_write_to, 'w') as file:
		file.seek(0)
		file.write(s_exp_library)

