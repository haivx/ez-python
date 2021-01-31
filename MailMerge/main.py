PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        tripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, tripped_name)
        with open(f"./Output/ReadyToSend/starting_letter_{tripped_name}.txt", mode="w") as file:
            file.write(new_letter)

