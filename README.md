# log_analyser

Simple log analyser to get timing info from files

## Description
This short script has been made to analyse a large quantity of logs from a recurring job to make a performance test.
It is used in case of you need re repeat a job treating one file a multiple of time and on multiple files:

You will pass to the script a folders of logs that contains timestamped execution lines.
And a configuration to be compliant to your log format.

## How to start

rename the "config_log_sample.py" into "config_log.py" and fill information inside depending on your project.

In the "config_log.py" file you can configure the definition of:
 - Start job line
 - End job line
 - Job name line
 - Job version line

The defined pattern will be searched in the file.
The time between Start and end will be saved and the version and job name will be used in the result file.

An extre error pattern can be given to detect errors.

