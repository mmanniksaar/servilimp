# storage.py
from whitenoise.storage import CompressedManifestStaticFilesStorage
from whitenoise.storage import MissingFileError

class NonStrictCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False

    def post_process(self, paths, dry_run=False, **options):
        # Kogu post_process'i tulemus
        processed_files = super().post_process(paths, dry_run, **options)
        # Kui ükski töötlus osas MissingFileError tõstatati, ignoreeri seda
        # Võite proovida konverteerida generatori selliseks, mis püüab erindeid
        # Järgnev lahendus on lihtsustatud: püüame läbi iteratsiooni ja ignoreerime MissingFileError'e
        def safe_processor():
            for item in processed_files:
                try:
                    yield item
                except MissingFileError as e:
                    # Logige hoiatuseks, mitte visake erandit
                    print("WARNING: Missing static file during post_process:", e)
                    continue
        return safe_processor()
