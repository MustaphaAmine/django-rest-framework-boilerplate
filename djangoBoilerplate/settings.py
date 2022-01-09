import os

# You will need different configurations for the settings.py file for development and production  
if 'DJANGO_SETTINGS' in os.environ:
    if os.environ['DJANGO_SETTINGS'] == "dev":
        print ("DEV SERVER")
        from .settings_dev import *
else:
    print ("PROD SERVER")
    from .settings_prod import *