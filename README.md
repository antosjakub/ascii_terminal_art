# ASCII art in the terminal

![alt text](rick_roll_20s/rick_ascii.png)

## steps

0) find the video
- high quality rick roll on YTB: https://www.youtube.com/watch?v=o-YBDTqX_ZU
- take the 20s interval from 3:07 to 3:27

1) download the video as .mp4
- use smthg like https://iyoutubetomp4.com/en9/

2) extract audio

    `$ ffmpeg -i out.mp4 -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000 out.mp3`


2) extract the frames as png or jpeg
- use for example a command line tool like ffmpeg or any online tool
- this will populate the current working directory with the .png files

    `$ ffmpeg -i input.mp4 %04d.png`

3) run convert_to_ascii.py script, for example:

    `$ python convert_to_ascii.py rick_roll_20s/images rick_roll_20s/ascii`

4) open a new terminal and run print_to_terminal.py, for example:

    `$ python print_to_term.py rick_roll_20s/`