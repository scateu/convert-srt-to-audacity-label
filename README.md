# convert-srt-to-audacity-label

Convert SRT file to audacity supported label. 

Useful when editing an long interview, with auto generated SRT files.


Multiple lines within a single SRT screen will be concatenated with `\\`.

## Installation

[Python 2/3](https://www.python.org/downloads/) is needed.

```bash
$ sudo pip install pysrt  #Linux or macOS
```
Or..

```bash
$ sudo easy_install pysrt
```

## Usage

     $ python convert-srt-to-audacity-label.py  /path/to/your/srt-file.srt

## Example

     $ python convert-srt-to-audacity-label.py demo.srt
     demo-LABELS.txt wrote.

## Platform

 - macOS (Tested)
 - Linux (Tested)
 - Windows (Didn't test, but shouldn't be a problem)

## Reference
 
  - <https://github.com/agermanidis/autosub>: Command-line utility for auto-generating subtitles for any video file (Google API)
