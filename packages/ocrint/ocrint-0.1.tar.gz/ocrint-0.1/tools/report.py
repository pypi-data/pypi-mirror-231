


def create_file(filename, content):
    print(f'Création du fichier {filename}...')
    content = content.replace('\r', '') \
        .replace('\n', '') \
        .replace('\t', '') \
        .replace('  ', '') \
        .replace('   ', '') \
        .replace('    ', '')
    with open(filename, 'w') as f:
        f.write(content)
    return True


def report_json(parent_path, data):
    import json
    import os
    import datetime
    report_file_name = f'report{datetime.time}.json'

    path = parent_path + '/' + report_file_name
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    return True
