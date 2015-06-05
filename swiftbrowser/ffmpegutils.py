import os
import commands
import time
import string
import logging
import functools

# from utils import funclogger, time2Stamp, stamp2Time

logging.basicConfig(level=logging.DEBUG)




def create_video_thumb(video, source_folder, cut_time=3, duration_time=0.001):
    """
    """
    # cut_video_name = full_video[-34:-13] + full_video[-4:]
    # cut_video = source_folder + 'upload/' + cut_video_name
    source_folder = '/home/pc/swift-webstorage/static/videos/'
    out = source_folder + video
    # logging.debug('in cut_video, cut_video:%s' % video)
    # ffmpeg
    # stat = commands.getoutput("ffmpeg -i " + first_video + " -ss " + shift_time + " -to " #+ in
    #     + " -acodec copy -vcodec copy " + LIST_FOLDER + "/" + new_folder + "/" + cut_video)
    stat = commands.getoutput("ffmpeg -i " + source_folder+ video + 
        " -ss " + str(cut_time) + ' -vframes 1 -s 80x60 '  +  out[:-4] + '.png')
    # logging.debug('in cut_video, stat:%s' % stat)
    return out[:-4] + '.png'


def get_file_with_prefix(files, frefix='DEMO_'):
    videos = []
    for file_ in files:
        # logging.debug('file_ :%s , len(file_): %s, frefix:%s, len prefix:%s, file_[0:len(frefix)]:%s' % (file_, len(file_), frefix, len(frefix), file_[0:len(frefix)] ))
        if len(file_) > len(frefix) and file_[0:len(frefix)] == frefix:
            videos.append(file_)
            # logging.debug('file is video:%s' % file_)
    return videos


def cut_video(full_video, source_folder, head_shift_time, duration_time):
    """
    """
    cut_video_name = full_video[-34:-13] + full_video[-4:]
    cut_video = source_folder + 'upload/' + cut_video_name
    logging.debug('in cut_video, cut_video:%s' % cut_video)
    # ffmpeg
    # stat = commands.getoutput("ffmpeg -i " + first_video + " -ss " + shift_time + " -to " #+ in
    #     + " -acodec copy -vcodec copy " + LIST_FOLDER + "/" + new_folder + "/" + cut_video)
    stat = commands.getoutput("ffmpeg -i " + full_video + " -y " +
        " -ss " + str(int(head_shift_time)) + ' -t ' + str(int(duration_time))  +
        " -acodec copy -vcodec copy " + cut_video)
    logging.debug('in cut_video, stat:%s' % stat)
    return cut_video


if __name__ == '__main__':
    print(create_video_thumb('leaving_1432888410-1432888430.mp4', 
        '/home/pc/swift-webstorage/swiftbrowser/' ))
    # editting(1430404940, 1430404952, '/root/catch_video/videos/' ,
    #     '/root/catch_video/videos/upload/')
    #sys.exit(main())
