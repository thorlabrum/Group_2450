from word import Word
from uvsim import UVSim 
import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk

def main():
    window = ctk.CTk()
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('blue')
    window.title('UV SIM')

    canvas = ctk.CTkCanvas(window)
    canvas.configure(bg = 'black')
    canvas.grid()

    path = ''
    def get_filepath():
        global path
        path = fd.askopenfilename(filetypes=[('Text Files', '*.txt')])
        filepath_lbl.configure(text=path)

    def run():
        sim = UVSim()
        if path != '':
            sim.read_file(path) #read filepath here
            memory, info = sim.operate()
            run_results.insert(f'Traceback: \n {info}, Final memory contents: {memory}')
            #also add so any errors go into the run_results instead

    info_label = ctk.CTkLabel(canvas, text='Welcome to UVSim')
    filepath_btn = ctk.CTkButton(canvas, text='open txt file', command=get_filepath)
    filepath_lbl = ctk.CTkLabel(canvas, text='no filepath open')
    run_btn = ctk.CTkButton(canvas, text = 'Run', command = run)
    run_results = ctk.CTkTextbox(canvas, height=5, width=1)

    info_label.grid(row=1, column=1, padx=20, pady=20, columnspan=2)
    filepath_btn.grid(row=2, column=1, padx=20, pady=20)
    filepath_lbl.grid(row=2, column=2, padx=20, pady=20)
    run_btn.grid(row=3, column=1, padx=20, pady=20)
    run_results.grid(row=3, column=2, padx=20, pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()
