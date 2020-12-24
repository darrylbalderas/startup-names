from googletrans.constants import LANGCODES
from collections import namedtuple

LANGUAGE = namedtuple('Language', 'name, code')

SUPPORTED_LANGUAGES = [
    LANGUAGE(t.lower(), LANGCODES[t.lower()]) for t in [
        "chinese (traditional)", "chinese (simplified)", "hindi", "Spanish", "Arabic",
        "Malay", "Russian", "Bengali", "Portuguese", "French", "Hausa", "Punjabi",
        "Telugu", "Javanese"
    ]
]
