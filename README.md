# File Encryption Tool

This is a simple 'decipher :)' tool for encrypting and decrypting files using os generated key(s) from cryptography library and a Tkinter GUI.

## Setup
1. Clone the repo and navigate to the tool directory

```bash
git clone <repo_url>
cd encryption_tool
```

2. Create virtual environment and install dependancies

```bash
python -m venv venv # create venv
venv\Scripts\activate # activate venv On Linux, use source venv/bin/activate
pip install -r requirements.txt # install dependancies
```

3. Run the application

```bash
python -m gui.main
```
# Usage

Once you run the app a GUI will appear:

    -Click "Encrypt File" to browse your os for any file you want encrypted to encrypt it.
        the file will be saved with a '.enc' extension.

    -Click "Decrypt File" to browse your os for the file that is encrypted to decrypt it.
        the file will be reverted to its original form.

