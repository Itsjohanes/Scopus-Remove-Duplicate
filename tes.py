def remove_duplicate_entries(input_file, output_file):
    entries = {}
    new_lines = []

    with open(input_file, 'r', encoding='utf-8') as file:
        current_entry = None
        for line in file:
            if line.startswith('@'):
                entry_start = line.find('{') + 1
                entry_end = line.find(',', entry_start)
                entry_key = line[entry_start:entry_end].strip()

                if entry_key not in entries:
                    entries[entry_key] = True
                    current_entry = entry_key
                    new_lines.append(line)
                else:
                    current_entry = None
            elif current_entry is not None:
                new_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    input_file_path = "C:/Users/acer/Downloads/duplikat/Gabungan.bib"  # Ganti dengan nama file .bib yang sesuai
    output_file_path = "C:/Users/acer/Downloads/duplikat/hapus.bib"  # Ganti dengan nama file .bib yang sesuai

    remove_duplicate_entries(input_file_path, output_file_path)
    print(f"File {output_file_path} berhasil dibuat tanpa duplikasi.")
