def reverseWordSentence(Sentence):
  
    # Splitting the Sentence into list of words.
    words = Sentence.split(" ")
      
    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]
      
    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)
  
    return newSentence
  
# Driver's Code
string=input("")
s=string.split()[::-1]
l=[]
for i in s:
    l.append(i)
newsten=" ".join(l)
print(reverseWordSentence(newsten))