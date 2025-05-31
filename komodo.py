import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

watch_files = [
    ""
]

python_env_folder = ""

class MultipleFilesHandler(FileSystemEventHandler):
    """Handles changes only for specific files."""

    def on_modified(self, event):
        if event.src_path in watch_files:  # Only act if the file is in the list
            filename = os.path.basename(event.src_path)
            destination = os.path.join(python_env_folder, filename)

            shutil.copy2(event.src_path, destination)
            print(f"Copied: {event.src_path} -> {destination}")

# Set up the observer
observer = Observer()
event_handler = MultipleFilesHandler()

# Watch the parent directories of all the files (without duplicates)
WATCH_DIRECTORIES = set(os.path.dirname(file) for file in watch_files)

for directory in WATCH_DIRECTORIES:
    observer.schedule(event_handler, directory, recursive=False)

# Start watching
print(f"Watching for changes in: {watch_files}")
observer.start()

try:
    while True:
        pass  # Keep script running
except KeyboardInterrupt:
    observer.stop()
observer.join()