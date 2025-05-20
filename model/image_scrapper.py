from bing_image_downloader import downloader

politicians = {
    "Narendra Modi": "Narendra Modi face",
    "Joe Biden": "Joe Biden face",
    "Vladimir Putin": "Vladimir Putin face",
    "Xi Jinping": "Xi Jinping face",
    "Emmanuel Macron": "Emmanuel Macron face",
    "Zelenskyy": "Volodymyr Zelenskyy face",
    "Rishi Sunak": "Rishi Sunak face",
    "Donald Trump": "Donald Trump face",
    "YS Rajashekar Reddy": "YS Rajashekar Reddy face",
    "Angela Merkel": "Angela Merkel face",
    "Rahul Gandhi": "Rahul Gandhi face",
    "Arvind Kejriwal": "Arvind Kejriwal face",
    "Boris Johnson": "Boris Johnson face",
    "Olaf Scholz": "Olaf Scholz face",
    "Justin Trudeau": "Justin Trudeau face",
    "Jacinda Ardern": "Jacinda Ardern face",
    "Scott Morrison": "Scott Morrison face",
    "YS Jagan": "YS Jagan face",
    "ChandraBabu Naidu": "ChandraBabu Naidu face",
    "Nara Lokesh": "Nara Lokesh face"
}

for name, query in politicians.items():
    print(f"Downloading images for: {name}")
    downloader.download(
        query=query,
        limit=10,               
        output_dir='dataset/train',  
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )