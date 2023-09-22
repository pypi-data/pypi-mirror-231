#!/usr/bin/env python3

import sys
import os
import logging as l


# PGP word list from https://en.wikipedia.org/wiki/PGP_word_list
# Hex: [Even Word, Odd Word]
PGP_WORD_LIST = [
    ['aardvark', 'adroitness'],
    ['absurd', 'adviser'],
    ['accrue', 'aftermath'],
    ['acme', 'aggregate'],
    ['adrift', 'alkali'],
    ['adult',  'almighty'],
    ['afflict',  'amulet'],
    ['ahead',  'amusement'],
    ['aimless',  'antenna'],
    ['Algol',  'applicant'],
    ['allow',  'Apollo'],
    ['alone',  'armistice'],
    ['ammo', 'article'],
    ['ancient',  'asteroid'],
    ['apple',  'Atlantic'],
    ['artist', 'atmosphere'],
    ['assume', 'autopsy'],
    ['Athens', 'Babylon'],
    ['atlas',  'backwater'],
    ['Aztec',  'barbecue'],
    ['baboon', 'belowground'],
    ['backfield',  'bifocals'],
    ['backward', 'bodyguard'],
    ['banjo',  'bookseller'],
    ['beaming',  'borderline'],
    ['bedlamp',  'bottomless'],
    ['beehive',  'Bradbury'],
    ['beeswax',  'bravado'],
    ['befriend', 'Brazilian'],
    ['Belfast',  'breakaway'],
    ['berserk',  'Burlington'],
    ['billiard', 'businessman'],
    ['bison',  'butterfat'],
    ['blackjack',  'Camelot'],
    ['blockade', 'candidate'],
    ['blowtorch',  'cannonball'],
    ['bluebird', 'Capricorn'],
    ['bombast',  'caravan'],
    ['bookshelf',  'caretaker'],
    ['brackish', 'celebrate'],
    ['breadline',  'cellulose'],
    ['breakup',  'certify'],
    ['brickyard',  'chambermaid'],
    ['briefcase',  'Cherokee'],
    ['Burbank',  'Chicago'],
    ['button', 'clergyman'],
    ['buzzard',  'coherence'],
    ['cement', 'combustion'],
    ['chairlift',  'commando'],
    ['chatter',  'company'],
    ['checkup',  'component'],
    ['chisel', 'concurrent'],
    ['choking',  'confidence'],
    ['chopper',  'conformist'],
    ['Christmas',  'congregate'],
    ['clamshell',  'consensus'],
    ['classic',  'consulting'],
    ['classroom',  'corporate'],
    ['cleanup',  'corrosion'],
    ['clockwork',  'councilman'],
    ['cobra',  'crossover'],
    ['commence', 'crucifix'],
    ['concert',  'cumbersome'],
    ['cowbell',  'customer'],
    ['crackdown',  'Dakota'],
    ['cranky', 'decadence'],
    ['crowfoot', 'December'],
    ['crucial',  'decimal'],
    ['crumpled', 'designing'],
    ['crusade',  'detector'],
    ['cubic',  'detergent'],
    ['dashboard',  'determine'],
    ['deadbolt', 'dictator'],
    ['deckhand', 'dinosaur'],
    ['dogsled',  'direction'],
    ['dragnet',  'disable'],
    ['drainage', 'disbelief'],
    ['dreadful', 'disruptive'],
    ['drifter',  'distortion'],
    ['dropper',  'document'],
    ['drumbeat', 'embezzle'],
    ['drunken',  'enchanting'],
    ['Dupont', 'enrollment'],
    ['dwelling', 'enterprise'],
    ['eating', 'equation'],
    ['edict',  'equipment'],
    ['egghead',  'escapade'],
    ['eightball',  'Eskimo'],
    ['endorse',  'everyday'],
    ['endow',  'examine'],
    ['enlist', 'existence'],
    ['erase',  'exodus'],
    ['escape', 'fascinate'],
    ['exceed', 'filament'],
    ['eyeglass', 'finicky'],
    ['eyetooth', 'forever'],
    ['facial', 'fortitude'],
    ['fallout',  'frequency'],
    ['flagpole', 'gadgetry'],
    ['flatfoot', 'Galveston'],
    ['flytrap',  'getaway'],
    ['fracture', 'glossary'],
    ['framework',  'gossamer'],
    ['freedom',  'graduate'],
    ['frighten', 'gravity'],
    ['gazelle',  'guitarist'],
    ['Geiger', 'hamburger'],
    ['glitter',  'Hamilton'],
    ['glucose',  'handiwork'],
    ['goggles',  'hazardous'],
    ['goldfish', 'headwaters'],
    ['gremlin',  'hemisphere'],
    ['guidance', 'hesitate'],
    ['hamlet', 'hideaway'],
    ['highchair',  'holiness'],
    ['hockey', 'hurricane'],
    ['indoors',  'hydraulic'],
    ['indulge',  'impartial'],
    ['inverse',  'impetus'],
    ['involve',  'inception'],
    ['island', 'indigo'],
    ['jawbone',  'inertia'],
    ['keyboard', 'infancy'],
    ['kickoff',  'inferno'],
    ['kiwi', 'informant'],
    ['klaxon', 'insincere'],
    ['locale', 'insurgent'],
    ['lockup', 'integrate'],
    ['merit',  'intention'],
    ['minnow', 'inventive'],
    ['miser',  'Istanbul'],
    ['Mohawk', 'Jamaica'],
    ['mural',  'Jupiter'],
    ['music',  'leprosy'],
    ['necklace', 'letterhead'],
    ['Neptune',  'liberty'],
    ['newborn',  'maritime'],
    ['nightbird',  'matchmaker'],
    ['Oakland',  'maverick'],
    ['obtuse', 'Medusa'],
    ['offload',  'megaton'],
    ['optic',  'microscope'],
    ['orca', 'microwave'],
    ['payday', 'midsummer'],
    ['peachy', 'millionaire'],
    ['pheasant', 'miracle'],
    ['physique', 'misnomer'],
    ['playhouse',  'molasses'],
    ['Pluto',  'molecule'],
    ['preclude', 'Montana'],
    ['prefer', 'monument'],
    ['preshrunk',  'mosquito'],
    ['printer',  'narrative'],
    ['prowler',  'nebula'],
    ['pupil',  'newsletter'],
    ['puppy',  'Norwegian'],
    ['python', 'October'],
    ['quadrant', 'Ohio'],
    ['quiver', 'onlooker'],
    ['quota',  'opulent'],
    ['ragtime',  'Orlando'],
    ['ratchet',  'outfielder'],
    ['rebirth',  'Pacific'],
    ['reform', 'pandemic'],
    ['regain', 'Pandora'],
    ['reindeer', 'paperweight'],
    ['rematch',  'paragon'],
    ['repay',  'paragraph'],
    ['retouch',  'paramount'],
    ['revenge',  'passenger'],
    ['reward', 'pedigree'],
    ['rhythm', 'Pegasus'],
    ['ribcage',  'penetrate'],
    ['ringbolt', 'perceptive'],
    ['robust', 'performance'],
    ['rocker', 'pharmacy'],
    ['ruffled',  'phonetic'],
    ['sailboat', 'photograph'],
    ['sawdust',  'pioneer'],
    ['scallion', 'pocketful'],
    ['scenic', 'politeness'],
    ['scorecard',  'positive'],
    ['Scotland', 'potato'],
    ['seabird',  'processor'],
    ['select', 'provincial'],
    ['sentence', 'proximate'],
    ['shadow', 'puberty'],
    ['shamrock', 'publisher'],
    ['showgirl', 'pyramid'],
    ['skullcap', 'quantity'],
    ['skydive',  'racketeer'],
    ['slingshot',  'rebellion'],
    ['slowdown', 'recipe'],
    ['snapline', 'recover'],
    ['snapshot', 'repellent'],
    ['snowcap',  'replica'],
    ['snowslide',  'reproduce'],
    ['solo', 'resistor'],
    ['southward',  'responsive'],
    ['soybean',  'retraction'],
    ['spaniel',  'retrieval'],
    ['spearhead',  'retrospect'],
    ['spellbind',  'revenue'],
    ['spheroid', 'revival'],
    ['spigot', 'revolver'],
    ['spindle',  'sandalwood'],
    ['spyglass', 'sardonic'],
    ['stagehand',  'Saturday'],
    ['stagnate', 'savagery'],
    ['stairway', 'scavenger'],
    ['standard', 'sensation'],
    ['stapler',  'sociable'],
    ['steamship',  'souvenir'],
    ['sterling', 'specialist'],
    ['stockman', 'speculate'],
    ['stopwatch',  'stethoscope'],
    ['stormy', 'stupendous'],
    ['sugar',  'supportive'],
    ['surmount', 'surrender'],
    ['suspense', 'suspicious'],
    ['sweatband',  'sympathy'],
    ['swelter',  'tambourine'],
    ['tactics',  'telephone'],
    ['talon',  'therapist'],
    ['tapeworm', 'tobacco'],
    ['tempest',  'tolerance'],
    ['tiger',  'tomorrow'],
    ['tissue', 'torpedo'],
    ['tonic',  'tradition'],
    ['topmost',  'travesty'],
    ['tracker',  'trombonist'],
    ['transit',  'truncated'],
    ['trauma', 'typewriter'],
    ['treadmill',  'ultimate'],
    ['Trojan', 'undaunted'],
    ['trouble',  'underfoot'],
    ['tumor',  'unicorn'],
    ['tunnel', 'unify'],
    ['tycoon', 'universe'],
    ['uncut',  'unravel'],
    ['unearth',  'upcoming'],
    ['unwind', 'vacancy'],
    ['uproot', 'vagabond'],
    ['upset',  'vertigo'],
    ['upshot', 'Virginia'],
    ['vapor',  'visitor'],
    ['village',  'vocalist'],
    ['virus',  'voyager'],
    ['Vulcan', 'warranty'],
    ['waffle', 'Waterloo'],
    ['wallet', 'whimsical'],
    ['watchword',  'Wichita'],
    ['wayside',  'Wilmington'],
    ['willow', 'Wyoming'],
    ['woodlark', 'yesteryear'],
    ['Zulu', 'Yucatan'],
  ]

