def get_menu_selection(menu_items):
	""" 
	Display a menu and return the user's selection
	"""
	print("\n")
	for menu_item in menu_items:
		print (menu_item)
	return input("\n Please select an option from above.  ")

def dislay_selection_error(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again \n".format (menu_selection))
	else:
		print("\n{} is not a number, please enter a number from th emenu above \n".format(menu_selection))
