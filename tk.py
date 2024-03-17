import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PyText")

        self.text_area = tk.Text(root)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.exit_program)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, content)

    def save_file(self):
        content = self.text_area.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

    def exit_program(self):
        self.root.quit()

def main():
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
