# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sddl']

package_data = \
{'': ['*']}

install_requires = \
['sddl-parser>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'sddl',
    'version': '0.1.0',
    'description': 'CLI frontend for sddl-parser',
    'long_description': '# SDDL\n\n## Usage\n\n```bash\n$ sddl -h\nusage: sddl [-h] [--type TYPE] [--list-types] [--json] [sddl]\n\nRead SDDL strings\n\npositional arguments:\n  sddl          SDDL string to parse. If not provided, read from stdin.\n\noptions:\n  -h, --help    show this help message and exit\n  --type TYPE   Type of ACE to parse. Default: GenericAccessRights\n  --list-types  List available ACE types\n  --json        Output as JSON\n\nExample: `sddl \'O:BAG:BAD:(A;;GA;;;WD)\'` or `echo \'O:BAG:BAD:(A;;GA;;;WD)\' | sddl`\n```\n\n## Examples\n\n- Using an alternative rights type\n\n```bash\nsddl \'O:SYG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)(A;ID;0x1200a9;;;AC)(A;ID;0x1200a9;;;\nS-1-15-2-2)\' --type RegistryKeyAccessRights\nOwner: LOCAL_SYSTEM\nGroup: LOCAL_SYSTEM\nDACL:\n  SDDL_AUTO_INHERITED\n    ACCESS_ALLOWED INHERITED KEY_CREATE_LINK|KEY_QUERY_VALUE|KEY_SET_VALUE|KEY_WOW64_64KEY|KEY_CREATE_SUB_KEY|DELETE|READ_CONTROL|WRITE_DAC|KEY_ENUMERATE_SUB_KEYS|WRITE_OWNER|SYNCHRONIZE|KEY_WRITE|KEY_NOTIFY|KEY_READ|KEY_ALL_ACCESS LOCAL_SYSTEM\n    ACCESS_ALLOWED INHERITED KEY_CREATE_LINK|KEY_QUERY_VALUE|KEY_SET_VALUE|KEY_WOW64_64KEY|KEY_CREATE_SUB_KEY|DELETE|READ_CONTROL|WRITE_DAC|KEY_ENUMERATE_SUB_KEYS|WRITE_OWNER|SYNCHRONIZE|KEY_WRITE|KEY_NOTIFY|KEY_READ|KEY_ALL_ACCESS BUILTIN_ADMINISTRATORS\n    ACCESS_ALLOWED INHERITED KEY_CREATE_LINK|KEY_QUERY_VALUE|READ_CONTROL|SYNCHRONIZE|KEY_ENUMERATE_SUB_KEYS BUILTIN_USERS\n    ACCESS_ALLOWED INHERITED KEY_CREATE_LINK|KEY_QUERY_VALUE|READ_CONTROL|SYNCHRONIZE|KEY_ENUMERATE_SUB_KEYS ALL_APP_PACKAGES\n    ACCESS_ALLOWED INHERITED KEY_CREATE_LINK|KEY_QUERY_VALUE|READ_CONTROL|SYNCHRONIZE|KEY_ENUMERATE_SUB_KEYS S-1-15-2-2\nSACL:\n```\n\n- Output to JSON\n\n```bash\n$ sddl \'O:SYG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)(A;ID;0x1200a9;;;AC)(A;ID;0x1200a9;;;\nS-1-15-2-2)\' --type RegistryKeyAccessRights --json\n{"owner": "LOCAL_SYSTEM", "group": "LOCAL_SYSTEM", "dacl": {"flags": ["SDDL_AUTO_INHERITED"], "aces": [{"type": "ACCESS_ALLOWED", "flags": ["INHERITED"], "rights": ["KEY_CREATE_LINK", "KEY_QUERY_VALUE", "KEY_SET_VALUE", "KEY_WOW64_64KEY", "KEY_CREATE_SUB_KEY", "DELETE", "READ_CONTROL", "WRITE_DAC", "KEY_ENUMERATE_SUB_KEYS", "WRITE_OWNER", "SYNCHRONIZE", "KEY_WRITE", "KEY_NOTIFY", "KEY_READ", "KEY_ALL_ACCESS"], "sid": "LOCAL_SYSTEM"}, {"type": "ACCESS_ALLOWED", "flags": ["INHERITED"], "rights": ["KEY_CREATE_LINK", "KEY_QUERY_VALUE", "KEY_SET_VALUE", "KEY_WOW64_64KEY", "KEY_CREATE_SUB_KEY", "DELETE", "READ_CONTROL", "WRITE_DAC", "KEY_ENUMERATE_SUB_KEYS", "WRITE_OWNER", "SYNCHRONIZE", "KEY_WRITE", "KEY_NOTIFY", "KEY_READ", "KEY_ALL_ACCESS"], "sid": "BUILTIN_ADMINISTRATORS"}, {"type": "ACCESS_ALLOWED", "flags": ["INHERITED"], "rights": ["KEY_CREATE_LINK", "KEY_QUERY_VALUE", "READ_CONTROL", "SYNCHRONIZE", "KEY_ENUMERATE_SUB_KEYS"], "sid": "BUILTIN_USERS"}, {"type": "ACCESS_ALLOWED", "flags": ["INHERITED"], "rights": ["KEY_CREATE_LINK", "KEY_QUERY_VALUE", "READ_CONTROL", "SYNCHRONIZE", "KEY_ENUMERATE_SUB_KEYS"], "sid": "ALL_APP_PACKAGES"}, {"type": "ACCESS_ALLOWED", "flags": ["INHERITED"], "rights": ["KEY_CREATE_LINK", "KEY_QUERY_VALUE", "READ_CONTROL", "SYNCHRONIZE", "KEY_ENUMERATE_SUB_KEYS"], "sid": "S-1-15-2-2"}]}, "sacl": null}\n```\n',
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
