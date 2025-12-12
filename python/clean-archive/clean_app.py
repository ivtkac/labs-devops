import sys
import os
import shutil
import zipfile
import tempfile
import logging
from pathlib import Path
from typing import Set

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def find_folders_to_remove(root_path: Path) -> Set[str]:
    folders_to_remove = set()

    for dirpath, dirnames, filenames in os.walk(root_path):
        rel_path = Path(dirpath).relative_to(root_path)

        if str(rel_path) == '.':
            continue

        if '__init__.py' not in filenames:
            folders_to_remove.add(str(rel_path))
            logger.debug(f"Marked for removal: {rel_path}")

            dirnames.clear()

    return folders_to_remove


def remove_folders(root_path: Path, folders_to_remove: Set[str]) -> None:
    for folder in folders_to_remove:
        folder_path = root_path / folder
        if folder_path.exists():
            shutil.rmtree(folder_path)
            logger.info(f"Removed folder: {folder}")


def create_cleaned_txt(root_path: Path, folders_to_remove: Set[str]) -> None:
    cleaned_file = root_path / 'cleaned.txt'
    sorted_folders = sorted(folders_to_remove)

    with open(cleaned_file, 'w') as f:
        for folder in sorted_folders:
            f.write(f"{folder}\n")

    logger.info(f"Created cleaned.txt with {len(sorted_folders)} entries")


def create_zip_archive(source_dir: Path, output_zip: Path) -> None:
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(source_dir)
                zipf.write(file_path, arcname)
                logger.debug(f"Added to archive: {arcname}")

    logger.info(f"Created new archive: {output_zip}")


def clean_archive(zip_file_path: str) -> None:
    zip_path = Path(zip_file_path)

    if not zip_path.exists():
        logger.error(f"File not found: {zip_file_path}")
        sys.exit(1)

    if not zipfile.is_zipfile(zip_path):
        logger.error(f"Not a valid zip file: {zip_file_path}")
        sys.exit(1)

    logger.info(f"Processing archive: {zip_path.name}")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        logger.info(f"Created temporary directory: {temp_dir}")

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(temp_path)
            logger.info("Extracted archive to temporary directory")

        folders_to_remove = find_folders_to_remove(temp_path)
        logger.info(f"Found {len(folders_to_remove)} folders to remove")

        remove_folders(temp_path, folders_to_remove)

        create_cleaned_txt(temp_path, folders_to_remove)

        output_name = zip_path.stem + '_new.zip'
        output_path = zip_path.parent / output_name
        create_zip_archive(temp_path, output_path)

        logger.info(f"Successfully created cleaned archive: {output_path}")


def main():
    """
    Entry point of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python clean_app.py <zip-file-name>")
        sys.exit(1)

    zip_file = sys.argv[1]

    try:
        clean_archive(zip_file)
        logger.info("Archive cleaning completed successfully")
    except Exception as e:
        logger.error(f"Error during archive cleaning: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()