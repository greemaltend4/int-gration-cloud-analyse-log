from main import lambda_handler

# Cette ligne est nécessaire uniquement si vous déployez la fonction Lambda via la CLI AWS ou le gestionnaire de fonctions AWS

# Si vous avez besoin d'une fonction handler spécifique 
def handler(event, context):
    return lambda_handler(event, context)
