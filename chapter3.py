grocery_list=["apple","orange","chicken","sabudana","garam masala","cheese"]

user_input= input("what letter should we check?")
user_input= str(user_input)

for item in grocery_list:
    if item[0]== (user_input):
        print(item)
    else:
        print ("no such items here")