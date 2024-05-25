import tkinter as tk
from llm import explain_new_word
from tkinter import filedialog
import json
from myvocab import MyVocab


class aDocs:
    def __init__(self):
        self.filename_txt = ""
        self.filename_pkl = ""
        self.root = tk.Tk()
        self.root.title("Read Docs")
        self.load_vocab()
        
        self.text = tk.Text(self.root,height=30,width=100,font=("Arial", 13))        
        self.text.grid(row=0, column=1)
        
        #Setup shortcut keys
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<e>', lambda event: self.get_text_selected(mode="eng"))
        self.root.bind('<v>', lambda event: self.get_text_selected(mode="vni"))
        self.root.bind('<n>', lambda event: MyVocab())
        self.root.bind('<Control-x>', lambda event: self.destroy())
        
        self.content = ""
        self.root.mainloop()
    
    
    #Load vocab from file myvocab.json
    def load_vocab(self):
        try:
            with open('myvocab.json', 'r', encoding='utf8') as file:
                self.my_vocab = json.load(file)
        except: 
            self.my_vocab = {}
            
    #Load file .txt to show in the text widget        
    def open_file(self):
        self.filename_txt = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.filename_txt:
            with open(self.filename_txt, "r") as file:
                self.content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", self.content)
            self.text.config(state='normal')  # Enable the widget for editing
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, self.content)
            self.text.config(state='disabled')
                        
    # Get the selected text and call explain_new_word function to get the meaning of the word
    def get_text_selected(self,mode):
        text = self.text.get("sel.first", "sel.last") 
        print('Running...')
        json_infor = explain_new_word(self.content,text,type=mode)  
        key = json_infor['word']
        self.my_vocab[key] = json_infor
        self.Infor_Widget(key)
        
    #Create a new window to show the meaning of the word
    def Infor_Widget(self,word):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Meaning: {word}")
        text = tk.Text(details_window, font=('Arial', 13))
        text.insert(tk.END, str(self.my_vocab[word]['meaning']))
        text.pack()
        self.save_vocab()
        
        details_window.bind('<q>', lambda event: details_window.destroy())
        
    #Close main root
    def destroy(self):
        self.root.destroy()
        self.save_vocab()
    
    #Save vocab to file myvocab.json
    def save_vocab(self):
        with open('myvocab.json', 'w',encoding='utf8') as file:
            json.dump(self.my_vocab, file)


if __name__ == '__main__':
    aDocs()