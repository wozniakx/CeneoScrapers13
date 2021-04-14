# CeneoScrapers13
# Etap1 Ekstrakcja pojedynczej opinii o produkcie
- pobranie kodu pojedynczej strony z opiniami o produkcie
- wydobycie z kodu strony fragmentu odpowiadajaego pojedynczej opinii
- zapisanie do pojedyncych zmiennych wartosci skladowych opinii
- obsluga bledow
- transformacja danych do docelowych typow

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|bs4.element.Tag|
|Identyfikator opinii|["data-entry-id"]|opinionId|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|rcmd|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista zalet|div[class*="positives"] ~ div.review-feature__item|pros|list|
|Lista wad|div[class*="negatives"] ~ div.review-feature__item|cons|list|
|Czy potwierdzona zakupem|div.review-pz|purasched|bool|
|Data wystawienia|span.user-post__published > time:nth-child(1)["datetime"]|publishDate|str|
|Data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchaseDate|str|
|Dla ilu osob przydatna|span[id^="votes-yes"]|useful|int|
|Dla ilu osob nieprzydanta|span[id^="votes-no"]|useless|int|

## Etap 2 Ekstrakcja wszystkich opinii o produkcie