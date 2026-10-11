import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    try:
        # create the root window
        root = tk.Tk()
        root.title("Heart Rate Calculator")

        frm_main = Frame(root)
        frm_main.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # call the function to populate the frame with widgets
        populate_main_window(frm_main)

        # start the tkinter main loop
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")


def populate_main_window(frm_main):
    """Populate the main window with labels, entry boxes, and buttons."""
    
    # labels
    lbl_age = Label(frm_main, text="Age:")
    lbl_range = Label(frm_main, text="Target Heart Rate Range:")
    
    # custom validated Integer Entry for Age
    ent_age = IntEntry(frm_main, width=5)
    
    # label to display the results dynamically
    lbl_result = Label(frm_main, text="", width=15, anchor="w")
    
    # status bar label at the bottom
    lbl_status = Label(frm_main, text="", fg="red", anchor="w")

    # layout widgets using grid
    lbl_age.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ent_age.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    lbl_range.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lbl_result.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # nested calculation function to update results dynamically
    def calculate(event=None):
        try:
            # clear error messages when beginning new calculation
            lbl_status.config(text="")
            
            val = ent_age.get()
            if val == "":
                lbl_result.config(text="")
                return
                
            age = int(val)
            
            # heart rate formula matches standard heart_rate.py logic
            max_heart_rate = 220 - age
            slow_target = round(max_heart_rate * 0.65)
            fast_target = round(max_heart_rate * 0.85)
            
            # display target range in the GUI
            lbl_result.config(text=f"{slow_target} - {fast_target} bpm")
            
        except ValueError:
            # catch empty or invalid text inputs
            lbl_result.config(text="")
            lbl_status.config(text="Please enter a valid age integer.")

    # nested clear function for clear button enhancement
    def clear():
        ent_age.delete(0, tk.END)
        lbl_result.config(text="")
        lbl_status.config(text="")
        ent_age.focus()

    # buttons
    btn_clear = Button(frm_main, text="Clear", command=clear)
    
    # position buttons and status bar
    btn_clear.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    lbl_status.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    # bind input changes to calculate dynamically without needing separate calculate button
    ent_age.bind("<KeyRelease>", calculate)
    
    # give primary focus to the age entry box upon launch
    ent_age.focus()


if __name__ == "__main__":
    main()
