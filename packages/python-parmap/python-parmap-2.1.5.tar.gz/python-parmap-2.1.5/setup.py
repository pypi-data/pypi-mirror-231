# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['parmap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-parmap',
    'version': '2.1.5',
    'description': 'Simple trivial parallelization',
    'long_description': '# Parallel Map\nParmap is a python equivalent to Matlab\'s parfor function. Parmap runs\ntrivially parallisable problems in multiple parallel processes.\n\nA problem is trivially parallisable is each iteration of the loop\ncan be computed independently of every other iteration.\n\n## Examples\n\n```python\nfrom parmap import parmap\n\nx = np.arange(5)\n\n\n# Parallelise a call to a function with one argument\ndef sqr(x):\n    return x * x\n\n\nparmap(sqr, x)\n>> > [0, 1, 4, 9, 16, 25]\n\n\n# Parallelise a function with two arguments\ndef hypot(x, y):\n    return np.sqrt(x ** 2 + y ** 2)\n\n\n# hypot is called on every combination of x[i] and x[j].\n# result has one hundred elements\nparmap(hypot, x, x)\n>> > [0, 1, 2, ... 7.071]\n\n\n# Parallelise a function with  a configuration option\ndef power(x, n):\n    return x ** n\n\n\n# parmap works accepts both positional and keyword arguments as keyword arguments\nfunction_args = dict(n=3)\nresult = parmap(hypot, x, fargs=function_args)\n\n\ndef hypotn(x, y, n):\n    return x ** n + y ** n\n\n\nresult = parmap(hypot, x, x, fargs=function_args)\n```\n\n## Choosing your method of concurrency\nPython is technically a single threaded application that does not allow multiple calculations to be performed at one time. There are three main tricks for getting around this limit.\n\n1. **Multiprocessing:** Multi-processing creates multiple, separate, Python processes on your computer that compete for resources. These processes are completely separate, and can communicate with each other only with some difficulty (the ability to communicate between processes is not exposed by parmap, which assumes the procesess are separate). Multi-processing is best for problems which involve lots of CPU calculations, but not a lot of reading/writing data from disk or the network.\n\n2. **Threading:** In threading mode, multiple tasks take turns using the CPU to complete their work, but spend most of their time asleep. Threads are must cheaper to create than processes, both in terms of memory needed, or time to create. Only one thread can run at a time in Python, so threading is of no advantage for CPU heavy tasks. However, tasks that involve downloading multiple files from the internet spend most of their time waiting anyway, and are ideal for threads.\n\n3. **Asyncio:** Asyncio is similar to threading, but each thread has very fine grain control over when it cedes control of the CPU. Where normal threads are told by the OS when to run and when to stop, asyncio "threadlets" announce when they\'ve reached a good stopping point. Asyncio is more complicated to implement, and not recommended if your code is not already designed with async in mind.\n\nYour choice of concurrency in parmap can be set using the "engine" keyword.\n\n```python\nis_prime = parmap(check_if_prime, x, engine="multi")\npdf_list = parmap(download_pdfs, url_list, engine="threads")\n```\n\nThe "serial" engine disables concurrency and runs the tasks in series with a normal for loop. If one of the tasks throws an uncaught exception, the code halts, allowing you to debug. The other engines skip over failed tasks and try to complete as many as possible.\n\n## Installation\n`pip install parmap`\n\nThe file `implementation.py` is stand alone. If you prefer, you can simply copy it into your source code.\n',
    'author': 'Fergal',
    'author_email': 'fergal.mullally@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fergalm/parmap',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.7',
}


setup(**setup_kwargs)
