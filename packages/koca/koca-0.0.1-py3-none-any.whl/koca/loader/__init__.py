from .bex_loader import *

bex = BexLoader()

def initialize_bex(app, config):
    with app.app_context():
        app.koca.bex = bex