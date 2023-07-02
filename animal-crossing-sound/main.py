import wave

def concatenate_audio_wave(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using Python's built-in wav module
    and save it to `output_path`. Note that extension (wav) must be added to `output_path`"""
    data = []
    for clip in audio_clip_paths:
        w = wave.open(clip, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(output_path, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

text = input("Animal Crossing-ify: ").lower()
text = text.replace("rl", "l")
text = text.replace("ll", "l")
text = [(x if x != " " else "_")+".wav" for x in text if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "+"ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()]
print(text)
text = ["./audio/"+x for x in text]
concatenate_audio_wave(text, "out.wav")