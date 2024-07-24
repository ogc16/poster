tweet = input()
try:
 if len(tweet) > 42:
    raise ValueError("Tweet length exceeds 42 characters")
except:
    print("Error")
else:
    print("Posted")
