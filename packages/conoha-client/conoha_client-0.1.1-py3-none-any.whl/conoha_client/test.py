import os
from pprint import pprint

import novaclient
from keystoneclient import client as kclient
from novaclient import client as nclient


def get_credentials():
    # ref: https://enakai00.hatenablog.com/entry/20131215/1387109226
    d = {}
    d["version"] = "2.0"
    d["username"] = os.environ["OS_USERNAME"]
    d["auth_url"] = os.environ["OS_AUTH_URL"]
    d["password"] = os.environ["OS_PASSWORD"]
    d["project_name"] = os.environ["OS_TENANT_NAME"]

    return d



keystone = kclient.Client(**get_credentials())
nova: novaclient.v2.Client = nclient.Client(**get_credentials())




# nova.CreateServer

print(nova.project_name)
servers = nova.servers.list()
pprint(dir(nova))
nova.servers.create()
# nova.










# for server in conn.list_servers():
#     server._computed




# # oclient.compute.client



# # oclient.compute.client.make_client
# # openstack


