import random
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
tab_star_difficult = [
    "e|---12-------------|",
    "B|---------10--9--8-|",
    "G|----9---9---------|",
    "D|--------10--------|",
    "A|---11-------------|",
    "E|------------------|",
    "",
    "e|----15------------|",
    "B|---------13--12---|",
    "G|----12---14-------|",
    "D|--------12--------|",
    "A|---13-------------|",
    "E|------------------|",
    "",
    "e|---19-------------|",
    "B|---------17--16---|",
    "G|----16---18-------|",
    "D|--------17--------|",
    "A|---18-------------|",
    "E|------------------|",
]
tab_let_her_go_easy = [
    "e|------------------|",
    "B|--------3--5--5--3|",
    "G|--2--2------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
    "",
    "e|------------------|",
    "B|--------3--5--3--3|",
    "G|--2--2------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
]
tab_let_her_go_intermediate = [
    "e|----5-------------|",
    "B|--------3--5--5--3|",
    "G|--2--2------------|",
    "D|--------4---------|",
    "A|------3-----------|",
    "E|------------------|",
    "",
    "e|------3-----------|",
    "B|--------3--5--3--3|",
    "G|--2--2------------|",
    "D|----------3-4-----|",
    "A|---2----4---------|",
    "E|------------------|",
]
tab_let_her_go_difficult = [
    "e|---10-------------|",
    "B|---------8--7--5--|",
    "G|----7---7---------|",
    "D|--------8---------|",
    "A|---9--------------|",
    "E|------------------|",
    "",
    "e|----12------------|",
    "B|---------10--8--7-|",
    "G|----9---9---------|",
    "D|--------10--------|",
    "A|---11-------------|",
    "E|------------------|",
]
tab_your_beautiful_easy = [
    "e|------------------|",
    "B|--------1--3--3--1|",
    "G|--0--0------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
    "",
    "e|------------------|",
    "B|--------1--3--1--1|",
    "G|--0--0------------|",
    "D|------------------|",
    "A|------------------|",
    "E|------------------|",
]
tab_your_beautiful_intermediate = [
    "e|----8-------------|",
    "B|--------1--3--3--1|",
    "G|--0--0------------|",
    "D|--------3---------|",
    "A|------2-----------|",
    "E|------------------|",
    "",
    "e|------3-----------|",
    "B|--------1--3--1--1|",
    "G|--0--0------------|",
    "D|----------3-5-----|",
    "A|---2----3---------|",
    "E|------------------|",
]
tab_your_beautiful_difficult = [
    "e|---12-------------|",
    "B|---------10--8--7-|",
    "G|----7---7---------|",
    "D|--------8---------|",
    "A|---9--------------|",
    "E|------------------|",
    "",
    "e|----15------------|",
    "B|---------13--12---|",
    "G|----12---14-------|",
    "D|--------12--------|",
    "A|---13-------------|",
    "E|------------------|",
]


songs_outside = {
        "Easy Level": ["star easy", "let her go easy", "your beautiful easy"],
        "Intermediate Level": ["star intermediate", "let her go intermediate", "your beautiful intermediate"],
        "Difficult Level": ["star hard ", "let her go hard", "your beautiful hard"]
    }

def main_menu():
    print("\n--- Main Menu ---")
    print("1. Random song and level select!")
    print("2. Choose level and song")
    choice = input("Select an option: ")
    return int(choice)

def menu_random_tabs():
    level = random.choice(list(songs_outside.keys()))
    song = random.choice(songs_outside[level])
    print(f"Level: {level}")
    print(f"Song Name: {song}")
    print_tab(song)


def dificulty_menu():
    print("\n--- Level Menu ---")
    print("1. Easy Level")
    print("2. Intermediate Level")
    print("3. Difficult Level")
    print("4. Exit")
    choice = input("Select an option: ")
    return int(choice)

def print_tab(name_song):
    if name_song == "star easy":
        for line in tab_star_easy:
            print(line)
    elif name_song == "star intermediate":
        for line in tab_star_intermediate:
            print(line)
    elif name_song == "star hard":
        for line in tab_star_difficult:
            print(line)
    elif name_song == "let her go easy":
        for line in tab_let_her_go_easy:
            print(line)
    elif name_song == "let her go intermediate":
        for line in tab_let_her_go_intermediate:
            print(line)
    elif name_song == "let her go hard":
        for line in tab_let_her_go_difficult:
            print(line)
    elif name_song == "your beautiful easy":
        for line in tab_your_beautiful_easy:
            print(line)
    elif name_song == "your beautiful intermediate":
        for line in tab_your_beautiful_intermediate:
            print(line)
    elif name_song == "your beautiful hard":
        for line in tab_your_beautiful_difficult:
            print(line)
    else:
        print("La canción o nivel no existe.")

def selected_song_one(songs):
    print(f"\n--- Choose from the available songs ---")
    for index, song in enumerate(songs):
            print(f"{index+1}. {song}")
    choice = int(input("Select an option: "))
    name_song = songs[choice-1]
    print_tab(name_song)
    return int(choice)

def song_menu(level):
    if level == 1:
        songs = songs_outside["Easy Level"]
    elif level == 2:
        songs = songs_outside["Intermediate Level"]
    elif level == 3:
        songs = songs_outside["Difficult Level"]
    else:
        return "Nivel no válido. Usa 1 para Easy, 2 para Intermediate o 3 para Difficult."
    
    return songs


def main():
    choice_main_menu = main_menu()
    print(choice_main_menu)
    if choice_main_menu == 1:
        menu_random_tabs()
    else:
        choice_level_dificulty = dificulty_menu()
        songs_menu_level = song_menu(choice_level_dificulty)
        cancion_tab = selected_song_one(songs_menu_level)
        print(cancion_tab)
if __name__ == "__main__":
    main()
