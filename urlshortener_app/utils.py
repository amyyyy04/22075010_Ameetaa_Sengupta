import shortuuid
from .models import URL

def generate_unique_short_code():
    while True:
        short_code = shortuuid.uuid()[:8]  # Adjust the length as needed
        if not URL.objects.filter(short_code=short_code).exists():
            return short_code
