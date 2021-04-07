import gzip
import shutil


with open ('C:\\Windows\\System32\\Tpar\PrintLogs\\09-11-20210329150930571-172031249105-MQC.txt', 'rb') as f_in:
    with gzip.open('C:\\Windows\\System32\\Tpar\PrintLogs\\09-11-20210329150930571-172031249105-MQC2.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

