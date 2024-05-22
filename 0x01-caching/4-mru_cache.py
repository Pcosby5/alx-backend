#!/usr/bin/env python3
"""Defines the MRUCache class."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching and
    implements a caching system using MRU algorithm."""

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using MRU algorithm.

        Args:
            key: The key for the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item (MRU)
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
            if key in self.cache_data:
                # Move the key to the end of the cache_data
                # dictionary to indicate it's the most recently used
                self.cache_data[key] = self.cache_data.pop(key)
                return self.cache_data[key]
        return None
