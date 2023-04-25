first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"

new_string = "R"
fixed_first_name = new_string+first_name[1::-1] + " " + last_name
print(fixed_first_name)
