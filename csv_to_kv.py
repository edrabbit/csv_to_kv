__author__ = "Ed Hunsinger"
__copyright__ = "Copyright 2013"
__email__ = "edrabbit@edrabbit.com"

import csv
import sys

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print '''
Usage: %s [csv_file] [output_file] [datetime_output_format] [datetime_input_fields]
  datetime_output_format is a string in sprintf format
  datetime_input_fields is a csv of the fields to pass to datetime_output_format
  If datetime_output_format and datetime_input_fields are not provided, we default to looking for a field named "timestamp"

  Ex. if you have the MONTH, DAY, YEAR, TIME in your data and you want a ISO8601 formatted datetime (YYYYMMDDT00:00:00) pass:
    csv_to_kv.py csv_file.csv output.log "%s%s%sT%s" "YEAR,MONTH,DAY,TIME"
'''
        exit(1)
    csv_file = sys.argv[1]
    output_file = sys.argv[2]
    if (len(sys.argv) < 5):
        datetime_default = True
        datetime_format = '%s'
        default_timestamp_field = 'timestamp'
        datetime_fields = (default_timestamp_field,)
    else:
        datetime_default = False
        datetime_format = sys.argv[3]
        datetime_fields = sys.argv[4]

    of = open(output_file, 'w')
    reader = csv.DictReader(open(csv_file))
    for row in reader:
        if datetime_default:
            try:
                row[default_timestamp_field]
            except KeyError:
                exit('Failed to find a field named %s in data'
                     % default_timestamp_field)
        timestamp = (datetime_format
                     % tuple([row[x] for x in datetime_fields.split(',')]))
        line = timestamp
        for k, v in row.items():
            line = '%s, %s="%s"' % (line, k, v)
        of.write('%s\n' % line)
        print line
    of.close()
