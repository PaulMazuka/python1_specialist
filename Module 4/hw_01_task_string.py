# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "Повседневная практика показывает, " \
       "что рамки и место обучения кадров представляет собой интересный эксперимент " \
       " проверки экономической целесообразности принимаемых решений." \
       "Значимость этих проблем настолько очевидна, что реализация намеченного плана развития обеспечивает " \
       "актуальность ." \
       "экономической целесообразности принимаемых решений. Равным образом консультация с профессионалами из IT в " \
       "значительной" \
       " степени обуславливает создание системы обучения кадров, соответствующей насущным потребностям?"
blow = 0
comma = 0
for letter in text:
    if letter == ",":
        comma += 1
    elif letter == ".":
        blow += 1

print("comma= ", comma, "blow=: ", blow)
if blow == comma:
    print("запятых и точек одинаково")


#  либо через метод строки .count
