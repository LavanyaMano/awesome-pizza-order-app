PIZZAS = (
	{
	"name": "Cheese Pizza",
	"cost": 5.00
	},
	{
	"name": "Pepperoni Pizza",
	"cost": 7.50
	},
	)
my_pizzas = []

def display_invalid_option(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again \n". format (menu_selection))
	else:
		print("\n{} is not a number, please enter a number from th emenu above \n". format(menu_selection))

def is_valid_pizza(pizza_selection,pizzas):
	return pizza_selection.isdigit() and int(pizza_selection)-1 < len(pizzas)

def display_pizzas(pizzas):
	if len(pizzas)>0:
		for index, pizza in enumerate(pizzas):
			print ("{}: {} cost: ${:,.2f}". format(index+1, pizza["name"],pizza["cost"]))
	else:
		print ("Pizza not found")


def display_total_cost(pizzas):
	total_cost = sum ([pizza["cost"] for pizza in pizzas])
	print("*"*30)
	print("Total Cost: ${:,.2f}".format(total_cost))

def display_order(pizzas):
	display_pizzas(pizzas)
	display_total_cost(pizzas)
	print("\n\n")

def order_pizza():
	global my_pizzas
	if len(my_pizzas)>0:
		print ("Thank you for your order!\n")
		my_pizzas=[]
	else:
		print("Please add pizzas to your order before completing the order\n")
		return False

def add_to_order():
	""" Prompts for adding pizza to the order """
	while True:
		print ("\n")
		display_pizzas(PIZZAS)
		print("0: Go back")
		pizza_selection = input ("\n Which pizza would you like to order")
		
		if pizza_selection== "0":
			break
		elif is_valid_pizza(pizza_selection,PIZZAS):
			my_pizzas.append(PIZZAS[int(pizza_selection)-1])
		else:
			display_invalid_option(pizza_selection)

def remove_from_order():
	"""Remove a pizza from my_pizzas based on user's input"""
	global my_pizzas
	while True:
		print ("\n")
		display_order(my_pizzas)
		print("0: Go back")

		pizza_selection = input ("\n Which pizza would you like to remove")
		
		if pizza_selection== "0":
			break
		elif is_valid_pizza(pizza_selection,my_pizzas):
			del my_pizzas[int(pizza_selection)-1]
			# my_pizzas.append(PIZZAS[int(pizza_selection)-1])
		else:
			display_invalid_option(pizza_selection)

					


def main():
	
	MENU_ITEMS = (
		"Menu Selection:",
		"1: Add Pizza to Order",
		"2: Remove Pizza from Order",
		"3: Display Order",
		"4: Order Pizza",
		"0: Exit",
		)

	while True:
		for Menu_item in MENU_ITEMS:
			print(Menu_item)

		menu_selection = input ("\n Please select an option from above?")
		
		if menu_selection == "0":
			break
		elif menu_selection == "1":
			add_to_order()
		elif menu_selection == "2":
			remove_from_order()
		elif menu_selection == "3":
			display_order(my_pizzas)
		elif menu_selection == "4":
			display_order(my_pizzas)
			order_pizza()
		else:
			display_invalid_option(menu_selection)

if __name__ == '__main__':
	main()
