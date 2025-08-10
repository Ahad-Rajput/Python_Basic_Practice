'''
A spam comment is defined as a text containg
following keywords:
"Make a lot of money", "subscribe this", "buy now", "click this"

Detect these spam
'''

spam1 = "make a lot of money"
spam2 = "subscribe this"
spam3 = "buy now"
spam4 = "click this"

msg = input("Enter your comment: ")

if((spam1 in msg.lower()) or (spam2 in msg.lower()) or (spam3 in msg.lower()) or (spam4 in msg.lower())):
    print("This is a spam comment!")
else:
    print("This is not a spam comment.")