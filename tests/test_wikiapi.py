from analyze_wikiedits.wikiapi import MediaWiki
from unittest import TestCase

class TestMediaWiki(TestCase):

    def setUp(self):
        self.wiki = MediaWiki("http://en.wikipedia.org/w/api.php")

    def test___init__(self):
        for url in [ "", "abc", "http://de.wikibooks.org/" ]:
            self.assertEquals(MediaWiki(url).api_url, url)

    def test_api(self):
        params = { "action": "query", "meta": "siteinfo" }

        self.assertEquals(
            self.wiki.api(params)["query"]["general"]["sitename"],
            "Wikipedia"
        )

    def test_query(self):
        self.assertEquals(
            self.wiki.query({ "meta": "siteinfo" })["query"]["general"]["sitename"],
            "Wikipedia"
        )

    def test_query_list(self):
        r = self.wiki.query_list("allcategories", {})

        self.assertEquals(r["query"]["allcategories"][0]["*"], "!")

    def test_random_article_id(self):
        for i in range(5):
            article_id = self.wiki.random_article_id()
            props = self.wiki.query({
                "pageids": article_id,
                "prop": "info"
            })["query"]["pages"][str(article_id)]

            self.assertIn("touched", props)
            self.assertNotIn("missing", props)
            self.assertNotIn("redirect", props)
            self.assertEquals(props["ns"], 0)
