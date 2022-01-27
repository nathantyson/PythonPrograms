#lab 8

#Nathan Tyson


def number_of_words():
    infile_name = open("test.txt", "r")
    data = infile_name.read()
    outfile_name = open("output.txt", "w")
    
    print(data, file=outfile_name)
    #
    # # infile_name.close()
    # # outfile_name.close()


def main():
    number_of_words()

main()