ACHIEVEMENTS = {


    "first_launch": {
        "name": "Welcome to Arcade Universe",
        "description": "Started Arcade Universe for the first time"
    },


    "first_snake": {
        "name": "First Bite",
        "description": "Eat your first food in Snake"
    },


    "snake_master": {
        "name": "Snake Master",
        "description": "Get a score of 50 in Snake"
    },


    "snake_snack": {
        "name": "Snake? More Like Snack",
        "description": "Eat 100 food in Snake"
    },


    "first_guess": {
        "name": "Lucky Guess",
        "description": "Win your first Guess Game"
    },


    "super_lucky": {
        "name": "Super Lucky",
        "description": "Win Guess Game in 1 try"
    },


    "unlucky": {
        "name": "Unlucky",
        "description": "Win Guess Game after 15+ tries. Maybe it was a difficult number... or you spammed random guesses!"
    },


    "brainrotted": {
        "name": "You're So Brainrotted GNG",
        "description": "You typed only 67 in Guess Game. Bro... why does this achievement even exist?"
    },


    "easy_bot": {
        "name": "Bot Beginner",
        "description": "Defeat Easy Tic-Tac-Toe bot"
    },


    "medium_bot": {
        "name": "Bot Fighter",
        "description": "Defeat Medium Tic-Tac-Toe bot"
    },


    "hard_bot": {
        "name": "Bot Destroyer",
        "description": "Defeat Hard Tic-Tac-Toe bot"
    },


    "impossible": {
        "name": "Impossible?",
        "description": "Defeat the Impossible Tic-Tac-Toe bot"
    }

}



def unlock(save, achievement_id):

    if achievement_id not in ACHIEVEMENTS:

        return False


    if achievement_id in save["achievements"]:

        return False


    save["achievements"].append(
        achievement_id
    )

    return True



def get_name(achievement_id):

    return ACHIEVEMENTS[achievement_id]["name"]



def get_description(achievement_id):

    return ACHIEVEMENTS[achievement_id]["description"]