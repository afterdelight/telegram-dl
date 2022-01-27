import io
from telethon import TelegramClient,sync
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterGif


api_id= your api_id
api_hash = 'your api_hash'
channel_link = ['channel1','channel2']
pic_down = './pic'
gif_down = './gif'
video_down = './video'
history_file='./history.txt'

def IsChongFu(content,file):
  xinxi = io.open(file, 'r', encoding='utf-8-sig')
  xinxi_list = xinxi.readlines()
  if(content+'\n' in xinxi_list):
    print(content+' is already done!')
    return True
  else:
    saveMessage(content,file)
    return False

def saveMessage(content,file):
  fp = open(file,'a+', encoding='utf-8-sig')
  fp.write(content+"\n")
  fp.close()

def download(client,file,filename):
    client.download_media(file,filename)


def getPhotoList(client,channel,InputMessagesFilterPhotos):
    channel_link = 'https://t.me/'+channel
    photos = client.get_messages(channel_link,None,filter=InputMessagesFilterPhotos)
    total = len(photos)
    index = 0
    for photo in photos:
        filename = pic_down + "/" + channel + "/" + str(photo.id) + ".jpg"
        index = index + 1
        if (IsChongFu(filename,history_file)):
            continue
        print("downloadind: ",index,"/",total," : ",filename)
        download(client,photo,filename)
    print('photo is done..')

def getGifList(client,channel,InputMessagesFilterGif):
    channel_link = 'https://t.me/'+channel
    gifs = client.get_messages(channel_link,None,filter=InputMessagesFilterGif)
    total = len(gifs)
    index = 0
    for gif in gifs:
        filename = gif_down + "/" + channel + "/" + str(gif.id) + ".mp4"
        index = index + 1
        if (IsChongFu(filename,history_file)):
            continue
        print("downloadind: ",index,"/",total," : ",filename)
        download(client,gif,filename)
    print('gif is done..')

def getVideoList(client,channel,InputMessagesFilterVideo):
    channel_link = 'https://t.me/'+channel
    videos = client.get_messages(channel_link,None,filter=InputMessagesFilterVideo)
    total = len(videos)
    index = 0
    for video in videos:
        filename = video_down + "/" + channel + "/" + str(video.id) + ".mp4"
        index = index + 1
        if (IsChongFu(filename,history_file)):
            continue
        print("downloadind: ",index,"/",total," : ",filename)
        download(client,video,filename)
    print('video is done...')

if __name__ == "__main__":
    client = TelegramClient('my_session',api_id=api_id,api_hash=api_hash).start()
    for channel in channel_link:
        print(channel+' is starting...')
        getPhotoList(client,channel,InputMessagesFilterPhotos)
        getGifList(client,channel,InputMessagesFilterGif)
        getVideoList(client,channel,InputMessagesFilterVideo)
    client.disconnect()
    print('ALL done !!')
