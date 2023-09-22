# pylint: disable=line-too-long
# pylint: disable=all

__doc__ = """Console-based recreation of the website ismyinternetworking.com's main purposes of internet connection testing and ping testing.

Licensed under a GNU AGPLv3 license.


Please note that this module is in no way affiliated with the official ismyinternetworking.com website; it was referenced because it makes a good test target... and it's neat."""

import time, os, threading, random
from ping3 import ping

sites_to_file = """www.ismyinternetworking.com
www.google.com
www.cloudflare.com
www.yahoo.com
www.bing.com
www.amazon.com
www.netflix.com
www.reddit.com
www.facebook.com
www.twitter.com
www.instagram.com
www.linkedin.com
"""  # some default websites to use to populate a missing websites.txt file

def load_websites(max_num_sites: int):  # load websites from the configuration file, or create a new file if missing
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "websites.txt")):
        with open("websites.txt", 'r') as file:
            all_websites = [line.strip() for line in file.readlines()]
            file.close()
        selected_websites = random.sample(all_websites, max(min(max_num_sites, len(all_websites)), 1) if max_num_sites > 0 else max(len(all_websites), 1))  # added maximum and minimum values as safeguards to protect against IndexOutOfRange errors, as well as adding accountability for if max_num_sites is equal or less than zero, ignoring it entirely and selecting all available sites
        return selected_websites
    else:
        with open("websites.txt", "x") as file:
            file.write(sites_to_file)
            file.close()
        with open("websites.txt", 'r') as file:
            all_websites = [line.strip() for line in file.readlines()]
            file.close()
        selected_websites = random.sample(all_websites, max(min(max_num_sites, len(all_websites)), 1) if max_num_sites > 0 else max(len(all_websites), 1))  # added maximum and minimum values as safeguards to protect against IndexOutOfRange errors, as well as adding accountability for if max_num_sites is equal or less than zero, ignoring it entirely and selecting all available sites
        return selected_websites

websites = load_websites(0)  # Limited list of websites to ping generated from a larger list of websites saved in a configuration file
ping_list = []  # list of ping results; old results get removed
ping_avg_list = []  # list of single-use ping results from each site; gets cleared between accesses
ping_avg_lock = threading.Lock()  # a lock to make threaded access to ping_avg_list safe
continue_checklist = []  # list of tokens; if equal to number of websites, continuing is allowed; gets cleared upon continue
continue_lock = threading.Lock()  # a lock to make threaded access to continue_checklist safe
threads = []  # list of active threads; gets cleared upon reinitializing threads

def cls():  # OS-aware screen-clear function
    os.system('cls' if os.name == 'nt' else 'clear')

def ping_website(website: str = "www.ismyinternetworking.com", timeout: int = 3):  # function used by each thread to ping available websites; default args provided
    try:
        result = ping(website, timeout, "ms")
        if result is not None:
            with ping_avg_lock:
                ping_avg_list.append(round(result,2))
        with continue_lock:
            continue_checklist.append(int(1))
    except Exception as e:  # logs any errors pinging websites to ping.error.log, located in the script directory
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ping.error.log")):
            with open('ping.error.log', 'a') as ping_error_log:
                ping_error_log.write(f"""{time.strftime('%Y-%m-%d,%H:%M:%S')};\n\t{e}\n\n""")
                ping_error_log.close()
        else:
            with open('ping.error.log', 'x') as ping_error_log:
                ping_error_log.write(f"""{time.strftime('%Y-%m-%d,%H:%M:%S')};\n\t{e}\n\n""")
                ping_error_log.close()

def init_threads():  # fuction to initialize threads to ping all available websites simultaneously; locks added for safety
    threads.clear()
    with ping_avg_lock:
        ping_avg_list.clear()
    with continue_lock:
        continue_checklist.clear()
    for website in websites:
        thread = threading.Thread(target=ping_website, args=(website, 2))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
def avg(var: list):  # function to find the average of values in a list (should really be a built-in function in Python by now)
    return round(sum(var)/len(var),2)

def calc_avg():  # function that averages ping_avg_list's values and appends the average to ping_list
    ping_list.append(avg(ping_avg_list) if len(ping_avg_list) != 0  else "N/A")

def display_results():  # function to output results to console
    if ping_list[-1] != "N/A":
        if ping_list[-1] < 150:
            result1 = 2
        elif 150 <= ping_list[-1] < 400:
            result1 = 3
        else:
            result1 = 1
        if len(ping_list) > 6:
            ping_list.pop(0)
        avg_ping = avg(ping_list)
        if avg_ping < 150:
            result2 = 2
        elif 150 <= avg_ping < 400:
            result2 = 3
        else:
            result2 = 1
            
        os.system(f'title "\rYES!!! | {ping_list[-1]}ms"')
        output = f"""    Internet:  \033[1;92mYES!!!\033[0m
----------------------------------------
Current Ping:  \033[1;9{result1}m{ping_list[-1]:,.2f}ms\033[0m
Average Ping:  \033[1;9{result2}m{avg_ping:,.2f}ms\033[0m
  (in last {len(ping_list)*5} seconds)\033[0m"""
        cls()
        print(output)
    else:
        os.system('title "\rNO!!!"')
        output = f"""    Internet:  \033[1;91mNO!!!\033[0m
----------------------------------------"""
        cls()
        print(output)
        ping_list.clear()

def set_console_size():  # function to format console window
    cols = 44
    lines = 8
    os.system(f'mode con: cols={cols} lines={lines}') 

def main():  # main function to run everything
    cls()
    set_console_size()
    while True:
        if int(time.time()) % 5 == 0:
            init_threads()
            if len(continue_checklist) == len(websites):
                continue_checklist.clear()
                calc_avg()
                display_results()
                time.sleep(1)
            else:
                time.sleep(0.5)
        else:
            time.sleep(0.5)
        
if __name__ == "__main__":  # main script body
    main()
