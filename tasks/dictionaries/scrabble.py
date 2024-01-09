letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key: value for key,value in zip(letters, points)}
letters_to_points.update({" ": 0})

player_to_points = {}

player_to_words = {
    "player1":      ["BLUE", "TENNIS", "EXIT"],
    "wordNerd":     ["EARTH", "EYES", "MACHINE"],
    "Lexi Con":     ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader":  ["ZAP", "COMA", "PERIOD"]
}

new_players_new_words = {
    "player2":      ["RED", "FOOTBALL", "enter"],
    "player3":      ["GREEN", "BASKETBALL", "escape"],
}


def score_word(word):
    point_total = 0
    for w in word.upper():
        if w in letters_to_points:
            point_total += letters_to_points[w]
        else:
            point_total += 0

    return point_total


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0

        for word in words:
            player_points += score_word(word)

        player_to_points.update({player: player_points})

    return player_to_points


def play_word(player, word):
    if player not in player_to_words:
        player_to_words.update({player: [word]})
    else:
        player_to_words[player].append(word)


def main():
    for player, words in new_players_new_words.items():
        [play_word(player, word) for word in words]

    print(update_point_totals())


if __name__ == "__main__":
    main()
