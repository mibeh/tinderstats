#! /usr/bin/env python3

# Author: Michael Ibeh
# Title:  tinderstats.py
# Description: Get Statistics from downloaded Tinder data

import json
from datetime import date
from tabulate import tabulate

def main():

    # Get data from file
    f = open('data.json', 'r')   
    data = json.load(f)
    f.close()
    
    # Used to print values
    table = []

    # Get swiping statistics
    first_swipe_day = list(data["Usage"]["swipes_likes"].keys())[0]
    most_recent_swipe_day = list(data["Usage"]["swipes_likes"].keys())[-1]
    
    most_right_single_day = 0
    right_swipes = 0
    for key in data["Usage"]["swipes_likes"]:
        right_swipes += data["Usage"]["swipes_likes"][key]
        if int(data["Usage"]["swipes_likes"][key]) > most_right_single_day:
            most_right_single_day = int(data["Usage"]["swipes_likes"][key])
    
    most_left_single_day = 0
    left_swipes = 0
    for key in data["Usage"]["swipes_passes"]:
        left_swipes += data["Usage"]["swipes_passes"][key]
        if int(data["Usage"]["swipes_passes"][key]) > most_left_single_day:
            most_left_single_day = int(data["Usage"]["swipes_passes"][key])

    most_matches_single_day = 0
    matches = 0
    for key in data["Usage"]["matches"]:
        matches += data["Usage"]["matches"][key]
        if int(data["Usage"]["matches"][key]) > most_matches_single_day:
            most_matches_single_day = int(data["Usage"]["matches"][key])

    total_swipes = right_swipes + left_swipes

    right_swipe_percentage = round(((right_swipes / total_swipes) * 100) , 2)

    match_percentage = round(((matches / right_swipes) * 100), 2)

    # Messaging Statistics
    most_messages_single_day = 0
    messages_sent = 0
    for key in data["Usage"]["messages_sent"]:
        messages_sent += data["Usage"]["messages_sent"][key]
        if int(data["Usage"]["messages_sent"][key]) > most_messages_single_day:
            most_messages_single_day = int(data["Usage"]["messages_sent"][key])

    most_recieved_single_day = 0
    messages_received = 0
    for key in data["Usage"]["messages_received"]:
        messages_received += data["Usage"]["messages_received"][key]
        if int(data["Usage"]["messages_received"][key]) > most_recieved_single_day:
            most_recieved_single_day = int(
                data["Usage"]["messages_received"][key])

    # App Usage Statistics
    most_app_open_single_day = 0
    app_opens = 0
    for key in data["Usage"]["app_opens"]:
        app_opens += data["Usage"]["app_opens"][key]
        if int(data["Usage"]["app_opens"][key]) > most_app_open_single_day:
            most_app_open_single_day = int(data["Usage"]["app_opens"][key])

    active_days = 0
    for key in data["Usage"]["advertising_id"]:
        active_days += 1

    start_date = first_swipe_day.split('-')
    end_date = most_recent_swipe_day.split('-')

    delta = date(int(start_date[0]), int(start_date[1]), int(start_date[2])) - date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
    total_days = int(str(delta.days)[1:])
    deactivated_days = total_days - active_days

    # Purchases
    num_boosts = int(data["Purchases"]["boost_usage"]["purchased"])

    months_tinder_gold = 0
    for purchase in data["Purchases"]["subscription"]:
        months_tinder_gold += int(purchase["terms"])

    average_swipes_per_day = round((total_swipes / active_days), 2)

    average_app_opens_day = round((app_opens / active_days), 2)
        
    table.append(["Total swipes", total_swipes])
    table.append(["Total right swipes", right_swipes])
    table.append(["Total left swipes", left_swipes])
    table.append(["Most right swipes in a day", most_right_single_day])
    table.append(["Most left swipes in a day", most_left_single_day])
    table.append(["Right swipe percentage            (%)", right_swipe_percentage])
    table.append(["Average Swipes per day", average_swipes_per_day])
    
    table.append(["Total matches", matches])
    table.append(["Most matches in a day", most_matches_single_day])
    table.append(["Matches to right swipe percentage (%)", match_percentage])
    
    table.append(["Messages sent", messages_sent])
    table.append(["Messages recieved", messages_received])
    table.append(["Most messages sent in a day", most_messages_single_day])
    table.append(["Most messages recieved in a day", most_recieved_single_day])

    table.append(["First day of swiping", first_swipe_day])
    table.append(["Most recent day of swiping", most_recent_swipe_day])
    table.append(["Number of times app opened", app_opens])
    table.append(["Average app opens per day", average_app_opens_day])
    table.append(["Most app opens in a day", most_app_open_single_day])

    table.append(["Total days on Tinder", total_days])
    table.append(["Days profile active", active_days])
    table.append(["Days profile deactivated", deactivated_days])
    table.append(["Boosts purchased", num_boosts])
    table.append(["Months of Tinder Gold purchased", months_tinder_gold])

    print(tabulate(table))

if __name__ == "__main__":
    main()
