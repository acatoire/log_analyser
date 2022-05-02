"""
Simple rest server to expose your created files
"""
import statistics
from datetime import datetime
from os import listdir
from os.path import isfile, join

import logging

from config_log import Config

logging.basicConfig(level=logging.INFO)


def list_files(mypath):

    content = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    logging.debug(f"Possibles files:{content}")

    result_dict = {}

    with open(Config.FILE_LIST_PATH, mode='w', encoding='utf8') as result_file:

        result_file.write(" file_name, name, component_version, duration, date\n")
        start_line = ""
        end_line = ""

        for file_name in content:
            # Only scan ".log" files
            if not file_name.endswith(".log"):
                continue

            # Let get the party started
            complete_path = join(mypath, file_name)
            error = False

            with open(complete_path) as file:
                while line := file.readline():
                    line_content = (line.rstrip())

                    if Config.VERSION_PATTERN[0] in line_content:

                        line_split = clean_and_split(line_content, Config.VERSION_PATTERN[2])
                        component_version = line_split[Config.VERSION_PATTERN[1]]

                    if Config.NAME_PATTERN[0] in line_content:
                        line_split = clean_and_split(line_content, Config.NAME_PATTERN[2])
                        file_read_name = line_split[Config.NAME_PATTERN[1]]

                    if Config.START_PATTERN[0] in line_content:
                        start_line = line_content.split(" ")[0].strip("[]") + Config.START_PATTERN[1]

                    if Config.END_PATTERN[0] in line_content:
                        end_line = line_content.split(" ")[0].strip("[]") + Config.END_PATTERN[1]

                    if Config.ERROR_PATTERN in line_content:
                        error = True

            if error:
                logging.error(f"Error on file: {file_name}")
                duration = "error"
                duration_s = "error"
            else:
                deta_start = datetime.strptime(start_line, Config.TIME_DEF)
                date_end = datetime.strptime(end_line, Config.TIME_DEF)
                duration = date_end - deta_start
                duration_s = duration.seconds + round(duration.microseconds/1000000, 1)

            file_stat = f"{file_name}, {file_read_name}.json, {component_version}, {duration}, {start_line}"

            if Config.REF == component_version:
                duration_name = f"{file_read_name}.ref"
            elif Config.PATCHED == component_version:
                duration_name = f"{file_read_name}.patched"
            else:
                duration_name = f"{file_read_name}.unknown"

            try:
                result_dict[duration_name].append(duration_s)
            except KeyError:
                result_dict.update({duration_name: ([duration_s])})

            logging.debug(file_stat)
            result_file.write(file_stat + "\n")

    with open(Config.TIME_FILE_PATH, mode='w', encoding='utf8') as result_file:

        result_file.write("nb, mean, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n")

        for key in sorted(result_dict.keys()):
            time_list = result_dict[key]
            if "error" in time_list:
                mean_time = "error"
            else:
                mean_time = f"{statistics.mean(time_list):0.1f}"

            file_stat = f"{time_list.__len__():02d},{key},{mean_time},{time_list}"
            logging.info(file_stat)
            result_file.write(file_stat.replace("[", "").replace("]", "").replace("'", "") + "\n")


def clean_and_split(line_content, splitters):

    line_clean = line_content

    for letter in splitters:
        line_clean = line_clean.replace(letter, ' ')

    return line_clean.split(' ')


if __name__ == '__main__':
    list_files(Config.LOG_FOLDER_PATH)
