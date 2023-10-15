SearchBot
================

This python script uses pyautogui python library to search out things one after another in a web browser.
The script automatically creates a new tab with keyboard shortcut and searches from the "Messages.txt" file with 3 cases to avoid bot detection and possible blocks. The script also uses different sleep times to avoid the same in each case.
At the end the tab is automatically closed.

How to use
=================
install pyautogui using the command 'pip install pyautogui' without single quotes.
Then put the desired text into Messages.txt file with new line for every search.
Ex :
Hello
I am
Ayush

Here "Hello", "I am" and "Ayush" will be separate searches.

Then run the script "Spam Text.py"
Within 5 seconds of running open the desired web browser (open the web browser before running the script if it takes time to load)
The 5 second window can be changed in the first sleep(5) call
Now wait for the searches to complete automatically
