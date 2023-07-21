from os import listdir, makedirs
from os.path import isfile, isdir, join, exists

import numpy as np
import pandas as pd

from PIL import Image
from PIL.ExifTags import TAGS
from matplotlib import pyplot as plt
from datetime import datetime

import uuid

# 要標記圖片的目錄
input_path = 'images'
# 紀錄檔的目錄
result_path = 'result'
# 合併mark圖片的目錄
merge_path = 'merge'
# mark的檔案名稱
mark_file = 'mark.jpg'
# mark覆蓋的透明度
mask_alpha = 0.2
# 預覽圖大小
fig_size = (10,10)
merge_file_label = False

def add_label(FILE_NAME,label):
    name,sub = FILE_NAME.split('.')
    return '{}_{}.{}'.format(name,label,sub)

def get_exif_time(img_path):
    with Image.open(img_path) as img:
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == 'DateTimeOriginal':
                    return value
        return None

def isjpg(FILE_NAME):
    name,sub = FILE_NAME.split('.')
    if sub == 'jpg' or sub == 'JPG' or sub == 'jpeg' or sub == 'JPEG':
        return True
    else:
        return False

# 建立所需資料夾
makedirs(merge_path, exist_ok=True)
makedirs(result_path, exist_ok=True)

#files = [f for f in listdir(input_path) if isfile(join(input_path, f)) and isjpg(f)]
main_dirs = [f for f in listdir(input_path) if isdir(join(input_path, f))]
main_dirs = sorted(main_dirs)

# 主資料夾
for main_dir in main_dirs:

    print('# === 主資料夾:{} ==='.format(main_dir))

    # 建立紀錄檔
    if exists(join(result_path, main_dir) + '.csv'):

        print('{}.csv紀錄檔已存在，阿你想怎樣？'.format(main_dir))
        print('(R)用新檔案取代 / (A)舊檔案繼續往下寫')

        while(True):
            option = input()
            if option == 'R':
                df_header = pd.DataFrame({'id':[],'folder':[],'image':[],'date':[],'time':[],'label1':[],'label2':[],'label3':[],'label2_index':[],'timeInterval(second)':[]})
                df_header.to_csv('{}/{}.csv'.format(result_path, main_dir), index=False)
                break
            elif option == 'A':
                break
            else:
                pass


    main_dir_path = join(input_path, main_dir)

    dirs = [f for f in listdir(main_dir_path) if isdir(join(main_dir_path, f))]
    dirs = sorted(dirs)

    label2_index = 0

    # 副資料夾
    for dir in dirs:
        print('## === 副資料夾:{} ===\n'.format(dir))

        dir_path = join(main_dir_path,dir)
        files = [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and isjpg(f)]
        files = sorted(files)

        ts_pre = None
        ts_start = None
        ts_end = None

        FIRST = False


        ts_marked = False

        # iterate the files in 副資料夾
        for i, f in enumerate(files):

            img_path = join(dir_path,f)

            timestamp = get_exif_time(img_path)
            date = (timestamp.split(' ')[0].replace(':','/'))

            time = (timestamp.split(' ')[1])

            print('{}/{}'.format(i+1, len(files)))

            print('檔案:{}'.format(f))
            print('日期:{}'.format(date))
            print('時間:{}'.format(time))
            img1 = Image.open(img_path)
            img2 = Image.open(mark_file)
            img_merge = Image.blend(img1, img2, alpha=mask_alpha)


            plt.figure(figsize = fig_size)
            plt.title(f)
            plt.imshow(img_merge)

            plt.axis("off")
            plt.show(block=False)


            label1 = input('label1出現個體,0=否,1=是:')

            if label1 == '0':
                label2 = None
                label3 = None
            else:
                label2 = input('label2第一張與否,0=否,1=是:')
                label3 = input('label3出現單/複數,0=單數,1=複數:')

            if  merge_file_label and label1 == '0':
                img_merge.save(join(merge_path,add_label(f,label1)))
                continue

            elif merge_file_label and label1 == '1':
                img_merge.save(join(merge_path,add_label(f,label1,label2,label3)))
                
            else: img_merge.save(join(merge_path,f))


            plt.close()

            timeInterval = None
            label2_index_out = None

            if (label2 == '1' and FIRST == True) or (label1 == '0' and FIRST == True):
                ts_end = ts_pre

                FIRST = False

                difference = ts_end - ts_start

                timeInterval = difference.seconds

                ts_marked = True

            # added 
            if ts_marked == False and i == len(files)-1:

                ts_end = datetime.strptime(timestamp, '%Y:%m:%d %H:%M:%S')
                difference = ts_end - ts_start
                timeInterval = difference.seconds


            if label2 == '1':
                #ts_start = timestamp
                ts_start = datetime.strptime(timestamp, '%Y:%m:%d %H:%M:%S')

                label2_index += 1
                label2_index_out = label2_index

                FIRST = True

            #print('FIRST:{}'.format(FIRST))
            #ts_pre = timestamp

            ts_pre = datetime.strptime(timestamp, '%Y:%m:%d %H:%M:%S')

            unique_id = uuid.uuid1()
            ID = (str(unique_id))


            # 寫入資料
            df_data = pd.DataFrame({'id':[ID],'folder':[dir],'image':[f],'date':[date],'time':[time],'label1':[label1],'label2':[label2],'label3':[label3],'label2_index':[label2_index_out],'timeInterval(second)':[timeInterval]})
            #df_data = pd.DataFrame({'folder':[dir],'image':[f],'date':[date],'time':[time],'label1':[label1],'label2':[label2],'label3':[label3]})
            df_data.to_csv('{}/{}.csv'.format(result_path, main_dir), mode='a', index=False, header=False)
            print('\n')

        print('===== END =====\n')

print('Done.')
