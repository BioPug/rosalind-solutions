from pathlib import Path

'''Read a text file and return its stripped content as a single string.'''
def read_text(file_path:str|Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

'''Read a text file and return a list of stripped non-empty lines.'''
def read_lines(file_path:str|Path) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

'''Read FASTA file and return a dictionary where keys are IDs and values are DNA sequences.'''
def read_fasta(file_path:str|Path) -> dict[str, str]:
    records: dict[str, str] = {}
    current_id = ''
    sequence: list[str] = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line1 = line.strip()
            if not line1:
                continue
            if line1[0] == '>':
                if current_id:
                    records[current_id] = "".join(sequence)
                current_id = line1[1:].strip()
                sequence = []
            else:
                sequence.append(line1)
        if current_id:
            records[current_id] = "".join(sequence)
    return records