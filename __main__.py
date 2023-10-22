import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

#Don't be a thief 
print("Successfully deployed!")
print("By 𝗕𝗔𝗧𝗠𝗔𝗡𝗛𝗖 • 𝗕𝗔𝗧𝗠𝗔𝗡𝗛𝗖𝗕𝗢𝗧")

if __name__ == "__main__":
    bot.run_until_disconnected()
