numbers=[
    1000,1000000,
        5,36,584,2023,2022,2020,2050,1991,2785,2654,1547,1364,874,695,276,100000000
]
from num2words import num2words

with open("arabic_text.txt", "a") as file:
    for number in numbers:
        arabic_text = num2words(number, lang='ar')
        file.write(f"{number}:{arabic_text}"+"\n")

