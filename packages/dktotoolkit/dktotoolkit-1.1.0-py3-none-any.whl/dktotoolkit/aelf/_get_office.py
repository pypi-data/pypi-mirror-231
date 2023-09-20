import sys
import json
import re

if __name__=="__main__":
    import os
    sys.path.insert(0, os.path.abspath('../..'))
#end

from dktotoolkit import compat_mode, write_message

def get_aelf_office(office, date, zone="", hunfolding=[], **kwargs):
    """
    legacy: use framagit.org/discord-catho/aelf-prayondiscord/utils/office:Office.fetch_and_structure_office_data() instead

    :param str office: name of the office
    :param str date: date, format YYYY-MM-DD
    :param str zone: Zone (france, romain, ...)
    :param list hunfolding: Hunfolding (usefull to repeat the "antienne" for exemple)
    :return: hunfolding with datas from AELF
    :rtypes: list
    """

    write_message("legacy: dktotoolkit.aelf.call_api_aelf ; please use submodule of framagit.org/discord-catho/aelf-prayondiscord/utils:Office.fetch_and_structure_office_data() instead", level='critical')
    raise Exception("moved inside aelf-prayondiscord.utils")


#
