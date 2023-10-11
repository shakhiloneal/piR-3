"""
A module that contains some 2D arrays with data.
The first row is always a header.
"""

grades = [
["Grade Code", "Grade",      "Family Grade",               "Lower Mark", "Upper Mark"],
["HD",   "High Distinction", "Hardly Decent",              "80",           "100"],
["D",    "Distinction",      "Disappointing",              "70",           "79"],
["C",    "Credit",           "Catastrophic",               "60",           "69"],
["P",    "Pass",             "Permanent failure",          "50",           "59"],
["N",    "Fail",             "Never show your face again", "0",            "49"],
]

#names generated with https://www.behindthename.com/random/
class_students = [\
["Student ID", "First Name", "Last Name", "Grade Code"],
["798154", "Brynhildr", "Blakeley", "N"],
["134789", "Felix", "Li", "N"],
["798951", "Paityn", "Summers", "P"],
["465120", "Turnus", "Elliot", "C"],
["963245", "Alysia", "Jervis", "D"],
["469120", "Muhammad", "Saad", "HD"],
]

rabbytes_club_students = [\
["First Name", "Joining year", "Rabbit"],
["Brynhildr", "2022", "Rabbit_1"],
["Turnus", "2023", "Rabbit_2"],
["Jamaluddin", "2022", "Rabbit_5"],
]

rabbytes_data = [\
["Rabbit", "Birth year", "Favorite treat"],
["Rabbit_1", "2022", "Carrots"],
["Rabbit_2", "2023", "Celery"],
["Rabbit_3", "2023", "Broccoli"],
["Rabbit_4", "2024", "Cabbage"],
["Rabbit_5", "2022", "Lettuce"],
]

tables = [grades, class_students, rabbytes_club_students, rabbytes_data]