PGP_REVERSE_WORD_LIST = {
    'AARDVARK': 0, 'ADROITNESS': 0,
    'ABSURD': 1, 'ADVISER': 1,
    'ACCRUE': 2, 'AFTERMATH': 2,
    'ACME': 3, 'AGGREGATE': 3,
    'ADRIFT': 4, 'ALKALI': 4,
    'ADULT': 5,  'ALMIGHTY': 5,
    'AFFLICT': 6,  'AMULET': 6,
    'AHEAD': 7,  'AMUSEMENT': 7,
    'AIMLESS': 8,  'ANTENNA': 8,
    'ALGOL': 9,  'APPLICANT': 9,
    'ALLOW': 10,  'APOLLO': 10,
    'ALONE': 11,  'ARMISTICE': 11,
    'AMMO': 12, 'ARTICLE': 12,
    'ANCIENT': 13,  'ASTEROID': 13,
    'APPLE': 14,  'ATLANTIC': 14,
    'ARTIST': 15, 'ATMOSPHERE': 15,
    'ASSUME': 16, 'AUTOPSY': 16,
    'ATHENS': 17, 'BABYLON': 17,
    'ATLAS': 18,  'BACKWATER': 18,
    'AZTEC': 19,  'BARBECUE': 19,
    'BABOON': 20, 'BELOWGROUND': 20,
    'BACKFIELD': 21,  'BIFOCALS': 21,
    'BACKWARD': 22, 'BODYGUARD': 22,
    'BANJO': 23,  'BOOKSELLER': 23,
    'BEAMING': 24,  'BORDERLINE': 24,
    'BEDLAMP': 25,  'BOTTOMLESS': 25,
    'BEEHIVE': 26,  'BRADBURY': 26,
    'BEESWAX': 27,  'BRAVADO': 27,
    'BEFRIEND': 28, 'BRAZILIAN': 28,
    'BELFAST': 29,  'BREAKAWAY': 29,
    'BERSERK': 30,  'BURLINGTON': 30,
    'BILLIARD': 31, 'BUSINESSMAN': 31,
    'BISON': 32,  'BUTTERFAT': 32,
    'BLACKJACK': 33,  'CAMELOT': 33,
    'BLOCKADE': 34, 'CANDIDATE': 34,
    'BLOWTORCH': 35,  'CANNONBALL': 35,
    'BLUEBIRD': 36, 'CAPRICORN': 36,
    'BOMBAST': 37,  'CARAVAN': 37,
    'BOOKSHELF': 38,  'CARETAKER': 38,
    'BRACKISH': 39, 'CELEBRATE': 39,
    'BREADLINE': 40,  'CELLULOSE': 40,
    'BREAKUP': 41,  'CERTIFY': 41,
    'BRICKYARD': 42,  'CHAMBERMAID': 42,
    'BRIEFCASE': 43,  'CHEROKEE': 43,
    'BURBANK': 44,  'CHICAGO': 44,
    'BUTTON': 45, 'CLERGYMAN': 45,
    'BUZZARD': 46,  'COHERENCE': 46,
    'CEMENT': 47, 'COMBUSTION': 47,
    'CHAIRLIFT': 48,  'COMMANDO': 48,
    'CHATTER': 49,  'COMPANY': 49,
    'CHECKUP': 50,  'COMPONENT': 50,
    'CHISEL': 51, 'CONCURRENT': 51,
    'CHOKING': 52,  'CONFIDENCE': 52,
    'CHOPPER': 53,  'CONFORMIST': 53,
    'CHRISTMAS': 54,  'CONGREGATE': 54,
    'CLAMSHELL': 55,  'CONSENSUS': 55,
    'CLASSIC': 56,  'CONSULTING': 56,
    'CLASSROOM': 57,  'CORPORATE': 57,
    'CLEANUP': 58,  'CORROSION': 58,
    'CLOCKWORK': 59,  'COUNCILMAN': 59,
    'COBRA': 60,  'CROSSOVER': 60,
    'COMMENCE': 61, 'CRUCIFIX': 61,
    'CONCERT': 62,  'CUMBERSOME': 62,
    'COWBELL': 63,  'CUSTOMER': 63,
    'CRACKDOWN': 64,  'DAKOTA': 64,
    'CRANKY': 65, 'DECADENCE': 65,
    'CROWFOOT': 66, 'DECEMBER': 66,
    'CRUCIAL': 67,  'DECIMAL': 67,
    'CRUMPLED': 68, 'DESIGNING': 68,
    'CRUSADE': 69,  'DETECTOR': 69,
    'CUBIC': 70,  'DETERGENT': 70,
    'DASHBOARD': 71,  'DETERMINE': 71,
    'DEADBOLT': 72, 'DICTATOR': 72,
    'DECKHAND': 73, 'DINOSAUR': 73,
    'DOGSLED': 74,  'DIRECTION': 74,
    'DRAGNET': 75,  'DISABLE': 75,
    'DRAINAGE': 76, 'DISBELIEF': 76,
    'DREADFUL': 77, 'DISRUPTIVE': 77,
    'DRIFTER': 78,  'DISTORTION': 78,
    'DROPPER': 79,  'DOCUMENT': 79,
    'DRUMBEAT': 80, 'EMBEZZLE': 80,
    'DRUNKEN': 81,  'ENCHANTING': 81,
    'DUPONT': 82, 'ENROLLMENT': 82,
    'DWELLING': 83, 'ENTERPRISE': 83,
    'EATING': 84, 'EQUATION': 84,
    'EDICT': 85,  'EQUIPMENT': 85,
    'EGGHEAD': 86,  'ESCAPADE': 86,
    'EIGHTBALL': 87,  'ESKIMO': 87,
    'ENDORSE': 88,  'EVERYDAY': 88,
    'ENDOW': 89,  'EXAMINE': 89,
    'ENLIST': 90, 'EXISTENCE': 90,
    'ERASE': 91,  'EXODUS': 91,
    'ESCAPE': 92, 'FASCINATE': 92,
    'EXCEED': 93, 'FILAMENT': 93,
    'EYEGLASS': 94, 'FINICKY': 94,
    'EYETOOTH': 95, 'FOREVER': 95,
    'FACIAL': 96, 'FORTITUDE': 96,
    'FALLOUT': 97,  'FREQUENCY': 97,
    'FLAGPOLE': 98, 'GADGETRY': 98,
    'FLATFOOT': 99, 'GALVESTON': 99,
    'FLYTRAP': 100,  'GETAWAY': 100,
    'FRACTURE': 101, 'GLOSSARY': 101,
    'FRAMEWORK': 102,  'GOSSAMER': 102,
    'FREEDOM': 103,  'GRADUATE': 103,
    'FRIGHTEN': 104, 'GRAVITY': 104,
    'GAZELLE': 105,  'GUITARIST': 105,
    'GEIGER': 106, 'HAMBURGER': 106,
    'GLITTER': 107,  'HAMILTON': 107,
    'GLUCOSE': 108,  'HANDIWORK': 108,
    'GOGGLES': 109,  'HAZARDOUS': 109,
    'GOLDFISH': 110, 'HEADWATERS': 110,
    'GREMLIN': 111,  'HEMISPHERE': 111,
    'GUIDANCE': 112, 'HESITATE': 112,
    'HAMLET': 113, 'HIDEAWAY': 113,
    'HIGHCHAIR': 114,  'HOLINESS': 114,
    'HOCKEY': 115, 'HURRICANE': 115,
    'INDOORS': 116,  'HYDRAULIC': 116,
    'INDULGE': 117,  'IMPARTIAL': 117,
    'INVERSE': 118,  'IMPETUS': 118,
    'INVOLVE': 119,  'INCEPTION': 119,
    'ISLAND': 120, 'INDIGO': 120,
    'JAWBONE': 121,  'INERTIA': 121,
    'KEYBOARD': 122, 'INFANCY': 122,
    'KICKOFF': 123,  'INFERNO': 123,
    'KIWI': 124, 'INFORMANT': 124,
    'KLAXON': 125, 'INSINCERE': 125,
    'LOCALE': 126, 'INSURGENT': 126,
    'LOCKUP': 127, 'INTEGRATE': 127,
    'MERIT': 128,  'INTENTION': 128,
    'MINNOW': 129, 'INVENTIVE': 129,
    'MISER': 130,  'ISTANBUL': 130,
    'MOHAWK': 131, 'JAMAICA': 131,
    'MURAL': 132,  'JUPITER': 132,
    'MUSIC': 133,  'LEPROSY': 133,
    'NECKLACE': 134, 'LETTERHEAD': 134,
    'NEPTUNE': 135,  'LIBERTY': 135,
    'NEWBORN': 136,  'MARITIME': 136,
    'NIGHTBIRD': 137,  'MATCHMAKER': 137,
    'OAKLAND': 138,  'MAVERICK': 138,
    'OBTUSE': 139, 'MEDUSA': 139,
    'OFFLOAD': 140,  'MEGATON': 140,
    'OPTIC': 141,  'MICROSCOPE': 141,
    'ORCA': 142, 'MICROWAVE': 142,
    'PAYDAY': 143, 'MIDSUMMER': 143,
    'PEACHY': 144, 'MILLIONAIRE': 144,
    'PHEASANT': 145, 'MIRACLE': 145,
    'PHYSIQUE': 146, 'MISNOMER': 146,
    'PLAYHOUSE': 147,  'MOLASSES': 147,
    'PLUTO': 148,  'MOLECULE': 148,
    'PRECLUDE': 149, 'MONTANA': 149,
    'PREFER': 150, 'MONUMENT': 150,
    'PRESHRUNK': 151,  'MOSQUITO': 151,
    'PRINTER': 152,  'NARRATIVE': 152,
    'PROWLER': 153,  'NEBULA': 153,
    'PUPIL': 154,  'NEWSLETTER': 154,
    'PUPPY': 155,  'NORWEGIAN': 155,
    'PYTHON': 156, 'OCTOBER': 156,
    'QUADRANT': 157, 'OHIO': 157,
    'QUIVER': 158, 'ONLOOKER': 158,
    'QUOTA': 159,  'OPULENT': 159,
    'RAGTIME': 160,  'ORLANDO': 160,
    'RATCHET': 161,  'OUTFIELDER': 161,
    'REBIRTH': 162,  'PACIFIC': 162,
    'REFORM': 163, 'PANDEMIC': 163,
    'REGAIN': 164, 'PANDORA': 164,
    'REINDEER': 165, 'PAPERWEIGHT': 165,
    'REMATCH': 166,  'PARAGON': 166,
    'REPAY': 167,  'PARAGRAPH': 167,
    'RETOUCH': 168,  'PARAMOUNT': 168,
    'REVENGE': 169,  'PASSENGER': 169,
    'REWARD': 170, 'PEDIGREE': 170,
    'RHYTHM': 171, 'PEGASUS': 171,
    'RIBCAGE': 172,  'PENETRATE': 172,
    'RINGBOLT': 173, 'PERCEPTIVE': 173,
    'ROBUST': 174, 'PERFORMANCE': 174,
    'ROCKER': 175, 'PHARMACY': 175,
    'RUFFLED': 176,  'PHONETIC': 176,
    'SAILBOAT': 177, 'PHOTOGRAPH': 177,
    'SAWDUST': 178,  'PIONEER': 178,
    'SCALLION': 179, 'POCKETFUL': 179,
    'SCENIC': 180, 'POLITENESS': 180,
    'SCORECARD': 181,  'POSITIVE': 181,
    'SCOTLAND': 182, 'POTATO': 182,
    'SEABIRD': 183,  'PROCESSOR': 183,
    'SELECT': 184, 'PROVINCIAL': 184,
    'SENTENCE': 185, 'PROXIMATE': 185,
    'SHADOW': 186, 'PUBERTY': 186,
    'SHAMROCK': 187, 'PUBLISHER': 187,
    'SHOWGIRL': 188, 'PYRAMID': 188,
    'SKULLCAP': 189, 'QUANTITY': 189,
    'SKYDIVE': 190,  'RACKETEER': 190,
    'SLINGSHOT': 191,  'REBELLION': 191,
    'SLOWDOWN': 192, 'RECIPE': 192,
    'SNAPLINE': 193, 'RECOVER': 193,
    'SNAPSHOT': 194, 'REPELLENT': 194,
    'SNOWCAP': 195,  'REPLICA': 195,
    'SNOWSLIDE': 196,  'REPRODUCE': 196,
    'SOLO': 197, 'RESISTOR': 197,
    'SOUTHWARD': 198,  'RESPONSIVE': 198,
    'SOYBEAN': 199,  'RETRACTION': 199,
    'SPANIEL': 200,  'RETRIEVAL': 200,
    'SPEARHEAD': 201,  'RETROSPECT': 201,
    'SPELLBIND': 202,  'REVENUE': 202,
    'SPHEROID': 203, 'REVIVAL': 203,
    'SPIGOT': 204, 'REVOLVER': 204,
    'SPINDLE': 205,  'SANDALWOOD': 205,
    'SPYGLASS': 206, 'SARDONIC': 206,
    'STAGEHAND': 207,  'SATURDAY': 207,
    'STAGNATE': 208, 'SAVAGERY': 208,
    'STAIRWAY': 209, 'SCAVENGER': 209,
    'STANDARD': 210, 'SENSATION': 210,
    'STAPLER': 211,  'SOCIABLE': 211,
    'STEAMSHIP': 212,  'SOUVENIR': 212,
    'STERLING': 213, 'SPECIALIST': 213,
    'STOCKMAN': 214, 'SPECULATE': 214,
    'STOPWATCH': 215,  'STETHOSCOPE': 215,
    'STORMY': 216, 'STUPENDOUS': 216,
    'SUGAR': 217,  'SUPPORTIVE': 217,
    'SURMOUNT': 218, 'SURRENDER': 218,
    'SUSPENSE': 219, 'SUSPICIOUS': 219,
    'SWEATBAND': 220,  'SYMPATHY': 220,
    'SWELTER': 221,  'TAMBOURINE': 221,
    'TACTICS': 222,  'TELEPHONE': 222,
    'TALON': 223,  'THERAPIST': 223,
    'TAPEWORM': 224, 'TOBACCO': 224,
    'TEMPEST': 225,  'TOLERANCE': 225,
    'TIGER': 226,  'TOMORROW': 226,
    'TISSUE': 227, 'TORPEDO': 227,
    'TONIC': 228,  'TRADITION': 228,
    'TOPMOST': 229,  'TRAVESTY': 229,
    'TRACKER': 230,  'TROMBONIST': 230,
    'TRANSIT': 231,  'TRUNCATED': 231,
    'TRAUMA': 232, 'TYPEWRITER': 232,
    'TREADMILL': 233,  'ULTIMATE': 233,
    'TROJAN': 234, 'UNDAUNTED': 234,
    'TROUBLE': 235,  'UNDERFOOT': 235,
    'TUMOR': 236,  'UNICORN': 236,
    'TUNNEL': 237, 'UNIFY': 237,
    'TYCOON': 238, 'UNIVERSE': 238,
    'UNCUT': 239,  'UNRAVEL': 239,
    'UNEARTH': 240,  'UPCOMING': 240,
    'UNWIND': 241, 'VACANCY': 241,
    'UPROOT': 242, 'VAGABOND': 242,
    'UPSET': 243,  'VERTIGO': 243,
    'UPSHOT': 244, 'VIRGINIA': 244,
    'VAPOR': 245,  'VISITOR': 245,
    'VILLAGE': 246,  'VOCALIST': 246,
    'VIRUS': 247,  'VOYAGER': 247,
    'VULCAN': 248, 'WARRANTY': 248,
    'WAFFLE': 249, 'WATERLOO': 249,
    'WALLET': 250, 'WHIMSICAL': 250,
    'WATCHWORD': 251,  'WICHITA': 251,
    'WAYSIDE': 252,  'WILMINGTON': 252,
    'WILLOW': 253, 'WYOMING': 253,
    'WOODLARK': 254, 'YESTERYEAR': 254,
    'ZULU': 255, 'YUCATAN': 255,
}

