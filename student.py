import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

root = tk.Tk()
root.title("Student Management System")

tk.Label(root, text="Register Number:").grid(row=0, column=0)
reg_no_entry = tk.Entry(root)
reg_no_entry.grid(row=0, column=1)

tk.Label(root, text="Semester:").grid(row=1, column=0)
sem_entry = tk.Entry(root)
sem_entry.grid(row=1, column=1)

tk.Label(root, text="Score:").grid(row=2, column=0)
score_entry = tk.Entry(root)
score_entry.grid(row=2, column=1)

def save_data():
    reg_no = reg_no_entry.get()
    sem = sem_entry.get()
    score = score_entry.get()

    if reg_no and sem and score:
        data = {'Register Number': [reg_no], 'Semester': [sem], 'Score': [score]}
        df = pd.DataFrame(data)
        try:
            existing_df = pd.read_excel('student_data.xlsx')
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass
        
        df.to_excel('student_data.xlsx', index=False)
        messagebox.showinfo("Info", "Data saved successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")

def show_performance():
    reg_no = reg_no_entry.get()
    if not reg_no:
        messagebox.showerror("Error", "Register number is required!")
        return

    try:
        df = pd.read_excel('student_data.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "No data available!")
        return

    student_data = df[df['Register Number'] == reg_no]
    if student_data.empty:
        messagebox.showerror("Error", "No data found for the entered register number!")
        return

    plt.figure()
    plt.plot(student_data['Semester'], student_data['Score'], marker='o')
    plt.xlabel('Semester')
    plt.ylabel('Score')
    plt.title(f'Performance of {reg_no}')
    plt.show()

def predict_performance():
    reg_no = reg_no_entry.get()
    if not reg_no:
        messagebox.showerror("Error", "Register number is required!")
        return

    try:
        df = pd.read_excel('student_data.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "No data available!")
        return

    student_data = df[df['Register Number'] == reg_no]
    if student_data.empty:
        messagebox.showerror("Error", "No data found for the entered register number!")
        return

    X = student_data['Semester'].values.reshape(-1, 1)
    y = student_data['Score'].values
    model = LinearRegression()
    model.fit(X, y)
    next_sem = student_data['Semester'].max() + 1
    predicted_score = model.predict(np.array([[next_sem]]))[0]

    messagebox.showinfo("Prediction", f'Predicted score for next semester (Semester {next_sem}): {predicted_score:.2f}')

def show_rank_list():
    try:
        df = pd.read_excel('student_data.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "No data available!")
        return

    rank_list = df.groupby('Register Number')['Score'].mean().sort_values(ascending=False)
    rank_window = tk.Toplevel(root)
    rank_window.title("Rank List")

    tk.Label(rank_window, text="Rank").grid(row=0, column=0)
    tk.Label(rank_window, text="Register Number").grid(row=0, column=1)
    tk.Label(rank_window, text="Average Score").grid(row=0, column=2)

    for i, (reg_no, avg_score) in enumerate(rank_list.items(), start=1):
        tk.Label(rank_window, text=i).grid(row=i, column=0)
        tk.Label(rank_window, text=reg_no).grid(row=i, column=1)
        tk.Label(rank_window, text=f'{avg_score:.2f}').grid(row=i, column=2)

tk.Button(root, text="Save Data", command=save_data).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Show Performance", command=show_performance).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Predict Performance", command=predict_performance).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Show Rank List", command=show_rank_list).grid(row=6, column=0, columnspan=2)

root.mainloop()
