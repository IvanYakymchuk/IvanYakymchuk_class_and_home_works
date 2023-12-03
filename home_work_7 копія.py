import os
import zipfile

def create_multivolume_archive(source_dir, archive_name, max_size):
    full_archive_path = os.path.join(source_dir, archive_name + '.zip')
    with zipfile.ZipFile(full_archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))


    archive_parts = []
    with zipfile.ZipFile(full_archive_path, 'r') as zipf:
        current_part = 1
        part_size = 0
        part_name = f"{archive_name}_{current_part:04d}.zip"
        for file_info in zipf.infolist():
            if part_size + file_info.file_size > max_size:
                current_part += 1
                part_name = f"{archive_name}_{current_part:04d}.zip"
                part_size = 0
                archive_parts.append(part_name)
            part_size += file_info.file_size
            with open(part_name, 'ab') as part_file:
                part_file.write(zipf.read(file_info.filename))
    return archive_parts

def merge_multivolume_archive(parts_directory, output_dir, output_name):
    merged_archive_path = os.path.join(output_dir, output_name + '.zip')
    with zipfile.ZipFile(merged_archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(parts_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, parts_directory))


    with zipfile.ZipFile(merged_archive_path, 'r') as zipf:
        zipf.extractall(output_dir)



