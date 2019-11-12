import serial
import spotipy
import webbrowser
import os


def do_authorization():
    print("Nothing")


def main():
    print("Spotifier Connected")
    command = ''
    browser_opened = False
    while not browser_opened:
        command = retrieve_command()
        print("Command found: " + command)
        if not browser_opened :
            open_browser()
            browser_opened = True


def open_browser():
    webbrowser.open('file://' + os.path.realpath("spotify.html"))


def get_spotify_credentials(command):
    if command == "Dragos":
        return ""


def do_request():
    sp = spotipy.Spotify()
    results = sp.search(q="weezer", limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])


def retrieve_command(serial_port="COM3"):
    connection = serial.Serial(serial_port, 9600)
    command = ''
    while not is_full_command(command):
        byte = connection.read()
        command += process_signal(byte)
    return command.strip()


def process_signal(info):
    return info.decode("utf-8")


def is_full_command(command):
    lastCaracter = command[-1:]
    if lastCaracter == '\n':
        return True
    return False


if __name__ == "__main__":
    main()
