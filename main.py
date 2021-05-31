# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ffmpy



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    video_path = "./yuki.mp4"
    udp_sink = "udp://127.0.0.1:15000"
    ff = ffmpy.FFmpeg(
        inputs={video_path:None},
        outputs={udp_sink:[ "-preset", "ultrafast", "-vcodec", "libx264", "-f", "h264"]}
    )
    print("ff.cmd : ", ff.cmd)
    ff.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
