def download_time(gb):
    megabytes_per_gigabytes = 1000
    bits_per_byte = 8
    megabits_per_second = 54
    return gb * megabytes_per_gigabytes * bits_per_byte / megabits_per_second


print(download_time(2))
