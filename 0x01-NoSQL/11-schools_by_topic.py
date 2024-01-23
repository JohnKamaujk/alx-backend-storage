#!/usr/bin/env python3
""" 11-schools by topics module"""


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic."""
    documents = mongo_collection.find(
        {{"topics": {"$in": [topic]}}},
    )
    return list(documents)
