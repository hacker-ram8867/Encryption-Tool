from encryptor import encrypt_file, decrypt_file
from pdf_encryptor import encrypt_pdf

def main():
    print("🔐 File Encryption Tool")
    print("-----------------------")
    print("1. Encrypt any file (text, audio, image, video, etc.)")
    print("2. Decrypt any encrypted file (.enc)")
    print("3. Encrypt PDF with password")
    print("0. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        filepath = input("Enter path to file: ").strip()
        password = input("Enter password to encrypt: ").strip()
        encrypt_file(filepath, password)
    elif choice == '2':
        filepath = input("Enter path to encrypted file (.enc): ").strip()
        password = input("Enter password to decrypt: ").strip()
        decrypt_file(filepath, password)
    elif choice == '3':
        input_pdf = input("Enter path to PDF file: ").strip()
        output_pdf = input("Enter output encrypted PDF filename: ").strip()
        password = input("Enter password for PDF encryption: ").strip()
        encrypt_pdf(input_pdf, output_pdf, password)
    elif choice == '0':
        print("Thankl you for using my encryption toll")
        exit(0)
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    while True:
        main()
        print()
