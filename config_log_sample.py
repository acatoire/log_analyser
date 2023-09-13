# Rename this file to config_log.py and use it.
# Exclude the new file from git if security is needed

class Config:

    # Path definitions
    # # Input folder where raw logs files ares stored, extension MUST be ".log"
    LOG_FOLDER_PATH = "C:/my/log/folder"
    # # Output file path where scan result will be stored
    TIME_FILE_PATH = "tmp/times.csv"
    FILE_LIST_PATH = "tmp/files.csv"

    # Lines definition
    # #Log timestamp string definition
    TIME_DEF = '%Y-%m-%dT%H:%M:%S,%f'
    # # Start/Stop definition as a tuple: ("text to find", "text to add at the end to correct the timing")
    # # The second parameter is used to correct 1/10s into milliseconds in some cases
    START_PATTERN = ("text to define start", "000")
    END_PATTERN = ("text to define end", "000")
    # # Job definition as tuple: ("text", id on split, extra split char as list)
    # # The second parameter is the id on the spaces splited line
    # # The third parameter the extra char to split (default empty)
    NAME_PATTERN = ("text with name", 12, ["/"])
    COMPONENT_VERSION_PATTERN = ("text for version", 15, ["/", "\\"])
    TCK_VERSION_PATERN = ("ComponentManager version:", -1, '')
    # # Error detection definition
    ERROR_PATTERN = "error text"

    # File qualification
    # # A file can be ref/patched/unknown, qualification will be added to the file name in the final csv
    # # If the REF text is found on any log line, the file will be qualified as "reference"
    # # If the PATCHED text is found on any log line, the file will be qualified as "patched"
    # # else the file will be qualified as "unknown"
    # # REMARQUE: PATCHED and REF must be exclusive to each other
    PATCHED = "patvch name"
    REF = "ref name"