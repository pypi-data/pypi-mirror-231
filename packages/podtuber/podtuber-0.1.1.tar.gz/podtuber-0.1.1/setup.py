# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['podtuber']

package_data = \
{'': ['*']}

install_requires = \
['pathvalidate>=3.1.0,<4.0.0',
 'podgen>=1.1.0,<2.0.0',
 'pytube>=15.0.0,<16.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['podtuber = podtuber.main:main']}

setup_kwargs = {
    'name': 'podtuber',
    'version': '0.1.1',
    'description': 'Simple Python application to create podcast `.rss` files from YouTube playlists.',
    'long_description': "podtuber\n========\n\nSimple Python application to create podcast `.rss` files from YouTube playlists.\n\nInstallation\n------------\nYou might want to start with creating a Python virtual env. For example:\n```shell\nconda create -n podtuber python=3\nconda activate podtuber\n```\n\nand then:\n```shell\npip install podtuber\n```\nyou might need to logout and login, in order for the new `podtuber` command to be updated in `PATH`.\n\nUsage\n-----\n- copy the [example config.toml](https://github.com/ZvikaZ/podtuber/blob/master/config.toml) to your working directory, and modify it as needed (it's thoroughly commented),\n- and run: \n```shell\npodtuber\n```\n\nNotes\n-----\n- The .rss file needs to be served from an HTTP(S) server. Running the server is out of the scope of this tool.\n\n- Also, you might want to periodically update the .rss file (because the playlist might have been updated).\nIt can be achieved for example by using a Cron job to run `podtuber` on regular times.",
    'author': 'Zvika Haramaty',
    'author_email': 'haramaty.zvika@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ZvikaZ/podtuber',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
