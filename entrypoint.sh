#!/bin/bash
shodan init ${SHODAN_API_KEY}
python -u /app/main.py $@
