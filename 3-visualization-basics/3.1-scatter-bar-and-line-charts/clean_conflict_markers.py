import json

def clean_conflict_markers(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # Clean the conflict markers
    clean_content = []
    in_conflict = False
    for line in content:
        if '<<<<<<<' in line:
            in_conflict = True
        elif '=======' in line:
            in_conflict = False
        elif '>>>>>>>' in line:
            in_conflict = False
        else:
            if not in_conflict:
                clean_content.append(line)

    # Try to parse the cleaned content as JSON
    try:
        json_content = ''.join(clean_content)
        json.loads(json_content)
        print("JSON structure is valid.")
        # Write the cleaned content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_content)
    except json.JSONDecodeError as e:
        print("JSON structure is still invalid:", e)

# Path to the notebook file
notebook_file = '3.1-scatter-bar-and-line-charts.ipynb'
clean_conflict_markers(notebook_file)
