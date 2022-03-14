import urllib.request
src="https://lcms.skku.edu/contents4/skku100001/6224af5a3146c/contents/media_files/screen.mp4"
def save_video(video_url) :
    savename = 'save_by_urllib.mp4'

    urllib.request.urlretrieve(video_url,savename)
    print("저장완료")

save_video(src)