import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
import PyPDF2

# Function to create a new PDF
def create_pdf(output_path):
    c = canvas.Canvas(output_path)
    c.drawString(100, 750, "Hello, this is a PDF created with Python!")
    c.drawString(100, 730, "You can add text, images, and more.")
    c.save()

# Function to create a PDF with user input from the GUI
def create_pdf_ui():
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
    if output_path:
        try:
            create_pdf(output_path)
            messagebox.showinfo("Success", "PDF created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create PDF: {e}")

# Function to add a blank page to an existing PDF
def add_page_to_pdf(input_pdf, output_pdf):
    try:
        with open(input_pdf, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            writer = PyPDF2.PdfWriter()

            # Copy original pages
            for page in reader.pages:
                writer.add_page(page)

            # Add new blank page
            writer.add_blank_page(width=210, height=297)

            with open(output_pdf, "wb") as output_f:
                writer.write(output_f)
        messagebox.showinfo("Success", "Blank page added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to edit PDF: {e}")

# Function to select a PDF and add a blank page
def edit_pdf_ui():
    input_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                   filetypes=[("PDF files", "*.pdf")])
        if output_path:
            add_page_to_pdf(input_path, output_path)

# Set up the GUI
root = tk.Tk()
root.title("PDF Tool")
root.geometry("300x150")

create_button = tk.Button(root, text="Create PDF", command=create_pdf_ui, width=20)
create_button.pack(pady=10)

edit_button = tk.Button(root, text="Add Blank Page to PDF", command=edit_pdf_ui, width=20)
edit_button.pack(pady=10)

root.mainloop()
