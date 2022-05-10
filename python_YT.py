import sys
from pytube import YouTube, Playlist

link = input("Enter the link (video or Playlist): ")

def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def progress_function(self,stream, chunk,file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)


def download_video(link):
    yt = YouTube(link,on_progress_callback=progress_function)
    q_choice = int(input("Choose quality : (1) Highest Video quality  (2) lowest video quality (3) Audio Only"))
    stream = None
    if q_choice == 1:
        stream = yt.streams.get_highest_resolution()
        if not stream:
            print("invalid link")
        else:
            stream.download()
            print("download completed")
    if q_choice == 2:
        stream = yt.streams.get_lowest_resolution()
        if not stream:
            print("invalid link")
        else:
            stream.download()
            print("download completed")
    if q_choice == 3:
        stream = yt.streams.get_audio_only()
        if not stream:
            print("invalid link")
        else:
            stream.download()
            print("download completed")
    
            

def app():
    print("Enter 1 or 2");
    print("1 Just download the video")
    print("2 Download the whole playlist")
    choice = int(input())
    if choice == 1:
        download_video(link)


    if choice == 2:
        p = Playlist(link)
        p_choice = int(input("(1) All Videos   (2) Audio only"))
        if p_choice == 1:
            print(f'Downloading the playlist: {p.title}')
            for video in p.videos:
                print(f'Downloading: {video.title}')
                video.streams.get_highest_resolution().download()
        if p_choice == 2:
            print(f'Downloading the playlist: {p.title}')
            for video in p.videos:
                print(f'Downloading: {video.title}')
                video.streams.get_audio_only().download()
        
    
if __name__=="__main__":
    app()