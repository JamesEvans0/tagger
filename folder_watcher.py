from threading import Thread
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def watch_folder():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = '/home/siddhant/team-guardian/tagger'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    folder_watcher = Thread(target = watch_folder)
    folder_watcher.daemon = True
    folder_watcher.start()
    try:
        while True:
            print 'here'
            time.sleep(1)
    except KeyboardInterrupt:
        print "Goodbye!"