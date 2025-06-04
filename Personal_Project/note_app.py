import tkinter as tk
from tkinter import ttk

def create_note():
    def save_note():
        title = title_entry.get()
        content = content_text.get("1.0", tk.END).strip()
        if title and content:
            notes_display_tab2.config(state='normal')
            notes_display_tab2.insert(tk.END, f"📝 {title}\n{content}\n{'-'*50}\n")
            notes_display_tab2.config(state='disabled')
            note_window.destroy()

    note_window = tk.Toplevel(root)
    note_window.title("New Note")
    note_window.geometry("400x250")
    note_window.resizable(False, False)

    frame = ttk.Frame(note_window, padding=15)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Title:").pack(anchor="w")
    title_entry = ttk.Entry(frame, width=40)
    title_entry.pack(fill="x", pady=5)

    ttk.Label(frame, text="Content:").pack(anchor="w")
    content_text = tk.Text(frame, height=6, wrap="word")
    content_text.pack(fill="both", pady=5)

    ttk.Button(frame, text="Save", command=save_note).pack(pady=5)

def delete_notes():
    notes_display_tab2.config(state='normal')
    notes_display_tab2.delete("1.0", tk.END)
    notes_display_tab2.config(state='disabled')

# === MAIN WINDOW ===
root = tk.Tk()
root.title("Notes App")
root.geometry("600x550")
root.resizable(False, False)

# Apply theme
style = ttk.Style()
style.theme_use('clam')

# Tabs
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Notes")
notebook.pack(expand=True, fill="both")

# === TAB 1 ===
frame1 = ttk.Frame(tab1, padding=20)
frame1.pack(expand=True, fill="both")

ttk.Label(frame1, text="Click 'New Note' to create a note.\nIt will appear in the 'Notes' tab.", font=("Segoe UI", 11)).pack(pady=30)

btn_frame = ttk.Frame(frame1)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="New Note", command=create_note, width=20).pack()

# === TAB 2 (WHERE NOTES SHOW UP) ===
frame2 = ttk.Frame(tab2, padding=10)
frame2.pack(expand=True, fill="both")

notes_display_tab2 = tk.Text(frame2, wrap="word", height=15, state="disabled", bg="#f7f7f7", relief="flat", bd=1)
notes_display_tab2.pack(expand=True, fill="both", pady=(0, 10))

ttk.Button(frame2, text="Delete All", command=delete_notes, width=20).pack()

# === RUN ===
root.mainloop()
