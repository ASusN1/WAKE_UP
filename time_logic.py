import time
import tkinter as tk

#editable time thing for the main menu, 
def create_editable_timer(parent_widget):
    
    timer_frame = tk.Frame(parent_widget)
    timer_frame.pack(side="left", pady=10, padx=5)
    
    # Store time values
    time_vars = {
        'hours': tk.StringVar(value="00"),
        'minutes': tk.StringVar(value="00"),
        'seconds': tk.StringVar(value="00")
    }
    
    # Store references to labels and entry fields
    display_widgets = {}
    
    def create_time_field(field, parent):
        field_frame = tk.Frame(parent)
        field_frame.pack(side="left", padx=2)
        
        label = tk.Label(field_frame, textvariable=time_vars[field], font=("Arial", 20), 
                        relief="solid", bd=1, width=3, cursor="hand2", bg="white")
        label.pack()
        
        entry = tk.Entry(field_frame, font=("Arial", 20), width=3, justify="center")
        #when user click on the time lable, it change to entry --> user can enter the time they want to count down
        def on_click(event):
            label.pack_forget()
            entry.pack()
            entry.delete(0, tk.END)
            entry.insert(0, time_vars[field].get())
            entry.focus_set()
            entry.select_range(0, tk.END)
        
        def confirm_edit(event=None):
            new_value = entry.get()
            
            # Validate input
            try:
                val = int(new_value)
                if field == 'hours':
                    if 0 <= val <= 23:
                        time_vars[field].set(f"{val:02d}")
                    else:
                        time_vars[field].set("00")
                else:  # minutes or seconds
                    if 0 <= val <= 59:
                        time_vars[field].set(f"{val:02d}")
                    else:
                        time_vars[field].set("00")
            except ValueError:
                # If not a valid number, keep the old value
                pass
            
            entry.pack_forget()
            label.pack()
        
        label.bind("<Button-1>", on_click)
        entry.bind("<Return>", confirm_edit)
        entry.bind("<FocusOut>", confirm_edit)
        
        display_widgets[field] = {'label': label, 'entry': entry, 'frame': field_frame}
        return field_frame
    
    # Create hours field
    create_time_field('hours', timer_frame)
    
    # Colon separator
    tk.Label(timer_frame, text=":", font=("Arial", 20)).pack(side="left", padx=3)
    
    # Create minutes field
    create_time_field('minutes', timer_frame)
    
    # Colon separator
    tk.Label(timer_frame, text=":", font=("Arial", 20)).pack(side="left", padx=3)
    
    # Create seconds field
    create_time_field('seconds', timer_frame)
    
    # Store the countdown state
    time_vars['is_running'] = False
    time_vars['after_id'] = None
    
    return time_vars

def start_countdown(time_vars, window):
    
    # Prevent multiple timers from running
    if time_vars.get('is_running', False):
        return
    
    time_vars['is_running'] = True
    
    def countdown():
        # Get current time values
        hours = int(time_vars['hours'].get())
        minutes = int(time_vars['minutes'].get())
        seconds = int(time_vars['seconds'].get())
        
        # Convert to total seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds
        
        # Decrement by 1 second
        total_seconds -= 1
        
        # Check if time is up
        if total_seconds < 0:
            total_seconds = 0
            time_vars['is_running'] = False
            # Timer is finished
            print("Time's up!")
            return
        
        # Convert back to hours, minutes, seconds
        new_hours = total_seconds // 3600
        new_minutes = (total_seconds % 3600) // 60
        new_seconds = total_seconds % 60
        
        # Update the display
        time_vars['hours'].set(f"{new_hours:02d}")
        time_vars['minutes'].set(f"{new_minutes:02d}")
        time_vars['seconds'].set(f"{new_seconds:02d}")
        
        # Schedule the next update in 1000ms (1 second)
        time_vars['after_id'] = window.after(1000, countdown)
    
    # Start the countdown
    countdown()

