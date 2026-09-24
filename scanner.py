from pathlib import Path
def scan_folder():

    beat_folder = Path(r"C:\Users\BEST\Desktop\beats\summer walker,muni long,kiana lede type beats\sampled beats")
    Recordings = []
    for file in beat_folder.iterdir():
        metadata = file.stem.split("_")

        Title, Bpm, Genre, Key, Price = metadata

        Bpm = int(Bpm)
        Price = int(Price)
        
        Beat = {"title" : Title,
                "bpm" : Bpm,
                "genre" : Genre,
                "key" : Key,
                "price" : Price,
                "filename" : file.name
                }
        Recordings.append(Beat)


    return Recordings


