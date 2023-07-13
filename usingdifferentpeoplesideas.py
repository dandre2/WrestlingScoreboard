import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Counting Seconds")
        self.counter = 90
        self.active_counter = False
        self.label = tk.Label(self, fg="black")
        self.label.pack()
        self.button = tk.Button(self, text='Start', width=50, command=self.start_stop)
        self.button.pack()

    def count(self):
        if self.active_counter:
            self.counter -= 1
            self.label.config(text=self.counter)
            self.label.after(1000, self.count)

    def start_stop(self):
        if self.button['text'] == 'Start':
            self.active_counter = True
            self.count()
            self.button.config(text="Stop")
        else:
            self.active_counter = False
            self.button.config(text="Start")


if __name__ == "__main__":
    App().mainloop()