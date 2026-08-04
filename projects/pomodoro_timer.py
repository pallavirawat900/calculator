import tkinter as tk
import customtkinter as ctk
from tkinter import Canvas

root = tk.Tk()
root.geometry("500x650")
root.title("pomodoro timer")
root.configure(bg="#060606")
root.resizable = (True,True)

title_frame= tk.Frame(root, bg = "#0E0D0D")
title_frame.pack(pady=(30,5))

pomodoro_label = tk.Label(title_frame, text="🍎POMODORO ",bg="#0E0D0D",
            font=("SF Display",25,"bold"),fg ="#E63946")
pomodoro_label.grid(row=0,column=0)

timer_label = tk.Label(title_frame, text="TIMER ",bg="#0C0C0C",
            font=("SF Display",25,"bold"),fg ="#F8F5F5")
timer_label.grid(row=0,column=1)

subtile_label = tk.Label(root,text="--Stay Focused & Productive--",
            font=("SF Display",12),bg = "#0A0A0A",fg="#FAF7F7")
subtile_label.pack(pady=(0,20))

timer_frame = tk.Frame(root,bg="#0C0C0C")
timer_frame.pack(pady= 20)

status_frame = tk.Frame(timer_frame,bg="#0C0C0C",padx=20,pady=8)
status_frame.pack(pady=10)

status_labal = tk.Label(status_frame,text="🟢Focus Time",
                        bg="#0C0C0C",fg="#4ADE80",
                        font=("SF Display",16,"bold"))
status_labal.pack()

canvas = tk.Canvas(timer_frame,bg="#0C0C0C",width=280,
                   height=260,highlightthickness=0)
canvas.pack()

canvas.create_oval(30,30,250,250,outline="#374151",width=15)

progress_arc=canvas.create_arc(30,30,250,250,start=90,
            extent=360,style="arc",outline="#FF5C5C",width=15)

timer_text = canvas.create_text(150,150,text="25:00",
             fill="white",font=("SF Display",55,"bold"))

minute = 25
second = 0
running = False

def start_timer():
    global running
    if not running:
        running = True
        countdown()
        
def countdown():
    global minute,second,running
    
    if not running:
        return
    
    canvas.itemconfig(timer_text,text=f"{minute:02}:{second:02}")
    if minute==0 and second==0:
        running = False
        return
    
    if second == 0:
        minute -= 1
        second = 59
    else:
        second -= 1
        
    total_second = 25*60
    current_second = minute*60 +second
    extent = (current_second/total_second)*360
    
    canvas.itemconfig(progress_arc,extent=extent)
    root.after(1000,countdown)
        
    
button_frame = tk.Frame(root, bg = "#0F172A")
button_frame.pack(pady=20)
start_button = ctk.CTkButton(button_frame,text="🟢Start",
            command=start_timer,fg_color="green",hover_color="#2ACE4B")
start_button.grid(row=0,column=0,padx=5)

def pause_timer():
    global running
    running = False
    
pause_button = ctk.CTkButton(button_frame,text="⏸️Pause",
                fg_color="#C1741C",hover_color="#C98C1C",command=pause_timer)    
pause_button.grid(row=0, column=1, padx=5)

def reset_timer():
    global running,minute,second
    running = False
    minute = 25
    second = 0
    
    canvas.itemconfig(timer_text,text = "25:00")
    canvas.itemconfig(progress_arc,extent=360)

reset_button = ctk.CTkButton(button_frame,text="🔄Reset",command=reset_timer)
reset_button.grid(row=0,column=3,padx =5)



root.mainloop()