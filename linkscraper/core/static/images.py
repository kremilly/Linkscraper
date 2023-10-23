#!/usr/bin/python3

from core.static.autoload import *

def images_files(url, filter_data, download):
    if download:
        download_resources(url, 'images', None, filter_data)
    else:
        start_time = time.time()
        html = session.get(url).content
        soup = bs(html, "html.parser")
    
        Table.header([
            ("Filename", "cyan", True),
            ("URL", "bold blue", False)
        ])

        links = []
        
        for img in soup.find_all("img"):
            img_url = urljoin(url, img.attrs.get("src"))
            
            if filter_data:
                if find(img_url, filter_data):
                    links.append(img_url)
            else:
                links.append(img_url)
    
        list_images = list(set(links))
    
        for img_url in list_images:
            Table.row(get_remote_file_size(img_url), img_url)
        
        end_time = "{:.2f}".format(time.time() - start_time)
        
        Table.caption(f"Total images files on page: {len(list_images)} - Time taken: {end_time} seconds")
        Table.display()
