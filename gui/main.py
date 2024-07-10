import tkinter as tk
from tkinter import filedialog, messagebox
from encryption.encrypt_decrypt import encrypt_file, decrypt_file

def encrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        encrypt_file(file_path)
        messagebox.showinfo("Success", "File encrypted successfully")

def decrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        decrypt_file(file_path)
        messagebox.showinfo("Success", "File decrypted successfully")

app = tk.Tk()
app.title("File Encryption 'Decipher' Tool")

# Adding padding to buttons
button_padding = {'padx': 20, 'pady': 10}

encrypt_button = tk.Button(app, text="Encrypt File", command=encrypt_action)
encrypt_button.pack(pady=10, **button_padding)

decrypt_button = tk.Button(app, text="Decrypt File", command=decrypt_action)
decrypt_button.pack(pady=10, **button_padding)

app.mainloop()
