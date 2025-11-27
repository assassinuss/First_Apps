import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import math

# Management_Colegiu_Clock.py
# Simple clock app: digital + analog, 12/24 toggle, timezone offset selector.
# Save this file and run with: python Management_Colegiu_Clock.py


class ClockApp:
    def __init__(self, root):
        self.root = root
        root.title("Clock App")
        root.resizable(False, False)

        self.frame = ttk.Frame(root, padding=12)
        self.frame.grid()

        # Settings
        self.use_24h = tk.BooleanVar(value=True)
        self.running = tk.BooleanVar(value=True)
        self.tz_offset = tk.IntVar(value=0)  # offset in hours from UTC

        # Digital display
        self.time_label = ttk.Label(self.frame, text="", font=("Segoe UI", 28))
        self.time_label.grid(row=0, column=0, columnspan=3, pady=(0,10))

        self.date_label = ttk.Label(self.frame, text="", font=("Segoe UI", 10))
        self.date_label.grid(row=1, column=0, columnspan=3)

        # Controls
        ttk.Checkbutton(self.frame, text="24-hour", variable=self.use_24h, command=self.update).grid(row=2, column=0, sticky="w", pady=(8,0))
        ttk.Checkbutton(self.frame, text="Running", variable=self.running).grid(row=2, column=1, sticky="w", pady=(8,0))

        ttk.Label(self.frame, text="UTC offset:").grid(row=2, column=2, sticky="e", padx=(6,0))
        tz_spin = ttk.Spinbox(self.frame, from_=-12, to=14, width=4, textvariable=self.tz_offset, command=self.update)
        tz_spin.grid(row=2, column=3, sticky="w", padx=(4,0))

        # Canvas for analog clock
        self.size = 260
        self.canvas = tk.Canvas(self.frame, width=self.size, height=self.size, bg="white", highlightthickness=0)
        self.canvas.grid(row=3, column=0, columnspan=4, pady=(12,0))
        self.center = (self.size // 2, self.size // 2)
        self.radius = int(self.size * 0.42)

        # Pre-draw clock face (numbers and circle)
        self._draw_face()

        # Start update loop
        self._update_loop()

    def _draw_face(self):
        cx, cy = self.center
        self.canvas.create_oval(cx - self.radius - 6, cy - self.radius - 6, cx + self.radius + 6, cy + self.radius + 6, fill="#f0f0f0", outline="#888")
        for h in range(1, 13):
            angle = math.radians((h / 12) * 360 - 90)
            x = cx + math.cos(angle) * (self.radius - 24)
            y = cy + math.sin(angle) * (self.radius - 24)
            self.canvas.create_text(x, y, text=str(h), font=("Segoe UI", 12, "bold"))

        # minute ticks
        for m in range(60):
            angle = math.radians((m / 60) * 360 - 90)
            r1 = self.radius - 6
            r2 = self.radius - (12 if m % 5 == 0 else 8)
            x1 = cx + math.cos(angle) * r1
            y1 = cy + math.sin(angle) * r1
            x2 = cx + math.cos(angle) * r2
            y2 = cy + math.sin(angle) * r2
            color = "#444" if m % 5 == 0 else "#aaa"
            self.canvas.create_line(x1, y1, x2, y2, fill=color)

        # placeholders for hands
        self.hour_hand = self.canvas.create_line(0,0,0,0, width=6, fill="#222", capstyle="round")
        self.minute_hand = self.canvas.create_line(0,0,0,0, width=4, fill="#111", capstyle="round")
        self.second_hand = self.canvas.create_line(0,0,0,0, width=2, fill="#c33", capstyle="round")
        self.center_dot = self.canvas.create_oval(cx-6, cy-6, cx+6, cy+6, fill="#222", outline="")

    def _get_now(self):
        # Use UTC plus tz offset to avoid dependency on external timezone libs
        now_utc = datetime.utcnow()
        offset = timedelta(hours=self.tz_offset.get())
        return now_utc + offset

    def _draw_hands(self, now):
        cx, cy = self.center
        hour = now.hour % 12
        minute = now.minute
        second = now.second
        micro = now.microsecond

        # Calculate angles
        second_angle = ((second + micro / 1_000_000) / 60) * 360
        minute_angle = ((minute + second / 60) / 60) * 360
        hour_angle = ((hour + minute / 60) / 12) * 360

        def endpoint(angle_deg, length):
            angle = math.radians(angle_deg - 90)
            x = cx + math.cos(angle) * length
            y = cy + math.sin(angle) * length
            return x, y

        hx, hy = endpoint(hour_angle, self.radius * 0.5)
        mx, my = endpoint(minute_angle, self.radius * 0.75)
        sx, sy = endpoint(second_angle, self.radius * 0.85)

        self.canvas.coords(self.hour_hand, cx, cy, hx, hy)
        self.canvas.coords(self.minute_hand, cx, cy, mx, my)
        self.canvas.coords(self.second_hand, cx, cy, sx, sy)

    def update(self):
        now = self._get_now()
        # Digital format
        if self.use_24h.get():
            time_str = now.strftime("%H:%M:%S")
        else:
            time_str = now.strftime("%I:%M:%S %p")
        date_str = now.strftime("%A, %d %B %Y (UTC%+d)" % self.tz_offset.get())

        self.time_label.config(text=time_str)
        self.date_label.config(text=date_str)

        # Analog
        self._draw_hands(now)

    def _update_loop(self):
        if self.running.get():
            self.update()
        # update ~ every 100 ms for smooth second hand
        self.root.after(100, self._update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()