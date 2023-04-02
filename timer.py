from tkinter import Tk, Label
from keyboard import add_hotkey, on_press
from PIL import ImageColor
from win32gui import GetWindowLong, SetWindowLong, SetLayeredWindowAttributes
from win32con import GWL_EXSTYLE, WS_EX_LAYERED, WS_EX_TRANSPARENT, LWA_ALPHA, LWA_COLORKEY
from win32api import RGB
import configvars as cfg
import soundalarm as alrm


def set_clickthrough(hwnd, color=None):
    styles = GetWindowLong(hwnd, GWL_EXSTYLE)
    styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
    SetWindowLong(hwnd, GWL_EXSTYLE, styles)

    if color:
        r, g, b = ImageColor.getcolor(color, "RGB")
        rgb = RGB(r, g, b)
        SetLayeredWindowAttributes(hwnd, rgb, 255, LWA_ALPHA)
        SetLayeredWindowAttributes(hwnd, rgb, 255, LWA_COLORKEY)


class Clock:
    def __init__(self, root):
        self.heavy_time_left = None
        self.mega_time_left = None

        self.root = root
        self.root.geometry(cfg.window_x_y_position_pixels)  # Position the window
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.config(bg=cfg.transparent_color)
        self.root.attributes('-alpha', cfg.visibility)  # Set window visibility level
        self.root.attributes('-transparentcolor', cfg.transparent_color)
        self.root.wm_attributes('-topmost', True)
        if cfg.transparent_bg:
            self.root.attributes('-transparent', cfg.transparent_color)

        add_hotkey(cfg.exit_key, self.close_window)  # Bind a keyboard event to close the window
        on_press(self.key_pressed)  # Bind a keyboard event to start the countdown

        text_weight = 'bold' if cfg.bold_text else 'normal'

        self.mega_label = Label(root, text='0', font=(cfg.font, cfg.text_size, text_weight), bg=cfg.mega_bg_color,
                                   fg=cfg.mega_text_color, width=2)
        set_clickthrough(self.mega_label.winfo_id(), cfg.transparent_color)
        self.mega_label.pack(expand=True, fill='both')

        self.heavy_label = Label(root, text='0', font=(cfg.font, cfg.text_size, text_weight), bg=cfg.heavy_bg_color,
                                    fg=cfg.heavy_text_color, width=2)
        set_clickthrough(self.heavy_label.winfo_id(), cfg.transparent_color)
        self.heavy_label.pack(expand=True, fill='both')

    def key_pressed(self, event):
        if event.name.lower() == cfg.mega_start_key.lower():
            self.mega_countdown(self.mega_label, cfg.mega_timeout_seconds, True)
        elif event.name.lower() == cfg.heavy_start_key.lower():
            self.heavy_countdown(self.heavy_label, cfg.heavy_timeout_seconds, True)

    def mega_countdown(self, label, time_left, new_run):
        if not new_run:
            if self.mega_time_left > time_left:
                return
            time_left -= 1
        elif self.mega_time_left == time_left:
            return
        self.mega_time_left = time_left

        if time_left >= 0:
            label.config(text=str(time_left))

            if time_left == cfg.sound_alarm_timeout_seconds and cfg.enable_sound_alarm:
                alrm.play_sound('mega')

            if time_left == 0 or time_left > cfg.mega_attention_timeout_seconds:
                label.config(bg=cfg.mega_bg_color, fg=cfg.mega_text_color)
            elif time_left <= cfg.mega_warning_timeout_seconds:
                label.config(bg=cfg.mega_warning_bg_color, fg=cfg.mega_warning_text_color)
            elif time_left <= cfg.mega_attention_timeout_seconds:
                label.config(bg=cfg.mega_attention_bg_color, fg=cfg.mega_attention_text_color)

            self.root.after(1000, lambda: self.mega_countdown(label, time_left, False))

    def heavy_countdown(self, label, time_left, new_run):
        if not new_run:
            if self.heavy_time_left > time_left:
                return
            time_left -= 1
        elif self.heavy_time_left == time_left:
            return
        self.heavy_time_left = time_left

        if time_left >= 0:
            label.config(text=str(time_left))

            if time_left == cfg.sound_alarm_timeout_seconds and cfg.enable_sound_alarm:
                alrm.play_sound('heavy')

            if time_left == 0 or time_left > cfg.heavy_attention_timeout_seconds:
                label.config(bg=cfg.heavy_bg_color, fg=cfg.heavy_text_color)
            elif time_left <= cfg.heavy_warning_timeout_seconds:
                label.config(bg=cfg.heavy_warning_bg_color, fg=cfg.heavy_warning_text_color)
            elif time_left <= cfg.heavy_attention_timeout_seconds:
                label.config(bg=cfg.heavy_attention_bg_color, fg=cfg.heavy_attention_text_color)

            self.root.after(1000, lambda: self.heavy_countdown(label, time_left, False))

    def close_window(self, event=None):
        alrm.destroy()
        self.root.destroy()


alrm.init(cfg.sound_alarm_timeout_seconds)
root = Tk()
clock = Clock(root)
root.mainloop()
