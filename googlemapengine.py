#Firewalls should not block this program
import webbrowser, sys, pyperclip
print("Please give the adddress: ")
address=input()
#Extracting data from clipboard
if len(address)<1:
    address=pyperclip.paste()
print("Opening the Google Map.....")
webbrowser.open('https://www.google.co.in/maps/place/'+address)
