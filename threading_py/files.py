import os
import requests
from time import perf_counter
import concurrent.futures as newThread
# from image_urls import img_urls

def download_img(url):
    img_bytes = requests.get(url).content
    img_name_split = url.split('/')[3]
    img_name = f'{img_name_split}.jpg'

    # try
    with open(f'images\{ img_name}','wb') as file:
        file.write(img_bytes)
        print(f"image download {img_name}")

    # except Exception as error:
    #     print(error)
    
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
    ]
if __name__ == '__main__':
    
    os.system('cls')
    start_time = perf_counter()

    # with newThread.ThreadPoolExecutor() as executor:
    #     executor.map(download_img,img_urls)
        

        # for x in executor.map(download_img,img_urls):
            # print(x)


    for url in img_urls:
        print(download_img(url))
    
    end_time = perf_counter()
    print(f"Time taken to execute { round(end_time-start_time,3) } ")



# old download method

# def download_img():
#     counter = 0
#     for url in img_urls:
#         img_bytes = requests.get(url).content
#         img_name_split = url.split('/')[3]
#         img_name = f'{img_name_split}.jpg'
    
#         try:
#             with open(f'images\{ img_name}','wb') as file:
#                 file.write(img_bytes)
#                 counter +=1
#                 print(f"image download {counter}")

#         except Exception as error:
#             print(error)