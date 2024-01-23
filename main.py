from tkinter import *
import math

# ----------------------------- CONSTANTS --------------------------------------#1
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
reps = 0


# ----------------------------- TIMER RESET --------------------------------------#4
def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="OO:OO")
  title_label.config(text="Timer")
  check_marks.config(text="")
  global reps
  reps = 0
  #timer 00:00
  #timer = Timer
  #reset check marks


# ----------------------------- TIMER MECHANISM --------------------------------------#3
def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_TIME * 60
  long_break_sec = LONG_BREAK_TIME * 60

  if reps % 8 == 0:
    count_down(long_break_sec)
    title_label.config(text="Break", fg="red")
  elif reps % 2 == 0:
    count_down(short_break_sec)
    title_label.config(text="Break", fg="PINK")
  else:
    count_down(work_sec)
    title_label.config(text="WORK", fg="GREEN")


# ----------------------------- COUNTDOWN MECHANISM --------------------------------------#2
def count_down(count):
  # "01:.25"
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

  if (count > 0):
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    mark = ""
    work_session = math.floor(reps / 2)
    for _ in range(work_session):
      mark += "✔"
    check_marks.config(text=mark)


# ----------------------------- UI SETUP --------------------------------------#1
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")

# 1.2. title
title_label = Label(text="Timer",
                    fg="GREEN",
                    bg=YELLOW,
                    font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# 1. canvas widgit
canvas = Canvas(width=230, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="image.png")
canvas.create_image(120, 120, image=tomato_img)
timer_text = canvas.create_text(120,
                                140,
                                text="OO:OO",
                                fill="white",
                                font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg="green", bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
