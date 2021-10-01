# 30daysleaderboard

Update - Now if you run this script it will tell you how many students got atleast 1 skill badge, how many completed atleast 1 track etc


I made this for the program #30DaysofGoogleCloud

For this you need to edit all the Qwiklabs Public URL  in the userurl.txt and run publiclistmaker.py to generate all the links in list and update the list in main.py

then after pushing it back to github you need to enable Github Actions from the action tab and then make a commit to start the Github Actions.
It has multi threading support and it scrapes the data in 6 seconds and it will automatically run on github action every 2 hours to scrap the data and generate JSON file.
For hosting use netlify as its free.

Note - Make sure all the Qwiklabs public URL are correct otherwise it will crash.

That's all, it will then automatically scrap the data and update the json file easily every hour.


Thank You
