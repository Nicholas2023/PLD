#!/usr/bin/python3
"""
A module that makes models a package
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call the reload() method on the storage instance
storage.reload()
