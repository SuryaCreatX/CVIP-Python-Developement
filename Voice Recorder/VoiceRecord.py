import pyaudio
import wave
import tkinter as tk
from tkinter import messagebox

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Voice Recorder")  
        
        description_label = tk.Label(root, text="Record and save audio using your microphone.\nPlease note that the audio is recorded via the system's microphone only.")
        description_label.pack(pady=10)
        
        self.is_recording = False
        self.frames = []
        
        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.save_button = tk.Button(root, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack(pady=5)
        
    def start_recording(self):
        self.is_recording = True
        self.frames = []
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)
        
        self.recording_label = tk.Label(root, text="Recording...", font=("Helvetica", 14, "bold"))
        self.recording_label.pack(pady=10)
        
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100
        self.filename = "output.wav"
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.fs,
                                  frames_per_buffer=self.chunk,
                                  input=True)
        
        while self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
            self.root.update()
        
        self.stream.stop_stream()
        self.stream.close()
        
    def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)
        
        if hasattr(self, 'recording_label'):
            self.recording_label.destroy()
        
    def save_recording(self):
        if len(self.frames) == 0:
            messagebox.showwarning("Warning", "No recording to save.")
            return
        
        self.start_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)
        
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        
        messagebox.showinfo("Success", "Recording saved as 'output.wav' on the desktop.")

root = tk.Tk()
app = VoiceRecorderApp(root)
root.mainloop()
