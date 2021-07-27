from django.core.management.base import BaseCommand, CommandError

from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from hashlib import sha1

import json
import sys

from django.conf import settings


class Command(BaseCommand):
    help = "Downloads all external static dependencies from the given json file."

    def add_arguments(self, parser):
        parser.add_argument("filename", type=str, help="Path to the dependency file.")

    def error(reason):
        self.stderr.write(self.style.ERROR(reason))
        sys.exit(1)

    def handle(self, *args, **options):
        filename = options["filename"]
        try:
            with open(filename, "r") as f:
                dependencies = json.loads(f.read())
        except FileNotFoundError:
            self.error("The given file is missing.")
        except json.JSONDecodeError:
            self.error("The given file is malformed.")

        for dependency in dependencies:
            # Check for unused/missing keys
            if set(["destination", "shasum", "url", "name"]) != set(dependency.keys()):
                self.error(
                    "The keys of the dependency don't match `destination, shasum, url,"
                    " name`."
                )

            path = str(settings.APPS_DIR / dependency["destination"])

            # Download
            response = urlopen(dependency["url"])
            f = BytesIO(response.read())

            # Sanity check the shasum of the file
            calculated = sha1(f.read())
            f.seek(0)
            if calculated.hexdigest() != dependency["shasum"]:
                self.error("The shasum of the downloaded file does not match.")

            # Load as zipfile and extract
            zipfile = ZipFile(f)

            # Extract all subfolders without the creating the topmost parent directory
            for info in zipfile.filelist:
                info.filename = info.filename.split("/", 1)[1]
                if info.filename:
                    zipfile.extract(info, path)

        self.stdout.write(self.style.SUCCESS("Successfully downloaded dependencies."))
