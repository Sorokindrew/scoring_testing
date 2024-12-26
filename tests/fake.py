class FakeStore:
    received_cached = 0
    def __init__(self, cached_data, data):
        self.data = data
        self.cached_data = cached_data

    def get(self, key):
        return self.data.get(key)

    def cache_get(self, key):
        if self.cached_data.get(key):
            FakeStore.received_cached += 1
        return self.cached_data.get(key)

    def cache_set(self, key, value, time):
        self.cached_data[key] = value