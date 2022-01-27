import io
import telethon
from telethon import TelegramClient,sync
from telethon.tl.types import (InputMessagesFilterChatPhotos,
                               InputMessagesFilterDocument,
                               InputMessagesFilterGif,
                               InputMessagesFilterPhotos,
                               InputMessagesFilterRoundVoice,
                               InputMessagesFilterVideo)
import time
import os
import shutil
import pathlib
from pathlib import Path
from tqdm import tqdm
import os.path
import sys
import ctypes

api_id= 0000000 #api id
api_hash = '000000000000000000000' #api hash
channel_id = -1000000000 #channel id

session = Path(__file__).stem
ctypes.windll.kernel32.SetConsoleTitleW(Path(__file__).name)

def callback(current, total):
    global pbar
    global prev_curr
    pbar.update(current-prev_curr)
    prev_curr = current       
    
def readFile(content,file):
    txtfile = io.open(file, 'r', encoding='utf-8-sig')
    txtfile_list = txtfile.readlines()
    if(content+'\n' in txtfile_list):
        print(content+' is already done!')
        return True
    else:
        return False
    
def saveMessage(content,file):
  fp = open(file,'a+', encoding='utf-8-sig')
  fp.write(content+"\n")
  fp.close()

def getDocumentList(client,channel_id,InputMessagesFilterDocument):
    print('Starting document download...')
    document_path = pathlib.Path(chat_title, 'Document')
    document_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    documents = client.iter_messages(channel_id,None,filter=InputMessagesFilterDocument, reverse = True)
    #use get.messages to get length of downloaded files
    documents2 = client.get_messages(channel_id,None,filter=InputMessagesFilterDocument, reverse = True)
    total_index = len(documents2)
    index = 0
    global pbar
    global prev_curr
    for document in documents:
        index = index + 1
        indexfile = "document" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=document.file.size, unit='B', unit_scale=True)
                filename = client.download_media(document, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(document_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('document is done..')
    
def getPhotoList(client,channel_id,InputMessagesFilterPhotos):
    print('Starting photo download...')
    photo_path = pathlib.Path(chat_title, 'Photo')
    photo_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    photos = client.iter_messages(channel_id,None,filter=InputMessagesFilterPhotos, reverse = True)
    #use get.messages to get length of downloaded files
    photos2 = client.get_messages(channel_id,None,filter=InputMessagesFilterPhotos, reverse = True)
    total_index = len(photos2)
    index = 0
    global pbar
    global prev_curr
    for photo in photos:    
        index = index + 1
        indexfile = "photo" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=photo.file.size, unit='B', unit_scale=True)
                filename = client.download_media(photo, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(photo_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('photo is done..')

def getRoundVoiceList(client,channel_id,InputMessagesFilterRoundVoice):
    print('Starting roundvoice download...')
    roundvoice_path = pathlib.Path(chat_title, 'RoundVoice')
    roundvoice_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    roundvoices = client.iter_messages(channel_id,None,filter=InputMessagesFilterRoundVoice, reverse = True)
    #use get.messages to get length of downloaded files
    roundvoices2 = client.get_messages(channel_id,None,filter=InputMessagesFilterRoundVoice, reverse = True)
    total_index = len(roundvoices2)
    index = 0
    global pbar
    global prev_curr
    for roundvoice in roundvoices:       
        sender = roundvoice.get_sender()
        username = sender.username
        index = index + 1
        indexfile = "roundvoice" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=roundvoice.file.size, unit='B', unit_scale=True)
                filename = client.download_media(roundvoice, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(roundvoice_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('RoundVoice is done..')

def getVideoList(client,channel_id,InputMessagesFilterVideo):
    print('Starting video download...')
    video_path = pathlib.Path(chat_title, 'Video')
    video_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    videos = client.iter_messages(channel_id,None,filter=InputMessagesFilterVideo, reverse = True)
    #use get.messages to get length of downloaded files
    videos2 = client.get_messages(channel_id,None,filter=InputMessagesFilterVideo, reverse = True)
    total_index = len(videos2)
    index = 0
    global pbar
    global prev_curr
    for video in videos:
        index = index + 1
        indexfile = "video" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=video.file.size, unit='B', unit_scale=True)
                filename = client.download_media(video, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(video_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('Video is done...')

def getGifList(client,channel_id,InputMessagesFilterGif):
    print('Starting gif download...')
    gif_path = pathlib.Path(chat_title, 'Gif')
    gif_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    gifs = client.iter_messages(channel_id,None,filter=InputMessagesFilterGif, reverse = True)
    #use get.messages to get length of downloaded files
    gifs2 = client.get_messages(channel_id,None,filter=InputMessagesFilterGif, reverse = True)
    total_index = len(gifs2)
    index = 0
    global pbar
    global prev_curr
    for gif in gifs:    
        index = index + 1
        indexfile = "gif" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=gif.file.size, unit='B', unit_scale=True)
                filename = client.download_media(gif, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(gif_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('gif is done..')

def getChatPhotoList(client,channel_id,InputMessagesFilterChatPhotos):
    print('Starting chatphoto download...')
    chatphoto_path = pathlib.Path(chat_title, 'ChatPhotos')
    chatphoto_path.mkdir(parents=True, exist_ok=True)
    #download with iter_messages to avoid telethon.errors.rpcerrorlist.FileReferenceExpiredError from get.messages
    chatphotos = client.iter_messages(channel_id,None,filter=InputMessagesFilterChatPhotos, reverse = True)
    #use get.messages to get length of downloaded files
    chatphotos2 = client.get_messages(channel_id,None,filter=InputMessagesFilterChatPhotos, reverse = True)
    total_index = len(chatphotos2)
    index = 0
    global pbar
    global prev_curr
    for chatphoto in chatphotos:    
        index = index + 1
        indexfile = "chatphoto" + str(index)
        if (readFile(indexfile,history_file)):
            continue
        else:
            print("\ndownloading file: ",index,"/",total_index," : ",indexfile)
            prev_curr = 0
            try:
                pbar = tqdm(total=chatphoto.file.size, unit='B', unit_scale=True)
                filename = client.download_media(chatphoto, progress_callback=callback)
                pbar.close()
                new_name = f'{index}_{filename}' 
                shutil.move(filename, os.path.join(chatphoto_path, new_name))
                saveMessage(indexfile,history_file)
                time.sleep(1)
            except AttributeError:
                print("There is no such attribute, skipping download...")
            except telethon.errors.rpcerrorlist.FileReferenceExpiredError:
                print('telethon File Reference Expired Error')
                ferror = open(file_error_location, "a")
                ferror.write('File Reference Expired Error: ' + indexfile + '\n')
                ferror.close() 
            except ConnectionRefusedError:   
                print('ConnectionRefusedError')
                ferror = open(file_error_location, "a")
                ferror.write('ConnectionRefusedError: ' + indexfile + '\n')
                ferror.close()
            except TimeoutError:
                print('TimeoutError')
                ferror = open(file_error_location, "a")
                ferror.write('TimeoutError: ' + indexfile + '\n')
                ferror.close()             
            except RpcCallFailError:
                print('RpcCallFailError')
                ferror = open(file_error_location, "a")
                ferror.write('RpcCallFailError: ' + indexfile + '\n')
                ferror.close()  
    print('chatphoto is done..')
    
if __name__ == "__main__":
    client = TelegramClient(session,api_id=api_id,api_hash=api_hash).start()
    result = client.iter_dialogs()
    for chat in result:
        #print(f'{chat.id}_{chat.title}')
        if chat.id == channel_id:
            chat_title = chat.title
    history_path = pathlib.Path(chat_title)   
    history_txt = f'{channel_id}_{"history.txt"}'    
    if os.path.isdir(history_path):
        print(f'{chat_title} folder exist')
    else:
        print(f'{chat_title} folder does not exist. creating one...')
        history_path.mkdir(parents=True, exist_ok=True)
    history_file = os.path.join(history_path, history_txt)
    #file_exists = os.path.isfile(history_path)  
    open(history_file, "a")
    error_txt = f'{channel_id}_{"error.txt"}' 
    file_error_location = os.path.join(history_path, error_txt)
    
    print(f'{chat_title} download is starting...')
    getDocumentList(client,channel_id,InputMessagesFilterDocument)
    getPhotoList(client,channel_id,InputMessagesFilterPhotos)   
    getGifList(client,channel_id,InputMessagesFilterGif)
    getChatPhotoList(client,channel_id,InputMessagesFilterChatPhotos)
    getVideoList(client,channel_id,InputMessagesFilterVideo)
    getRoundVoiceList(client,channel_id,InputMessagesFilterRoundVoice)
        
    client.disconnect()
    print('ALL done !!')
