import logging

from dktotoolkit.verbose import write_message

def aelf_officecontent_to_elements(office_content, hunfolding:list=[], skip_empty_items:bool=True):
    """
    legacy: use framagit.org/discord-catho/aelf-prayondiscord/utils/office:Office.office_content_to_elements() instead

    :param dict office_content: datas from AELF API, v1
    :param list hunfolding: Hunfolding (usefull to repeat the "antienne" for exemple, optionnal)
    :param bool skip_empty_item: skip empty items, or keep it inside the hunfolding ?
    :return: hunfolding (or "hunfolding-like") with datas from AELF
    :rtypes: list
    """

    write_message("legacy: dktotoolkit.aelf.aelf_officecontent_to_elements ; please use submodule of framagit.org/discord-catho/aelf-prayondiscord/utils/office:Office.office_content_to_elements() instead", level='critical')

    raise Exception("moved inside aelf-prayondiscord.utils")

    # from moved inside aelf-prayondiscord.utils.office import Office
    # return office_content_to_elements(
    #     office_content=office_content,
    #     hunfolding=hunfolding,
    #     skip_empty_items=skip_empty_items
    # )
#
