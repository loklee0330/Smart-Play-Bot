import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import datetime
import time

def click_burst(target_time_str, x, y, num_clicks, interval_ms, safety_delay_ms):
    # Parse with milliseconds (HH:MM:SS:MMM)
    try:
        h, m, s, ms = map(int, target_time_str.split(":"))
    except ValueError:
        messagebox.showerror("Error", "Time must be HH:MM:SS:MMM")
        return
    # Add safety buffer
    ms += safety_delay_ms
    if ms >= 1000:
        s += ms // 1000
        ms = ms % 1000
    target_time = (
        h * 3600 +
        m * 60 +
        s +
        ms / 1000.0
    )
    # Wait until just before target time
    while True:
        now = datetime.datetime.now()
        now_time = (
            now.hour * 3600 +
            now.minute * 60 +
            now.second +
            now.microsecond / 1_000_000
        )
        if now_time >= target_time:
            break
        time.sleep(0.0005)  # 0.5ms precision

    # Burst of clicks
    for i in range(num_clicks):
        pyautogui.click(x=int(x), y=int(y))
        time.sleep(interval_ms / 1000.0)

def start_click():
    time_str = entry_time.get()
    x = entry_x.get()
    y = entry_y.get()
    num_clicks = entry_num_clicks.get()
    interval_ms = entry_interval.get()
    safety_delay_ms = entry_safety.get()
    # Validate all fields
    try:
        h, m, s, ms = map(int, time_str.split(":"))
        assert 0 <= h < 24
        assert 0 <= m < 60
        assert 0 <= s < 60
        assert 0 <= ms < 1000
        x = int(x)
        y = int(y)
        num_clicks = int(num_clicks)
        interval_ms = int(interval_ms)
        safety_delay_ms = int(safety_delay_ms)
        assert num_clicks > 0 and num_clicks <= 20
        assert 1 <= interval_ms <= 100
        assert 0 <= safety_delay_ms <= 200
    except Exception:
        messagebox.showerror("Error", "Please check all fields (time: HH:MM:SS:MMM, X/Y: int, clicks: 1-20, interval: 1-100, safety: 0-200)")
        return
    info = (
        f"Will click at {x},{y} at {time_str} (+{safety_delay_ms}ms safety delay)\n"
        f"Sends {num_clicks} clicks, {interval_ms}ms apart."
    )
    messagebox.showinfo("Info", info)
    threading.Thread(target=click_burst, args=(time_str, x, y, num_clicks, interval_ms, safety_delay_ms), daemon=True).start()

def update_mouse_position():
    x, y = pyautogui.position()
    mouse_pos_label.config(text=f"Current Mouse Position: X={x}  Y={y}")
    root.after(100, update_mouse_position)

def fill_current_position(event=None):
    x, y = pyautogui.position()
    entry_x.delete(0, tk.END)
    entry_x.insert(0, str(x))
    entry_y.delete(0, tk.END)
    entry_y.insert(0, str(y))
    messagebox.showinfo("Info", f"Filled X={x}, Y={y} into the boxes!")

root = tk.Tk()
root.title("Competitive Booking Clicker (Agency Adjustable Edition)")

# Time input
tk.Label(root, text="Time (HH:MM:SS:MMM):").grid(row=0, column=0, sticky='e')
entry_time = tk.Entry(root)
entry_time.insert(0, "07:00:00:000")
entry_time.grid(row=0, column=1)

# X coordinate input
tk.Label(root, text="X coordinate:").grid(row=1, column=0, sticky='e')
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1)

# Y coordinate input
tk.Label(root, text="Y coordinate:").grid(row=2, column=0, sticky='e')
entry_y = tk.Entry(root)
entry_y.grid(row=2, column=1)

# Number of clicks input
tk.Label(root, text="Number of Clicks:").grid(row=3, column=0, sticky='e')
entry_num_clicks = tk.Entry(root)
entry_num_clicks.insert(0, "5")
entry_num_clicks.grid(row=3, column=1)

# Interval input
tk.Label(root, text="Interval between Clicks (ms):").grid(row=4, column=0, sticky='e')
entry_interval = tk.Entry(root)
entry_interval.insert(0, "10")
entry_interval.grid(row=4, column=1)

# Safety delay input
tk.Label(root, text="Safety Delay (ms):").grid(row=5, column=0, sticky='e')
entry_safety = tk.Entry(root)
entry_safety.insert(0, "8")
entry_safety.grid(row=5, column=1)

# Start button
button_start = tk.Button(root, text="Start", command=start_click)
button_start.grid(row=6, column=0, columnspan=2, pady=(10,0))

# Live Mouse Position Label
mouse_pos_label = tk.Label(root, text="Current Mouse Position: X=0 Y=0", fg="blue")
mouse_pos_label.grid(row=7, column=0, columnspan=2, pady=10)

# Button to fill current position
get_position_button = tk.Button(root, text="Use Current Mouse Position", command=fill_current_position)
get_position_button.grid(row=8, column=0, columnspan=2, pady=(0, 10))

# Instruction/shortcut tip label
instruction_label = tk.Label(
    root,
    text="Tip: Press Ctrl+C in this window to auto-fill X/Y with current mouse position.",
    fg="green"
)
instruction_label.grid(row=9, column=0, columnspan=2, pady=(0,0))

# Bind Ctrl+C to fill_current_position
root.bind('<Control-c>', fill_current_position)

# Start updating mouse position in UI
update_mouse_position()

# Agency tip for user
tk.Label(root, text=(
    "Agency Pro Tip: Sync your PC clock with NTP before launch.\n"
    "Defaults: 5 clicks, 10ms interval, 8ms safety = best practice for gov queues."
), fg="red").grid(row=10, column=0, columnspan=2, pady=(0,10))

root.mainloop()