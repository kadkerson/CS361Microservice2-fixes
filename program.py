import os
import time
import json

DATABASE = "exampledatabase.txt"        # enter database location
PIPELINE = "examplepipeline.txt"        # enter location + file extension for pipeline.txt
SLEEP_INTERVAL = 2                      # replace with number of seconds program should wait between checks



def read_file(filepath):
    """
    Read a text file and return a list of non-empty lines.
    """
    with open(filepath, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write_file(filepath, lines):
    """
    Write a list of strings to a text file.
    """
    with open(filepath, "w") as file:
        for line in lines:
            file.write(line + "\n")


def parse_object(line):
    """
    Convert a JSON string (from the database or pipeline) into a Python object.
    Used to turn request objects and stored database entries into a format the service can work with.
    """
    return json.loads(line)


def format_json_object(obj):
    """
    Convert a Python object to a JSON string for storage in the database/pipeline.
    """
    return json.dumps(obj)


def load_database(path=DATABASE):
    """
    Load JSON entries from the database file into a list of Python objects.
    """
    lines = read_file(path)
    return [parse_object(line) for line in lines if line.startswith("{")]


def find_matches(request_objects, database):
    """
    Find all database entries that match the non-empty fields in the request object.
    """
    matches = []
    for entry in database:
        match = True
        for field, value in request_objects.items():
            if value == "":
                continue
            if field not in entry or entry[field] != value:
                match = False
                break
        if match:
            matches.append(entry)
    return matches


def check_request():
    """
    Read the pipeline file and return a request object if a valid request is present,
    otherwise return None.
    """
    lines = read_file(PIPELINE)
    if len(lines) < 2 or lines[0].lower() != "request":
        return None
    obj_line = parse_object(lines[1])
    return obj_line if isinstance(obj_line, dict) else None


def write_reply(objects):
    """
    Write a reply header and all matching objects back to the pipeline file.
    """
    output_lines = ["reply"]
    for obj in objects:
        output_lines.append(format_json_object(obj))
    write_file(PIPELINE, output_lines)



# main
def main():

    while True:
        request_objects = check_request()
        if request_objects:
            db = load_database()
            matches = find_matches(request_objects, db)
            write_reply(matches)
        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__": main()