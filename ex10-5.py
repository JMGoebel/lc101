# Note: The pass is a placeholder to allow
# the code to compile. Remove it when you
# begin coding.

new_inventory = {}

def set_inventory(inventory, fruit, quantity=0):
    inventory[fruit] = quantity

# make these tests work...
# new_inventory = {}
set_inventory(new_inventory, 'strawberries', 10)
print('strawberries' in new_inventory)
print(new_inventory['strawberries'])
set_inventory(new_inventory, 'strawberries', 25)
print(new_inventory['strawberries'])