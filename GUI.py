import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk
import sounddevice as sd
import soundfile as sf
import threading 
import requests

def start ():

    global PATH
    global is_recording
    is_recording = True

    def get_path():
        global PATH
        PATH = filedialog.askopenfilename(title='Select file', filetypes=[('Audio Files', '*.wav *.mp3')])
        
    def submit():
        global PATH
        print("Path:", PATH)
        if PATH:
            url = 'http://127.0.0.1:5000/predict'

            with open(PATH, 'rb') as f:
                files = {'file': f}
                response = requests.post(url, files=files)
                print('here')
            print("API response:", response.json())

    def start_rec():
        global is_recording
        global PATH
        is_recording = True

        def record():
            with sf.SoundFile('output.wav',samplerate=44100, mode='w', channels=2) as file:
                with sd.InputStream(samplerate=44100, channels=2, callback=lambda indata, frames, time, status: file.write(indata)):
                    while is_recording:
                        sd.sleep(100)

        threading.Thread(target=record, daemon=True).start()
        PATH = 'output.wav'

    def end_rec():
        global is_recording
        is_recording = False

    def submit_rec():
        pass

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

    submit_rec_file = tk.Button(right_frame, text='Submit',width=40,bg='lightgrey',fg='black',command=submit)
    submit_rec_file.pack(padx=5,pady=7)

    root.mainloop()