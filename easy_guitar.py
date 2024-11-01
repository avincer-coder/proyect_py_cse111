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

songs_outside = {
        "Easy Level": ["star easy", "let her go easy", "your beautiful easy"],
        "Intermediate Level": ["star intermediate", "let her go intermediate", "your beautiful intermediate"],
        "Difficult Level": ["star hard ", "let her go hard", "your beautiful hard"]
    }

#Primer main_menu opciones para random o escojer cancion
#La parte donde seleccionamos la cancion debe ir en una funcion 
# necesitramos una funcion para escojer una cancion random
# 4 tests para las funciones respectivamente

def main_menu():
    print("\n--- Main Menu ---")
    print("1. Random song and level select!")
    print("2. Choose level and song")
    choice = input("Select an option: ")
    return int(choice)

def random():
    print("TEXTO RANDOM")



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
    
    # print(f"\n--- Songs for {level} ---")
    easy_songs = songs[level]
    print(f"\n--- Songs for {level} ---")
    for index, song in enumerate(easy_songs):
        print(f"{index+1}. {song}")
    return easy_songs

    
        
    

def main():
    choice_main_menu = main_menu()
    print(choice_main_menu)
    if choice_main_menu == 1:
        random()
    else:
        print("Logica escojer")


    # while True:
    #     show_menu()
    #     choice = input("Select an option: ")
    #     selected_lvl_song = ""
    #     if choice == "1":
    #         level = "Easy Level"
    #         print(f"You selected {level}.")
    #         selected_lvl_song = show_songs(level)
            
            
    #     elif choice == "2":
    #         level = "Intermediate Level"
    #         print(f"You selected {level}.")
    #         selected_lvl_song = show_songs(level)
    #         #no me regresa la cancion
    #     elif choice == "3":
    #         level = "Difficult Level"
    #         print(f"You selected {level}.")
    #         selected_lvl_song = show_songs(level)
    #     elif choice == "4":
    #         print("Exiting the menu...")
    #         break
    #     else:
    #         print("Invalid option, please try again.")

    #     # Song selection
        
    #     song_choice = int(input("Select a song by number: "))
    #     one_selected_song = selected_lvl_song[song_choice-1]
    #     print(one_selected_song)
    #     if one_selected_song == "star easy":
    #         for line in tab_star_easy:
    #             print(line)
    #     if one_selected_song == "star intermediate":
    #         for line in tab_star_intermediate:
    #             print(line)
    print("esto een main")
if __name__ == "__main__":
    main()
