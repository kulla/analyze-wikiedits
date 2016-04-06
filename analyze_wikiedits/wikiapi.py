"""This module contains classes for accessing articles and properties of a
MediaWiki via its API. See https://www.mediawiki.org/wiki/API:Main_page for a
documentation about this API.
"""

# Copyright (C) 2016 Stephan Kulla
#
# This file is part of "Analyze Wikiedits".
#
# "Analyze Wikiedits" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Analyze Wikiedits" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Analyze Wikiedits". If not, see <http://www.gnu.org/licenses/>.

class MediaWiki(object):
    """Basic class for accessing articles and properties of a MediaWiki."""

    def __init__(self, api_url):
        """Initialize the object.

        Arguments:

            api_url - URL to the `api.php` file of the MediaWiki
                      e.g. "https://en.wikipedia.org/w/api.php"
        """
        self.api_url = api_url
