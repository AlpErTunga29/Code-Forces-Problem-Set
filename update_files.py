#Question from codeforces.com called Update Files

def main():

    number_of_test_cases = int( input() )

    for i in range(number_of_test_cases):

        number_of_computers, number_of_cables = input().split()
        number_of_computers = int(number_of_computers)
        number_of_cables = int(number_of_cables)

        num_computer_updated = 1
        sum_hours = 0

        while(num_computer_updated < number_of_computers):

            if num_computer_updated < number_of_cables:
                num_computer_updated += num_computer_updated

            else:
                #num_computer_updated += number_of_cables
                division = (number_of_computers - num_computer_updated) // number_of_cables
                remainder = (number_of_computers - num_computer_updated) % number_of_cables

                if division < 1:
                    sum_hours += 1

                elif remainder != 0:
                    sum_hours += division + 1

                else:
                    sum_hours += division

                break

            sum_hours += 1


        print(sum_hours)


if __name__=="__main__":
    main()
