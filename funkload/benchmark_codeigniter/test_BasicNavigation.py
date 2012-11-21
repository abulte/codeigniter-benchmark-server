# -*- coding: iso-8859-15 -*-
"""basic_navigation FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
# from webunit.utility import Upload
# from funkload.utils import Data
from funkload.Lipsum import Lipsum
from funkload.utils import get_default_logger
#from funkload.utils import xmlrpc_get_credential

log = get_default_logger('console')

class BasicNavigation(FunkLoadTestCase):
    """XXX

    This test use a configuration file BasicNavigation.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_basic_navigation(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0001.request
        self.get(server_url + "/", description="Get /")
        self.assert_('Typography' in self.getBody(), "Home page loading failure")

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0042.request
        self.get(server_url + "/news", description="Get /news")
        self.assert_('List of news' in self.getBody(), "News list loading failure")
        # store the number of news
        # nb_news_before = len(self.listHref(content_pattern='View article'))

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0078.request
        self.get(server_url + "/news/create", description="Get /news/create")
        self.assert_('Create a news item' in self.getBody(), "News form loading failure")

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0097.request
        title = Lipsum().getSubject(uniq=True)
        self.post(server_url + "/news/create", params=[
            ['title', title],
            ['text', Lipsum().getParagraph()],
            ['submit', 'Create news item']],
            description="Post /news/create")
        self.assert_('Congrats' in self.getBody(), "News creation failure")

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0099.request
        self.get(server_url + "/news", description="Get /news")
        # do we have one more news ?
        news_links = self.listHref(content_pattern='View article')
        # nb_news_after = len(news_links)
        # self.assert_(nb_news_after == nb_news_before + 1, "New news not listed")

        # /var/folders/0n/nbbtwsqs6zl3z6k91czbkkvr0000gn/T/tmp6np8jv_funkload/watch0101.request
        last_news = news_links[-1]
        self.get(server_url + "/%s" % last_news, description="Get new news")
        # verifying that page exists is implicit

        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
