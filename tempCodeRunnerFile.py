while 1:
    password = input("Enter the password: ").strip()
    ans = 0

    # length check
    if len(password) >= 8:
        ans += 1

    # lowercase check
    for i in password:
        if i >= 'a' and i <= 'z':
            ans += 1
            break

    # uppercase check
    for i in password:
        if i >= 'A' and i <= 'Z':
            ans += 1
            break    

    # special character check
    for i in password:
        if (33 <= ord(i) <= 47) or (58 <= ord(i) <= 64) or (91 <= ord(i) <= 96) or (123 <= ord(i) <= 126):
            ans += 1
            break

    # digit check
    for i in password:
        if i >= '0' and i <= '9':
            ans += 1
            break   

    if ans == 5:
        print("Your password is valid:", password)
        break
    else:
        print("Invalid password, try again!")
