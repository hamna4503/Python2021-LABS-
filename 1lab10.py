def stats(file):
    content=file.read()
    words=content.split()
    lines=content.split("\n")
    file.close()
    print("The number of lines are :",len(lines))
    print("The number of words are: ",len(words))
    print("Number of characters: ", len(content))
file1=open("d:/new.txt","r")
stats(file1)