# RFC 1760
# 2048 words
SKEYS_LIST = [
             "A",     "ABE",   "ACE",   "ACT",   "AD",    "ADA",   "ADD",
    "AGO",   "AID",   "AIM",   "AIR",   "ALL",   "ALP",   "AM",    "AMY",
    "AN",    "ANA",   "AND",   "ANN",   "ANT",   "ANY",   "APE",   "APS",
    "APT",   "ARC",   "ARE",   "ARK",   "ARM",   "ART",   "AS",    "ASH",
    "ASK",   "AT",    "ATE",   "AUG",   "AUK",   "AVE",   "AWE",   "AWK",
    "AWL",   "AWN",   "AX",    "AYE",   "BAD",   "BAG",   "BAH",   "BAM",
    "BAN",   "BAR",   "BAT",   "BAY",   "BE",    "BED",   "BEE",   "BEG",
    "BEN",   "BET",   "BEY",   "BIB",   "BID",   "BIG",   "BIN",   "BIT",
    "BOB",   "BOG",   "BON",   "BOO",   "BOP",   "BOW",   "BOY",   "BUB",
    "BUD",   "BUG",   "BUM",   "BUN",   "BUS",   "BUT",   "BUY",   "BY",
    "BYE",   "CAB",   "CAL",   "CAM",   "CAN",   "CAP",   "CAR",   "CAT",
    "CAW",   "COD",   "COG",   "COL",   "CON",   "COO",   "COP",   "COT",
    "COW",   "COY",   "CRY",   "CUB",   "CUE",   "CUP",   "CUR",   "CUT",
    "DAB",   "DAD",   "DAM",   "DAN",   "DAR",   "DAY",   "DEE",   "DEL",
    "DEN",   "DES",   "DEW",   "DID",   "DIE",   "DIG",   "DIN",   "DIP",
    "DO",    "DOE",   "DOG",   "DON",   "DOT",   "DOW",   "DRY",   "DUB",
    "DUD",   "DUE",   "DUG",   "DUN",   "EAR",   "EAT",   "ED",    "EEL",
    "EGG",   "EGO",   "ELI",   "ELK",   "ELM",   "ELY",   "EM",    "END",
    "EST",   "ETC",   "EVA",   "EVE",   "EWE",   "EYE",   "FAD",   "FAN",
    "FAR",   "FAT",   "FAY",   "FED",   "FEE",   "FEW",   "FIB",   "FIG",
    "FIN",   "FIR",   "FIT",   "FLO",   "FLY",   "FOE",   "FOG",   "FOR",
    "FRY",   "FUM",   "FUN",   "FUR",   "GAB",   "GAD",   "GAG",   "GAL",
    "GAM",   "GAP",   "GAS",   "GAY",   "GEE",   "GEL",   "GEM",   "GET",
    "GIG",   "GIL",   "GIN",   "GO",    "GOT",   "GUM",   "GUN",   "GUS",
    "GUT",   "GUY",   "GYM",   "GYP",   "HA",    "HAD",   "HAL",   "HAM",
    "HAN",   "HAP",   "HAS",   "HAT",   "HAW",   "HAY",   "HE",    "HEM",
    "HEN",   "HER",   "HEW",   "HEY",   "HI",    "HID",   "HIM",   "HIP",
    "HIS",   "HIT",   "HO",    "HOB",   "HOC",   "HOE",   "HOG",   "HOP",
    "HOT",   "HOW",   "HUB",   "HUE",   "HUG",   "HUH",   "HUM",   "HUT",
    "I",     "ICY",   "IDA",   "IF",    "IKE",   "ILL",   "INK",   "INN",
    "IO",    "ION",   "IQ",    "IRA",   "IRE",   "IRK",   "IS",    "IT",
    "ITS",   "IVY",   "JAB",   "JAG",   "JAM",   "JAN",   "JAR",   "JAW",
    "JAY",   "JET",   "JIG",   "JIM",   "JO",    "JOB",   "JOE",   "JOG",
    "JOT",   "JOY",   "JUG",   "JUT",   "KAY",   "KEG",   "KEN",   "KEY",
    "KID",   "KIM",   "KIN",   "KIT",   "LA",    "LAB",   "LAC",   "LAD",
    "LAG",   "LAM",   "LAP",   "LAW",   "LAY",   "LEA",   "LED",   "LEE",
    "LEG",   "LEN",   "LEO",   "LET",   "LEW",   "LID",   "LIE",   "LIN",
    "LIP",   "LIT",   "LO",    "LOB",   "LOG",   "LOP",   "LOS",   "LOT",
    "LOU",   "LOW",   "LOY",   "LUG",   "LYE",   "MA",    "MAC",   "MAD",
    "MAE",   "MAN",   "MAO",   "MAP",   "MAT",   "MAW",   "MAY",   "ME",
    "MEG",   "MEL",   "MEN",   "MET",   "MEW",   "MID",   "MIN",   "MIT",
    "MOB",   "MOD",   "MOE",   "MOO",   "MOP",   "MOS",   "MOT",   "MOW",
    "MUD",   "MUG",   "MUM",   "MY",    "NAB",   "NAG",   "NAN",   "NAP",
    "NAT",   "NAY",   "NE",    "NED",   "NEE",   "NET",   "NEW",   "NIB",
    "NIL",   "NIP",   "NIT",   "NO",    "NOB",   "NOD",   "NON",   "NOR",
    "NOT",   "NOV",   "NOW",   "NU",    "NUN",   "NUT",   "O",     "OAF",
    "OAK",   "OAR",   "OAT",   "ODD",   "ODE",   "OF",    "OFF",   "OFT",
    "OH",    "OIL",   "OK",    "OLD",   "ON",    "ONE",   "OR",    "ORB",
    "ORE",   "ORR",   "OS",    "OTT",   "OUR",   "OUT",   "OVA",   "OW",
    "OWE",   "OWL",   "OWN",   "OX",    "PA",    "PAD",   "PAL",   "PAM",
    "PAN",   "PAP",   "PAR",   "PAT",   "PAW",   "PAY",   "PEA",   "PEG",
    "PEN",   "PEP",   "PER",   "PET",   "PEW",   "PHI",   "PI",    "PIE",
    "PIN",   "PIT",   "PLY",   "PO",    "POD",   "POE",   "POP",   "POT",
    "POW",   "PRO",   "PRY",   "PUB",   "PUG",   "PUN",   "PUP",   "PUT",
    "QUO",   "RAG",   "RAM",   "RAN",   "RAP",   "RAT",   "RAW",   "RAY",
    "REB",   "RED",   "REP",   "RET",   "RIB",   "RID",   "RIG",   "RIM",
    "RIO",   "RIP",   "ROB",   "ROD",   "ROE",   "RON",   "ROT",   "ROW",
    "ROY",   "RUB",   "RUE",   "RUG",   "RUM",   "RUN",   "RYE",   "SAC",
    "SAD",   "SAG",   "SAL",   "SAM",   "SAN",   "SAP",   "SAT",   "SAW",
    "SAY",   "SEA",   "SEC",   "SEE",   "SEN",   "SET",   "SEW",   "SHE",
    "SHY",   "SIN",   "SIP",   "SIR",   "SIS",   "SIT",   "SKI",   "SKY",
    "SLY",   "SO",    "SOB",   "SOD",   "SON",   "SOP",   "SOW",   "SOY",
    "SPA",   "SPY",   "SUB",   "SUD",   "SUE",   "SUM",   "SUN",   "SUP",
    "TAB",   "TAD",   "TAG",   "TAN",   "TAP",   "TAR",   "TEA",   "TED",
    "TEE",   "TEN",   "THE",   "THY",   "TIC",   "TIE",   "TIM",   "TIN",
    "TIP",   "TO",    "TOE",   "TOG",   "TOM",   "TON",   "TOO",   "TOP",
    "TOW",   "TOY",   "TRY",   "TUB",   "TUG",   "TUM",   "TUN",   "TWO",
    "UN",    "UP",    "US",    "USE",   "VAN",   "VAT",   "VET",   "VIE",
    "WAD",   "WAG",   "WAR",   "WAS",   "WAY",   "WE",    "WEB",   "WED",
    "WEE",   "WET",   "WHO",   "WHY",   "WIN",   "WIT",   "WOK",   "WON",
    "WOO",   "WOW",   "WRY",   "WU",    "YAM",   "YAP",   "YAW",   "YE",
    "YEA",   "YES",   "YET",   "YOU",   "ABED",  "ABEL",  "ABET",  "ABLE",
    "ABUT",  "ACHE",  "ACID",  "ACME",  "ACRE",  "ACTA",  "ACTS",  "ADAM",
    "ADDS",  "ADEN",  "AFAR",  "AFRO",  "AGEE",  "AHEM",  "AHOY",  "AIDA",
    "AIDE",  "AIDS",  "AIRY",  "AJAR",  "AKIN",  "ALAN",  "ALEC",  "ALGA",
    "ALIA",  "ALLY",  "ALMA",  "ALOE",  "ALSO",  "ALTO",  "ALUM",  "ALVA",
    "AMEN",  "AMES",  "AMID",  "AMMO",  "AMOK",  "AMOS",  "AMRA",  "ANDY",
    "ANEW",  "ANNA",  "ANNE",  "ANTE",  "ANTI",  "AQUA",  "ARAB",  "ARCH",
    "AREA",  "ARGO",  "ARID",  "ARMY",  "ARTS",  "ARTY",  "ASIA",  "ASKS",
    "ATOM",  "AUNT",  "AURA",  "AUTO",  "AVER",  "AVID",  "AVIS",  "AVON",
    "AVOW",  "AWAY",  "AWRY",  "BABE",  "BABY",  "BACH",  "BACK",  "BADE",
    "BAIL",  "BAIT",  "BAKE",  "BALD",  "BALE",  "BALI",  "BALK",  "BALL",
    "BALM",  "BAND",  "BANE",  "BANG",  "BANK",  "BARB",  "BARD",  "BARE",
    "BARK",  "BARN",  "BARR",  "BASE",  "BASH",  "BASK",  "BASS",  "BATE",
    "BATH",  "BAWD",  "BAWL",  "BEAD",  "BEAK",  "BEAM",  "BEAN",  "BEAR",
    "BEAT",  "BEAU",  "BECK",  "BEEF",  "BEEN",  "BEER",  "BEET",  "BELA",
    "BELL",  "BELT",  "BEND",  "BENT",  "BERG",  "BERN",  "BERT",  "BESS",
    "BEST",  "BETA",  "BETH",  "BHOY",  "BIAS",  "BIDE",  "BIEN",  "BILE",
    "BILK",  "BILL",  "BIND",  "BING",  "BIRD",  "BITE",  "BITS",  "BLAB",
    "BLAT",  "BLED",  "BLEW",  "BLOB",  "BLOC",  "BLOT",  "BLOW",  "BLUE",
    "BLUM",  "BLUR",  "BOAR",  "BOAT",  "BOCA",  "BOCK",  "BODE",  "BODY",
    "BOGY",  "BOHR",  "BOIL",  "BOLD",  "BOLO",  "BOLT",  "BOMB",  "BONA",
    "BOND",  "BONE",  "BONG",  "BONN",  "BONY",  "BOOK",  "BOOM",  "BOON",
    "BOOT",  "BORE",  "BORG",  "BORN",  "BOSE",  "BOSS",  "BOTH",  "BOUT",
    "BOWL",  "BOYD",  "BRAD",  "BRAE",  "BRAG",  "BRAN",  "BRAY",  "BRED",
    "BREW",  "BRIG",  "BRIM",  "BROW",  "BUCK",  "BUDD",  "BUFF",  "BULB",
    "BULK",  "BULL",  "BUNK",  "BUNT",  "BUOY",  "BURG",  "BURL",  "BURN",
    "BURR",  "BURT",  "BURY",  "BUSH",  "BUSS",  "BUST",  "BUSY",  "BYTE",
    "CADY",  "CAFE",  "CAGE",  "CAIN",  "CAKE",  "CALF",  "CALL",  "CALM",
    "CAME",  "CANE",  "CANT",  "CARD",  "CARE",  "CARL",  "CARR",  "CART",
    "CASE",  "CASH",  "CASK",  "CAST",  "CAVE",  "CEIL",  "CELL",  "CENT",
    "CERN",  "CHAD",  "CHAR",  "CHAT",  "CHAW",  "CHEF",  "CHEN",  "CHEW",
    "CHIC",  "CHIN",  "CHOU",  "CHOW",  "CHUB",  "CHUG",  "CHUM",  "CITE",
    "CITY",  "CLAD",  "CLAM",  "CLAN",  "CLAW",  "CLAY",  "CLOD",  "CLOG",
    "CLOT",  "CLUB",  "CLUE",  "COAL",  "COAT",  "COCA",  "COCK",  "COCO",
    "CODA",  "CODE",  "CODY",  "COED",  "COIL",  "COIN",  "COKE",  "COLA",
    "COLD",  "COLT",  "COMA",  "COMB",  "COME",  "COOK",  "COOL",  "COON",
    "COOT",  "CORD",  "CORE",  "CORK",  "CORN",  "COST",  "COVE",  "COWL",
    "CRAB",  "CRAG",  "CRAM",  "CRAY",  "CREW",  "CRIB",  "CROW",  "CRUD",
    "CUBA",  "CUBE",  "CUFF",  "CULL",  "CULT",  "CUNY",  "CURB",  "CURD",
    "CURE",  "CURL",  "CURT",  "CUTS",  "DADE",  "DALE",  "DAME",  "DANA",
    "DANE",  "DANG",  "DANK",  "DARE",  "DARK",  "DARN",  "DART",  "DASH",
    "DATA",  "DATE",  "DAVE",  "DAVY",  "DAWN",  "DAYS",  "DEAD",  "DEAF",
    "DEAL",  "DEAN",  "DEAR",  "DEBT",  "DECK",  "DEED",  "DEEM",  "DEER",
    "DEFT",  "DEFY",  "DELL",  "DENT",  "DENY",  "DESK",  "DIAL",  "DICE",
    "DIED",  "DIET",  "DIME",  "DINE",  "DING",  "DINT",  "DIRE",  "DIRT",
    "DISC",  "DISH",  "DISK",  "DIVE",  "DOCK",  "DOES",  "DOLE",  "DOLL",
    "DOLT",  "DOME",  "DONE",  "DOOM",  "DOOR",  "DORA",  "DOSE",  "DOTE",
    "DOUG",  "DOUR",  "DOVE",  "DOWN",  "DRAB",  "DRAG",  "DRAM",  "DRAW",
    "DREW",  "DRUB",  "DRUG",  "DRUM",  "DUAL",  "DUCK",  "DUCT",  "DUEL",
    "DUET",  "DUKE",  "DULL",  "DUMB",  "DUNE",  "DUNK",  "DUSK",  "DUST",
    "DUTY",  "EACH",  "EARL",  "EARN",  "EASE",  "EAST",  "EASY",  "EBEN",
    "ECHO",  "EDDY",  "EDEN",  "EDGE",  "EDGY",  "EDIT",  "EDNA",  "EGAN",
    "ELAN",  "ELBA",  "ELLA",  "ELSE",  "EMIL",  "EMIT",  "EMMA",  "ENDS",
    "ERIC",  "EROS",  "EVEN",  "EVER",  "EVIL",  "EYED",  "FACE",  "FACT",
    "FADE",  "FAIL",  "FAIN",  "FAIR",  "FAKE",  "FALL",  "FAME",  "FANG",
    "FARM",  "FAST",  "FATE",  "FAWN",  "FEAR",  "FEAT",  "FEED",  "FEEL",
    "FEET",  "FELL",  "FELT",  "FEND",  "FERN",  "FEST",  "FEUD",  "FIEF",
    "FIGS",  "FILE",  "FILL",  "FILM",  "FIND",  "FINE",  "FINK",  "FIRE",
    "FIRM",  "FISH",  "FISK",  "FIST",  "FITS",  "FIVE",  "FLAG",  "FLAK",
    "FLAM",  "FLAT",  "FLAW",  "FLEA",  "FLED",  "FLEW",  "FLIT",  "FLOC",
    "FLOG",  "FLOW",  "FLUB",  "FLUE",  "FOAL",  "FOAM",  "FOGY",  "FOIL",
    "FOLD",  "FOLK",  "FOND",  "FONT",  "FOOD",  "FOOL",  "FOOT",  "FORD",
    "FORE",  "FORK",  "FORM",  "FORT",  "FOSS",  "FOUL",  "FOUR",  "FOWL",
    "FRAU",  "FRAY",  "FRED",  "FREE",  "FRET",  "FREY",  "FROG",  "FROM",
    "FUEL",  "FULL",  "FUME",  "FUND",  "FUNK",  "FURY",  "FUSE",  "FUSS",
    "GAFF",  "GAGE",  "GAIL",  "GAIN",  "GAIT",  "GALA",  "GALE",  "GALL",
    "GALT",  "GAME",  "GANG",  "GARB",  "GARY",  "GASH",  "GATE",  "GAUL",
    "GAUR",  "GAVE",  "GAWK",  "GEAR",  "GELD",  "GENE",  "GENT",  "GERM",
    "GETS",  "GIBE",  "GIFT",  "GILD",  "GILL",  "GILT",  "GINA",  "GIRD",
    "GIRL",  "GIST",  "GIVE",  "GLAD",  "GLEE",  "GLEN",  "GLIB",  "GLOB",
    "GLOM",  "GLOW",  "GLUE",  "GLUM",  "GLUT",  "GOAD",  "GOAL",  "GOAT",
    "GOER",  "GOES",  "GOLD",  "GOLF",  "GONE",  "GONG",  "GOOD",  "GOOF",
    "GORE",  "GORY",  "GOSH",  "GOUT",  "GOWN",  "GRAB",  "GRAD",  "GRAY",
    "GREG",  "GREW",  "GREY",  "GRID",  "GRIM",  "GRIN",  "GRIT",  "GROW",
    "GRUB",  "GULF",  "GULL",  "GUNK",  "GURU",  "GUSH",  "GUST",  "GWEN",
    "GWYN",  "HAAG",  "HAAS",  "HACK",  "HAIL",  "HAIR",  "HALE",  "HALF",
    "HALL",  "HALO",  "HALT",  "HAND",  "HANG",  "HANK",  "HANS",  "HARD",
    "HARK",  "HARM",  "HART",  "HASH",  "HAST",  "HATE",  "HATH",  "HAUL",
    "HAVE",  "HAWK",  "HAYS",  "HEAD",  "HEAL",  "HEAR",  "HEAT",  "HEBE",
    "HECK",  "HEED",  "HEEL",  "HEFT",  "HELD",  "HELL",  "HELM",  "HERB",
    "HERD",  "HERE",  "HERO",  "HERS",  "HESS",  "HEWN",  "HICK",  "HIDE",
    "HIGH",  "HIKE",  "HILL",  "HILT",  "HIND",  "HINT",  "HIRE",  "HISS",
    "HIVE",  "HOBO",  "HOCK",  "HOFF",  "HOLD",  "HOLE",  "HOLM",  "HOLT",
    "HOME",  "HONE",  "HONK",  "HOOD",  "HOOF",  "HOOK",  "HOOT",  "HORN",
    "HOSE",  "HOST",  "HOUR",  "HOVE",  "HOWE",  "HOWL",  "HOYT",  "HUCK",
    "HUED",  "HUFF",  "HUGE",  "HUGH",  "HUGO",  "HULK",  "HULL",  "HUNK",
    "HUNT",  "HURD",  "HURL",  "HURT",  "HUSH",  "HYDE",  "HYMN",  "IBIS",
    "ICON",  "IDEA",  "IDLE",  "IFFY",  "INCA",  "INCH",  "INTO",  "IONS",
    "IOTA",  "IOWA",  "IRIS",  "IRMA",  "IRON",  "ISLE",  "ITCH",  "ITEM",
    "IVAN",  "JACK",  "JADE",  "JAIL",  "JAKE",  "JANE",  "JAVA",  "JEAN",
    "JEFF",  "JERK",  "JESS",  "JEST",  "JIBE",  "JILL",  "JILT",  "JIVE",
    "JOAN",  "JOBS",  "JOCK",  "JOEL",  "JOEY",  "JOHN",  "JOIN",  "JOKE",
    "JOLT",  "JOVE",  "JUDD",  "JUDE",  "JUDO",  "JUDY",  "JUJU",  "JUKE",
    "JULY",  "JUNE",  "JUNK",  "JUNO",  "JURY",  "JUST",  "JUTE",  "KAHN",
    "KALE",  "KANE",  "KANT",  "KARL",  "KATE",  "KEEL",  "KEEN",  "KENO",
    "KENT",  "KERN",  "KERR",  "KEYS",  "KICK",  "KILL",  "KIND",  "KING",
    "KIRK",  "KISS",  "KITE",  "KLAN",  "KNEE",  "KNEW",  "KNIT",  "KNOB",
    "KNOT",  "KNOW",  "KOCH",  "KONG",  "KUDO",  "KURD",  "KURT",  "KYLE",
    "LACE",  "LACK",  "LACY",  "LADY",  "LAID",  "LAIN",  "LAIR",  "LAKE",
    "LAMB",  "LAME",  "LAND",  "LANE",  "LANG",  "LARD",  "LARK",  "LASS",
    "LAST",  "LATE",  "LAUD",  "LAVA",  "LAWN",  "LAWS",  "LAYS",  "LEAD",
    "LEAF",  "LEAK",  "LEAN",  "LEAR",  "LEEK",  "LEER",  "LEFT",  "LEND",
    "LENS",  "LENT",  "LEON",  "LESK",  "LESS",  "LEST",  "LETS",  "LIAR",
    "LICE",  "LICK",  "LIED",  "LIEN",  "LIES",  "LIEU",  "LIFE",  "LIFT",
    "LIKE",  "LILA",  "LILT",  "LILY",  "LIMA",  "LIMB",  "LIME",  "LIND",
    "LINE",  "LINK",  "LINT",  "LION",  "LISA",  "LIST",  "LIVE",  "LOAD",
    "LOAF",  "LOAM",  "LOAN",  "LOCK",  "LOFT",  "LOGE",  "LOIS",  "LOLA",
    "LONE",  "LONG",  "LOOK",  "LOON",  "LOOT",  "LORD",  "LORE",  "LOSE",
    "LOSS",  "LOST",  "LOUD",  "LOVE",  "LOWE",  "LUCK",  "LUCY",  "LUGE",
    "LUKE",  "LULU",  "LUND",  "LUNG",  "LURA",  "LURE",  "LURK",  "LUSH",
    "LUST",  "LYLE",  "LYNN",  "LYON",  "LYRA",  "MACE",  "MADE",  "MAGI",
    "MAID",  "MAIL",  "MAIN",  "MAKE",  "MALE",  "MALI",  "MALL",  "MALT",
    "MANA",  "MANN",  "MANY",  "MARC",  "MARE",  "MARK",  "MARS",  "MART",
    "MARY",  "MASH",  "MASK",  "MASS",  "MAST",  "MATE",  "MATH",  "MAUL",
    "MAYO",  "MEAD",  "MEAL",  "MEAN",  "MEAT",  "MEEK",  "MEET",  "MELD",
    "MELT",  "MEMO",  "MEND",  "MENU",  "MERT",  "MESH",  "MESS",  "MICE",
    "MIKE",  "MILD",  "MILE",  "MILK",  "MILL",  "MILT",  "MIMI",  "MIND",
    "MINE",  "MINI",  "MINK",  "MINT",  "MIRE",  "MISS",  "MIST",  "MITE",
    "MITT",  "MOAN",  "MOAT",  "MOCK",  "MODE",  "MOLD",  "MOLE",  "MOLL",
    "MOLT",  "MONA",  "MONK",  "MONT",  "MOOD",  "MOON",  "MOOR",  "MOOT",
    "MORE",  "MORN",  "MORT",  "MOSS",  "MOST",  "MOTH",  "MOVE",  "MUCH",
    "MUCK",  "MUDD",  "MUFF",  "MULE",  "MULL",  "MURK",  "MUSH",  "MUST",
    "MUTE",  "MUTT",  "MYRA",  "MYTH",  "NAGY",  "NAIL",  "NAIR",  "NAME",
    "NARY",  "NASH",  "NAVE",  "NAVY",  "NEAL",  "NEAR",  "NEAT",  "NECK",
    "NEED",  "NEIL",  "NELL",  "NEON",  "NERO",  "NESS",  "NEST",  "NEWS",
    "NEWT",  "NIBS",  "NICE",  "NICK",  "NILE",  "NINA",  "NINE",  "NOAH",
    "NODE",  "NOEL",  "NOLL",  "NONE",  "NOOK",  "NOON",  "NORM",  "NOSE",
    "NOTE",  "NOUN",  "NOVA",  "NUDE",  "NULL",  "NUMB",  "OATH",  "OBEY",
    "OBOE",  "ODIN",  "OHIO",  "OILY",  "OINT",  "OKAY",  "OLAF",  "OLDY",
    "OLGA",  "OLIN",  "OMAN",  "OMEN",  "OMIT",  "ONCE",  "ONES",  "ONLY",
    "ONTO",  "ONUS",  "ORAL",  "ORGY",  "OSLO",  "OTIS",  "OTTO",  "OUCH",
    "OUST",  "OUTS",  "OVAL",  "OVEN",  "OVER",  "OWLY",  "OWNS",  "QUAD",
    "QUIT",  "QUOD",  "RACE",  "RACK",  "RACY",  "RAFT",  "RAGE",  "RAID",
    "RAIL",  "RAIN",  "RAKE",  "RANK",  "RANT",  "RARE",  "RASH",  "RATE",
    "RAVE",  "RAYS",  "READ",  "REAL",  "REAM",  "REAR",  "RECK",  "REED",
    "REEF",  "REEK",  "REEL",  "REID",  "REIN",  "RENA",  "REND",  "RENT",
    "REST",  "RICE",  "RICH",  "RICK",  "RIDE",  "RIFT",  "RILL",  "RIME",
    "RING",  "RINK",  "RISE",  "RISK",  "RITE",  "ROAD",  "ROAM",  "ROAR",
    "ROBE",  "ROCK",  "RODE",  "ROIL",  "ROLL",  "ROME",  "ROOD",  "ROOF",
    "ROOK",  "ROOM",  "ROOT",  "ROSA",  "ROSE",  "ROSS",  "ROSY",  "ROTH",
    "ROUT",  "ROVE",  "ROWE",  "ROWS",  "RUBE",  "RUBY",  "RUDE",  "RUDY",
    "RUIN",  "RULE",  "RUNG",  "RUNS",  "RUNT",  "RUSE",  "RUSH",  "RUSK",
    "RUSS",  "RUST",  "RUTH",  "SACK",  "SAFE",  "SAGE",  "SAID",  "SAIL",
    "SALE",  "SALK",  "SALT",  "SAME",  "SAND",  "SANE",  "SANG",  "SANK",
    "SARA",  "SAUL",  "SAVE",  "SAYS",  "SCAN",  "SCAR",  "SCAT",  "SCOT",
    "SEAL",  "SEAM",  "SEAR",  "SEAT",  "SEED",  "SEEK",  "SEEM",  "SEEN",
    "SEES",  "SELF",  "SELL",  "SEND",  "SENT",  "SETS",  "SEWN",  "SHAG",
    "SHAM",  "SHAW",  "SHAY",  "SHED",  "SHIM",  "SHIN",  "SHOD",  "SHOE",
    "SHOT",  "SHOW",  "SHUN",  "SHUT",  "SICK",  "SIDE",  "SIFT",  "SIGH",
    "SIGN",  "SILK",  "SILL",  "SILO",  "SILT",  "SINE",  "SING",  "SINK",
    "SIRE",  "SITE",  "SITS",  "SITU",  "SKAT",  "SKEW",  "SKID",  "SKIM",
    "SKIN",  "SKIT",  "SLAB",  "SLAM",  "SLAT",  "SLAY",  "SLED",  "SLEW",
    "SLID",  "SLIM",  "SLIT",  "SLOB",  "SLOG",  "SLOT",  "SLOW",  "SLUG",
    "SLUM",  "SLUR",  "SMOG",  "SMUG",  "SNAG",  "SNOB",  "SNOW",  "SNUB",
    "SNUG",  "SOAK",  "SOAR",  "SOCK",  "SODA",  "SOFA",  "SOFT",  "SOIL",
    "SOLD",  "SOME",  "SONG",  "SOON",  "SOOT",  "SORE",  "SORT",  "SOUL",
    "SOUR",  "SOWN",  "STAB",  "STAG",  "STAN",  "STAR",  "STAY",  "STEM",
    "STEW",  "STIR",  "STOW",  "STUB",  "STUN",  "SUCH",  "SUDS",  "SUIT",
    "SULK",  "SUMS",  "SUNG",  "SUNK",  "SURE",  "SURF",  "SWAB",  "SWAG",
    "SWAM",  "SWAN",  "SWAT",  "SWAY",  "SWIM",  "SWUM",  "TACK",  "TACT",
    "TAIL",  "TAKE",  "TALE",  "TALK",  "TALL",  "TANK",  "TASK",  "TATE",
    "TAUT",  "TEAL",  "TEAM",  "TEAR",  "TECH",  "TEEM",  "TEEN",  "TEET",
    "TELL",  "TEND",  "TENT",  "TERM",  "TERN",  "TESS",  "TEST",  "THAN",
    "THAT",  "THEE",  "THEM",  "THEN",  "THEY",  "THIN",  "THIS",  "THUD",
    "THUG",  "TICK",  "TIDE",  "TIDY",  "TIED",  "TIER",  "TILE",  "TILL",
    "TILT",  "TIME",  "TINA",  "TINE",  "TINT",  "TINY",  "TIRE",  "TOAD",
    "TOGO",  "TOIL",  "TOLD",  "TOLL",  "TONE",  "TONG",  "TONY",  "TOOK",
    "TOOL",  "TOOT",  "TORE",  "TORN",  "TOTE",  "TOUR",  "TOUT",  "TOWN",
    "TRAG",  "TRAM",  "TRAY",  "TREE",  "TREK",  "TRIG",  "TRIM",  "TRIO",
    "TROD",  "TROT",  "TROY",  "TRUE",  "TUBA",  "TUBE",  "TUCK",  "TUFT",
    "TUNA",  "TUNE",  "TUNG",  "TURF",  "TURN",  "TUSK",  "TWIG",  "TWIN",
    "TWIT",  "ULAN",  "UNIT",  "URGE",  "USED",  "USER",  "USES",  "UTAH",
    "VAIL",  "VAIN",  "VALE",  "VARY",  "VASE",  "VAST",  "VEAL",  "VEDA",
    "VEIL",  "VEIN",  "VEND",  "VENT",  "VERB",  "VERY",  "VETO",  "VICE",
    "VIEW",  "VINE",  "VISE",  "VOID",  "VOLT",  "VOTE",  "WACK",  "WADE",
    "WAGE",  "WAIL",  "WAIT",  "WAKE",  "WALE",  "WALK",  "WALL",  "WALT",
    "WAND",  "WANE",  "WANG",  "WANT",  "WARD",  "WARM",  "WARN",  "WART",
    "WASH",  "WAST",  "WATS",  "WATT",  "WAVE",  "WAVY",  "WAYS",  "WEAK",
    "WEAL",  "WEAN",  "WEAR",  "WEED",  "WEEK",  "WEIR",  "WELD",  "WELL",
    "WELT",  "WENT",  "WERE",  "WERT",  "WEST",  "WHAM",  "WHAT",  "WHEE",
    "WHEN",  "WHET",  "WHOA",  "WHOM",  "WICK",  "WIFE",  "WILD",  "WILL",
    "WIND",  "WINE",  "WING",  "WINK",  "WINO",  "WIRE",  "WISE",  "WISH",
    "WITH",  "WOLF",  "WONT",  "WOOD",  "WOOL",  "WORD",  "WORE",  "WORK",
    "WORM",  "WORN",  "WOVE",  "WRIT",  "WYNN",  "YALE",  "YANG",  "YANK",
    "YARD",  "YARN",  "YAWL",  "YAWN",  "YEAH",  "YEAR",  "YELL",  "YOGA",
    "YOKE"
  ]

