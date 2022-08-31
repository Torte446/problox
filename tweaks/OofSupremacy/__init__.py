import os, shutil
import pyglet
pyglet.options['search_local_libs'] = True

def play_audio(filename):
    sound = pyglet.media.load(filename)
    player = pyglet.media.Player()
    player.queue(sound)
    player.loop = False
    player.play()

if __name__ == "__main__":
    print("This is a Problox tweak! To run this, you will have to put it into the Problox tweaks folder and enabled it.")

def set_state(state: bool, problox, roblox, robloxstudio):
    if state == True:
        print("\nOofSupremacy v1")
        sounds = roblox + "\\content\\sounds"
        shutil.copy2(sounds + "\\ouch.ogg", "backup.ogg")
        os.remove(sounds + "\\ouch.ogg")
        shutil.copy2("oof.ogg", sounds+"\\ouch.ogg")
        print("Happy oofing!")
        play_audio("oof.ogg")
    else:
        print("\nOofSupremacy v1")
        sounds = roblox + "\\content\\sounds"
        os.remove(sounds + "\\ouch.ogg")
        shutil.copy2("backup.ogg", sounds+"\\ouch.ogg")
        print("Unhappy euhing!")
        play_audio("backup.ogg")
