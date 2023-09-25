PLACEHOLDER = "[name]"

#Extracts names from the inveted_names.txt and turnes it into a list
with open("Day40/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

#Saves the letter content as a string
with open("Day40/input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
    #Loops through the name
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"Day40/output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)