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
