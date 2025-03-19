BOT_NAME = "ADCB_UAE"
SPIDER_MODULES = ["ADCB_UAE.spiders"]
NEWSPIDER_MODULE = "ADCB_UAE.spiders"
#USER_AGENT = "ADCB_UAE (+http://www.yourdomain.com)"
ROBOTSTXT_OBEY = False
#CONCURRENT_REQUESTS = 32
#DOWNLOAD_DELAY = 3
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
#COOKIES_ENABLED = False
#TELNETCONSOLE_ENABLED = False
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q = 0.9,*/*;q=0.8",
#SPIDER_MIDDLEWARES = {
#DOWNLOADER_MIDDLEWARES = {
#EXTENSIONS = {
#ITEM_PIPELINES = {
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
CONCURRENT_REQUESTS = 3
DOWNLOAD_DELAY = 2

# Custom pipeline
ITEM_PIPELINES = {
    "ADCB_UAE.pipelines.JsonWriterPipeline": 1,
}
AUTOTHROTTLE_ENABLED = True