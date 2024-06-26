def strength(password):
    conditions_local = {}
    if len(password) >= 8:
        conditions_local["length"] = True
    else:
        conditions_local["length"] = False

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    conditions_local["uppercase"] = uppercase

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    conditions_local["digit"] = digit

    if all(conditions_local.values()):
        return "Strong Password"
    else:
        return "Week password"


call = strength(input("Enter your password: "))
print(call)




