
with open("Day 24/Mail Merge Project/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    

with open("Day 24/Mail Merge Project/Input/Letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        invite_name = letter_content.replace("[name]", stripped_name)
        with open(f"Day 24\Mail Merge Project\Output\Ready_to_Send\letter_for_{stripped_name}.docx", mode = "w") as completed_letter:   #Automatically created the number of file.docx for the given number of names.
            completed_letter.write(invite_name)



