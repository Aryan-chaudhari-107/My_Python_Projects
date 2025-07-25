from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="TIMER")
    tick_mark.config(text="")
    global REPS
    REPS = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        text.config(text="BREAK", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        text.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        text.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            marks += "✔"
        tick_mark.config(text="marks")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Timer text
text = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
text.grid(column=1, row=0)


#start button
start = Button(text="Start", command=start_timer, width=10, highlightthickness=0)
start.grid(column=0, row=2)


#reset button
reset = Button(text="Reset", command=reset_timer, width=10, highlightthickness=0)
reset.grid(column=2, row=2)


#tick mark
tick_mark = Label(font=(FONT_NAME, 15))
tick_mark.config(fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)


#putting img on window and putting clock on img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
