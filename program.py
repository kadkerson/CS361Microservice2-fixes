import os
import time

DATABASE = "exampledatabase.txt" #enter database location
PIPELINE = "examplepipeline.txt" #enter location + file extension for pipleine.txt
SLEEP_INTERVAL = 2 #replace with number of seconds program should wait between checks



# functions, trying to split up to make modifying easier
# program is set up to not rely on structs or objects, just that data is requested to align with the communication contract



# easy reading and writing

def read_file(filepath):
    with open(filepath, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write_file(filepath, lines):
    with open(filepath, "w") as file:
        for line in lines:
            file.write(line + "\n")



# parsing objects

def parse_object(line):
    content = line[1:-1]
    parts = content.split(";")
    return parts



# formatting reply in same structure as request

def format_object(prop):
    return "{" + ";".join(str(p) for p in prop) + "}"



# database parsing and finding matches

def load_database(path=DATABASE):
    lines = read_file(path)
    return [parse_object(line) for line in lines if line.startswith("{")]

def find_matches(request_objects, database):
    matches = []
    for entry in database:
        match = True
        for a, field in enumerate(request_objects):
            if field == "":
                continue
            if a >= len(entry) or entry [a] != field:
                match = False
                break
        if match:
            matches.append(entry)
    return matches



# handle requests and replies

def check_request():
    lines = read_file(PIPELINE)
    if len(lines) < 2 or lines[0].lower() != "request":
        return None
    obj_line = lines[1]
    return parse_object(obj_line)

def write_reply(objects):
    output_lines = ["reply"]
    output_lines += [format_object(obj) for obj in objects]
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