import random 

print("Welcome to CoDeco APP")

random_word=["ght","uoi","oiu","erf","xyz","hac","pak","osh","qwe"]
secret_word=(random.choice(random_word))

name = input("Enter Your Name: ")
password = input("Enter Your English Word Password Only: ")

print("Successful Login, Thanks For ❤️ ", name)

while True:
    message = input("Enter Your Message: ")
    words = message.split()

    if message == "Q":
        print("-----------CoDeco Program IS Over--------------")
        break
    else:
        pass

    coding = input("Enter 1 for Coding and 'password' for Decoding Message: ")

    if coding == "1":
        my_list_message = []
        for word in words:
            if len(word) >= 3:
                r1 = random.choice(random_word)
                r2 = random.choice(random_word)
                message_result = r1 + word[1:] + word[0] + r2
                my_list_message.append(message_result)
            else:
                my_list_message.append(word[::-1])
        print("Encoded Message:", " ".join(my_list_message))

    elif coding == password:
        my_list_message = []
        for word in words:
            if len(word) >= 9: 
                word = word[3:-3]
                message_result = word[-1] + word[:-1]
                my_list_message.append(message_result)
            else:
                my_list_message.append(word[::-1])  
        print("Decoded Message:", " ".join(my_list_message))

    else:
        print("Invalid input. Please enter '1' for coding or 'password' for decoding.")
