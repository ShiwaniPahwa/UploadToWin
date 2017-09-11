from clarifai import rest
from clarifai.rest import ClarifaiApp

def upload_win(post):
    app = ClarifaiApp(api_key='a5f07c4b20b84ff8a66790faedaf9314')
    model = app.models.get

