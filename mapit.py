import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    sys.argv = sys.argv[1:]
    address = ' '.join(sys.argv)
else:
    address = pyperclip.paste()

print (address)
webbrowser.open('https://www.google.com/maps/place/' + address)