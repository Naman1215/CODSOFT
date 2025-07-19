import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.configure(bg='#f0f0f0')

        self.tasks = self.load_tasks()

        # --- UI Elements ---
        header_font = ('Helvetica', 16, 'bold')
        self.header = tk.Label(root, text="To-Do List 📝", font=header_font, bg='#f0f0f0')
        self.header.pack(pady=10)

        # Frame for the listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=5, padx=10)

        self.task_listbox = tk.Listbox(
            self.frame,
            width=50,
            height=12,
            selectmode=tk.SINGLE,
            font=('Helvetica', 10),
            bd=0,
            highlightthickness=0
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry widget for new tasks
        self.entry = tk.Entry(root, font=('Helvetica', 12), width=38)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task_event) # Allow adding with Enter key

        # Frame for buttons
        button_frame = tk.Frame(root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        btn_font = ('Helvetica', 10)

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, font=btn_font, bg='#c8e6c9')
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(button_frame, text="Mark Complete", command=self.update_task, font=btn_font, bg='#fff9c4')
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, font=btn_font, bg='#ffcdd2')
        self.delete_button.grid(row=0, column=2, padx=5)
        
        # Save tasks when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.populate_tasks()

    def load_tasks(self):
        """Loads tasks from the JSON file."""
        if not os.path.exists(TASKS_FILE):
            return []
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            messagebox.showerror("Error", f"Could not read tasks from {TASKS_FILE}.")
            return []

    def save_tasks(self):
        """Saves the current list of tasks to the JSON file."""
        with open(TASKS_FILE, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def populate_tasks(self):
        """Clears and repopulates the listbox with current tasks."""
        self.task_listbox.delete(0, tk.END)
        for i, task_item in enumerate(self.tasks):
            status = "✓" if task_item["completed"] else " "
            display_text = f"[{status}] {task_item['task']}"
            self.task_listbox.insert(tk.END, display_text)
            # Style completed tasks differently
            if task_item["completed"]:
                self.task_listbox.itemconfig(i, {'fg': 'gray', 'font': ('Helvetica', 10, 'italic')})
            else:
                 self.task_listbox.itemconfig(i, {'fg': 'black', 'font': ('Helvetica', 10)})

    def add_task(self):
        """Adds a new task from the entry widget to the list."""
        task_description = self.entry.get()
        if task_description:
            self.tasks.append({"task": task_description, "completed": False})
            self.entry.delete(0, tk.END)
            self.populate_tasks()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def add_task_event(self, event):
        """Wrapper to add task on Enter key press."""
        self.add_task()

    def update_task(self):
        """Marks the selected task as completed or incomplete."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.populate_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        """Deletes the selected task from the list."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_to_delete = self.tasks[selected_index]['task']
            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete this task?\n\n'{task_to_delete}'"):
                self.tasks.pop(selected_index)
                self.populate_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
            
    def on_closing(self):
        """Saves tasks and closes the application."""
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()