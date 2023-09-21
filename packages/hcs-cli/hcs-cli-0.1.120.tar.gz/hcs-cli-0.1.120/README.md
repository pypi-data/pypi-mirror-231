# horizon-cloud-service-cli

[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://github.com/vmware-labs/compliance-dashboard-for-kubernetes/blob/main/LICENSE)

- [horizon-cloud-service-cli](#horizon-cloud-service-cli)
  - [Overview](#overview)
  - [Try it out](#try-it-out)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
      - [Mac \& Linux](#mac--linux)
      - [Windows](#windows)
      - [Use the CLI](#use-the-cli)
  - [Authentication Methods](#authentication-methods)
    - [Security Practice](#security-practice)
  - [Documentation](#documentation)
  - [Contributing](#contributing)
  - [License](#license)


## Overview
Command line toolbox for [VMware Horizon Cloud Service (HCS) Next-Gen](https://www.vmware.com/products/horizon-cloud.html). It provides human-friendly operations based on HCS REST API.

## Try it out


### Prerequisites
* Python 3.10+
* Pip3

Refer to [Setup Prerequisites](doc/dev-setup.md#setup-prerequisites) for more details.

### Installation

#### Mac & Linux

Install the tool
```
pip3 install hcs-cli
```

#### Windows
Install the tool.
```
pip install hcs-cli
```
If you have python installed with option "Add python to path", it should be fine. Otherwise, you need to add python and it's Script directory to path.

#### Use the CLI
Use with default public HCS service. 
```
hcs login
```
Run a command, for example, list templates:
```
hcs admin template list
```

## Authentication Methods

For the first time with each profile, it needs authentication.
There are three ways to authenticate:

| Example                                | Purpose                                |
|----------------------------------------|----------------------------------------|
| hcs login [--org \<org-id\>]                             | Login with configured credentials, otherwise do an interactive login using browser. Note that if your CSP default org is not the target org for HCS, the _--org_ argument must be specified for initial login.|
| hcs login --api-token \<csp-api-token\> | Login with CSP API token. Reference: [Get CSP User API Token](doc/get-csp-user-api-token.md). |
| hcs login --client-id \<client-id\> --client-secret \<client-secret\> [--org \<org-id\>] | Login with OAuth client id/secret. |

To get the current authentication information:
```
hcs login -d
```

### Security Practice
HCS CLI stores authentication information in a conventional way. The profile and authentication state after login are stored in the current user home directory. The best practice is to use it on a single user system with admin privilege.

## Documentation
* [Work with development environments](doc/work-with-dev-envs.md)
* [HCS CLI Cheatsheet](doc/hcs-cli-cheatsheet.md)
* [HCS Plan, a resource manager for deployment](doc/hcs-plan.md)
* [Development Setup](doc/dev-setup.md)
* [Context Programming](https://github.com/nanw1103/context-programming)

  
## Contributing

The horizon-cloud-service-cli project team welcomes contributions from the community. Before you start working with horizon-cloud-service-cli, please read and sign our Contributor License Agreement [CLA](https://cla.vmware.com/cla/1/preview). If you wish to contribute code and you have not signed our CLA, our bot will prompt you to do so when you open a Pull Request. For any questions about the CLA process, please refer to our [FAQ]([https://cla.vmware.com/faq](https://cla.vmware.com/faq)).

## License

Apache 2.0


