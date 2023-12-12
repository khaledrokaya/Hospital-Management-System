import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

excel_file = r"data\employee_data.xlsx"


class employee_page:

    def __init__(self):
        self.employee = tk.Tk()
        self.employee.geometry(f"500x400+{(self.employee.winfo_screenwidth()-500)//2}+{(self.employee.winfo_screenheight()-475)//2}")
        self.employee.title("Admin Manager")
        self.employee.iconbitmap(r"media\employee.ico")
        self.employee.resizable(False, False)
        self.employee.configure(background="white")
        self.create_or_load_employee_data()
        tk.Label(text="Please Choose to continue", font=("arial", 20, "bold"), fg="black", bg="white").place(x=80, y=4)

        btt_add = tk.Button(self.employee, text="Add employee", font=('monospace', 13, 'bold'), bg="#00A1D1", fg='white', command=self.add_employees)
        btt_add.place(x=150, y=100, width=200, height=43)

        btt_search = tk.Button(self.employee, text="Search an employee", font=('monospace', 13, 'bold'), bg="#00A1D1", fg='white', command=self.show)
        btt_search.place(x=150, y=200, width=200, height=43)

        btt_Exit = tk.Button(self.employee, text="Exit", font=('monospace', 13, 'bold'), bg="#00A1D1", fg='white', command=self.employee.quit)
        btt_Exit.place(x=150, y=300, width=200, height=43)

    def add_employees(self):
        self.employees = tk.Tk()
        self.employees.geometry(f"1000x700+{(self.employees.winfo_screenwidth()-1000)//2}+{(self.employees.winfo_screenheight()-775)//2}")
        self.employees.title("Admin Manager")
        self.employees.iconbitmap(r"media\employee.ico")
        self.employees.configure(bg="white")
        self.employees.resizable(False, False)
        tk.Label(self.employees, text="Employee management system", bg="#0992F6", fg="white", font=("arial", 30, "bold"), width="500",
                 justify="center").pack()
        self.frame1 = tk.Frame(self.employees, relief=tk.RAISED, borderwidth=3, bg="silver")
        self.frame1.place(x=20, y=60, width=950, height=600)
        self.frame2 = tk.Frame(self.frame1, relief=tk.RAISED, borderwidth=2, bg="silver")
        self.frame2.place(x=10, y=20, width=900, height=500)

        # ------labels and button in personal info_____
        title1 = tk.Label(self.frame2, text="personal information", font=('Oblique', 11, 'bold', 'underline'), fg="black", bg="silver")
        title1.place(x=10, y=0)
        self.frame3 = tk.Frame(self.frame2, borderwidth=3, bg="silver")
        self.frame3.place(x=10, y=20, width=430, height=450)
        self.lbl_jop = tk.Label(self.frame3, text="personal Jop :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_jop.place(x=3, y=2)
        self.options = ["doctor", "nurse", "pharmacist", "receptionist", "accountant", "manager", "head nurse", "head of department"]
        self.jop = ttk.Combobox(self.frame3, values=self.options, state="readonly", font=("arial", 15, "normal"))
        self.jop.place(x=135, y=2, height=27, width=200)

        self.lbl_id = tk.Label(self.frame3, text="personal ID :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_id.place(x=3, y=55)
        self.en_id = tk.Entry(self.frame3, fg="black", bg="white", justify="center")
        self.en_id.place(x=135, y=55, height=27, width=200)

        self.lbl_fname = tk.Label(self.frame3, text="First Name:", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_fname.place(x=3, y=110)
        self.en_fname = tk.Entry(self.frame3, fg="black", bg="white", justify="center")
        self.en_fname.place(x=135, y=110, height=27, width=200)

        self.lbl_mname = tk.Label(self.frame3, text="Middle Name:", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_mname.place(x=3, y=170)
        self.en_mname = tk.Entry(self.frame3, fg="black", bg="white", justify="center")
        self.en_mname.place(x=135, y=170, height=27, width=200)

        self.lbl_lname = tk.Label(self.frame3, text="Surname :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_lname.place(x=3, y=225)
        self.en_lname = tk.Entry(self.frame3, fg="black", bg="white", justify="center")
        self.en_lname.place(x=135, y=225, height=27, width=200)

        self.lbl_day = tk.Label(self.frame3, text="Day of birth :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_day.place(x=3, y=280)
        self.days = [str(i) for i in range(1, 31)]
        self.day = ttk.Combobox(self.frame3, values=self.days, state="readonly", font=("arial", 15, "normal"))
        self.day.place(x=155, y=280, height=27, width=160)

        self.lbl_month = tk.Label(self.frame3, text="Month of birth :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_month.place(x=3, y=335)
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.month = ttk.Combobox(self.frame3, values=self.months, state="readonly", font=("arial", 15, "normal"))
        self.month.place(x=155, y=335, height=27, width=160)

        self.lbl_day = tk.Label(self.frame3, text="Year of birth :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_day.place(x=3, y=390)
        self.current_datetime = datetime.datetime.now()
        self.years = [str(i) for i in range(1950, self.current_datetime.year + 1)]
        self.year = ttk.Combobox(self.frame3, values=self.years, state="readonly", font=("arial", 15, "normal"))
        self.year.place(x=155, y=390, height=27, width=160)

        # ---------------------------------------------------------------------------
        title2 = tk.Label(self.frame2, text="additional information", font=('Oblique', 11, 'bold', 'underline'), fg="black", bg="silver")
        title2.place(x=450, y=0)
        self.frame4 = tk.Frame(self.frame2, borderwidth=3, bg="silver")
        self.frame4.place(x=450, y=20, width=430, height=450)

        self.lbl_city = tk.Label(self.frame4, text="City :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_city.place(x=3, y=45)
        self.en_city = tk.Entry(self.frame4, fg="black", bg="white", justify="center")
        self.en_city.place(x=135, y=45, height=27, width=200)

        self.lbl_code = tk.Label(self.frame4, text="Postal Code:", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_code.place(x=3, y=105)
        self.en_code = tk.Entry(self.frame4, fg="black", bg="white", justify="center")
        self.en_code.place(x=135, y=105, height=27, width=200)

        self.lbl_address = tk.Label(self.frame4, text="Address:", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_address.place(x=3, y=170)
        self.en_address = tk.Entry(self.frame4, fg="black", bg="white", justify="center")
        self.en_address.place(x=135, y=170, height=27, width=200)

        self.lbl_gender = tk.Label(self.frame4, text="Gender :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_gender.place(x=3, y=225)
        self.gend = ["male", "Female"]
        self.gender = ttk.Combobox(self.frame4, values=self.gend, state="readonly", font=("arial", 15, "normal"))
        self.gender.place(x=155, y=225, height=27, width=160)

        self.lbl_statue = tk.Label(self.frame4, text="Marital status :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_statue.place(x=3, y=280)
        self.status = ["Single", "maried"]
        self.martial_statue = ttk.Combobox(self.frame4, values=self.status, state="readonly", font=("arial", 15, "normal"))
        self.martial_statue.place(x=155, y=280, height=27, width=160)

        self.lbl_phone1 = tk.Label(self.frame4, text="Mobile Phone :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_phone1.place(x=3, y=335)
        self.phone1_fname = tk.Entry(self.frame4, fg="black", bg="white", justify="center")
        self.phone1_fname.place(x=155, y=335, height=27, width=160)

        self.lbl_phone2 = tk.Label(self.frame4, text="Home Phone :", font=('monospace', 15, 'bold'), bg="silver")
        self.lbl_phone2.place(x=3, y=390)
        self.phone2_fname = tk.Entry(self.frame4, fg="black", bg="white", justify="center")
        self.phone2_fname.place(x=155, y=390, height=27, width=160)

        # -----button -------#

        self.exit_btn = tk.Button(self.frame1, text="Exit", font=('monospace', 13, 'bold'), bg="#0992F6", fg="white", command=self.employees.destroy)
        self.exit_btn.place(x=650, y=550, width=170, height=35)
        self.reset_btn = tk.Button(self.frame1, text="Reset", font=('monospace', 13, 'bold'), bg="#0992F6", fg="white", command=self.reset_entries)
        self.reset_btn.place(x=360, y=550, width=170, height=35)
        self.save_btn = tk.Button(self.frame1, text="save record", font=('monospace', 13, 'bold'), bg="#0992F6", fg="white", command=self.save_record)
        self.save_btn.place(x=70, y=550, width=170, height=35)

    def create_or_load_employee_data(self):
        try:
            self.df = pd.read_excel(excel_file)
        except FileNotFoundError:
            data = ["personal Jop", "Personal ID", "First Name", "Middle Name", "Surname", "Day of Birth", "Month of Birth", "Year of Birth", "City", "Postal Code", "Address", "Gender", "Marital Status", "Mobile Phone", "Home Phone", "Date and Time"]
            self.df = pd.DataFrame(columns=data)
            self.df.to_excel(excel_file, index=False)

    def save_record(self):
        personal_jop = self.jop.get()
        personal_id = self.en_id.get()
        first_name = self.en_fname.get()
        middle_name = self.en_mname.get()
        surname = self.en_lname.get()
        day_of_birth = self.day.get()
        birth = self.day.get()
        month_of_birth = self.month.get()
        year_of_birth = self.year.get()
        city = self.en_city.get()
        postal_code = self.en_code.get()
        address = self.en_address.get()
        gender = self.gender.get()
        marital_status = self.martial_statue.get()
        mobile_phone = self.phone1_fname.get()
        home_phone = self.phone2_fname.get()
        current_datetime = datetime.datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d  %H:%M:%S")
        data = {
            "personal Jop": personal_jop,
            "Personal ID": personal_id,
            "First Name": first_name,
            "Middle Name": middle_name,
            "Surname": surname,
            "Day of Birth": day_of_birth,
            "Month of Birth": month_of_birth,
            "Year of Birth": year_of_birth,
            "City": city,
            "Postal Code": postal_code,
            "Address": address,
            "Gender": gender,
            "Marital Status": marital_status,
            "Mobile Phone": mobile_phone,
            "Home Phone": home_phone,
            "Date and Time": current_datetime
        }

        # ------control---------#
        for key, value in data.items():
            if not len(value):
                messagebox.showerror("warning", f"the {key} is missing")
                return

        if not mobile_phone or len(mobile_phone) != 11:
            messagebox.showerror("Phone Number Error", "Please enter a valid 11-digit phone number")
            self.phone1_fname.delete(0, tk.END)
            return

        if not home_phone or len(home_phone) != 11:
            messagebox.showerror("Phone Number Error", "Please enter a 11-digit phone number")
            self.phone2_fname.delete(0, tk.END)
            return

        self.df = self.df._append(data, ignore_index=True)
        self.df.to_excel(excel_file, index=False)
        self.reset_entries()

    def reset_entries(self):
        # Clear all entry fields
        self.jop.set("")  # Reset the job selection
        self.en_id.delete(0, tk.END)
        self.en_fname.delete(0, tk.END)
        self.en_mname.delete(0, tk.END)
        self.en_lname.delete(0, tk.END)
        self.day.set("")  # Reset the day selection
        self.month.set("")  # Reset the month selection
        self.year.set("")  # Reset the year selection
        self.en_city.delete(0, tk.END)
        self.en_code.delete(0, tk.END)
        self.en_address.delete(0, tk.END)
        self.gender.set("")  # Reset the gender selection
        self.martial_statue.set("")  # Reset the marital status selection
        self.phone1_fname.delete(0, tk.END)
        self.phone2_fname.delete(0, tk.END)

    def show(self):
        self.root = tk.Tk()
        self.root.title("employee Maintenance")
        self.root.geometry(f"1135x745+{(self.root.winfo_screenwidth()-1135)//2}+{(self.root.winfo_screenheight()-820)//2}")
        self.root.resizable(False, True)
        self.employee_details_frame = tk.LabelFrame(self.root)
        self.employee_details_frame.place(x=10)

        self.nameLabel = tk.Label(self.employee_details_frame, text="Surname:", font=('times new roman', 15, 'bold'), fg='black')
        self.nameLabel.grid(row=0, column=0, padx=20, pady=2)

        self.nameEntry = tk.Entry(self.employee_details_frame, font=("arial", 15), bd=7, width=18)
        self.nameEntry.grid(row=0, column=1, padx=8)

        self.numLabel = tk.Label(self.employee_details_frame, text="First Name:", font=('times new roman', 15, 'bold'), fg='black')
        self.numLabel.grid(row=0, column=2, padx=20, pady=2)

        self.numEntry = tk.Entry(self.employee_details_frame, font=("arial", 15), bd=7, width=18)
        self.numEntry.grid(row=0, column=3, padx=8)

        self.employeeLabel = tk.Label(self.employee_details_frame, text="employee ID:", font=('times new roman', 15, 'bold'), fg='black')
        self.employeeLabel.grid(row=0, column=4, padx=20, pady=2)

        self.employeeEntry = tk.Entry(self.employee_details_frame, font=("arial", 15), bd=7, width=18)
        self.employeeEntry.grid(row=0, column=5, padx=8)

        searchButton = tk.Button(self.employee_details_frame, text="Search" , bg="#0992F6", fg="white", font=('arial', 12, 'bold'), bd=7, command=self.search_employee)
        searchButton.grid(row=1, column=2, padx=20, pady=8)

        searchButton = tk.Button(self.employee_details_frame,  bg="#0992F6", fg="white",text="Reset", font=('arial', 12, 'bold'), bd=7, command=self.reset_window)
        searchButton.grid(row=1, column=3, padx=20, pady=8)

        show_frame = tk.Frame(self.root, bg="#F2F4F4")
        show_frame.place(x=10, y=100, width=1125, height=605)

        scroll_x = tk.Scrollbar(show_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(show_frame, orient=tk.VERTICAL)

        data = ["personal Jop", "Personal ID", "First Name", "Middle Name", "Surname", "Day of Birth", "Month of Birth", "Year of Birth", "City", "Postal Code", "Address", "Gender", "Marital Status", "Mobile Phone", "Home Phone", "Date and Time"]
        self.employee_table = ttk.Treeview(show_frame, columns=data, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.employee_table.place(x=18, y=1, width=1130, height=587)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        # Attach scroll_bars to the Treeview
        self.employee_table.config(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack the scroll_bars
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.LEFT, fill=tk.Y)
        self.employee_table["show"] = 'headings'
        for name in data:
            self.employee_table.heading(name, text=name)
            self.employee_table.column(name, width=117)
        self.load_employee_data()

    def reset_window(self):
        # Clear all entry fields
        self.nameEntry.delete(0, tk.END)
        self.numEntry.delete(0, tk.END)
        self.employeeEntry.delete(0, tk.END)

        # Load data into Treeview
        self.load_employee_data()

    def load_employee_data(self):
        data = ["personal Jop", "Personal ID", "First Name", "Middle Name", "Surname", "Day of Birth", "Month of Birth", "Year of Birth", "City", "Postal Code", "Address", "Gender", "Marital Status", "Mobile Phone", "Home Phone", "Date and Time"]
        # Clear existing data in the Treeview
        for record in self.employee_table.get_children():
            self.employee_table.delete(record)

        # Load data into Treeview
        for index, row in self.df.iterrows():
            values = list()
            for name in data:
                values.append(row[name])
            self.employee_table.insert('', tk.END, values=values)

    def search_employee(self):
        data = ["personal Jop", "Personal ID", "First Name", "Middle Name", "Surname", "Day of Birth", "Month of Birth", "Year of Birth", "City", "Postal Code", "Address", "Gender", "Marital Status", "Mobile Phone", "Home Phone", "Date and Time"]
        # Get search values from entry fields
        surname = self.nameEntry.get()
        first_name = self.numEntry.get()
        employee_ID = int(self.employeeEntry.get())

        # Filter data based on search values
        filtered_data = self.df[(self.df['Surname'] == surname) & (self.df['First Name'] == first_name) & (
                    self.df['Personal ID'] == int(employee_ID))]

        # Clear existing data in the Treeview
        for record in self.employee_table.get_children():
            self.employee_table.delete(record)

        # Load filtered data into Treeview
        for index, row in filtered_data.iterrows():
            values = [row[name] for name in data]
            self.employee_table.insert('', tk.END, values=values)

    def employee_run(self):
        self.employee.mainloop()


if __name__ == "__main__":
    employee = employee_page()
    employee.employee_run()
