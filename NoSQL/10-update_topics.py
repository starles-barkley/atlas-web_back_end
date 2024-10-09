#!/usr/bin/env python3
""" update_topics Module
"""

from pymongo import MongoClient

client = MongoClient()


def update_topics(mongo_collection, name, topics):
    """ Updates topics in document based on name
    """
    mongo_collection.update_one({'name': name}, {'$addToSet': {'topics': topics}})
