#!/usr/bin/env python3
"""Validate CITATION.cff against the pinned official CFF 1.2.0 schema.

Requires PyYAML and jsonschema. Supply --schema for an offline run, or explicitly
use --download-schema to fetch the schema with its expected SHA-256 digest.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

import jsonschema
import yaml

SCHEMA_URL = "https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json"
SCHEMA_SHA256 = "0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b"
ROOT = Path(__file__).resolve().parent.parent

parser = argparse.ArgumentParser(description=__doc__)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--schema", type=Path)
group.add_argument("--download-schema", action="store_true")
args = parser.parse_args()
data = urlopen(SCHEMA_URL, timeout=30).read() if args.download_schema else args.schema.read_bytes()
if hashlib.sha256(data).hexdigest() != SCHEMA_SHA256:
    raise SystemExit("CFF schema digest differs from the reviewed official 1.2.0 schema")
schema = json.loads(data)
citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))

def string_dates(value):
    if isinstance(value, dict):
        return {key: string_dates(child) for key, child in value.items()}
    if isinstance(value, list):
        return [string_dates(child) for child in value]
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    return value

jsonschema.Draft7Validator.check_schema(schema)
jsonschema.Draft7Validator(schema, format_checker=jsonschema.FormatChecker()).validate(string_dates(citation))
print("PASS: CITATION.cff validates against the official CFF 1.2.0 schema (SHA-256 pinned)")
