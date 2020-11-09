import random

def main():
    continuing = True
    instructions()

    while continuing == True:

        rolls = []
        rolls_string = ''
        input_string = input("What do you want to roll?: ")  

        if input_string == 'quit' or input_string == 'Quit':
            continuing = False
        else:
            #try blocks to see if input formatted correctly
            try:
                split_string = input_string.split("d")
            except:
                instructions()
            else:
                try:
                    number_of_rolls = int(split_string[0])
                except:
                    instructions()
                else:
                    try:
                        d_type = int(split_string[1])
                    except:
                        instructions()
                    else:
                        #rolls the chosen dice the specified number of times
                        for _ in range(number_of_rolls):
                            rolls.append(random.randint(1, d_type))
                        #joins the rolls into a printable string
                        for i in rolls:
                            rolls_string += ''.join(str(i)) + ' '
                        #prints the sum total of the rolls followed by each individual roll
                        print(f"You rolled {sum(rolls)}: {rolls_string}")
            
def instructions():
    print("Please enter the number of rolls followed by the dice you wish to roll.")
    print("For example '3d12' would be three rolls of a twelve sided dice (d12).")
    print("Or enter 'quit' to quit.")

main()
        