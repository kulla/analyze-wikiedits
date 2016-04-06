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

    def __init__(self, url):
        """ Initialize the object.

        Params:

        url - URL to the wiki like "https://en.wikipedia.org/"
        """
        self.url = url
