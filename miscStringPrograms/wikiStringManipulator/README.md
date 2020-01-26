Takes a string and adds a character to the string when the string is copied
. The intent is to copy a list of strings on several lines, then add an
 asterik to the beginning of each line to autoformat the string into markdown
 . Then allow the user to paste the string with the newly formatted text. 
 
 After the user copies a text, the user will run the program. The program will:
 1. copy the text from the clipboard
 2. format the text copied from the clipboard
    - determine how the string will be stored for manipulation within the
     program. 
    - determine an appropriate place to break the string
 3. copy the formatted text back to the clipboard. 