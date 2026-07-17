import json
import os

from core.achievements import unlock



SAVE_FILE = "save.json"



DEFAULT_SAVE = {

    "coins": 0,

    "snake_highscore": 0,

    "guess_best": 999,

    "achievements": [],

    "settings": {

        "fullscreen": False

    }

}





def load_save():


    if not os.path.exists(SAVE_FILE):

        data = DEFAULT_SAVE.copy()


    else:


        with open(SAVE_FILE, "r") as file:

            data = json.load(file)





    # make sure old saves get new stuff

    if "achievements" not in data:

        data["achievements"] = []



    if "coins" not in data:

        data["coins"] = 0





    # first launch achievement

    if "first_launch" not in data["achievements"]:


        unlock(
            data,
            "first_launch"
        )


        save_game(data)



    return data





def save_game(data):


    with open(SAVE_FILE, "w") as file:


        json.dump(

            data,

            file,

            indent=4

        )





def add_coins(data, amount):


    data["coins"] += amount


    save_game(data)