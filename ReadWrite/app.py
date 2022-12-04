# myfile = open('file.txt')


"""
content = myfile.read(10)

print(content)

myfile.seek(0)      # yete sa chgrenq, file skselua kardal en masic, vortex vor cursory kangnela (sovorabar file-i verjic)
data = myfile.read(10)

print(data)


"""
#
# content_list = myfile.readlines()
#
# myfile.close()
#
# print(content_list[0])

# WE CAN DO THIS // this open and closed file auto

# with open('file.txt') as my_file:
#     new_content = my_file.read()
# print(new_content)

#
# with open('file.txt', mode='a') as my_file:
#     my_file.write('\n THIS iS A NeW Sentence')
#
# new_appended_file = open('file.txt')
#
# print(new_appended_file.read())

item_avlb_dict = {}

myfile = open('file.txt')

item_in_stock = myfile.readlines()

myfile.close()

for item in item_in_stock:
    item_name = item.split()[0]
    item_price = item.split()[1]
    print(f"{item_name} : {item_price}")
    item_avlb_dict.update({item_name: item_price})

print(item_avlb_dict)
