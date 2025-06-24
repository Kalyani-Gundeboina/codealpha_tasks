import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source_folder():
    folder = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder)

def select_dest_folder():
    folder = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, folder)

def move_jpg_files():
    source = source_entry.get()
    destination = dest_entry.get()

    if not os.path.isdir(source) or not os.path.isdir(destination):
        messagebox.showerror("Error", "Select valid source and destination folders")
        return

    files_moved = 0

    for file in os.listdir(source):
        if file.lower().endswith('.jpg'):
            src_path = os.path.join(source, file)
            dest_path = os.path.join(destination, file)
            shutil.move(src_path, dest_path)
            files_moved += 1

    messagebox.showinfo("Done", f"{files_moved} .jpg files moved.")

# GUI Setup
root = tk.Tk()
root.title("JPG File Mover")
root.geometry("400x300")

tk.Label(root, text="Move .jpg Files to New Folder", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Select Source Folder:").pack()
source_entry = tk.Entry(root, width=40)
source_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_source_folder).pack()

tk.Label(root, text="Select Destination Folder:").pack(pady=10)
dest_entry = tk.Entry(root, width=40)
dest_entry.pack(pady=5)
tk.Button(root, text="Browse", command=select_dest_folder).pack()

tk.Button(root, text="Move .jpg Files", command=move_jpg_files, bg="lightgreen").pack(pady=20)

root.mainloop()
