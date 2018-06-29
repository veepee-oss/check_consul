# check_consul

[![License][license-img]][license-href]

1. [Overview](#overview)
2. [Description](#description)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Limitations](#limitations)
6. [Development](#development)
7. [Miscellaneous](#miscellaneous)

## Overview

Consul is a distributed service mesh to connect, secure, and configure services
across any runtime platform and public or private cloud.

[consul.io][overview-href]

## Description

Check Consul health  and state. This plugin request the  Consul API to retrieve
healths checks status.

## Setup

This check has the following dependencies :

- python (2 or 3)
- consulate

## Usage

```bash
python check_consul_service.py \
  -t ${CONSUL_TOKEN} \
  -H ${CONSUL_HOST} \
  -p ${CONSUL_PORT} \
  ${CONSUL_SERVICE}
```

## Limitations

So far, this is compatible with Python 2.7, 3.5 and 3.6.

## Development

Please read carefully [CONTRIBUTING.md][contribute-href]  before making a merge
request.

## Miscellaneous

```
    ╚⊙ ⊙╝
  ╚═(███)═╝
 ╚═(███)═╝
╚═(███)═╝
 ╚═(███)═╝
  ╚═(███)═╝
   ╚═(███)═╝
```

[license-img]: https://img.shields.io/badge/license-Apache-blue.svg
[license-href]: LICENSE
[overview-href]: https://www.consul.io/
[contribute-href]: CONTRIBUTING.md
