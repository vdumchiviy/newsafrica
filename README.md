# Task: Read  both *json* and *xml* files and select top 10 the most frequent words, in the news, with more then 6 letters.

### Features: resolved the situation when we have, for example, 5 words with length 10, 4 words with length 9 and 7 words with length 8. In that case the result will consist of 5 words with length 10, 4 words with length 9 and only one word with length 8 

#### Example of json file:
```json
{
  "rss": {
    "_xmlns:votpusk": "https://www.votpusk.ru/news.asp",
    "_version": "2.0",
    "channel": {
      "description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ",
      "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ",
      "items": [
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=544347",
          "_id": "544347",
          "pubDate": "Mon, 17 Oct 2016 00:28 +0300",
          "description": "Израильский турист погиб а еще трое получили ранения в результате автомобильной аварии в Йоханнесбурге Южная Африка Об этом сообщил 2 канал в воскресенье 16 октября Трагедия произошла когда автомобиль туристов стал участником ДТП а именно когда произошло лобовое столкновение Авария произошла всего через несколько дней после того как семья туристов в Грузии потеряла двух детей в автомобильной аварии MIGnews com",
          "link": "https://www.votpusk.ru/news.asp?msg=544347 ",
          "title": "Израильский турист погиб в ДТП в Африке"
        },
		...    
        ],
      "category": "Туризм - Африка",
      "language": "ru",
      "link": "https://www.votpusk.ru/news.asp",
      "title": "Новости Африка"
    }
  }
}
```

#### Example of xml file:
```xml
<?xml version='1.0' encoding='utf-8'?>
<rss version="2.0">
	<channel>
		<title>Новости Африка</title>
		<link>https://www.votpusk.ru/news.asp</link>
		<description>Африка - Лента туристических новостей портала В ОТПУСК.РУ </description>
		<language>ru</language>
		<category>Туризм - Африка</category>
		<lastBuildDate>Thu, 1 Dec 2016 17:27 +0300 </lastBuildDate>
		<item id="544347">
			<title>Израильский турист погиб в ДТП в Африке</title>
			<link>https://www.votpusk.ru/news.asp?msg=544347 </link>
			<description>Израильский турист погиб а еще трое получили ранения в результате автомобильной аварии в Йоханнесбурге Южная Африка Об этом сообщил 2 канал в воскресенье 16 октября Трагедия произошла когда автомобиль туристов стал участником ДТП а именно когда произошло лобовое столкновение Авария произошла всего через несколько дней после того как семья туристов в Грузии потеряла двух детей в автомобильной аварии MIGnews com</description>
			<pubDate>Mon, 17 Oct 2016 00:28 +0300</pubDate>
			<guid>https://www.votpusk.ru/news.asp?msg=544347</guid>
		</item>
		....
	</channel>
</rss>    
```