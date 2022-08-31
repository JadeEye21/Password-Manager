import base64
import json
import maskpass

flag = True
f = open("password.json", 'a+')
while(flag):
    cond = input("Do you want to add or search(A/B): ")
    if(cond == 'A'):
        site = input("Input site name: ")
        username = input("Input username: ")
        password = maskpass.askpass(prompt="Enter password: ")
        # password = base64.b64encode(password)
        inputData = {site:[username, password]}
        json.dump(inputData, f)


    elif(cond=='B'):
        site = input("Enter site: ")
        # with open("password.json", 'r') as f:
        out = json.load(f)
        try:
            print("Username: ", out[site][0])
            print("Password: ", out[site][1])

        except KeyError:
            continue
    else:
        print("Wrong choice")

    check = input("Key not present or wrong keyword, do you want to restart (Y/N): ")
    if check == 'N':
        flag = False
    else:
        continue
f.close()
# data = {"gmail": ["harshadsonu62@gmail.com", "password"]}
# with open("password.json", 'w') as f:
#     json.dump(data, f)
#
# with open("password.json", 'r') as f:
#     out = json.load(f)
#
# print(out["gmail"][0],"\n",out["gmail"][1])