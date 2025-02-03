with open("my_file.txt", mode = "r") as file:
    contents = file.read()
    print(contents)
    #file.close()   # need to close the file, as we use resources during the opened time
                    # to not forget it we use "with open(file) as file" to save it. Normally its forgotten to close it
with open("my_file.txt", mode="a") as file: # w is writing, a is appending like in a list in the past
    file.write("\nNew text.")