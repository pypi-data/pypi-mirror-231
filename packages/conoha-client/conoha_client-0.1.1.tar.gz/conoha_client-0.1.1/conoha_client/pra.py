import json
import sys
from pprint import pprint

# import requests
# from api import billing as B
# from api.server import list_servers
import click

@click.command()
@click.option('--greet', help='word to greet', default='hello')
@click.argument('to')
def cli(greet, to):
    click.echo(f'{greet} {to}')

def main():
    cli()
# VM一覧を取得
# VMの作成日時からの経過時間を取得

# pprint(B.payment_history())
# pprint(B.payment_total())
# pprint(B.billing_invoices())
# pprint(B.detail_invoice("1359752607"))
# sys.exit()

# svrs = list_servers()

# for s in svrs:
#     pprint(s)
#     print(s.elapsed_from_created())
# sys.exit()





# def create_server(tid, sgroup, stag, token, admin_pass, fid, iid, Sval):
#     _api = "https://compute.tyo1.conoha.io/v2/" + tid + "/servers"
#     _header = {"Accept": "application/json", "X-Auth-Token": token}
#     _body = {"server": {
#                 "security_groups": [{"name": sgroup}],
#                 "metadata": {"instance_name_tag": stag},
#                 "adminPass": admin_pass,
#                 "flavorRef": fid,
#                 "imageRef": iid,
#                 "user_data": Sval,
#         }}

#     try:
#         _res = requests.post(_api, data=json.dumps(_body), headers=_header)
#         if json.loads(_res.text)["server"]:
#             print("Success: WordPress new server started!")
#     except (ValueError, NameError, ConnectionError, RequestException, HTTPError) as e:
#         print("Error: Could not create server.", e)
#         sys.exit()
#     except KeyError:
#         print("Error Code   : {code}¥nError Message: {res}".format(
#                 code=_res.text["badRequest"]["message"],
#                 res=_res.text["badRequest"]["code"]))
#         sys.exit()

# Token = get_conoha_token(TENANT, APIUSER, APIPASS)
# Fuuid = get_flavor_uuid(TENANT, Token, FLAVORNAME)
# Iuuid = get_image_uuid(TENANT, Token, IMAGENAME)
# Svalue = get_startup_base64(SCRIPTPATH)


# print(Token)
# print(Fuiid)
# print(Iuuid)
# print(Svalue)

