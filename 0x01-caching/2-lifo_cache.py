#!/usr/bin/env python3
"""Defines the LIFOCache class."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and
    implements a caching system using LIFO algorithm."""

    def __init__(self):
        """Initialize the LIFOCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using LIFO algorithm.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the last item put in cache (LIFO)
                discarded_key = next(reversed(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
