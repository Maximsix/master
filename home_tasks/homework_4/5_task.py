import re

text = """Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так.
Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад.
Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе.
В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году н.э.
Этот трактат по теории этики был очень популярен в эпоху Возрождения.
Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32!"""
sentences = re.split(r"\.[\s{2,10}\n\t]\.", text)
sentence_list = []
#
for sentence_index in sentences:
     for x in sentence_index.split('\n'):
          sentence_list.append(x)
          print(f"<{x}>")
print(sentence_list)
# Interesting solution.  But take a look how it could be done in 1 line of code
# sentences = re.findall("[А-Я].*?[.!](?=\n|$)", text)
# for sentence in sentences:
#      print(f"<{sentence}>")
