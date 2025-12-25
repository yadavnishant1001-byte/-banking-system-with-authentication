# Simple account login/create program
import os

a = None  # stored account number (string)
b = None  # stored password (string)
Name = None
Age = None
gender = None
I = 1000

# Load account if exists
try:
    with open("account.txt","r") as f:
        data = [s.strip() for s in f.read().split(",")]
        if len(data) >= 2 and data[0] and data[1]:
            a = data[0]
            b = data[1]
            if len(data) >= 3:
                Name = data[2]
            if len(data) >= 4:
                Age = data[3]
            if len(data) >= 5:
                gender = data[4]
except FileNotFoundError:
    pass

logged_in = False
current_account = None

while True:
    print("Login Menu")
    try:
        x = int(input("Enter 0 to login, Enter 1 to create new account, Enter 2 to exit: "))
    except ValueError:
        print("Invalid input. Enter 0, 1 or 2.")
        continue

    if x == 0:
        if a is None:
            print("No account found. Please create an account first.")
            continue
        max_attempts = 3
        attempts = 0
        success = False
        back_to_menu = False
        while attempts < max_attempts:
            print("Enter 'b' at any prompt to return to the main menu.")
            A = input("Enter the account number (or 'b' to go back): ").strip()
            if A.lower() == 'b':
                print("Returning to main menu.")
                back_to_menu = True
                break
            B = input("Enter the password (or 'b' to go back): ").strip()
            if B.lower() == 'b':
                print("Returning to main menu.")
                back_to_menu = True
                break
            if A == a and B == b:
                print("Login successful ")
                print("Account:", A)
                success = True
                logged_in = True
                current_account = A
                break
            else:
                attempts += 1
                print(f"Invalid (attempt {attempts}/{max_attempts})")
        if back_to_menu:
            continue
        if success:
            break
        else:
            print("Too many failed login attempts. Returning to menu.")

    elif x == 1:
        print("Create new account (enter 'b' at any prompt to go back)")
        Name = input("Enter your name (or 'b' to go back): ").strip()
        if Name.lower() == 'b':
            print("Returning to main menu.")
            continue
        Age = input("Enter your age (or 'b' to go back): ").strip()
        if Age.lower() == 'b':
            print("Returning to main menu.")
            continue
        gender = input("Enter your gender (or 'b' to go back): ").strip()
        if gender.lower() == 'b':
            print("Returning to main menu.")
            continue
        accountnumber = input("Enter your account number (or 'b' to go back): ").strip()
        if accountnumber.lower() == 'b':
            print("Returning to main menu.")
            continue
        password = input("Enter new password (or 'b' to go back): ")
        if password.lower() == 'b':
            print("Returning to main menu.")
            continue
        password_ = input("Enter the password again: ")
        if password_ == 'b':
            print("Returning to main menu.")
            continue

        if password == password_:
            a = accountnumber.strip()
            b = password
            with open("account.txt", "w") as f:
                f.write(f"{accountnumber},{password},{Name},{Age},{gender}")
            print("Account created successfully")
            print("Please login now")
            continue
        else:
            print("Password incorrect")

    elif x == 2:
        print("Exiting program")
        break

    else:
        print("Invalid choice, try again")

# after login menu
if logged_in:
    print("Name", Name)
    print("Age", Age)
    print("Gender", gender)
    print("Your account number is", current_account)
    # Simple account menu displayed line-by-line
    while True:
        print("\nSelect an option:")
        print("1. Check balance")
        print("2. Add balance")
        print("3. Withdraw balance")
        print("4. Logout")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            print(f"Your account balance is {I}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to add: "))
                if amount > 0:
                    I += amount
                    print(f"Amount added successfully. New balance is {I}")
                else:
                    print("Enter a positive amount.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Enter a positive amount.")
                elif amount > I:
                    print("Insufficient balance")
                else:
                    I -= amount
                    print(f"Amount withdrawn successfully. New balance is {I}")
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            print("Logging out...")
            logged_in = False
            current_account = None
            break
        else:
            print("Invalid choice, try again")
else:
    print("No successful login. Program ended.")
