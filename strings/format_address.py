def format_address(address_string):
    house_number = 0
    street_name = []
    address_list = address_string.split()
    for part in address_list:
        if part.isdigit():
            house_number = part
        else:
            street_name.append(part)
    return "house number {0} on street named {1}".format(house_number,' '.join(street_name))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

