import question_d

def main():
    while True:
        num = input('Display Multiplication Table? (Y/N): ')

        if num == 'Y' or num == 'y':
            result = question_d.create_multiplication_table(5,10)
            print("Multiplication Table:")
            question_d.display_multiplication_table(result)

            while True:
                repeat_table = input("Display multiplication table again? (Y/N): ")

                if repeat_table == 'Y' or repeat_table == 'y':
                    print("Multiplication TableL")
                    question_d.display_multiplication_table(result)
                elif repeat_table == 'N' or repeat_table == 'n':
                    print("Exiting Program")
                    

        elif num == 'N' or num == 'n':
            print("Exiting Program")
            return
        else:
            print("Invalid Input")

main()    