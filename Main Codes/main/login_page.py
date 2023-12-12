import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
import signup_page as sg
import employees_page as em
import pharmacist_page as ph
import reception_page as rc

icon_image = r"media\login.ico"
BG_image = r"media\main_page.gif"
excel_file = r"data\login_data.xlsx"


def load_or_create_excel_file():
    try:
        return pd.read_excel(excel_file)
    except FileNotFoundError:
        columns = {
            "id": list(), "name": list(), "phone": list(), "password": list(), "job": list(), "specialty": list()
        }
        return pd.DataFrame(columns)


class login_page:
    def __init__(self):
        # Initialize the login page window
        self.login = tk.Tk()
        self.login.geometry(f"564x400+{(self.login.winfo_screenwidth()-564)//2}+{(self.login.winfo_screenheight()-400)//2}")
        self.login.title("Login Page")
        self.login.config(bg="#ffffff")
        self.login.resizable(False, False)
        self.login.iconbitmap(icon_image)
        self.newApp = None

        # Load a background image for the login page
        self.bg_image = tk.PhotoImage(file=BG_image)
        tk.Label(self.login, width=564, height=150, image=self.bg_image, text="SIGN IN", compound="center", font=("arial", 30, "bold"), fg="#ffffff").pack()

        # Read login data from a excel file
        self.df = load_or_create_excel_file()
        self.df.to_excel(excel_file, index=False)

        # Create labels and input fields for user ID and password
        tk.Label(text="User ID: ", font=("arial", 15, "normal"), fg="black", bg="#ffffff").place(x=60, y=180)
        tk.Label(text="password: ", font=("arial", 15, "normal"), fg="black", bg="#ffffff").place(x=50, y=230)

        # Create login and signup buttons
        tk.Button(self.login, text="Login", font=("arial", 20, "bold"), borderwidth=0, bg="#00A1D1", width=10, activebackground="#ffffff", activeforeground="black", command=self.validateId).place(x=50, y=310)
        tk.Button(self.login, text="Signup", font=("arial", 20, "bold"), borderwidth=0, bg="#00A1D1", width=10, activebackground="#ffffff", activeforeground="black", command=self.signupPage).place(x=360, y=310)

        # Create input fields for user ID and password
        self.userID = tk.Entry(font=("arial", 16, "normal"), highlightthickness=4, bg="white", fg="black", relief="solid", borderwidth=0)
        self.userID.place(x=200, y=180)
        self.userID.config(highlightbackground="#00A1D1", highlightcolor="#00A1D1")
        self.password = tk.Entry(font=("arial", 16, "normal"), bg="white", highlightthickness=4, fg="black", relief="solid", borderwidth=0, show="*")
        self.password.place(x=200, y=230)
        self.password.config(highlightbackground="#00A1D1", highlightcolor="#00A1D1")

    # Method to navigate to the signup page
    def signupPage(self):
        self.login.destroy()
        self.newApp = sg.signup_page()
        self.newApp.signup_run()

    # Method to validate user ID and initiate password validation
    def validateId(self):
        if len(self.userID.get()) < 14 or len(self.userID.get()) > 14:
            messagebox.showwarning("Warning", "ID isn't valid. It should be at least 14 characters.")
            self.userID.delete(0, tk.END)
        elif int(self.userID.get()) not in self.df["id"].values:
            messagebox.showerror("Error", "ID Not Found.")
            self.userID.delete(0, tk.END)
        else:
            self.validatePass()

    # Method to validate the password and navigate to different pages based on the user's role
    def validatePass(self):
        if int(self.password.get()) not in self.df.loc[self.df["id"] == int(self.userID.get()), "password"].values:
            messagebox.showwarning("Warning", "password isn't correct. Try again, please.")
            self.password.delete(0, tk.END)
        else:
            if str(self.df.loc[self.df["id"] == int(self.userID.get()), "job"].values[0]) == "IT":
                self.login.destroy()
                new_app = em.employee_page()
                new_app.employee_run()
            elif str(self.df.loc[self.df["id"] == int(self.userID.get()), "job"].values[0]) == "pharmacist":
                self.login.destroy()
                new_app = ph.PharmacyApp()
                new_app.pharmacy_run()
            else:
                self.login.destroy()
                new_app = rc.Reception()

    def login_page_run(self):
        self.login.mainloop()


if __name__ == "__main__":
    login = login_page()
    login.login_page_run()
