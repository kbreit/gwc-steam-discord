#!/usr/bin/env python3

import os
import httpx



def main():
    usersteamnumber = "ABC123"
    apikey = "ABC123"

    steam_user_url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apikey}&steamid={usersteamnumber}&format=json&include_appinfo=true"
    response = httpx.get(steam_user_url)
    user_game_data = response.json()
    #print(user_game_data["response"]["games"])
    #return(user_game_data)
    for game in user_game_data["response"]["games"]:
        steam_game_number = game["appid"]
        name = game["name"]
        print(name, "-", steam_game_number, "-", round((game["playtime_forever"])/60, 1), "hrs",)
        steam_achieve_url = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={steam_game_number}&key={apikey}&steamid={usersteamnumber}"
        achievement_response = httpx.get(steam_achieve_url)
        achievement_user_data = achievement_response.json()
        playerstats = achievement_user_data.get("playerstats")
        if "achievements" not in playerstats:
            #print("N/A")
            continue
        print(achievement_user_data["playerstats"]["achievements"])
        
        
    return user_game_data
if __name__ == "__main__":
    main()

