#wap to read the file from a  given file "poem.txt" and find if the file contain the word twinkle

with open ("poem.txt") as f:
    content=f.read()
    print(content)
    if ("twinkle" in content):
         print("Twinkle is present!")
    else:
         print("Twinkle is not present!")