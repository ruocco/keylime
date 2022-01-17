"""
SPDX-License-Identifier: Apache-2.0
Copyright 2021 Angelo Ruocco - IBM Research Lab Zurich
"""

def retry_time(exponential, base, ntries, logger):
    if exponential:
        if base > 1:
            return base**ntries
        else:
            try:
                logger.warning("Base %f incompatible with exponential backoff", base)
            except:
                None

    return abs(base)
