# My Python Capstone Project
# Beat Catalog Manager

A small Python project for cataloging music beats. It scans beat filenames, stores their metadata in SQLite, and provides a Streamlit interface and a command line menu to browse and manage the catalog.

## Features

- Import beat metadata from files in a folder
- View all beats in the local catalog
- Search by title
- Filter by genre or musical key
- Update a beat's genre, key, BPM, or price in the Streamlit app
- Delete beats by title

## How beat filenames are read

The scanner expects each filename (without its extension) to contain five underscore-separated fields in this order:

```text
Title_BPM_Genre_Key_Price.ext
```

For example:

```text
Late_Night_92_RnB_Cmin_25.wav
```

The current scanner splits on every underscore, so the title and other fields must not contain underscores. BPM and price must be whole numbers. Files that do not follow this format can cause an import error.

## Setup

Requirements: Python 3 and Streamlit. SQLite is included with Python.

1. Clone this repository and open a terminal in its directory.
2. (Recommended) Create and activate a virtual environment.
3. Install Streamlit:

   ```bash
   python -m pip install streamlit
   ```

4. Open `scanner.py` and change `beat_folder` to the folder that contains your beat files. The current value points to a folder on the original developer's Windows computer.

The SQLite database file, `beats.db`, is created in the current working directory the first time the application runs. It is local application data and is ignored by Git.

## Run the app

Start the Streamlit web interface from the repository directory:

```bash
python -m streamlit run app.py
```

Streamlit prints a local URL to open in your browser.

To use the command line menu instead:

```bash
python catalog_manager.py
```

Choose **Import Beats** in the app or option **1** in the command line menu to scan the folder and add new filenames to the database. Existing filenames are ignored during import.

## Project files

- `app.py` — Streamlit user interface.
- `catalog_manager.py` — command line interface.
- `database.py` — SQLite setup and catalog operations.
- `scanner.py` — reads beat filenames and extracts metadata.
- `project_template.md` — capstone project summary and expected value.


This is a learning project and should be tested with copies of beat files and a backup of the database before managing important catalog data.
