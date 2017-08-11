# convert-srt-to-audacity-label

Convert SRT file to audacity supported label. 

Useful when editing an long interview, with auto generated SRT files.


Multiple lines within a single SRT screen will be concatenated with `\\`.

## Installation

[Python 2](https://www.python.org/downloads/) is needed.

```bash
$ sudo pip2 install pysrt  #Linux or macOS
```

## Usage

     $ python2 convert-srt-to-audacity-label.py  /path/to/your/srt-file.srt

     $ python2 convert-srt-to-audacity-label.py demo.srt
     demo-LABELS.txt wrote.

## Platform

 - macOS (Tested)
 - Linux (Tested)
 - Windows (Didn't test, but shouldn't be a problem)
