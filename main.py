from collections import OrderedDict
import os
Lyrics = os.fsencode("Lyrics")

with os.scandir(Lyrics) as files:
    for filename in files:
        file = open(filename, "r")
        lyrics = file.read()
        for char in lyrics:
            if char == "?":
                lyrics = lyrics.replace(char, "")
        lyrics = lyrics.lower().split()
        lyrics_dict = {}

        for word in lyrics:
            if word not in lyrics_dict.keys():
                lyrics_dict.update({word: 1})
            else:
                lyrics_dict[word] += 1

        sorted_file = OrderedDict(sorted(lyrics_dict.items(), key=lambda kv: kv[1], reverse=True))

        workingfile = open(f"Tables/Table {filename.name.decode('utf-8').split('.')[0]}.txt", "w")

        for word, number in sorted_file.items():
            workingfile.write(f"{number}\t{word}\n")