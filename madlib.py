filename = "a_raining_day.txt"
words_to_fill = ["Adjective", "Color", "Noun", "Plural_Noun", "Persons_Name", "Place", "Adverb", "Plural_Name", "Noun", "Verb", "Plural_Noun", "Plural_Noun"]

print("Fill MadLib: A Raining Day")

user_inputs = []
for word in words_to_fill:
    print(word, end='')
    user_input = input(" :")
    user_inputs.append(user_input)

with open(filename, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

title = lines[0]
content = "\n".join(lines[1:]).strip()

print(content)

for i in range(len(words_to_fill)):
    content = content.replace("[" + words_to_fill[i] + "]", user_inputs[i], 1)
print(content)