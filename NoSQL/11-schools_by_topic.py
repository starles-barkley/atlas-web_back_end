#!/usr/bin/env python3
""" Search by Topic Module
"""

from pymongo import MongoClient

client = MongoClient()


def schools_by_topic(mongo_collection, topic):
    """ Search by topic
    """
    res = []
    for doc in mongo_collection.find({'topics': topic}):
        res.append(doc)
    return res
