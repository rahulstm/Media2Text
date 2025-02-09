import os
import json
import whisper
from pathlib import Path

def find_audio_files(folder_path, file_types={'.mp3', '.wav'}):
   
    audio_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(tuple(file_types)):
                audio_files.append(os.path.join(root, file))
    return audio_files

def transcribe_audio_file(audio_path, model):
   
    result = model.transcribe(audio_path)
    return result["text"]

def save_transcription(file_path, text, save_folder):
    
    save_folder = Path(save_folder)
    save_folder.mkdir(parents=True, exist_ok=True) 
    save_file = save_folder / (Path(file_path).stem + ".json")
    
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump({"file": file_path, "transcription": text}, f, indent=4)

def process_audio_files(input_folder, output_folder):
    
    model = whisper.load_model("tiny")  
    audio_files = find_audio_files(input_folder)
    
    for audio in audio_files:
        print(f"Processing: {audio}")
        text = transcribe_audio_file(audio, model)
        save_transcription(audio, text, output_folder)
        print(f"Transcription saved for: {audio}\n")

if __name__ == "__main__":
    input_folder_path = r"C:\Users\hp\Downloads\Python_Assignment\media_folder" 
    output_folder_path = r"C:\Users\hp\Downloads\Python_Assignment\transcriptions"  
    process_audio_files(input_folder_path, output_folder_path)
