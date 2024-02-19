from Article import Article 

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def set_name(self, new_name):
        self._name = new_name

    def set_category(self, new_category):
        self._category = new_category

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.all_magazines:
            for article in magazine._articles:
                titles.append(article.title())
        return titles

    def contributing_authors(self):
        authors = []
        for article in self._articles:
            authors.append(article.author().name())
        return list(set(authors))

    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)

    @classmethod
    def all(cls):
        return cls.all_magazines