NUM_NAMES = ["ZERO", "WAN", "TOOTH", "THREE", "FORR", "FIFE", "SIX", "SEVEN",]

def pgp_words_from_bytes(some_bytes, swap=False):
  """Use the PGP wordlist to convert bytes to words
     `shift` means use even word for odd and vice versa"""
  to_return = []
  byte_num = 0
  for byte in some_bytes:
    index = (byte_num + (1 if swap else 0)) % 2
    to_return.append(PGP_WORD_LIST[byte][index])
    byte_num += 1
  return ' '.join(to_return)


def test_pgp_words_from_bytes():
    assert pgp_words_from_bytes(b'\xde\xad\xbe\xef') == "tactics perceptive skydive unravel"
    assert pgp_words_from_bytes(b'\xde\xad\xbe') == "tactics perceptive skydive"
    assert pgp_words_from_bytes(b'\xde\xad') == "tactics perceptive"
    assert pgp_words_from_bytes(b'\xde') == "tactics"
    assert pgp_words_from_bytes(b'') == ""
    assert pgp_words_from_bytes(b'\xad\xbe\xef') == "ringbolt racketeer uncut"
    assert pgp_words_from_bytes(b'\xbe\xef') == "skydive unravel"
    assert pgp_words_from_bytes(b'\xef') == "uncut"

    assert pgp_words_from_bytes(b'\xde\xad\xbe\xef', True) == "telephone ringbolt racketeer uncut"
    assert pgp_words_from_bytes(b'\xde\xad\xbe', True) == "telephone ringbolt racketeer"
    assert pgp_words_from_bytes(b'\xde\xad', True) == "telephone ringbolt"
    assert pgp_words_from_bytes(b'\xde', True) == "telephone"
    assert pgp_words_from_bytes(b'') == ""
    assert pgp_words_from_bytes(b'\xad\xbe\xef', True) == "perceptive skydive unravel"
    assert pgp_words_from_bytes(b'\xbe\xef', True) == "racketeer uncut"
    assert pgp_words_from_bytes(b'\xef', True) == "unravel"


