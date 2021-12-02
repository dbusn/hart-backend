# https://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html

MappingCMUtoReed = {
    'IY': 'EE',
    'AA':'AH',
    'EY': 'AY',
    'AY': 'I',
    'AE': 'AE',
    'AO': 'AW',
    'EH': 'EH',
    'ER': 'ER',
    'IH': 'IH',
    'UH': 'UU',
    'AH': 'UH',
    'OW': 'OW', #changed
    'OY': 'OY',
    'D': 'D', 
    'M': 'M', 
    'S': 'S',
    'W': 'W',
    'DH': 'DH',
    'K': 'K', 
    'P': 'P',
    'T': 'T',
    'B': 'B',
    'G': 'G',
    'F': 'F',
    'SH': 'SH',
    'TH': 'TH',
    'V': 'V',
    'Z': 'Z',
    'ZH': 'ZH',
    'CH': 'CH',
    'JH': 'J',
    'HH': 'H', 
    'R': 'R',
    'L': 'L',
    'Y': 'Y',
    'N': 'N',
    'NG': 'NG',
    'AW': 'OE', #changed
    'UW': 'OO' #changed
}   

REEDPhonemes = set(MappingCMUtoReed.values())

CMUPhonemes = set(MappingCMUtoReed.keys())
