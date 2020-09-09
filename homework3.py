text_tolstoy = '''Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему.
Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. 
Положение это продолжалось уже третий день и мучительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и домочадцы чувствовали, 
что нет смысла в их сожительстве и что на каждом постоялом дворе случайно сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. 
Жена не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потерянные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей новое место; 
повар ушел вчера со двора, во время самого обеда; черная кухарка и кучер просили расчета.
На третий день после ссоры князь Степан Аркадьич Облонский — Стива, как его звали в свете, — в обычный час, то есть в восемь часов утра, проснулся не в спальне жены, 
а в своем кабинете, на сафьянном диване. Он повернул свое полное, выхоленное тело на пружинах дивана, как бы желая опять заснуть надолго, с другой стороны крепко обнял подушку и прижался к ней щекой; но вдруг вскочил, сел на диван и открыл глаза.
«Да, да, как это было? — думал он, вспоминая сон. — Да, как это было? Да! Алабин давал обед в Дармштадте; нет, не в Дармштадте, а что-то американское. Да, но там Дармштадт был в Америке. 
Да, Алабин давал обед на стеклянных столах, да, — и столы пели: Il mio tesoro 1 и не Il mio tesoro, а что-то лучше, и какие-то маленькие графинчики, и они же женщины», — вспоминал он.
Глаза Степана Аркадьича весело заблестели, и он задумался, улыбаясь. «Да, хорошо было, очень хорошо. Много еще что-то там было отличного, да не скажешь словами и мыслями даже наяву не выразишь».
И, заметив полосу света, пробившуюся сбоку одной из суконных стор, он весело скинул ноги с дивана, отыскал ими шитые женой (подарок ко дню рождения в прошлом году), обделанные в золотистый сафьян туфли, 
и по старой, девятилетней привычке, не вставая, потянулся рукой к тому месту, где в спальне у него висел халат. И тут он вспомнил вдруг, как и почему он спит не в спальне жены, а в кабинете; улыбка исчезла с его лица, он сморщил лоб.
«Ах, ах, ах! Ааа!..» — замычал он, вспоминая все, что было. И его воображению представились опять все подробности ссоры с женою, вся безвыходность его положения и мучительнее всего собственная вина его.
«Да! она не простит и не может простить. И всего ужаснее то, что виной всему я, виной я, а не виноват. В этом-то вся драма, — думал он. — Ах, ах, ах!» — приговаривал он с отчаянием, вспоминая самые тяжелые для себя впечатления из этой ссоры.
Неприятнее всего была та первая минута, когда он, вернувшись из театра, веселый и довольный, с огромною грушей для жены в руке, не нашел жены в гостиной; к удивлению, не нашел ее и в кабинете и, наконец, увидал ее в спальне с несчастною, открывшею все, запиской в руке.
Она, эта вечно озабоченная, и хлопотливая, и недалекая, какою он считал ее, Долли, неподвижно сидела с запиской в руке и с выражением ужаса, отчаяния и гнева смотрела на него.
— Что это? это? — спрашивала она, указывая на записку.
И при этом воспоминании, как это часто бывает, мучало Степана Аркадьича не столько самое событие, сколько то, как он ответил на эти слова жены.
С ним случилось в эту минуту то, что случается с людьми, когда они неожиданно уличены в чем-нибудь слишком постыдном. Он не сумел приготовить свое лицо к тому положению, в которое он становился перед женой после открытия его вины. Вместо того чтоб оскорбиться, отрекаться, оправдываться, просить прощения, оставаться даже равнодушным — все было бы лучше того, что он сделал! — его лицо совершенно невольно («рефлексы головного мозга», — подумал Степан Аркадьич, который любил физиологию), совершенно невольно вдруг улыбнулось привычною, доброю и потому глупою улыбкой.
Эту глупую улыбку он не мог простить себе. Увидав эту улыбку, Долли вздрогнула, как от физической боли, разразилась, со свойственною ей горячностью, потоком жестоких слов и выбежала из комнаты. С тех пор она не хотела видеть мужа.'''

#1. Методом строк очистить текст от знаков препинания

print('Задание 1')

mark = '.,:;?!—«»()'
for i in mark:
        text_tolstoy = text_tolstoy.replace(i, ' ')

print(text_tolstoy)

# Сформировать list со словами (split)

print('Задание 2')

text_list = text_tolstoy.split()
print(text_list)

# Привести все слова к нижнему регистру (map)
# PRO. Выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.

print('Задание 3')

text_tolstoy_lower = list(map(lambda x: x.lower(), text_list))
print(text_tolstoy_lower)

#PRO

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

tolstoy_lemm = []
for i in text_tolstoy_lower:
    tolstoy_lemm.append(morph.parse(i)[0].normal_form)
print(tolstoy_lemm)

# Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

print('Задание 4')

text_tolstoy_dict = {a: text_tolstoy_lower.count(a) for a in text_tolstoy_lower}
print(text_tolstoy_dict)

# Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)

print('Задание 5')

popword = list(text_tolstoy_dict.items())
popword.sort(key=lambda i:i[1], reverse=True)
print(popword[:5])

various_words = set(text_tolstoy_lower)
print("Разных слов в тексте - ", len(various_words))