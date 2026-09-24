# Beat Catalog Manager — Capstone Project

1. What problem does this project solve?

Producers and beat sellers can accumulate large folders of instrumentals with useful details embedded in their filenames, such as title, tempo, genre, musical key, and price. Finding a particular beat or comparing the catalog by genre or key can become tedious when the information is only available by opening files one at a time.

This project turns those filename details into a searchable local catalog.

2. What tools were used?

- Python for application logic.
- Streamlit for a browser-based interface.
- SQLite for local data storage.
- pathlib for reading files and extracting filename stems.

The scanner parses filenames in the format `Title_BPM_Genre_Key_Price.mp3`. The database layer imports the parsed information and provides search, filter, update, and delete operations. The project also includes a command line interface.

 3. What insights or solutions does the project offer?

The catalog makes it possible to inspect a collection without opening every audio file. A user can search by title, filter by genre or key, and see BPM and price alongside each beat.

The project can help answer practical catalog questions, such as:

- Which beats are listed under a particular genre or key?
- What tempo and price are associated with a beat?
- Which filename details need to be corrected in the catalog?

The project does not yet analyze audio or validate whether the filename metadata is accurate. Those could be future improvements.

#4. How could a business or community benefit?

For an independent producer or small beat-selling business, a searchable catalog can reduce the time spent locating and organizing work. Keeping title, tempo, genre, key, and price together can also make it easier to prepare selections for customers and maintain consistent listings.

The expected benefit is improved organization and faster retrieval. The project has not measured time saved or business impact, so those outcomes should be evaluated with real users and a larger catalog.

