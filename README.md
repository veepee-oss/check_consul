# check_consul

1. [Overview](#overview)
2. [Description](#description)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Limitations](#limitations)
6. [Miscellaneous](#miscellaneous)

## Overview

Icinga plugins for Consul.

## Description

This plugin request the Consul API to retrieve healths checks status.

## Setup

This check has the following dependencies :

- python (2 or 3)
- consulate

## Usage

```
python check_consul_service.py \
  -t ${CONSUL_TOKEN} \
  -H ${CONSUL_HOST} \
  -p ${CONSUL_PORT} \
  ${CONSUL_SERVICE}
```

## Limitations

So far, this is compatible with Python 2.7, 3.5 and 3.6.

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
