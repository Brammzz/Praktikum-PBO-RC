import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.boxlogin = tk.Tk()
        self.boxlogin.title('Login')
        self.boxlogin.geometry('300x200')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.boxlogin, text='Username:').pack()
        tk.Entry(self.boxlogin, textvariable=self.username).pack()

        tk.Label(self.boxlogin, text='Password:').pack()
        tk.Entry(self.boxlogin, textvariable=self.password, show='*').pack()

        tk.Button(self.boxlogin, text='Login', command=self.checking_on).pack()
        tk.Button(self.boxlogin, text='Register', command=self.open_register).pack()

        self.users = {}
        self.registered = False

    def checking_on(self):
        if not self.registered:
            messagebox.showinfo('Info', 'Anda belum mendaftarkan akun. Silakan daftar terlebih dahulu.')
            return

        if self.username.get() in self.users and self.password.get() == self.users[self.username.get()]:
            messagebox.showinfo('Successful', 'Input benar, Anda Berhasil Login')
        else:
            messagebox.showerror('Error', 'Usernamenya atau Password yang anda masukkan salah')

    def open_register(self):
        self.boxlogin.withdraw()
        self.jendela_register = Register(self.boxlogin, self.users, self)
        self.jendela_register.jendela.protocol("WM_DELETE_WINDOW", lambda: self.close_register())
        self.jendela_register.mainloop()

    def close_register(self):
        self.boxlogin.deiconify()

    def run(self):
        self.boxlogin.mainloop()

class Register:
    def __init__(self, master, users, login_ref):
        self.master = master
        self.users = users
        self.login_ref = login_ref

        self.jendela = tk.Toplevel(self.master)
        self.jendela.title('Register')
        self.jendela.geometry('300x300')

        self.username_register = tk.StringVar()
        self.password_register = tk.StringVar()
        self.cek_password = tk.StringVar()

        tk.Label(self.jendela, text='Username:').pack()
        self.username_entry = tk.Entry(self.jendela, textvariable=self.username_register)
        self.username_entry.pack()

        tk.Label(self.jendela, text='Password:').pack()
        self.password_entry = tk.Entry(self.jendela, textvariable=self.password_register, show='*')
        self.password_entry.pack()

        tk.Label(self.jendela, text='Confirm Password:').pack()
        self.cek_password_entry = tk.Entry(self.jendela, textvariable=self.cek_password, show='*')
        self.cek_password_entry.pack()

        tk.Button(self.jendela, text='Register', command=self.register_button).pack()

    def register_button(self):
        username = self.username_register.get()
        password = self.password_register.get()
        confirm_password = self.cek_password.get()

        if not username or not password or not confirm_password:
            messagebox.showerror('Error', 'Silahkan isi semua kolom')
            return

        if password != confirm_password:
            messagebox.showerror('Error', 'Konfirmasi password tidak sesuai')
            return

        if self.username_own(username):
            messagebox.showerror('Register Failed', 'Username sudah digunakan')
            return

        self.users[username] = password
        messagebox.showinfo('Register Success', 'Akun telah berhasil didaftarkan')
        self.login_ref.registered = True
        self.jendela.destroy()
        self.login_ref.boxlogin.deiconify()

    def username_own(self, username):
        return username in self.users


login = Login()
login.run()
