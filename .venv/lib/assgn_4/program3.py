import customer

Scott = customer.Customer("Scott", "Quashen", "scottquashen.sq@gmail.com")
print(Scott.first_name)

# this works because we defined in the customer class how the object is iterated over - not iterable by default
for item in Scott:
    print(item)