def eight_bytes_from_6_words(six_words):
    try:
        numbers = [SKEYS_LIST.index(six_words[i]) for i in range(0,6)]
    except ValueError as e:
        print(f"At least one of '{six_words}' is not an S/KEYS word.  Quitting.")
        sys.exit(1)
    return ((numbers[0] << 55) + \
            (numbers[1] << 44) + \
            (numbers[2] << 33) + \
            (numbers[3] << 22) + \
            (numbers[4] << 11) + \
            (numbers[5] << 0)) >> 2 # The last two are parity bits not checking


def six_words_from_8_bytes(eight_byte_int):
    sixty_six_bits = "{:064b}".format(eight_byte_int) + "{:02b}".format(parity_bits(eight_byte_int))
    return [
        SKEYS_LIST[int(sixty_six_bits[0:11], 2)],
        SKEYS_LIST[int(sixty_six_bits[11:22], 2)],
        SKEYS_LIST[int(sixty_six_bits[22:33], 2)],
        SKEYS_LIST[int(sixty_six_bits[33:44], 2)],
        SKEYS_LIST[int(sixty_six_bits[44:55], 2)],
        SKEYS_LIST[int(sixty_six_bits[55:66], 2)],
    ]


def int_from_8_bytes(eight_bytes):
    return \
    (eight_bytes[0] << 56) + \
    (eight_bytes[1] << 48) + \
    (eight_bytes[2] << 40) + \
    (eight_bytes[3] << 32) + \
    (eight_bytes[4] << 24) + \
    (eight_bytes[5] << 16) + \
    (eight_bytes[6] <<  8) + \
    (eight_bytes[7] <<  0)

