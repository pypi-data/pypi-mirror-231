# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['custom_image_builder', 'custom_image_builder.exception']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2==3.1.2',
 'MarkupSafe==2.1.3',
 'PyJWT==2.8.0',
 'certifi==2023.7.22',
 'cffi==1.15.1',
 'charset-normalizer==3.2.0',
 'cryptography==41.0.3',
 'globus-compute-common==0.2.0',
 'globus-compute-sdk==2.3.2',
 'globus-sdk==3.27.0',
 'idna==3.4',
 'packaging==23.1',
 'pika==1.3.2',
 'pycparser==2.21',
 'pydantic==1.10.12',
 'requests==2.31.0',
 'tblib==1.7.0',
 'texttable==1.6.7',
 'typing_extensions==4.7.1',
 'urllib3==2.0.4',
 'websockets==10.3']

setup_kwargs = {
    'name': 'custom-image-builder',
    'version': '0.1.3',
    'description': 'A python package that enables user to build their custom singularity image on HPC cluster',
    'long_description': '# Building a singular container for HPC using globus-compute\n\n## Context\n* One of the executions configurations of [globus-compute](https://www.globus.org/compute) requires a registered container which is spun up to execute the user function on the HPC.\n\n* HPCs do not run docker containers(due to security reasons as discussed [here](https://docs.vscentrum.be/software/singularity.html)) and support only an apptainer/singularity image.\n\n* Installing the apptainer setup to build the singularity image locally is not a straightforward process especially on windows and mac systems as discussed in the [documentation](https://apptainer.org/docs/admin/main/installation.html).\n\nUsing this python library the user can specify their custom image specification to build an apptainer/singularity image \nwhich would be used to in-turn to run their functions on globus-compute. The library registers the container and \nreturns the container id which would be used by the globus-compute executor to execute the user function.\n\n\n## Prerequisite.\nA [globus-compute-endpoint](https://globus-compute.readthedocs.io/en/latest/endpoints.html) setup on HPC cluster. \n\n\n\n## Example\n\nConsider the following use-case where the user wants to execute a pandas operation on HPC using globus-compute.\nThey need a singularity image which would be used by the globus-compute executor. The library can be leveraged as follows:\n```python\nfrom custom_image_builder import build_and_register_container\n\ntutorial_endpoint = "01e21ddf-6eb4-41db-8e1d-2bcfe0c8314f"\ncontainer_id = build_and_register_container(endpoint_id=tutorial_endpoint,\n                                            image_file_name="my-test-image", \n                                            base_image_type="docker", \n                                            base_image="python:3.8",\n                                            pip_packages=["pandas"])\n\nprint("Container id ", container_id)\n\nfrom globus_compute_sdk import Executor\n\n# User function runs on the HPC node\ndef transform():\n    import pandas as pd\n    data = {\n        \'City\': [\'New York\', \'San Francisco\', \'Los Angeles\']\n    }\n    return pd.DataFrame(data)\n\n\nwith Executor(endpoint_id=tutorial_endpoint,\n              container_id=container_id) as ex:\n    fut = ex.submit(transform)\n    \n\nprint(fut.result())\n\n```\n',
    'author': 'ritwik-deshpande',
    'author_email': 'ritwikdeshpande01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
