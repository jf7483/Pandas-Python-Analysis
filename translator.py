import json


with open("tranzlashun.json") as file:
    data = json.load(file)


input1 = input("Enter english: ")

print(data[input1])


# create an empty list to store the translated words
translated = []

# open english word file and connecting english word to lol cat word using dictionary
# in this case data is our dictionary
# if lol cat word exists for english word append to transalted list
with open("english.txt") as eng:
    for line in eng:
        value=data.get(line.strip())
        if value is not None:
            translated.append(value)
            print (value)

# create a file to write the translated words
lol_cat = open('lol_cat.txt', 'w')

for item in translated:
    lol_cat.write(str(item) + '\n')




# lol_cat.write(str(value) + '\n')

lol_cat.close()