def test_int_from_8_bytes():
    assert int_from_8_bytes([0xde, 0xad, 0xbe, 0xef, 0xfe, 0xed, 0xfa, 0xce]) == 0xdeadbeeffeedface


# Examples from RFC 2289
def test_six_words_from_8_bytes():
    assert six_words_from_8_bytes(0x85c43ee03857765b) == "FOWL KID MASH DEAD DUAL OAF".split()
    assert six_words_from_8_bytes(0xD1854218EBBB0B51) == "ROME MUG FRED SCAN LIVE LACE".split()
    assert six_words_from_8_bytes(0x63473EF01CD0B444) == "CARD SAD MINI RYE COL KIN".split()
    assert six_words_from_8_bytes(0xC5E612776E6C237A) == "NOTE OUT IBIS SINK NAVE MODE".split()
    assert six_words_from_8_bytes(0x50076F47EB1ADE4E) == "AWAY SEN ROOK SALT LICE MAP".split()
    assert six_words_from_8_bytes(0x65D20D1949B5F7AB) == "CHEW GRIM WU HANG BUCK SAID".split()
    assert six_words_from_8_bytes(0xD150C82CCE6F62D1) == "ROIL FREE COG HUNK WAIT COCA".split()
    assert six_words_from_8_bytes(0x849C79D4F6F55388) == "FOOL STEM DONE TOOL BECK NILE".split()
    assert six_words_from_8_bytes(0x8C0992FB250847B1) == "GIST AMOS MOOT AIDS FOOD SEEM".split()
    assert six_words_from_8_bytes(0x3F3BF4B4145FD74B) == "TAG SLOW NOV MIN WOOL KENO".split()
    assert six_words_from_8_bytes(0x9E876134D90499DD) == "INCH SEA ANNE LONG AHEM TOUR".split()
    assert six_words_from_8_bytes(0x7965E05436F5029F) == "EASE OIL FUM CURE AWRY AVIS".split()
    assert six_words_from_8_bytes(0x50FE1962C4965880) == "BAIL TUFT BITS GANG CHEF THY".split()
    assert six_words_from_8_bytes(0x87066DD9644BF206) == "FULL PEW DOWN ONCE MORT ARC".split()
    assert six_words_from_8_bytes(0x7CD34C1040ADD14B) == "FACT HOOF AT FIST SITE KENT".split()
    assert six_words_from_8_bytes(0x5AA37A81F212146C) == "BODE HOP JAKE STOW JUT RAP".split()
    assert six_words_from_8_bytes(0xF205753943DE4CF9) == "ULAN NEW ARMY FUSE SUIT EYED".split()
    assert six_words_from_8_bytes(0xDDCDAC956F234937) == "SKIM CULT LOB SLAM POE HOWL".split()
    assert six_words_from_8_bytes(0xB203E28FA525BE47) == "LONG IVY JULY AJAR BOND LEE".split()
    assert six_words_from_8_bytes(0xBB9E6AE1979D8FF4) == "MILT VARY MAST OK SEES WENT".split()
    assert six_words_from_8_bytes(0x63D936639734385B) == "CART OTTO HIVE ODE VAT NUT".split()
    assert six_words_from_8_bytes(0x87FEC7768B73CCF9) == "GAFF WAIT SKID GIG SKY EYED".split()
    assert six_words_from_8_bytes(0xAD85F658EBE383C9) == "LEST OR HEEL SCOT ROB SUIT".split()
    assert six_words_from_8_bytes(0xD07CE229B5CF119B) == "RITE TAKE GELD COST TUNE RECK".split()
    assert six_words_from_8_bytes(0x27BC71035AAF3DC6) == "MAY STAR TIN LYON VEDA STAN".split()
    assert six_words_from_8_bytes(0xD51F3E99BF8E6F0B) == "RUST WELT KICK FELL TAIL FRAU".split()
    assert six_words_from_8_bytes(0x82AEB52D943774E4) == "FLIT DOSE ALSO MEW DRUM DEFY".split()
    assert six_words_from_8_bytes(0x4F296A74FE1567EC) == "AURA ALOE HURL WING BERG WAIT".split()

