import sys
from pprint import pprint

import openstack

# TODO


conn: openstack.connection.Connection = openstack.connect()

def search_image(name:str, mem_gb:int):
    images = conn.list_images() # show_allはTrue/Falseどちらも223

    print(len(images))

    for image in images:
        print(image.name, image.id, image.properties)
        break
        # image

def search_flavor():

    pass





sys.exit()




for server in conn.list_servers():
    print("########################")
    print(server.private_v4, server.name, server.image.name)
    pprint(server.to_dict())

# required args ?
## name
## image id
## flavor id  # コア数を指定
conn.create_server()



















