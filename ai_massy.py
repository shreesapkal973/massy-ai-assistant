import tkinter as tk
from tkinter import ttk, scrolledtext
import pyttsx3
import speech_recognition as sr
import json
import random
from translate import Translator

class AIMassy:
    def __init__(self):
        self.name = "Massy"
        self.personality = {
            "species": "Female Robot Cat",
            "emotions": ["happy", "curious", "caring", "playful"],
            "knowledge_domains": ["general", "science", "arts", "technology"],
            "languages": ["en", "es", "fr", "de", "ja", "zh"]
        }
        
        self.window = tk.Tk()
        self.window.title("AI Massy - Your Personal Robot Cat Assistant")
        self.window.geometry("800x600")
        
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', 'female')
        
        self.setup_gui() 