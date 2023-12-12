import login_page as lg
from login_page import ttk, tk, pd, messagebox

icon_image = r"media\signup.ico"
BG_image = r"media\main_page.gif"
excel_file = r"data\login_data.xlsx"


class signup_page:
    def __init__(self):
        # Initialize the signup page window
        self.signup = tk.Tk()
        self.signup.geometry(f"564x400+{(self.signup.winfo_screenwidth() - 564) // 2}+{(self.signup.winfo_screenheight() - 400) // 2}")
        self.signup.title("Signup Page")
        self.signup.resizable(False, False)
        self.signup.iconbitmap(icon_image)
        self.new_app = None

        # Make background image
        self.bg_image = tk.PhotoImage(file=BG_image)
        tk.Label(self.signup, image=self.bg_image).place(relwidth=1, relheight=1)

        # Read excel data file
        self.df = pd.read_excel(excel_file)

        # Create labels and input fields for user information
        tk.Label(self.signup, text="Signup", bg="#0992F6", fg="white", font=("arial", 30, "bold"), width="500", justify="center").pack(pady=20)
        tk.Label(text="User name: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=100)
        self.userName = tk.Entry(font=("arial", 15, "normal"), bg="white", fg="black", borderwidth=0)
        self.userName.place(x=200, y=100)
        tk.Label(text="job: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=140)
        options = ["doctor", "nurse", "pharmacist", "IT", "receptionist", "accountant", "manager", "head nurse", "head of department"]
        self.comboVar = tk.StringVar()
        self.combo = ttk.Combobox(self.signup, textvariable=self.comboVar, values=options, state="readonly", font=("arial", 15, "normal"))
        self.combo.place(x=200, y=140)
        self.comboVar = "Choose Job"
        self.combo.set(self.comboVar)
        tk.Label(text="specialty: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=180)
        self.userSpecialty = tk.Entry(font=("arial", 15, "normal"), bg="white", fg="black", borderwidth=0)
        self.userSpecialty.place(x=200, y=180)
        tk.Label(text="Phone: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=220)
        self.userPhone = tk.Entry(font=("arial",  15, "normal"), bg="white", fg="black", borderwidth=0)
        self.userPhone.place(x=200, y=220)
        tk.Label(text="ID: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=260)
        self.userID = tk.Entry(font=("arial", 15, "normal"), bg="white", fg="black", borderwidth=0)
        self.userID.place(x=200, y=260)
        tk.Label(text="Password: ", font=("arial", 15, "bold"), fg="white", bg="#0992F6").place(x=40, y=300)
        self.userPass = tk.Entry(font=("arial", 15, "normal"), bg="white", fg="black", borderwidth=0)
        self.userPass.place(x=200, y=300)

        # Create a signup button
        tk.Button(self.signup, text="Signup", font=("arial", 20, "bold"), borderwidth=0, bg="white", width=10, activebackground="#0992F6", activeforeground="white", command=self.validateSignup).place(x=50, y=340)
        tk.Button(self.signup, text="Exit", font=("arial", 20, "bold"), borderwidth=0, bg="white", width=10, activebackground="#0992F6", activeforeground="white", command=self.open_login_page).place(x=350, y=340)

    # Method to validate user input for signup
    def validateSignup(self):
        USER_DATA = {
            "User Name": self.userName.get(),
            "Job": self.combo.get(),
            "Specialty": self.userSpecialty.get(),
            "Phone": str(self.userPhone.get()),
            "ID": str(self.userID.get()),
            "Password": str(self.userPass.get())
        }
        for key, value in USER_DATA.items():
            if not value or value == "Choose Job":
                messagebox.showerror("Error", f"{key} is missing.")
                return
        if not self.userPhone.get().isdigit():
            messagebox.showerror("Error", "Phone number should contain only digits.")
            return
        if not self.userID.get().isdigit():
            messagebox.showerror("Error", "ID should contain only digits.")
            return
        if int(USER_DATA['ID']) in self.df['id'].values:
            messagebox.showerror("Error", "ID is exist already try again.")
            return

        # If all validation passes, open a confirmation window
        confirm = tk.Toplevel()
        confirm.config(bg="#ffffff")
        confirm.title("confirm")
        confirm.geometry("250x130+550+230")
        tk.Label(confirm, text="Are You Sure?", font=("arial", 22, "bold"), justify="center", bg="#ffffff").pack(pady=10)
        tk.Button(confirm, text="Confirm", font=("arial", 20, "bold"), borderwidth=0, bg="#00A1D1", fg="white", width=7, activebackground="white", activeforeground="black", command=self.confirmData).place(x=0, y=70)
        tk.Button(confirm, text="Edit", font=("arial", 20, "bold"), borderwidth=0, bg="#00A1D1", fg="white", width=7, activebackground="white", activeforeground="black", command=confirm.destroy).place(x=125, y=70)

    # Method to confirm and save user data to a DataFrame
    def confirmData(self):
        data = {"id": str(self.userID.get()), "name": self.userName.get(), "phone": str(self.userPhone.get()),
                "password": str(self.userPass.get()), "job": self.combo.get(), "specialty": self.userSpecialty.get()}
        self.df = self.df._append(data, ignore_index=True)
        self.df.to_excel(excel_file, index=False)
        self.open_login_page()

    def open_login_page(self):
        self.signup.destroy()
        self.new_app = lg.login_page()
        self.new_app.login_page_run()

    def signup_run(self):
        self.signup.mainloop()


if __name__ == "__main__":
    signup = signup_page()
    signup.signup_run()
