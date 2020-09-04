#-*- coding:utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import pysrt
import argparse
import codecs
import os
import code

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="input srt file name")
parser.add_argument("audio_filepath", help="audio asset filepath")

args = parser.parse_args()

subs = pysrt.open(args.filename, encoding='utf-8')

output_filename = os.path.splitext(args.filename)[0]+'.fcpxml'
output = codecs.open(output_filename, 'w', 'utf-8')

xmlheader = """
<fcpxml version="1.8">
    <import-options>
        <!-- <option key="library location" value="file:///Volumes/FCPXLibraries/MyLibrary.fcpbundle"/> -->
        <option key="library location" value="file:///Volumes/Montalcino/Document/FCPX/Workflow/Doc%20Migration/Editorial/Examples/WorkflowDocExamples.fcpbundle" />
    </import-options>
    <!-- Resources -->
    <resources>
        <format id="r1" name="FFVideoFormat1080p25" />
        <asset id="r2" src="file://{audio_filepath}" start="0s" duration="6240s" hasVideo="0" hasAudio="1" format="r1" audioSources="1" audioChannels="1" audioRate="44100" />
    </resources>
    <project name="MyProjectWithMarkers">
        <!-- Project Story Elements -->
        <sequence format="r1">
            <spine>
""".format(audio_filepath=os.path.abspath(args.audio_filepath))

xmltail = """
            </spine>
        </sequence>
    </project>
</fcpxml>
"""

output.write(xmlheader)

"""
         |     s     |  gap    | s_next    |
       start        end         

<asset-clip name="MyMovie3" ref="r2" offset="5s" start="15s" duration="5s" audioRole="SpeakerA" /> 
"""

def srt_time_to_fcpx_time(s, fcp_scale=441000):
    m_fcp_scale = int(fcp_scale / 1000)
    return s.hours * 60 * 60 * fcp_scale + s.minutes * 60 * fcp_scale + s.seconds * fcp_scale + s.milliseconds * m_fcp_scale

for i in range(len(subs)):
    s = subs[i]
    start = srt_time_to_fcpx_time(s.start)
    end = srt_time_to_fcpx_time(s.end)
    duration = srt_time_to_fcpx_time(s.duration)

    #output.write("<asset-clip name=\"%s\" ref=\"r2\" offset=\"%d/441000s\" start=\"%d/441000s\" duration=\"%d/441000s\" audioRole=\"SpeakerA\" />\n"%(s.text.replace('\n',' \\\\ '), start, start, duration))

    assert(start+duration == end)

    if i != len(subs) - 1: 
        s_next = subs[i+1]  #Gap between two sentences
        duration_gap = srt_time_to_fcpx_time(s_next.start) - end
        #output.write("<asset-clip name=\"%s\" ref=\"r2\" offset=\"%d/441000s\" start=\"%d/441000s\" duration=\"%d/441000s\" audioRole=\"SpeakerA\" />\n"%("SPACE", end, end, duration_gap))
        assert(start+duration+duration_gap == srt_time_to_fcpx_time(s_next.start))
#    code.interact(local=locals())
    output.write("<asset-clip name=\"%s\" ref=\"r2\" offset=\"%d/441000s\" start=\"%d/441000s\" duration=\"%d/441000s\" audioRole=\"SpeakerA\" />\n"%(s.text.replace('\n',' \\\\ '), start, start, duration+duration_gap))

output.write(xmltail)
output.close()

print("%s wrote." % output_filename)
