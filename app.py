import streamlit as st
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
st.title("Beat Catalog Manager")
st.write("Welcome to my Beat Catalog Manager!")

option = st.sidebar.selectbox(
    "Choose an option",
    [
        "View All Beats",
        "Search for a Beat",
        "Filter Beats",
        "Update Beat",
        "Delete Beat",
        "Import Beats"
    ]
)
if option == "View All Beats":
    results = view_all_beats()
    st.dataframe(results, hide_index=True)

elif option == "Search for a Beat":
    title = st.text_input("Enter the name of the beat")

    if st.button("Search"):
        results = search_beat(title)

        if results:
            st.dataframe(results, hide_index=True)
        else:
            st.warning("Beat not found.")

elif option == "Filter Beats":
    filter_option = st.selectbox(
        "Filter by",
        ["Genre", "Key"]
    )

    if filter_option == "Genre":
        value = st.text_input("Enter the genre")
    else:
        value = st.text_input("Enter the key")

    if st.button("Filter"):
        results = filter_beats(
            filter_option.lower(),
            value
        )

        if results:
            st.dataframe(results, hide_index=True)
        else:
            st.warning("No beats found.")

elif option == "Update Beat":
    title = st.text_input("Enter the name of the beat")

    update_option = st.selectbox(
        "What would you like to update?",
        ["Genre", "Key", "BPM", "Price"]
    )

    new_option = st.text_input("Enter the new option")

    if st.button("Update"):
        success = update_beat(title, update_option.lower(), new_option)

        if success:
            st.success("Beat updated successfully.")
        else:
            st.warning("Beat not found.")

elif option == "Delete Beat":
    title = st.text_input("Enter the name of the beat to delete")

    if st.button("Delete"):
        success = delete_beat(title)

        if success:
            st.success("Beat deleted successfully.")
        else:
            st.warning("Beat not found.")

elif option == "Import Beats":
    st.write("Scan your beat folder and add new beats to the database.")

    if st.button("Import Beats"):
        import_beats()
        st.success("Beats imported successfully.")