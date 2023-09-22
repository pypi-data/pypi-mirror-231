from importer import RetractionWatch


def main():
    rw = RetractionWatch()
    rw.import_retraction_watch_data(instrumentation=None)
    rw.pull_crossmark(instrumentation=None)


if __name__ == "__main__":
    main()
