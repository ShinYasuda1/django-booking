import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

def save_event():
    event_date = cal.get_date()
    event_name = event_entry.get()

    if event_name and event_date:
        with open("events.txt", "a") as file:
            file.write(f"{event_date}: {event_name}\n")
        event_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "イベントが保存されました。")
    else:
        messagebox.showerror("エラー", "日付とイベント名を入力してください。")

def show_events():
    try:
        with open("events.txt", "r") as file:
            events = file.read()
        messagebox.showinfo("イベント一覧", events)
    except FileNotFoundError:
        messagebox.showinfo("イベント一覧", "イベントはまだ保存されていません。")

app = tk.Tk()
app.title("カレンダー")

cal = DateEntry(app, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=0, column=0, padx=10, pady=10)

event_entry = tk.Entry(app, width=30)
event_entry.grid(row=0, column=1, padx=10, pady=10)

save_button = tk.Button(app, text="イベントを保存", command=save_event)
save_button.grid(row=0, column=2, padx=10, pady=10)

show_button = tk.Button(app, text="イベント一覧を表示", command=show_events)
show_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

app.mainloop()