def test_eight_bytes_from_6_words():
    assert eight_bytes_from_6_words("FOWL KID MASH DEAD DUAL OAF".split()) == 0x85c43ee03857765b
    assert eight_bytes_from_6_words("ROME MUG FRED SCAN LIVE LACE".split()) == 0xD1854218EBBB0B51
    assert eight_bytes_from_6_words("CARD SAD MINI RYE COL KIN".split()) == 0x63473EF01CD0B444
    assert eight_bytes_from_6_words("NOTE OUT IBIS SINK NAVE MODE".split()) == 0xC5E612776E6C237A
    assert eight_bytes_from_6_words("AWAY SEN ROOK SALT LICE MAP".split()) == 0x50076F47EB1ADE4E
    assert eight_bytes_from_6_words("CHEW GRIM WU HANG BUCK SAID".split()) == 0x65D20D1949B5F7AB
    assert eight_bytes_from_6_words("ROIL FREE COG HUNK WAIT COCA".split()) == 0xD150C82CCE6F62D1
    assert eight_bytes_from_6_words("FOOL STEM DONE TOOL BECK NILE".split()) == 0x849C79D4F6F55388
    assert eight_bytes_from_6_words("GIST AMOS MOOT AIDS FOOD SEEM".split()) == 0x8C0992FB250847B1
    assert eight_bytes_from_6_words("TAG SLOW NOV MIN WOOL KENO".split()) == 0x3F3BF4B4145FD74B
    assert eight_bytes_from_6_words("INCH SEA ANNE LONG AHEM TOUR".split()) == 0x9E876134D90499DD
    assert eight_bytes_from_6_words("EASE OIL FUM CURE AWRY AVIS".split()) == 0x7965E05436F5029F
    assert eight_bytes_from_6_words("BAIL TUFT BITS GANG CHEF THY".split()) == 0x50FE1962C4965880
    assert eight_bytes_from_6_words("FULL PEW DOWN ONCE MORT ARC".split()) == 0x87066DD9644BF206
    assert eight_bytes_from_6_words("FACT HOOF AT FIST SITE KENT".split()) == 0x7CD34C1040ADD14B
    assert eight_bytes_from_6_words("BODE HOP JAKE STOW JUT RAP".split()) == 0x5AA37A81F212146C
    assert eight_bytes_from_6_words("ULAN NEW ARMY FUSE SUIT EYED".split()) == 0xF205753943DE4CF9
    assert eight_bytes_from_6_words("SKIM CULT LOB SLAM POE HOWL".split()) == 0xDDCDAC956F234937
    assert eight_bytes_from_6_words("LONG IVY JULY AJAR BOND LEE".split()) == 0xB203E28FA525BE47
    assert eight_bytes_from_6_words("MILT VARY MAST OK SEES WENT".split()) == 0xBB9E6AE1979D8FF4
    assert eight_bytes_from_6_words("CART OTTO HIVE ODE VAT NUT".split()) == 0x63D936639734385B
    assert eight_bytes_from_6_words("GAFF WAIT SKID GIG SKY EYED".split()) == 0x87FEC7768B73CCF9
    assert eight_bytes_from_6_words("LEST OR HEEL SCOT ROB SUIT".split()) == 0xAD85F658EBE383C9
    assert eight_bytes_from_6_words("RITE TAKE GELD COST TUNE RECK".split()) == 0xD07CE229B5CF119B
    assert eight_bytes_from_6_words("MAY STAR TIN LYON VEDA STAN".split()) == 0x27BC71035AAF3DC6
    assert eight_bytes_from_6_words("RUST WELT KICK FELL TAIL FRAU".split()) == 0xD51F3E99BF8E6F0B
    assert eight_bytes_from_6_words("FLIT DOSE ALSO MEW DRUM DEFY".split()) == 0x82AEB52D943774E4
    assert eight_bytes_from_6_words("AURA ALOE HURL WING BERG WAIT".split()) == 0x4F296A74FE1567EC



