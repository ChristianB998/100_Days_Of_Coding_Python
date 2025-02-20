# Please don't read the comments and print statements. Bit the temper today.

# FileNotFound

# try:
#     file = open("a_file.txt") # will cause error, we don't have it
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asdfgh"]) # will not work, dosn't exist, again.
# except FileNotFoundError:
#     #print("Surprise, there was an error. Who would have expected this.")
#     file = open("a_file.txt", "w")
#     file.write("Write something in this empty txt file. Now!!!")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist. Look in the a_dictionary, where is this key !!!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     #file.close()
#     #print("File was closed. What else? Who wrote this, everytime I need to close it. Thank god the with ... exists")
#     raise TypeError("This is an error that I made up. Funny")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# Test 1
# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")
#
# make_pie(4)

# Test 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
#
# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             pass
#     return total_likes
#
#
# count_likes(facebook_posts)


