from dotenv import load_dotenv
from io import StringIO
import os
import base64
import requests
import ipywidgets as widgets
from ipywidgets import HBox, VBox
from IPython.display import display

def load_remote_env(*, env_url, file=None):
    def on_load(b):
        try:
            key = workshop_key.value
            if file is not None:
                resp = requests.get(f'{env_url}/api/workshop?key={key}&file={os.path.basename(file)}', timeout=5)
            else:
                resp = requests.get(f'{env_url}/api/workshop?key={key}', timeout=5)
            if resp.status_code == 200:
                env_encoded = resp.json()['env_encoded']
                load_dotenv(stream=StringIO(base64.b64decode(env_encoded).decode()), override=True)
                print(f"Successfully loaded environment variables for the {os.environ['WORKSHOP_NAME']} workshop from remote env file")
            elif resp.status_code == 403:
                print('workshop expired')
            elif resp.status_code == 404:
                print('unknown workshop')
        except Exception as e:
            print('Unknown error trying to load workshop environment variables', e)

    instructions = widgets.Label(value="Please enter the Workshop Key provided by the instructor:")
    workshop_key = widgets.Text(placeholder='Workshop Key', disabled=False)
    load_workshop = widgets.Button(description='Load')
    load_workshop.on_click(on_load)
    hbox = HBox([workshop_key, load_workshop])
    vbox = VBox([instructions, hbox])
    display(vbox)
    