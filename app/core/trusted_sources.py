# app/core/trusted_sources.py

import os
import yaml
from app.models.source_item import SourceItem  # if you split it out
from ....trusted_sources.trusted_sources.new_zealand import *
class TrustedSourceLoader:
    @staticmethod
    def load(country: str, category: str):
        base_path = "..../trusted_sources/trusted_sources/new_zealand"  # Adjust this path as needed
        path = os.path.join(base_path, country, f"{category}.yaml")
        if not os.path.exists(path):
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return [SourceItem(**item) for item in data]
