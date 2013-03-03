#csv_to_kv

So you've got a csv that you want to turn into a log file.
Perhaps you want to upload it to [Splunk Storm](http://www.splunkstorm.com) which is configured to look for a
nice timestamp at the beginning of each line by default, oh and you want
key/value pairs for easier human reading.

Use this to convert that csv.

```
Usage: %s [csv_file] [output_file] [datetime_output_format] [datetime_input_fields]
```
datetime_output_format is a string in sprintf format
datetime_input_fields is a csv of the fields to pass to datetime_output_format
If datetime_output_format and datetime_input_fields are not provided, we default to looking for a field named "timestamp"

Ex. if you have the MONTH, DAY, YEAR, TIME in your data and you want a ISO8601 formatted datetime (YYYYMMDDT00:00:00):

```
    csv_to_kv.py csv_file.csv output.log "%s%s%sT%s" "YEAR,MONTH,DAY,TIME"
```