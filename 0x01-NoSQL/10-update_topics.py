#!/usr/bin/env python3
""" 10-module update topics module """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document """
    mongo_collection.update_many(
        {name: name},
        {"$set": {topics: topics}}
    )
