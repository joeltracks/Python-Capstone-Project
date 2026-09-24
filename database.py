import sqlite3
from scanner import scan_folder

# Creating a Connection to a Sqlite database
cx = sqlite3.connect("beats.db", check_same_thread=False)
    # Cursor object to send Sqlite commands to database
cursor = cx.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS beats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
bpm INTEGER,
genre TEXT,
beat_key TEXT,
price INTEGER,
filename TEXT UNIQUE
)
""")
def import_beats():
    beats = scan_folder()
    for beat in beats:
        cursor.execute("""
        INSERT OR IGNORE INTO beats (title, bpm, genre, beat_key, price, filename)
        VALUES (?, ?, ?, ?, ?, ?)
""",(
        beat["title"],
        beat["bpm"],
        beat["genre"],
        beat["key"],
        beat["price"],
        beat["filename"]
    ))
    cx.commit()

def view_all_beats():
    cursor.execute("SELECT * FROM beats")
    results = cursor.fetchall()

    beats = []

    for beat in results:
        beats.append({
            "ID": beat[0],
            "Title": beat[1],
            "BPM": beat[2],
            "Genre": beat[3],
            "Key": beat[4],
            "Price": beat[5],
            "Filename": beat[6]
        })

    return beats
    
def search_beat(title):
    cursor.execute(
        "SELECT * FROM beats WHERE LOWER(title) = LOWER(?)",
        (title,)
    )

    results = cursor.fetchall()

    beats = []

    for beat in results:
        beats.append({
            "ID": beat[0],
            "Title": beat[1],
            "BPM": beat[2],
            "Genre": beat[3],
            "Key": beat[4],
            "Price": beat[5],
            "Filename": beat[6]
        })

    return beats

def update_beat(title, update_option, new_option):
    if update_option == "genre":
        column = "genre"

    elif update_option == "key":
        column = "beat_key"

    elif update_option == "bpm":
        column = "bpm"

    elif update_option == "price":
        column = "price"

    else:
        return False
    cursor.execute(
        f"UPDATE beats SET {column} = ? WHERE LOWER(title) = LOWER(?)",
        (new_option, title)
    )
    updated = cursor.rowcount
    cx.commit()

    if updated == 1:
        return True
    else:
        return False

def filter_beats(filter_type, value):
    if filter_type == "genre":
        cursor.execute(
            "SELECT * FROM beats WHERE LOWER(genre) = LOWER(?)",
            (value,)
        )

    elif filter_type == "key":
        cursor.execute(
            "SELECT * FROM beats WHERE LOWER(beat_key) = LOWER(?)",
            (value,)
        )

    results = cursor.fetchall()
    return results

def delete_beat(title):
    cursor.execute("DELETE FROM beats WHERE LOWER(title) = LOWER(?)", (title,))
    deleted = cursor.rowcount
    cx.commit()

    if deleted == 1:
        return True
    else:
        return False





