"""The Armenian alphabet. Sources:

- `<https://www.unicode.org/charts/PDF/U0530.pdf>`_

"""

__author__ = ["Caio Geraldes <caio.geraldes@usp.br>"]


UPPER = [
    "\u0531",  # Ա ARMENIAN CAPITAL LETTER AYB
    "\u0535",  # Ե ARMENIAN CAPITAL LETTER ECH
    "\u0537",  # Է ARMENIAN CAPITAL LETTER EH
    "\u0538",  # Ը ARMENIAN CAPITAL LETTER ET
    "\u053B",  # Ի ARMENIAN CAPITAL LETTER INI
    "\u0548",  # Ո ARMENIAN CAPITAL LETTER VO
    "\u0555",  # Օ ARMENIAN CAPITAL LETTER OH
]

LOWER = [
    "\u0561",  # ա ARMENIAN SMALL LETTER AYB
    "\u0565",  # ե ARMENIAN SMALL LETTER ECH
    "\u0567",  # է ARMENIAN SMALL LETTER EH
    "\u0568",  # ը ARMENIAN SMALL LETTER ET
    "\u056B",  # ի ARMENIAN SMALL LETTER INI
    "\u0578",  # ո ARMENIAN SMALL LETTER VO
    "\u0585",  # օ ARMENIAN SMALL LETTER OH
]

LOWER_LIGATURES = ["\u0587"]  # և ARMENIAN SMALL LIGATURE ECH YIWN

UPPER_SEMIVOWELS = [
    "\u0545",  # Յ ARMENIAN CAPITAL LETTER YI
    "\u0552",  # Ւ ARMENIAN CAPITAL LETTER YIWN
]

LOWER_SEMIVOWELS = [
    "\u0575",  # յ ARMENIAN SMALL LETTER YI
    "\u0582",  # ւ ARMENIAN SMALL LETTER YIWN
]

UPPER_CONSONANTS = [
    "\u0532",  # Բ ARMENIAN CAPITAL LETTER BEN
    "\u0533",  # Գ ARMENIAN CAPITAL LETTER GIM
    "\u0534",  # Դ ARMENIAN CAPITAL LETTER DA
    "\u0536",  # Զ ARMENIAN CAPITAL LETTER ZA
    "\u0539",  # Թ ARMENIAN CAPITAL LETTER TO
    "\u053A",  # Ժ ARMENIAN CAPITAL LETTER ZHE
    "\u053C",  # Լ ARMENIAN CAPITAL LETTER LIWN
    "\u053D",  # Խ ARMENIAN CAPITAL LETTER XEH
    "\u053E",  # Ծ ARMENIAN CAPITAL LETTER CA
    "\u053F",  # Կ ARMENIAN CAPITAL LETTER KEN
    "\u0540",  # Հ ARMENIAN CAPITAL LETTER HO
    "\u0541",  # Ձ ARMENIAN CAPITAL LETTER JA
    "\u0542",  # Ղ ARMENIAN CAPITAL LETTER GHAD
    "\u0543",  # Ճ ARMENIAN CAPITAL LETTER CHEH
    "\u0544",  # Մ ARMENIAN CAPITAL LETTER MEN
    "\u0546",  # Ն ARMENIAN CAPITAL LETTER NOW
    "\u0547",  # Շ ARMENIAN CAPITAL LETTER SHA
    "\u0549",  # Չ ARMENIAN CAPITAL LETTER CHA
    "\u054A",  # Պ ARMENIAN CAPITAL LETTER PEH
    "\u054B",  # Ջ ARMENIAN CAPITAL LETTER JHEH
    "\u054C",  # Ռ ARMENIAN CAPITAL LETTER RA
    "\u054D",  # Ս ARMENIAN CAPITAL LETTER SEH
    "\u054E",  # Վ ARMENIAN CAPITAL LETTER VEW
    "\u054F",  # Տ ARMENIAN CAPITAL LETTER TIWN
    "\u0550",  # Ր ARMENIAN CAPITAL LETTER REH
    "\u0551",  # Ց ARMENIAN CAPITAL LETTER CO
    "\u0553",  # Փ ARMENIAN CAPITAL LETTER PIWR
    "\u0554",  # Ք ARMENIAN CAPITAL LETTER KEH
    "\u0555",  # Օ ARMENIAN CAPITAL LETTER OH
    "\u0556",  # Ֆ ARMENIAN CAPITAL LETTER FEH
]


LOWER_CONSONANTS = [
    "\u0562",  # բ ARMENIAN SMALL LETTER BEN
    "\u0563",  # գ ARMENIAN SMALL LETTER GIM
    "\u0564",  # դ ARMENIAN SMALL LETTER DA
    "\u0566",  # զ ARMENIAN SMALL LETTER ZA
    "\u0569",  # թ ARMENIAN SMALL LETTER TO
    "\u056A",  # ժ ARMENIAN SMALL LETTER ZHE
    "\u056C",  # լ ARMENIAN SMALL LETTER LIWN
    "\u056D",  # խ ARMENIAN SMALL LETTER XEH
    "\u056E",  # ծ ARMENIAN SMALL LETTER CA
    "\u056F",  # կ ARMENIAN SMALL LETTER KEN
    "\u0570",  # հ ARMENIAN SMALL LETTER HO
    "\u0571",  # ձ ARMENIAN SMALL LETTER JA
    "\u0572",  # ղ ARMENIAN SMALL LETTER GHAD
    "\u0573",  # ճ ARMENIAN SMALL LETTER CHEH
    "\u0574",  # մ ARMENIAN SMALL LETTER MEN
    "\u0576",  # ն ARMENIAN SMALL LETTER NOW
    "\u0577",  # շ ARMENIAN SMALL LETTER SHA
    "\u0579",  # չ ARMENIAN SMALL LETTER CHA
    "\u057A",  # պ ARMENIAN SMALL LETTER PEH
    "\u057B",  # ջ ARMENIAN SMALL LETTER JHEH
    "\u057C",  # ռ ARMENIAN SMALL LETTER RA
    "\u057D",  # ս ARMENIAN SMALL LETTER SEH
    "\u057E",  # վ ARMENIAN SMALL LETTER VEW
    "\u057F",  # տ ARMENIAN SMALL LETTER TIWN
    "\u0580",  # ր ARMENIAN SMALL LETTER REH
    "\u0581",  # ց ARMENIAN SMALL LETTER CO
    "\u0583",  # փ ARMENIAN SMALL LETTER PIWR
    "\u0584",  # ք ARMENIAN SMALL LETTER KEH
    "\u0586",  # ֆ ARMENIAN SMALL LETTER FEH
]

PUNCTUATION = [
    "\u0589",  # ։ ARMENIAN FULL STOP
    "\u058A",  # ֊ ARMENIAN HYPHEN = yentamna
    "\u055B",  # ՛ ARMENIAN EMPHASIS MARK = shesht
    "\u055C",  # ՜ ARMENIAN EXCLAMATION MARK = batsaganchakan nshan
    "\u055D",  # ՝ ARMENIAN COMMA = bowt
    "\u055E",  # ՞ ARMENIAN QUESTION MARK = hartsakan nshan
    "\u055F",  # ՟ ARMENIAN ABBREVIATION MARK = patiw
]
