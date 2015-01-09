def status_to_int(status):
    return {
        'ACTIVE': 1,
        'SUCCESS': 2,
        'FAILED': 3,
        'BAD': 4,
        }.get(status, 'No')

a = status_to_int('A')
print(a)

import sqlite3
