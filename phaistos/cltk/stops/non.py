"""
Old Norse: "Clément Besnier <clem@clementbesnier.fr>". Stopwords were defined by picking up in Altnordisches Elementarbuch by Ranke and Hofmann A new introduction to Old Norse by Barnes Viking Language 1 by Byock (this book provides a list of most frequent words in the sagas sorted by part of speech)
"""

STOPS: list[str] = [
    "í",  # prepositions and adverbs
    "gegnum",
    "svá",
    "eigi",
    "ekki",
    "vel",
    "upp",
    "síðan",
    "þó",
    "heim",
    "út",
    "hér",
    "mjök",
    "ór",
    "áðr",
    "saman",
    "inn",
    "undir",
    "heldr",
    "brott",
    "enn",
    "niðr",
    "ofan",
    "aptr",
    "illa",
    "lengi",
    "hversu",
    "aldri",
    "mikit",
    "um",
    "fram",
    "umhverfis",
    "innan",
    "meðal",
    "á",
    "milli",
    "til",
    "at",
    "frá",
    "gegn",
    "hjá",
    "mót",
    "nær",
    "undan",
    "eptir",
    "fyrir",
    "með",
    "við",
    "yfir",
    "útan",
    "án",
    "meðan",
    "þegar",  # adverbs
    "þangar",
    "hva",
    "hverr",
    "ok",  # conjuctions and relative pronouns
    "eða",
    "en",
    "sem",
    "er",
    "þá",
    "ef",
    "hvárt",
    "bæði",
    "þótt",
    "né",
    "enda",
    "hvági",
    "sá",  # demonstrative
    "þess",
    "þeim",
    "þann",
    "þeir",
    "þeira",
    "sú",
    "þeirar",
    "þeiri",
    "þær",
    "þat",
    "því",
    "þau",
    "því",
    "siá",
    "þessa",
    "þessum",
    "þenna",
    "þessír",
    "þessar",
    "þessi",
    "þetta",
    "þessu",
]
