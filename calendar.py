from tkinter import *
import calendar

def display_calendar():
    
    screen = Tk()
    screen.config(background= "blue")
    screen.title("Calendar")
    screen.geometry("600x800")
    fetchyear = int(year_field.get())
    cal = calendar.Calendar(fetchyear)
    cal_year = Label(screen, text= cal, font= "Arial 20 Bold")
    cal_year.grid(row=5, column=1)





    screen.mainloop()

if __name__ == "__main__":
    # Create the main window
    screen2 = Tk()
    screen2.config(background= "red")
    screen2.title("Calendar")
    screen2.geometry("600x800")

    cal = Label(screen2, text= "CALENDAR", bg= "blue", font= ("Arial", 28, 'bold'))
    year = Label(screen2, bg= "blue", font= ("Arial", 20, 'bold'))
    year_field = Entry(screen2, font= "Arial 20 bold")
    show = Button(screen2, text= "Show Calendar", fg= "black", bg= "white", font= ("Arial", 20, 'bold'), command= display_calendar)
    
    exit_button = Button(screen2, text= "Exit", fg= "black", bg= "white", font= ("Arial", 20, 'bold'), command= screen2.quit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    show.grid(row=4, column=1)
    exit_button.grid(row=6, column=1)

    # Run the application
    screen2.mainloop()


# import tkinter as tk
# import calendar

# def show_calendar():
#     try:
#         fetchyear = int(year_field.get())
#         cal = calendar.TextCalendar().formatyear(fetchyear)
#         cal_year.config(text=cal)
#     except ValueError:
#         cal_year.config(text="Invalid year. Please enter a valid number.")

# # Create the main window
# screen = tk.Tk()
# screen.config(background="blue")
# screen.title("Calendar")
# screen.geometry("600x800")

# # Create input field and button
# year_label = tk.Label(screen, text="Enter Year:", font="Arial 14", bg="blue", fg="white")
# year_label.pack(pady=10)

# year_field = tk.Entry(screen, font="Arial 14")
# year_field.pack(pady=10)

# show_button = tk.Button(screen, text="Show Calendar", font="Arial 14", command=show_calendar)
# show_button.pack(pady=10)

# # Create label to display the calendar
# cal_year = tk.Label(screen, text="", font="Courier 12", bg="blue", fg="white", justify="left")
# cal_year.pack(pady=20)

# # Run the application
# screen.mainloop()
