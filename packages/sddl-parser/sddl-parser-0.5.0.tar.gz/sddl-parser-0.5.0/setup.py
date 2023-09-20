# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sddl_parser']

package_data = \
{'': ['*']}

install_requires = \
['parsy>=2.1,<3.0']

setup_kwargs = {
    'name': 'sddl-parser',
    'version': '0.5.0',
    'description': 'Parse SDDL strings',
    'long_description': '# Install\n```\npip3 install sddl-parser\n```\n\n# Usage\nParse an SDDL string\n\n```py\n>> from sddl_parser import parse_sddl\n>> sddl = "O:SYG:SYD:AI(A;ID;GA;;;SY)"\n>> parse_sddl(sddl)\nSDDL(\n    owner=SIDEnum.LOCAL_SYSTEM,\n    group=SIDEnum.LOCAL_SYSTEM,\n    dacl=ACL(\n        flags={SDDLFlags.SDDL_AUTO_INHERITED},\n        aces=[\n            ACE(\n                type=AceType.ACCESS_ALLOWED,\n                flags={AceFlags.INHERITED},\n                object_guid="",\n                rights_int=268435456,\n                inherit_object_guid="",\n                sid=SIDEnum.LOCAL_SYSTEM,\n                conditional_ace=None,\n                rights={GenericAccessRights.GENERIC_ALL},\n            )\n        ],\n    ),\n    sacl=None,\n)\n```\n\nParse an ACE\n\n```py\n>> from sddl_parser import parse_ace\n>> ace = "(A;ID;0x10030;;;AC)"\n>> parse_ace(ace)\nACE(\n    type=AceType.ACCESS_ALLOWED,\n    flags={AceFlags.INHERITED},\n    object_guid="",\n    rights_int=65584,\n    inherit_object_guid="",\n    sid=SIDEnum.ALL_APP_PACKAGES,\n    conditional_ace=None,\n    rights={\n        GenericAccessRights.ACCESS4,\n        GenericAccessRights.DELETE,\n        GenericAccessRights.ACCESS5,\n    },\n)\n```\n\nSee that `GenericAccessRights.ACCESS4` is returned. That\'s an indication that the SDDL type should be specified. To get more accurate rights, use `.as_type()` on the object or pass the Rights object to the parse_ace function\n\n```py\n>> from sddl_parser import parse_ace, FileAccessRights\n>> ace = "(A;ID;0x1200a9;;;AC)"\n>> # alternatively, run parse_ace(ace, FileAccessRights)\n>> parse_ace(ace).as_type(FileAccessRights)\nACE(\n    type=AceType.ACCESS_ALLOWED,\n    flags={AceFlags.INHERITED},\n    object_guid="",\n    rights_int=1179817,\n    inherit_object_guid="",\n    sid=SIDEnum.ALL_APP_PACKAGES,\n    conditional_ace=None,\n    rights={\n        FileAccessRights.FILE_EXECUTE,\n        FileAccessRights.FILE_READ_DATA,\n        FileAccessRights.FILE_READ_ATTRIBUTES,\n        FileAccessRights.READ_CONTROL,\n        FileAccessRights.SYNCHRONIZE,\n        FileAccessRights.FILE_GENERIC_EXECUTE,\n        FileAccessRights.FILE_READ_EA,\n        FileAccessRights.FILE_GENERIC_READ,\n    },\n)\n```\n\nAll rights are IntEnums, so if you want to check for generic rights, `FileAccessRights.DELETE` is equivalent to `GenericAccessRights.DELETE`\n\nIf you want to map SIDs to strings, you can pass in `sidmap`:\n\n```py\n>>> from sddl_parser import api\n>>> test = "O:S-1-20-20-20G:SYD:"\n>>> sidmap = {"S-1-20-20-20": "DOMAIN\\\\user"}\n>>> api.parse_sddl(test, sidmap=sidmap)\nSDDL(\n    owner="DOMAIN\\\\user",\n    group=SIDEnum.LOCAL_SYSTEM,\n    dacl=ACL(flags={SDDLFlags.NO_ACCESS_CONTROL}, aces=[]),\n    sacl=None,\n)\n```\n\n# Access Rights Available\n\nAll right enums are given here\n\n```\n>> from sddl_parser import rights_enums\n>> for x in dir(rights_enums):\n>>   print(i)\nAlpcAccessRights\nAuditAccessRights\nDebugAccessRights\nDesktopAccessRights\nDirectoryAccessRights\nDirectoryServiceAccessRights\nEnlistmentAccessRights\nEventAccessRights\nFileAccessRights\nFileDirectoryAccessRights\nFilterConnectionPortAccessRights\nFirewallAccessRights\nFirewallFilterAccessRights\nGenericAccessRights\nIoCompletionAccessRights\nJobAccessRights\nKeyAccessRights\nLsaAccountAccessRights\nLsaPolicyAccessRights\nLsaSecretAccessRights\nLsaTrustedDomainAccessRights\nMemoryPartitionAccessRights\nMutantAccessRights\nPrintSpoolerAccessRights\nProcessAccessRights\nRegistryKeyAccessRights\nRegistryTransactionAccessRights\nResourceManagerAccessRights\nSamAliasAccessRights\nSamDomainAccessRights\nSamGroupAccessRights\nSamServerAccessRights\nSamUserAccessRights\nSemaphoreAccessRights\nServiceAccessRights\nServiceControlManagerAccessRights\nSessionAccessRights\nSymbolicLinkAccessRights\nThreadAccessRights\nTimerAccessRights\nTokenAccessRights\nTraceAccessRights\nTransactionAccessRights\nTransactionManagerAccessRights\nWindowStationAccessRights\nWnfAccessRights\n```\n\n# Shoulders of Giants\n- [An0ther0ne]\n- [James Forshaw]\n\n[An0ther0ne]: https://github.com/An0ther0ne\n[James Forshaw]: https://twitter.com/tiraniddo\n',
    'author': 'Max Harley',
    'author_email': 'maxh@maxh.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