def parity_bits(someint):
    rolling_sum = 0b00
    while someint != 0:
        rolling_sum += someint & 0b11
        someint = someint >> 2
    return rolling_sum & 0b11

def test_parity_bits():
    assert parity_bits(0b101010001010101110101010101010) == 0b01
    assert parity_bits(0b01010001010101110101010101010) == 0b11
    assert parity_bits(0b1010001010101110101010101010) == 0b11
    assert parity_bits(0b010001010101110101010101010) == 0b01
    for tiny in (0b00, 0b01, 0b10, 0b11):
        assert parity_bits(tiny) == tiny


def usage(program_name):
    return f"""Usage: {program_name} [-p] [-r] <filename>
  -p  Use PGP wordlist instead of S/KEYS wordlist.  Takes longer to type, but
      is a one-to-one relationship with bytes.  S/KEYS wordlist maps 11-bit
      chunks instead of bytes.
  -r  Expect <filename> to be filled with words and output binary"""


def main():
    # l.basicConfig(level=l.INFO)
    if len(sys.argv) < 2:
        print(usage(sys.argv[0]))
        sys.exit(1)

    if "-h" in sys.argv or "--help" in sys.argv:
        print(usage(sys.argv[0]))
        sys.exit(0)

    skeys_words = True
    reverse = False

    filename = sys.argv[-1]

    if "-p" in sys.argv:
        skeys_words = False
    if "-pr" in sys.argv or "-rp" in sys.argv:
        skeys_words = False
        reverse = True
    if "-r" in sys.argv:
        reverse = True

    if reverse:
        with open(filename, "r") as f:
            words = f.read().split()
            if skeys_words:
                if words[-1].upper() != "PADD" or words[-2].upper() not in NUM_NAMES:
                    print("File corrupt or truncated.  Quitting", file=sys.stderr)
                    sys.exit(1)
                num_padding_bytes = NUM_NAMES.index(words[-2].upper())
                num_bytes_to_output = ((len(words) - 2) // 6) * 8 - num_padding_bytes
                num_bytes_left_to_output = num_bytes_to_output
                while num_bytes_left_to_output > 8:
                    eight_bytes = eight_bytes_from_6_words(
                        [words.pop(0).upper() for i in range(0, 6)]
                    )
                    eight_bytes = [
                        (eight_bytes >> 56) & 0xff,
                        (eight_bytes >> 48) & 0xff,
                        (eight_bytes >> 40) & 0xff,
                        (eight_bytes >> 32) & 0xff,
                        (eight_bytes >> 24) & 0xff,
                        (eight_bytes >> 16) & 0xff,
                        (eight_bytes >>  8) & 0xff,
                        (eight_bytes >>  0) & 0xff,
                    ]
                    sys.stdout.buffer.write(bytearray(eight_bytes))
                    num_bytes_left_to_output -= 8
                eight_bytes = eight_bytes_from_6_words(
                    [words.pop(0).upper() for i in range(0, 6)]
                )
                eight_bytes = [
                    (eight_bytes >> 56) & 0xff,
                    (eight_bytes >> 48) & 0xff,
                    (eight_bytes >> 40) & 0xff,
                    (eight_bytes >> 32) & 0xff,
                    (eight_bytes >> 24) & 0xff,
                    (eight_bytes >> 16) & 0xff,
                    (eight_bytes >>  8) & 0xff,
                    (eight_bytes >>  0) & 0xff,
                ]
                sys.stdout.buffer.write(
                    bytearray(eight_bytes[0:num_bytes_left_to_output])
                )
            else:
                for word in words:
                    sys.stdout.buffer.write(
                        bytearray([PGP_REVERSE_WORD_LIST[word.upper()]])
                    )
    else:
        with open(filename, "rb") as f:
            num_bytes = os.stat(filename).st_size
            if skeys_words:
                remainder = num_bytes % 8
                quotient = num_bytes // 8
                num_padding_bytes = (8 - remainder) % 8
                if num_padding_bytes > 0:
                    l.info(f"{num_bytes} = {quotient} * 8 + {remainder} bytes")
                    l.info(f"Padding with {num_padding_bytes} bytes")
                num_bytes_read = 0
                while num_bytes_read < quotient * 8:
                    eight_bytes = f.read(8)
                    l.info(f"eight_bytes: {eight_bytes}")
                    print(" ".join(six_words_from_8_bytes(int_from_8_bytes(eight_bytes))), end=" ")
                    num_bytes_read += 8
                if (num_padding_bytes > 0):
                    eight_bytes = f.read(8) + b'\x00' * num_padding_bytes
                    l.info(f"eight_bytes: {eight_bytes}")
                    print(
                        " ".join(six_words_from_8_bytes(int_from_8_bytes(
                            eight_bytes
                        ))),
                        end=" "
                    )
                print(f"{NUM_NAMES[num_padding_bytes]} PADD")
            else:
                # Hoping 1024 means don't need to worry about setting swap to True
                latest = f.read(1024)
                while latest != b'':
                    print(pgp_words_from_bytes(latest))
                    latest = f.read(1024)


if __name__ == "__main__":
    main()
