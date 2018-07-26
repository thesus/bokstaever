from bokstaever.models import Settings

def info(request):
    return { 'settings': Settings.load() }
