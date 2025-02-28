import csv
import sys

def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Invalid Input")
        return

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as database_file:
        reader = csv.DictReader(database_file)
        head_list = reader.fieldnames
        p = head_list[0]
        head_list = head_list[1:]
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variableyes
    
    with open(sys.argv[2]) as dna_file:
        dna_text = dna_file.read()


    # TODO: Find longest match of each STR in DNA sequence
    dna_dict = {}
    for i in head_list:
        dna_dict[i] = str(longest_match(dna_text,i))

    # TODO: Check database for matching profiles
    for d in rows:
        name = d[p]
        del d[p]
        if (d == dna_dict):
            print(name)
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
