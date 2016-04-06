from analyze_wikiedits.wikiapi import MediaWiki
from unittest import TestCase

class TestMediaWiki(TestCase):

    def test___init__(self):
        for url in [ "", "abc", "http://de.wikibooks.org/" ]:
            self.assertEquals(MediaWiki(url).api_url, url)
