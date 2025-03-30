#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

formatted_name_list = []
formatted_letter = []
with open("Input/Names/invited_names.txt", "r") as file:
    unformatted_name_list = file.readlines()
    for name in unformatted_name_list:
        formatted_name_list.append(name.strip("\n"))

with open("Input/Letters/starting_letter.txt") as file:
    for line in file.readlines():
        formatted_letter.append(line)

for current_name in formatted_name_list:
    with open(f"Output/ReadyToSend/{current_name}_invite.txt", mode="w") as file:
        for line in formatted_letter:
            file.write(line.replace("[name]", current_name))