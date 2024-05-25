import tkinter as tk
import json


class MyVocab:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Vocab")
        self.root.bind('<q>', lambda event: self.destroy())
        self.open_file()
        self.root.mainloop()
        
    def open_file(self):
        with open('myvocab.json', 'r', encoding='utf8') as file:
            self.my_vocab = json.load(file)

        # Create a Listbox widget       
        listbox = tk.Listbox(self.root, width=50, height=20, font=('Arial', 20)) 
        listbox.bind('<<ListboxSelect>>', self.show_details)
        keys = self.my_vocab.keys()
        tk.Label(self.root, text=f"My Vocab: {len(list(keys))}", font=('Arial', 20)).grid(row=0, column=1)

        for key in keys:
            listbox.insert(tk.END, key)

        # Display the Listbox widget
        listbox.grid(row=1, column=1)
        
    def show_details(self, event):
        # Get the selected word
        widget = event.widget
        selection = widget.curselection()
        word = widget.get(selection[0])

        # Create a new window
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Meaning: {word}")

        # Create a Label widget
        text = tk.Text(details_window, font=('Arial', 13))

        # Insert the details
        text.insert(tk.END,f"({self.my_vocab[word]['parts of speech']})\n" + str(self.my_vocab[word]['meaning']))

        # Display the Text widget
        text.pack()
        details_window.bind('<q>', lambda event: details_window.destroy())


    def destroy(self):
        self.root.destroy()
        
        
if __name__ == '__main__':
    MyVocab()
        