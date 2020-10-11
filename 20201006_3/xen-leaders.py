from collections import namedtuple
from sys import stdin
from typing import List

Record = namedtuple('Record', ['first_name', 'last_name', 'title', 'hours', 'minutes', 'seconds'])


if __name__ == '__main__':
    # read all records
    records: List[Record] = []
    for i, line in enumerate(stdin):
        line = line.strip()
        if len(line) == 0:
            break
        first, last, rest = line.split(' ', 2)
        title, result = rest.rsplit(' ', 1)
        hours, minutes, seconds = map(lambda x: int(x), result.rsplit(':'))
        records.append(Record(
            first_name=first,
            last_name=last,
            title=title,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ))

    # find top 3
    top_3: List[Record] = []
    distinct_count = 0
    for record in sorted(records, key=lambda x: (x.hours, x.minutes, x.seconds, x.last_name, x.first_name, x.title)):
        if distinct_count == 0:
            top_3.append(record)
            distinct_count += 1
        elif top_3[-1].hours == record.hours and top_3[-1].minutes == record.minutes and top_3[-1].seconds == record.seconds:
            top_3.append(record)
        elif distinct_count < 3:
            top_3.append(record)
            distinct_count += 1
        else:
            break

    # print results in table
    first_name_width = max(map(lambda rec: len(rec.first_name), top_3))
    last_name_width = max(map(lambda rec: len(rec.last_name), top_3))
    title_width = max(map(lambda rec: len(rec.title), top_3))
    for record in top_3:
        formatted_first = record.first_name.ljust(first_name_width, ' ')
        formatted_last = record.last_name.ljust(last_name_width, ' ')
        formatted_title = record.title.ljust(title_width, ' ')
        print(f'{formatted_first} {formatted_last} {formatted_title} {record.hours}:{record.minutes}:{record.seconds}')
