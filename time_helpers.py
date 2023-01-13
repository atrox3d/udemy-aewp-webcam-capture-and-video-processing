def seconds2timestamp(seconds):
    print(f'seconds2timestamp | {seconds=}')
    h = seconds / 3600
    hours = int(h)
    h_decimal = h - hours

    m = h_decimal * 60
    minutes = int(m)
    m_decimal = m - minutes

    seconds = round(m_decimal * 60, 2)

    timestamp = f'{hours:02}:{minutes:02}:{seconds:02}'

    print(f'seconds2timestamp | {hours=}, {minutes=}, {seconds=}, {timestamp=}')
    return timestamp


def timestamp2seconds(timestamp):
    hours, minutes, seconds = [float(n) for n in timestamp.split(':')]
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f'timestamp2seconds | {timestamp=}, {hours=}, {minutes=}, {seconds=}, {total_seconds=}')
    return total_seconds


if __name__ == '__main__':
    timestamp = '01:01:1.88'
    seconds = timestamp2seconds(timestamp)
    print(f'{timestamp=} = {seconds=}')

    timestamp = seconds2timestamp(seconds)
    print(f'{seconds=} = {timestamp=}')

