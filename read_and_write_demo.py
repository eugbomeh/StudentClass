file_name = 'data.txt'
with open(file_name) as f:
    for line in f:
        print(line.strip())


record_to_add = "john,schmoe:python,ruby,javascript"



with open(file_name, "a+") as to_write:
    to_write.write("\n"+record_to_add)





