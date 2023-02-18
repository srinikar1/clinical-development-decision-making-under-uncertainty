
def write_to_file (string):

    f = open("Block Detail.csv", "a")
    f.write(string + '\n')
    f.close()
    pass
