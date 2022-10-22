from search.spiders.sweetwater import SweetwaterSpider
# from search.spiders.thomann import ThomannSpider
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings



def run():

    settings = get_project_settings()
    configure_logging()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(SweetwaterSpider)
        # yield runner.crawl(ThomannSpider)
        reactor.stop()

    crawl()
    reactor.run() 




if __name__ == '__main__':
    run()
