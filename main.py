import json
import xml.etree.ElementTree as ET


def add_word_to_dict(word, dict):
    if len(word) >= 6:
        try:
            dict[word] += 1
        except KeyError:
            dict[word] = 1
    # print(dict)


def get_top_words(words, current_size, result_top_words, words_left):
    result = words_left
    for key, value in words.items():
        if value == current_size:
            result -= 1
            result_top_words.append(key)
        if result == 0:
            break

    return result


def words_to_top(words, top_words_count):
    result = list()
    top_digits = set()
    for key, value in words.items():
        # print(key, value)
        top_digits.add(value)
    top_digits = sorted(top_digits, reverse=True)

    for size in top_digits:
        top_words_count = get_top_words(
            words, size, result, top_words_count)
        if top_words_count == 0:
            break

    return result


def main_json():
    all_need_words = dict()
    result = list()
    top_words_count = 10

    with open("files/newsafr.json", "r", encoding="utf-8") as json_file:
        news_text = json_file.read()
        news = json.loads(news_text)

    for item in news["rss"]["channel"]["items"]:
        for word in item["description"].lower().split():
            add_word_to_dict(word, all_need_words)

    result = words_to_top(all_need_words, top_words_count)

    print(f"JSON: {result}")


def main_xml():
    all_need_words = dict()
    result = list()
    top_words_count = 10

    root = ET.parse("files/newsafr.xml",
                    ET.XMLParser(encoding="utf-8")).getroot()
    for items in root.findall("channel/item/description"):

        item = items.text.lower()
        for word in item.split():
            add_word_to_dict(word, all_need_words)

    result = words_to_top(all_need_words, top_words_count)

    print(f"XML: {result}")


main_json()
main_xml()
