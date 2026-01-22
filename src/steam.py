#!/usr/bin/env python3

import os
import httpx



def main():
    usersteamnumber = "ABC123"
    apikey = "ABC123"

    steamgameurl = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={usersteamnumber}&format=json&include_appinfo=true"
    response = httpx.get(steamgameurl)
    user_game_data = response.json()
    #print(user_game_data["response"]["games"])
    #return(user_game_data)
    for game in user_game_data["response"]["games"]:
        steamgamenumber = game["appid"]
        name = game["name"]
        print(game["name"], "-", game["appid"], "-", round((game["playtime_forever"])/60, 1), "hrs",)
        steamachieveurl = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={steamgamenumber}&key={apikey}&steamid={usersteamnumber}"
        achieve_response = httpx.get(steamachieveurl)
        achieve_user_data = achieve_response.json()
        playerstats = achieve_user_data.get("playerstats")
        if "achievements" not in playerstats:
            print("N/A")
            continue
        print(achieve_user_data["playerstats"]["achievements"])
        
        
    return user_game_data
if __name__ == "__main__":
    main()

