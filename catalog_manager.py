from database import (
    create_table,
    import_beats,
    view_all_beats,
    search_beat,
    filter_beats,
    update_beat,
    delete_beat
)

create_table()


while True:
     print("\n1. Import/Add beats")
     print("2. View all beats")
     print("3. Search for a beat")
     print("4. Filter beats")
     print("5. Update beat")
     print("6. Delete beat")
     print("7. Exit")

     try:
          option = int(input("Please select an option: "))

     except ValueError:
                print(f"Please enter a valid number between {1} and {7}")
                continue

     if option == 1:
            import_beats()
            print("Beats imported successfully.")

     elif option == 2:
            results = view_all_beats()
            for beat in results:
                  print(beat)

     elif option == 3:
           title = input("Enter the name of the beat: ")
           result = search_beat(title)
           if result:
                  print(result)
           else:
                 print("Beat not found.")

     elif option == 4:
           print("1. Filter by Genre")
           print("2. Filter by Key")
           
           filter_option = int(input("Please select a filter: "))
           if filter_option == 1:
                  genre = input("Enter genre: ")
                  results = filter_beats("genre", genre)
           elif filter_option == 2:
                  key = input("Enter key: ")
                  results = filter_beats("key", key)
           else:
                  print("Invalid filter option.")
                  continue
           if results:
                  for beat in results:
                         print(beat)
           else:
                 print("No beats found.")
           

     elif option == 5:
           title = input("Enter the name of the beat: ")
           new_genre = input("Enter the new genre: ")
           success = update_beat(title, new_genre)
           if success:
                  print("Beat updated successfully.")
           else:
                 print("Beat not found.")

     elif option == 6:
           title = input("Enter the name of the beat to delete: ")
           success = delete_beat(title)
           if success:
                 print("Beat deleted successfully.")
           else:
                 print("Beat not found.")

     elif option == 7:
           print("Leaving program...")
           break

     

     