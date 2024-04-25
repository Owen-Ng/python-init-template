from model.lru_cache import Lru_cache
class UrlController:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = Lru_cache(self.cache_size)
    def DownloadOrInCacheURL(self, url):
        # check if in cache
        response = self.cache.get(url)
        if response != "":
            return response[0] + " IN_CACHE " + str(response[2])
        # Not in cache so need to add the new url
        response = self.cache.insert(url)
        return response[0] + " DOWNLOADED " + str(response[2])


        