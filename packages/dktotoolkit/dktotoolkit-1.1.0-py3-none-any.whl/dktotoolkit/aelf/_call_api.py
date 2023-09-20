# -*- coding: utf-8 -*-
"""
@author: Pierre
"""

import sys
import re
import requests, json

if __name__=="__main__":
    import os
    sys.path.insert(0, os.path.abspath('../..'))
#end


from dktotoolkit.datestr import is_valid_date
from dktotoolkit.html import request_html_page

from dktotoolkit.verbose import write_message

def _modify_datas(datas, requested_url):
    if 'informations' in datas:
        datas['informations']['url'] = requested_url
    #

    return datas


def call_api_aelf(
        office_name,
        date,
        zone=None,
        return_alldatas=True # retourner toutes les donnees ou juste la priere
):
    """
    legacy: use framagit.org/discord-catho/aelf-prayondiscord/utils/office:Office.call_api_aelf() instead

    :param str office_name: nom de l'office
    :param str date: jour
    :param str zone: calendrier utilise
    :param bool return alldatas: Retourner toutes les donnees (informations + priere) ou juste la priere
    """

    write_message("legacy: dktotoolkit.aelf.call_api_aelf ; please use submodule of framagit.org/discord-catho/aelf-prayondiscord/utils:Office.call_api_aelf() instead", level='critical')
    raise Exception("moved inside aelf-prayondiscord.utils")

    # from moved inside aelf-prayondiscord.utils.office import Office
    # return Office.call_api_aelf(
    #     office_name=office_name,
    #     date=date,
    #     zone=zone,
    #     return_alldatas=return_alldatas
    # )

#endDef



if __name__=="__main__":
    print(call_api_aelf("informations", date="2023-05-21"))
    print()
    #print(api_aelf("informations",the_day="3 juin"))
    print()
    #print(api_aelf("informations",the_day="hier"))
    print()
    #print(api_aelf("informations",the_day="avant-hier"))
    print()
