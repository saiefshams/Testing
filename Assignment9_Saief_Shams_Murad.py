import time
def filePulling():
    fileInp = open("inp_file.txt", "w")
    fileInp.write("Python is an interpreted, high-level, and general-purpose programming language.")
    fileInp.close()
    file1 = input("Enter the input file: ")
    file2 = input("Enter the output file: ")
    print("\n\nDisplaying the contents of the input file...\n")
    fileInp = open(file1, "r")
    print(fileInp.read())
    fileInp.close()
    try:
        fileOut = open(file2, "r")
        print(fileOut.read())
        fileOut.close()
    except:
        print('\n\n{} {}'.format(file2, "does not exist!!!"))
    print("\n\n#################################After copying from input to output file##############################\n")
    lineCount1 = 0
    fileInp = open(file1, "r")
    content1 = fileInp.read()
    lineN1 = content1.split("\n")
    charN1 = 0
    for line in lineN1:
        lineCount1 += 1
        charN1 += len(line)
    #print(charN)
    #print(lineCount)
    fileOut = open(file2, "w")
    for line in content1:
        fileOut.write(line)
    fileOut = open(file2, "r")
    #print(fileOut.read())
    print(lineCount1, "line and", charN1, "chars have been copied to the output file")
    fileOut.close()
    fileInp.close()
    fileOut = open(file2, "a")
    fileOut.write("\nIt was created by Guido van Rossum and first released in 1991.")
    fileOut = open(file2, "r")
    lineCount2 = 0
    content2 = fileOut.read()
    lineN2 = content2.split("\n")
    charN2 = 0
    for line in lineN2:
        lineCount2 += 1
        charN2 += len(line)
    print("\n\n#################################After appending to the output file##############################\n")
    print("Updated count of lines in the output file is: ", lineCount2)
    print("Updated count of characters in the output file is: ", charN2)
    print("\n\nDisplaying the contents of the output file...\n")
    print(content2)
    fileOut.close()
    time.sleep(30)
filePulling()