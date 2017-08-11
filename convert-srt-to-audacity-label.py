#-*- coding:utf-8
import pysrt
import argparse
import codecs
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input srt file name")
args = parser.parse_args()

subs = pysrt.open(args.filename, encoding='utf-8')

output_filename = os.path.splitext(args.filename)[0]+'-LABELS.txt'
output = codecs.open(output_filename, 'w', 'utf-8')

for s in subs:
    start = s.start.hours * 60 * 60 + s.start.minutes * 60 + s.start.seconds + s.start.milliseconds/1000.0
    end = s.end.hours * 60 * 60 + s.end.minutes * 60 + s.end.seconds + s.end.milliseconds/1000.0
    output.write( "%.6f\t%.6f\t%s\n" % (start,end,s.text.replace('\n',' \\\\ ') ) )

output.close()

print "%s wrote." % output_filename
