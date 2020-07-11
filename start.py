import login_functions as func

print("Enter login or register [l\\r]")
status = input()

if status == "l":
    func.login()
elif status == "r":
    func.register()
else: 
    print("Invalid status!")

exit()