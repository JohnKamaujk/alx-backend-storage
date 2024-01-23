#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    # Total number of logs
    total_logs = mongo_collection.count_documents({})

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_stats = {method: mongo_collection.count_documents
                     ({"method": method}) for method in methods}

    # Number of logs with method=GET and path=/status
    status_check_count = mongo_collection.count_documents
    ({"method": "GET", "path": "/status"})

    # Display results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_stats[method]}")
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    log_stats(nginx_collection)
