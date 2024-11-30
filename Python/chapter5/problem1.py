#Write a programme To create a dictionary of Hindi words with values as their English translation.
#Provide user  with an option to look into it

words={
    "machli":"fish",
    "billi":"cat",
    "chuha":"rat"
}
word=input("Enter the word:")
print(f"The english meaning of {word} is : {words[word.lower()]}")

#.lower() function conbert all words in lowercase and .upper() convert all in uppercase!