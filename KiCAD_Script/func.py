import pprint
import numpy as np

'''
Parses the list of s expressions to find the template part 

@params:
	- lib_list: nested list of data from library file 
	- template_symbol: name of template part to be used (string)
@returns: 
	- template: template part to be copied (list)
'''
def find_template(lib_list, template_symbol): 
	index = 0
	for item in lib_list:
		symbol_name = item[1]
		if symbol_name == template_symbol:
			template = lib_list[index] #get template 
		index += 1

	return template


'''
store data from excel sheet in copy of template part 

@params: 
	- template: template part as a nested list 
	- data_row: dictionary containing data for part to be copied 
	- template_name: name of the template part being used
@returns: 
	- part: template list with updated data from data_row
'''
def store_in_template(template, data_row, template_name): 
	outer_index = 0
	
	for item in template: 
		
		length = len(template[outer_index])

		if 'symbol' in template[outer_index]:
			template[outer_index + 1] = data_row["Refs"]

		inner_index = 0
		#might try to change this so the fields are in a tuple and it just loops through the entire tuple to see if it is found

		while inner_index < length: 
			try:
				if template[outer_index][inner_index].strip() == "symbol":
					name = template[outer_index][inner_index + 1].split(template_name)
					new_name = data_row["Refs"] + name[1]
					template[outer_index][inner_index + 1] = new_name

			except AttributeError:
				pass
			except IndexError:
				pass

			if template[outer_index][inner_index] == "Datasheet":
				template[outer_index][inner_index + 1] = data_row["Datasheet"]

			if template[outer_index][inner_index] == "Description":
				template[outer_index][inner_index + 1] = data_row["Description"]

			if template[outer_index][inner_index] == "Footprint":
				template[outer_index][inner_index + 1] = data_row["Footprint"]

			if template[outer_index][inner_index] == "Manufacturer":
				template[outer_index][inner_index + 1] = data_row["Manufacturer"]

			if template[outer_index][inner_index] == "Manufacturer Part Number":
				template[outer_index][inner_index + 1] = data_row["Manufacturer Part Number"]

			if template[outer_index][inner_index] == "Reference":
				template[outer_index][inner_index + 1] = data_row["Reference"]

			if template[outer_index][inner_index] == "Display Value":
				template[outer_index][inner_index + 1] = data_row["Display Value"]

			if template[outer_index][inner_index] == "Supplier 1":
				template[outer_index][inner_index + 1] = data_row["Supplier 1"]

			if template[outer_index][inner_index] == "Supplier 1 Part Number":
				template[outer_index][inner_index + 1] = data_row["Supplier 1 Part Number"]

			if template[outer_index][inner_index] == "Supplier 2":
				template[outer_index][inner_index + 1] = data_row["Supplier 2"]

			if template[outer_index][inner_index] == "Supplier 2 Part Number":
				template[outer_index][inner_index + 1] = data_row["Supplier 2 Part Number"]

			if template[outer_index][inner_index] == "Value":
				template[outer_index][inner_index + 1] = data_row["Value"]

			if template[outer_index][inner_index] == "ki_keywords":
				template[outer_index][inner_index + 1] = data_row["ki_keywords"]
			inner_index += 1

		outer_index += 1

	return template


'''
determine if there is any data formatting errors in a row of data 

@params: 
	- data_row: dictionary containing data for part to be copied 
@returns: 
	- error: bool 
'''
def find_formatting_error(data_row):
	error = False
	comma = -1

	for key, value in data_row.items():
		try: 
			comma = value.find(',')
		except AttributeError:
			pass

		if value == "no_data" and key != "Supplier 2 Part Number" and key != "Supplier 2":
			error = True

		if comma == 1: 
			error = True

	return(error)



