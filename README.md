# 🔐 Advanced Password Generator

A customizable password generator built with Python.

## Features
- Generate a password with a custom number of **alphabets**, **digits**, and **symbols**
- Password is **randomized** and **shuffled** to ensure maximum security
- **Automatically copies** the generated password to clipboard for easy use (Linux support via `xclip`)
- Simple to use with a **command-line interface**

## How to Run
1. **Clone the repository:**

   ```bash
   git clone https://github.com/Hardikjain09/password-generator.git
   cd password-generator

    Set up your environment:

        Install dependencies:

    pip install pyperclip
    sudo apt install xclip  # for Linux users

Run the script:

    python password_generator.py

    Input:

        Enter the number of alphabets, digits, and symbols you want in your password.

    Result:

        The script will generate a random password based on your input and automatically copy it to your clipboard.

Example Output

Enter the number of alphabets: 4 
Enter the number of digits: 2 
Enter the number of symbols: 2 
Your password is: hT9$a8Yp \n
🔁 Password copied to clipboard! 

Author

Made with ❤️ by Hardik Jain
