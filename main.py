from word import Word
from uvsim import UVSim 
from memory_editor import MemoryEditor
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import customtkinter as ctk

def main():
    window = ctk.CTk()
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('green')
    window.title('UVSIM')

    canvas1 = ctk.CTkCanvas(window)
    canvas1.configure(bg = 'white')

    canvas2 = ctk.CTkCanvas(window)
    canvas1.configure(bg='white')

    canvas3 = ctk.CTkCanvas(window)
    canvas3.configure(bg='white')

    path = ''
    sim = 0
    mem_editor = 0
    
    def get_filepath():
        nonlocal path
        nonlocal sim
        path = fd.askopenfilename(filetypes=[('Text Files', '*.txt')])
        filepath_lbl.configure(text=path)
        if path != '':
            con_editor_btn.grid(row=4, column=4, padx=20, pady=20)

    def go_to_editor():
        nonlocal sim, mem_editor
        sim = UVSim()
        sim.read_file(path) #read filepath here
        mem_editor = MemoryEditor(sim)
        canvas1.grid_remove()
        canvas2.grid()

    def mem_insert():
        # Read from value and insert into position
        nonlocal mem_editor
        val=int(value_entry.get())
        pos=int(pos_entry.get())
        mem_editor.insert_val(val, pos)

    def mem_delete():
        # delete position from memory
        nonlocal mem_editor
        pos=int(pos_entry.get())
        mem_editor.delete(pos)

    def mem_copy():
        # copy value from position into clipboard
        nonlocal mem_editor
        pos=int(pos_entry.get())
        mem_editor.copy(pos)

    def mem_cut():
        # copy value from position into clipboard and delete from memory
        nonlocal mem_editor
        pos=int(pos_entry.get())
        mem_editor.cut(pos)

    def mem_paste():
        # paste value from clipboard into position in memory
        nonlocal mem_editor
        pos=int(pos_entry.get())
        mem_editor.paste(pos)

    def save_memory():
        nonlocal path, sim
        with open(path, 'w') as file:
            file.write(str(sim.memory))        

    def edit_help():
        mb.showinfo(title=help,
                    message="""This screen allows you to edit the memory loaded into the simulator before
                    running the simulator. 
                    Insert: Insert the value specified in 'Value' into 'Position'
                    Delete: Delete the value specified in 'Position', remaining values shift
                    Copy: Copy the value in 'Position' to the clipboard
                    Cut: Cut the value in 'Position'
                    Paste: Paste the value from your clipboard into 'Position'
                    Save: Saves the current memory to the same textfile""")
        
    def run_help():
        mb.showinfo(title=help, 
                    message="""This screen runs the memory of UVSim and shows:
                    the list of commands run and
                    the final memory after the system runs""")
        
    def read_continue():
        pass

    def start_over():
        canvas3.grid_remove()
        canvas1.grid()        

    def run():
        nonlocal sim
        memory, info = sim.operate()
        run_results.insert(f'Traceback: \n {info}') 
        final_mem.insert(f'Final memory contents: {memory}')

    welcome_label = ctk.CTkLabel(canvas1, text='Welcome to UVSim')
    filepath_lbl = ctk.CTkLabel(canvas1, text='no filepath open')
    filepath_btn = ctk.CTkButton(canvas1, text='open txt file', command=get_filepath)
    con_editor_btn = ctk.CTkButton(canvas1, text='Continue', command=go_to_editor)
    welcome_label.grid(row=1, column=1, padx=20, pady=20, columnspan=2)
    filepath_lbl.grid(row=2, column=2, padx=20, pady=20)
    filepath_btn.grid(row=2, column=1, padx=20, pady=20)

    editor_label = ctk.CTkLabel(canvas2, text='UVSim Memory Editor')
    value_label = ctk.CTkLabel(canvas2, text='Value:')
    pos_label = ctk.CTkLabel(canvas2, text='Position:')
    cur_mem_label = ctk.CTkLabel(canvas2, text='Current Memory:')
    insert_btn = ctk.CTkButton(canvas2, text='Insert', command=mem_insert)
    del_btn = ctk.CTkButton(canvas2, text='Delete', command=mem_delete)
    cpy_btn = ctk.CTkButton(canvas2, text='Copy', command=mem_copy)
    cut_btn = ctk.CTkButton(canvas2, text='Cut', command=mem_cut)
    paste_btn = ctk.CTkButton(canvas2, text='Paste', command=mem_paste)
    save_btn=ctk.CTkButton(canvas2, text='Save', command=save_memory)
    run_btn = ctk.CTkButton(canvas2, text='Run', command=run)
    help_btn=ctk.CTkButton(canvas2, text='Help', command=edit_help)
    value_entry=ctk.CTkEntry(canvas2)
    pos_entry=ctk.CTkEntry(canvas2)
    edit_mem_textbox=ctk.CTkTextbox(canvas2, height=10, width=50)
    editor_label.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
    value_label.grid(row=2, column=1, padx=20, pady=20)
    pos_label.grid(row=3, column=1, padx=20, pady=20)
    cur_mem_label.grid(row=2, column=3, columnspan=2, padx=20, pady=20)
    insert_btn.grid(row=4, column=1, columnspan=2, padx=20, pady=20)
    del_btn.grid(row=5, column=1, columnspan=2, padx=20, pady=20)
    cpy_btn.grid(row=6, column=1, columnspan=2, padx=20, pady=20)
    cut_btn.grid(row=7, column=1, columnspan=2, padx=20, pady=20)
    paste_btn.grid(row=8, column=1, columnspan=2, padx=20, pady=20)
    save_btn.grid(row=9, column=1, padx=20, pady=20)
    run_btn.grid(row=9, column=1, padx=20, pady=20)
    help_btn.grid(row=9, column=2, padx=20, pady=20)
    value_entry.grid(row=2, column=2, padx=20, pady=20)
    pos_entry.grid(row=3, column=2, padx=20, pady=20)
    edit_mem_textbox.grid(row=3, column=3, columnspan=2, padx=20, pady=20)

    results_label = ctk.CTkLabel(canvas3, text='Run UVSim')
    ops_traceback_label = ctk.CTkLabel(canvas3, text='Operations Traceback:')
    final_mem_label = ctk.CTkLabel(canvas3, text='Final Memory Contents')
    read_label = ctk.CTkLabel(canvas3, text='Read:')
    read_cont_btn = ctk.CTkButton(canvas3, text='Continue', command=read_continue)
    startover_btn = ctk.CTkButton(canvas3, text='Start Over', command=start_over)
    entry_help_btn = ctk.CTkButton(canvas3, text='Help', command=run_help)
    read_entry = ctk.CTkEntry(canvas3)
    final_mem = ctk.CTkTextbox(canvas3, height=10, width=5)
    run_results = ctk.CTkTextbox(canvas3, height=10, width=5)
    results_label.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
    ops_traceback_label.grid(row=2, column=1, columnspan=2, padx=20, pady=20)
    final_mem_label.grid(row=4, column=3, columnspan=4, padx=20, pady=20)
    read_label.grid(row=2, column=3, padx=20, pady=20)
    read_cont_btn.grid(row=3, column=4, padx=20, pady=20)
    startover_btn.grid(row=9, column=4, padx=20, pady=20)
    entry_help_btn.grid(row=9, column=1, padx=20, pady=20)
    read_entry.grid(row=2, column=4, padx=20, pady=20)
    run_results.grid(row=3, column=2, padx=20, pady=20)

    canvas1.grid()
    window.mainloop()

if __name__ == "__main__":
    main()
