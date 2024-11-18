import customtkinter as ctk
from tkinter import filedialog, messagebox, ttk, simpledialog
import PyPDF2
import os
import subprocess

# Set the appearance and theme of the application
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# List to store selected PDF paths
selected_pdfs = []
# Variable to store the output directory
output_directory = ""

# Function to print the last page of a PDF
def print_last_page(pdf_path):
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            last_page = reader.pages[-1]

            # Create a temporary PDF file for the last page
            writer = PyPDF2.PdfWriter()
            writer.add_page(last_page)
            temp_pdf = "last_page_temp.pdf"

            with open(temp_pdf, "wb") as temp:
                writer.write(temp)

            # Cross-platform printing
            if os.name == 'nt':  # Windows
                import win32api
                win32api.ShellExecute(0, "print", temp_pdf, None, ".", 0)
            else:  # macOS or Linux
                subprocess.run(["lp", temp_pdf], check=True)

            messagebox.showinfo("Success", f"Last page of {pdf_path} printed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to print last page: {e}")

# Function to select multiple PDFs and print their last pages
def print_last_pages_ui():
    if selected_pdfs:
        for pdf_path in selected_pdfs:
            print_last_page(pdf_path)
    else:
        messagebox.showwarning("No Files Selected", "Please select PDF files first.")

# Function to select multiple PDF files and add them to the list
def select_multiple_files_ui():
    global selected_pdfs
    pdf_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if pdf_paths:
        selected_pdfs.extend(pdf_paths)
        update_table()

# Function to update the table with detailed information of selected PDFs
def update_table():
    for i in tree.get_children():
        tree.delete(i)
    for pdf_path in selected_pdfs:
        file_name = os.path.basename(pdf_path)
        try:
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                num_pages = len(reader.pages)
            file_size = os.path.getsize(pdf_path) / 1024  # Size in KB
            tree.insert("", "end", values=(file_name, f"{file_size:.2f} KB", num_pages))
        except Exception as e:
            tree.insert("", "end", values=(file_name, "Error reading file", "-"))

# Function to set the location to save files
def set_output_directory():
    global output_directory
    output_directory = filedialog.askdirectory()
    if output_directory:
        messagebox.showinfo("Output Directory Set", f"Files will be saved to: {output_directory}")

# Function to rename multiple PDF files
def rename_files_ui():
    if not selected_pdfs:
        messagebox.showwarning("No Files Selected", "Please select PDF files first.")
        return
    rename_prefix = simpledialog.askstring("Rename Files", "Enter the prefix for renaming files:")
    if rename_prefix:
        for index, pdf_path in enumerate(selected_pdfs):
            directory = os.path.dirname(pdf_path)
            new_name = f"{rename_prefix}_{index + 1}.pdf"
            new_path = os.path.join(directory, new_name)
            try:
                os.rename(pdf_path, new_path)
                selected_pdfs[index] = new_path
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename {pdf_path}: {e}")
        update_table()
        messagebox.showinfo("Success", "Files renamed successfully!")

# Set up the GUI
root = ctk.CTk()
root.title("PDF Tool")
root.geometry("800x700")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

button_frame = ctk.CTkFrame(root, fg_color='#FFFFFF')
button_frame.grid(row=0, column=0, pady=10, sticky="ew")
button_frame.columnconfigure((0, 1, 2), weight=1)

# Create buttons with CustomTkinter for a modern look
button_style = {
    "font": ("Arial", 14),
    "corner_radius": 8,  # Rounded corners
    "fg_color": "#FFFFFF",
    "text_color": "#000000",
    "hover_color": "#e0e0e0"
}

print_button = ctk.CTkButton(button_frame, text="🖨️ Print Last Page", command=print_last_pages_ui, **button_style)
print_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

select_button = ctk.CTkButton(button_frame, text="📂 Select Files", command=select_multiple_files_ui, **button_style)
select_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

set_directory_button = ctk.CTkButton(button_frame, text="💾 Set Directory", command=set_output_directory, **button_style)
set_directory_button.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

rename_frame = ctk.CTkFrame(root, fg_color='#FFFFFF')
rename_frame.grid(row=2, column=0, pady=10, sticky="ew")
rename_frame.columnconfigure(0, weight=1)

rename_button = ctk.CTkButton(rename_frame, text="✏️ Rename Files", command=rename_files_ui, **button_style)
rename_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Set up the table to show detailed information of selected PDFs
tree = ttk.Treeview(root, columns=("File Name", "Size", "Pages"), show="headings")
tree.heading("File Name", text="File Name")
tree.heading("Size", text="Size (KB)")
tree.heading("Pages", text="Pages")
tree.grid(row=1, column=0, pady=10, sticky="nsew")

root.mainloop()
