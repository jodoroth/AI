import os
from Backend.Features import playAssistantSound
import eel # type: ignore
from Backend.Features import * # type: ignore
from Backend.command import *


eel.init('Frontend')

playAssistantSound()
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)




