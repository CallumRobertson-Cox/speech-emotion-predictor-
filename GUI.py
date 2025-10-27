import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk

PATH = None

def get_path():
    global PATH
    PATH = filedialog.askopenfilename(title='Select file', filetypes=[('Audio Files', '*.wav *.mp3')])
    
def submit():
    print(PATH)

def start_rec():
    print("Recording has started")

def end_rec():
    print("Recording has ended")

def submit_rec():
    print("Recording submitted")

BG_COLOR = "#bff1ff"

root = tk.Tk()
root.title("Speech to emotion")
root.geometry("700x400")
root.configure(bg=BG_COLOR)

top_frame = tk.Frame(root, bg=BG_COLOR)
top_frame.pack(side='top',pady=20,fill='x')

left_frame = tk.Frame(root, bg=BG_COLOR)
left_frame.pack(side='left',anchor='sw')

right_frame = tk.Frame(root, bg=BG_COLOR)
right_frame.pack(side='right', anchor='se')

Label = tk.Label(top_frame, text = "Submit an audio File or speak into your microphone for an emotion prediction", font=('Arial',15), bg=BG_COLOR)
Label.pack(side='top')

img = Image.open('emotions.png')
img = img.resize((380,190))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(top_frame, image=photo,bg=BG_COLOR)
img_label.pack(pady=10)

import_file_button = tk.Button(left_frame,text='Choose File',width=40,bg='lightgrey',fg='black',command=get_path)
import_file_button.pack(pady=15, padx=5)

submit_file_button = tk.Button(left_frame,text='Submit',width=40,bg='lightgrey',fg='black', command=submit)
submit_file_button.pack(pady=15, padx=5)

start_recording_button = tk.Button(right_frame,text='Record',width=40, bg='lightgrey',fg='black',command=start_rec)
start_recording_button.pack(padx=5, pady=7)

end_recording_button = tk.Button(right_frame,text='End Recording',width=40, bg='lightgrey',fg='black',command=end_rec)
end_recording_button.pack(padx=5, pady=7)

submit_rec_file = tk.Button(right_frame, text='Submit',width=40,bg='lightgrey',fg='black',command=submit_rec)
submit_rec_file.pack(padx=5,pady=7)

root.mainloop()