tab_star_easy = [
    "e|------------------|",
    "B|--------0--2--2--0|",
    "G|--3--3------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
    "",
    "e|------------------|",
    "B|--------0--3--2--0|",
    "G|--3--3------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
    "",
    "e|------------------|",
    "B|--------0--2--2--0|",
    "G|--3--3------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
]
tab_star_intermediate = [
    "e|----6-------------|",
    "B|--------0--2--2--0|",
    "G|--3--3------------|",
    "D|--------4---------|",
    "A|------3-----------|",
    "E|------1-----------|",
    "",
    "e|------1-----------|",
    "B|--------0--3--2--0|",
    "G|--3--3------------|",
    "D|----------3-4-----|",
    "A|---2----4---------|",
    "E|------6-----------|",
    "",
    "e|------------------|",
    "B|--------0--2--2--0|",
    "G|--3--3------------|",
    "D|-----6------------|",
    "A|-----5------------|",
    "E|----3-------------|",
]



def show_menu():
    print("\n--- Level Menu ---")
    print("1. Easy Level")
    print("2. Intermediate Level")
    print("3. Difficult Level")
    print("4. Exit")

def show_songs(level):
    songs = {
        "Easy Level": ["star easy", "let her go easy", "your beautiful easy"],
        "Intermediate Level": ["star intermediate", "let her go intermediate", "your beautiful intermediate"],
        "Difficult Level": ["star hard ", "let her go hard", "your beautiful hard"]
    }
    
    print(f"\n--- Songs for {level} ---")
    easy_songs = songs[level]

# Imprimir las canciones guardadas
    print(f"\n--- Songs for {level} ---")
    for song in easy_songs:
        print(song)
    print(easy_songs)
        
    

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            level = "Easy Level"
            print(f"You selected {level}.")
            show_songs(level)
            
        elif choice == "2":
            level = "Intermediate Level"
            print(f"You selected {level}.")
            show_songs(level)
            #no me regresa la cancion
        elif choice == "3":
            level = "Difficult Level"
            print(f"You selected {level}.")
            show_songs(level)
        elif choice == "4":
            print("Exiting the menu...")
            break
        else:
            print("Invalid option, please try again.")

        # Song selection
        song_choice = input("Select a song by number: ")
        if song_choice in ["1", "2", "3"]:
            print(f"You selected {song_choice}.")
            if song_choice == "1":
                for line in tab_star_easy:
                    print(line)
            elif song_choice == "2":
                for line in tab_star_intermediate:
                    print(line)
        elif song_choice == "4":
            continue
        else:
            print("Invalid song selection, returning to level menu.")
if __name__ == "__main__":
    main()
