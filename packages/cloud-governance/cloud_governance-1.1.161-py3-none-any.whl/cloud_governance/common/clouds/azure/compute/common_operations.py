from typing import Optional, Union

from azure.core.paging import ItemPaged
from azure.identity import DefaultAzureCredential

from cloud_governance.cloud_resource_orchestration.utils.common_operations import string_equal_ignore_case
from cloud_governance.main.environment_variables import environment_variables


class CommonOperations:

    def __init__(self):
        self.__environment_variables_dict = environment_variables.environment_variables_dict
        self._default_creds = DefaultAzureCredential()
        self._subscription_id = self.__environment_variables_dict.get('AZURE_SUBSCRIPTION_ID')

    def _item_paged_iterator(self, item_paged_object: ItemPaged):
        """
        This method iterates the paged object and return the list
        :param item_paged_object:
        :return:
        """
        iterator_list = []
        try:
            page_item = item_paged_object.next()
            while page_item:
                iterator_list.append(page_item)
                page_item = item_paged_object.next()
        except StopIteration:
            pass
        return iterator_list

    def check_tag_name(self, tags: Optional[dict], tag_name: str):
        """
        This method checks tag is present and return its value
        :param tags:
        :param tag_name:
        :return:
        """
        if tags:
            for key, value in tags.items():
                if string_equal_ignore_case(key, tag_name):
                    return value
        return ''
