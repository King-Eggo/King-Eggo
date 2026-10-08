#!/usr/bin/env python3
import time
import sys
import random

# Color formatting for terminal output
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# 50 Commands with 2 levels each = 100 Questions total
LEVELS = [
    # 1. ls
    {
        "q": "Level 1: What command lists files and directories in the current folder?",
        "ans": ["ls"],
        "hint": "Short for 'list'."
    },
    {
        "q": "Level 2: What command lists ALL files, including hidden ones (starting with .)?",
        "ans": ["ls -a", "ls -a ", "ls -la", "ls -al", "ls -l -a"],
        "hint": "Combine 'ls' with the flag for 'all' (-a)."
    },

    # 2. cd
    {
        "q": "Level 3: What command is used to change the current directory?",
        "ans": ["cd"],
        "hint": "Short for 'change directory'."
    },
    {
        "q": "Level 4: What command takes you directly back to your home directory?",
        "ans": ["cd", "cd ~", "cd $HOME"],
        "hint": "Either 'cd' alone or 'cd' followed by a tilde (~)."
    },

    # 3. pwd
    {
        "q": "Level 5: What command prints the absolute path of your current working directory?",
        "ans": ["pwd"],
        "hint": "Acronym for 'Print Working Directory'."
    },
    {
        "q": "Level 6: Which command option resolves all symlinks to display the physical directory path?",
        "ans": ["pwd -P"],
        "hint": "Use 'pwd' with the flag for 'Physical'."
    },

    # 4. mkdir
    {
        "q": "Level 7: What command creates a new directory named 'test'?",
        "ans": ["mkdir test"],
        "hint": "'make directory' followed by 'test'."
    },
    {
        "q": "Level 8: What flag allows 'mkdir' to create parent directories as needed without error?",
        "ans": ["mkdir -p", "mkdir --parents"],
        "hint": "Flag '-p' stands for parents."
    },

    # 5. rm
    {
        "q": "Level 9: What command deletes a single regular file named 'file.txt'?",
        "ans": ["rm file.txt"],
        "hint": "'remove' followed by the filename."
    },
    {
        "q": "Level 10: What command combination recursively and forcefully removes a non-empty directory 'data'?",
        "ans": ["rm -rf data", "rm -fr data", "rm -r -f data"],
        "hint": "Uses the recursive (-r) and force (-f) flags."
    },

    # 6. cp
    {
        "q": "Level 11: What command copies 'file1.txt' to 'file2.txt'?",
        "ans": ["cp file1.txt file2.txt"],
        "hint": "Short for 'copy', followed by source then destination."
    },
    {
        "q": "Level 12: What option must be added to 'cp' to copy an entire directory recursively?",
        "ans": ["cp -r", "cp -R", "cp --recursive"],
        "hint": "Use the '-r' or '-R' flag."
    },

    # 7. mv
    {
        "q": "Level 13: What command renames 'old.txt' to 'new.txt'?",
        "ans": ["mv old.txt new.txt"],
        "hint": "Short for 'move'."
    },
    {
        "q": "Level 14: Which flag prevents 'mv' from overwriting an existing destination file silently?",
        "ans": ["mv -i", "mv --interactive"],
        "hint": "Flag '-i' prompts before overwriting (interactive)."
    },

    # 8. touch
    {
        "q": "Level 15: What command creates an empty file named 'notes.txt'?",
        "ans": ["touch notes.txt"],
        "hint": "Command used to update access/modification times or create empty files."
    },
    {
        "q": "Level 16: What option used with 'touch' changes ONLY the modification time of a file?",
        "ans": ["touch -m"],
        "hint": "Flag '-m' stands for modification."
    },

    # 9. cat
    {
        "q": "Level 17: What command displays the full content of a text file in the terminal?",
        "ans": ["cat"],
        "hint": "Short for 'concatenate'."
    },
    {
        "q": "Level 18: What flag allows 'cat' to display line numbers alongside text?",
        "ans": ["cat -n"],
        "hint": "Flag '-n' stands for number."
    },

    # 10. echo
    {
        "q": "Level 19: What command prints text or variable values to standard output?",
        "ans": ["echo"],
        "hint": "Prints its arguments to the terminal screen."
    },
    {
        "q": "Level 20: What flag enables interpretation of backslash escapes (like \\n) in 'echo'?",
        "ans": ["echo -e"],
        "hint": "Flag '-e' enables escape sequence interpretation."
    },

    # 11. grep
    {
        "q": "Level 21: What command searches for lines matching a pattern within files?",
        "ans": ["grep"],
        "hint": "Global Regular Expression Print."
    },
    {
        "q": "Level 22: What flag makes 'grep' perform a case-insensitive search?",
        "ans": ["grep -i"],
        "hint": "Flag '-i' ignores case distinction."
    },

    # 12. find
    {
        "q": "Level 23: What command walks directory trees to locate files matching specific criteria?",
        "ans": ["find"],
        "hint": "Primary utility for searching files in directory hierarchies."
    },
    {
        "q": "Level 24: What 'find' expression matches files specifically by filename pattern (case-sensitive)?",
        "ans": ["-name", "find -name"],
        "hint": "Used like: find . -name '*.txt'"
    },

    # 13. chmod
    {
        "q": "Level 25: What command changes read, write, and execute permissions on files?",
        "ans": ["chmod"],
        "hint": "Short for 'change mode'."
    },
    {
        "q": "Level 26: What numeric command grants full permissions (rwx) to user, group, and others?",
        "ans": ["chmod 777", "chmod 777 file"],
        "hint": "Binary 111 = 7 for each permission tier."
    },

    # 14. chown
    {
        "q": "Level 27: What command changes user ownership of a file?",
        "ans": ["chown"],
        "hint": "Short for 'change owner'."
    },
    {
        "q": "Level 28: What syntax sets user 'alice' and group 'admin' on 'file.txt' using chown?",
        "ans": ["chown alice:admin file.txt"],
        "hint": "Format is 'user:group filename'."
    },

    # 15. sudo
    {
        "q": "Level 29: What command prefixes commands to run them with superuser (root) privileges?",
        "ans": ["sudo"],
        "hint": "SuperUser DO."
    },
    {
        "q": "Level 30: What 'sudo' flag opens an interactive superuser shell session?",
        "ans": ["sudo -i", "sudo -s", "sudo su"],
        "hint": "Flag '-i' or '-s' provides a root shell."
    },

    # 16. df
    {
        "q": "Level 31: What command displays filesystem disk space usage?",
        "ans": ["df"],
        "hint": "'Disk Free'."
    },
    {
        "q": "Level 32: What flag renders 'df' output in human-readable units (e.g., MB, GB)?",
        "ans": ["df -h"],
        "hint": "Flag '-h' for human-readable."
    },

    # 17. du
    {
        "q": "Level 33: What command estimates disk space usage for files and directories?",
        "ans": ["du"],
        "hint": "'Disk Usage'."
    },
    {
        "q": "Level 34: What flag combination displays a human-readable total summary size of a folder?",
        "ans": ["du -sh", "du -hs"],
        "hint": "Combines '-s' (summary) and '-h' (human-readable)."
    },

    # 18. ps
    {
        "q": "Level 35: What command reports a snapshot of currently active processes?",
        "ans": ["ps"],
        "hint": "Short for 'process status'."
    },
    {
        "q": "Level 36: What standard syntax option set with 'ps' lists every process on the system in detail?",
        "ans": ["ps aux", "ps -ef"],
        "hint": "Commonly used as 'ps aux' or 'ps -ef'."
    },

    # 19. top
    {
        "q": "Level 37: What default utility displays dynamic, real-time Linux processes and CPU/memory usage?",
        "ans": ["top"],
        "hint": "Standard interactive task manager."
    },
    {
        "q": "Level 38: Inside 'top', what keypress sorts running processes by memory usage?",
        "ans": ["M", "m", "shift+m"],
        "hint": "Press uppercase 'M'."
    },

    # 20. kill
    {
        "q": "Level 39: What command terminates a process by specifying its PID?",
        "ans": ["kill"],
        "hint": "Sends a signal to a process (default SIGTERM)."
    },
    {
        "q": "Level 40: What signal number forces immediate, non-catchable process termination (SIGKILL)?",
        "ans": ["9", "-9", "SIGKILL"],
        "hint": "Used as 'kill -9 <PID>'."
    },

    # 21. head
    {
        "q": "Level 41: What command outputs the beginning section (first 10 lines) of a file?",
        "ans": ["head"],
        "hint": "Opposite of 'tail'."
    },
    {
        "q": "Level 42: How do you show exactly the first 5 lines of 'data.txt' using 'head'?",
        "ans": ["head -n 5 data.txt", "head -5 data.txt"],
        "hint": "Use '-n 5' or '-5'."
    },

    # 22. tail
    {
        "q": "Level 43: What command displays the last lines of a text file?",
        "ans": ["tail"],
        "hint": "Opposite of 'head'."
    },
    {
        "q": "Level 44: What flag allows 'tail' to output appended data live as a log file grows?",
        "ans": ["tail -f", "tail --follow"],
        "hint": "Flag '-f' stands for follow."
    },

    # 23. tar
    {
        "q": "Level 45: What utility manipulates archived collections of files?",
        "ans": ["tar"],
        "hint": "Tape ARchive."
    },
    {
        "q": "Level 46: What flag string extracts a gzipped tar archive (tar.gz)?",
        "ans": ["-xvf", "xvf", "-xzf", "xzf", "-zxvf", "zxvf"],
        "hint": "Extract (x), gzip (z), verbose (v), file (f)."
    },

    # 24. gzip
    {
        "q": "Level 47: What default Linux single-file compression utility creates .gz files?",
        "ans": ["gzip"],
        "hint": "GNU zip."
    },
    {
        "q": "Level 48: What flag uncompresses a file using 'gzip'?",
        "ans": ["gzip -d", "gzip --decompress", "gzip -d "],
        "hint": "Flag '-d' decompress (or use gunzip)."
    },

    # 25. history
    {
        "q": "Level 49: What command prints the list of previously executed commands?",
        "ans": ["history"],
        "hint": "Displays shell history list."
    },
    {
        "q": "Level 50: What shortcut syntax re-executes command number 42 from history?",
        "ans": ["!42"],
        "hint": "Exclamation mark followed by line number."
    },

    # 26. clear
    {
        "q": "Level 51: What command clears the terminal screen buffer?",
        "ans": ["clear"],
        "hint": "Wipes screen output. Shortcut Ctrl+L also works."
    },
    {
        "q": "Level 52: What keyboard shortcut clears terminal screen in Bash?",
        "ans": ["ctrl+l", "ctrl + l", "ctrl-l"],
        "hint": "Control key plus the letter L."
    },

    # 27. alias
    {
        "q": "Level 53: What command defines custom shortcuts for commands in shell?",
        "ans": ["alias"],
        "hint": "Example: alias ll='ls -la'"
    },
    {
        "q": "Level 54: What command removes an established shell shortcut alias?",
        "ans": ["unalias"],
        "hint": "Prefix 'un' to 'alias'."
    },

    # 28. wget
    {
        "q": "Level 55: What non-interactive network downloader fetches files via HTTP, HTTPS, or FTP?",
        "ans": ["wget"],
        "hint": "World Wide Web 'get'."
    },
    {
        "q": "Level 56: What flag allows 'wget' to resume a partially downloaded file?",
        "ans": ["wget -c", "wget --continue"],
        "hint": "Flag '-c' stands for continue."
    },

    # 29. curl
    {
        "q": "Level 57: What command transfers data to or from a server using protocols like HTTP, REST, or FTP?",
        "ans": ["curl"],
        "hint": "Client URL."
    },
    {
        "q": "Level 58: What flag tells 'curl' to follow HTTP redirects (301/302 responses)?",
        "ans": ["curl -L", "curl --location"],
        "hint": "Flag '-L' follows location headers."
    },

    # 30. ssh
    {
        "q": "Level 59: What protocol/command provides encrypted remote login to remote systems?",
        "ans": ["ssh"],
        "hint": "Secure Shell."
    },
    {
        "q": "Level 60: What flag allows specifying a non-standard SSH connection port (e.g., 2222)?",
        "ans": ["ssh -p", "ssh -p 2222"],
        "hint": "Flag '-p' specifies port."
    },

    # 31. scp
    {
        "q": "Level 61: What command transfers files securely between hosts over SSH?",
        "ans": ["scp"],
        "hint": "Secure Copy Protocol."
    },
    {
        "q": "Level 62: What flag allows 'scp' to recursively copy directories?",
        "ans": ["scp -r", "scp -P"],
        "hint": "Flag '-r' enables recursive directory copy."
    },

    # 32. ping
    {
        "q": "Level 63: What network command sends ICMP ECHO_REQUEST packages to verify host reachability?",
        "ans": ["ping"],
        "hint": "Tests network connectivity to an IP/domain."
    },
    {
        "q": "Level 64: What flag limits 'ping' to send only a specific number of requests before exiting?",
        "ans": ["ping -c"],
        "hint": "Flag '-c' stands for count."
    },

    # 33. systemctl
    {
        "q": "Level 65: What command inspects and controls the systemd system and service manager?",
        "ans": ["systemctl"],
        "hint": "System control command."
    },
    {
        "q": "Level 66: What full command starts a service named 'nginx' using systemctl?",
        "ans": ["systemctl start nginx", "sudo systemctl start nginx"],
        "hint": "'systemctl [action] [service]'."
    },

    # 34. wc
    {
        "q": "Level 67: What utility counts lines, words, and characters in a file?",
        "ans": ["wc"],
        "hint": "Word Count."
    },
    {
        "q": "Level 68: What flag restricts 'wc' to print ONLY the line count?",
        "ans": ["wc -l"],
        "hint": "Flag '-l' stands for lines."
    },

    # 35. sort
    {
        "q": "Level 69: What command sorts lines of text files alphanumerically?",
        "ans": ["sort"],
        "hint": "Arranges data in order."
    },
    {
        "q": "Level 70: What flag forces 'sort' to perform a numerical sort rather than lexicographical?",
        "ans": ["sort -n"],
        "hint": "Flag '-n' stands for numeric."
    },

    # 36. uniq
    {
        "q": "Level 71: What command filters out repeated adjacent lines from text stream?",
        "ans": ["uniq"],
        "hint": "Short for 'unique'."
    },
    {
        "q": "Level 72: What flag causes 'uniq' to count line occurrences?",
        "ans": ["uniq -c"],
        "hint": "Flag '-c' stands for count."
    },

    # 37. sed
    {
        "q": "Level 73: What stream editor utility modifies/replaces text patterns in a stream non-interactively?",
        "ans": ["sed"],
        "hint": "Stream Editor."
    },
    {
        "q": "Level 74: What expression syntax replaces 'foo' with 'bar' globally in sed?",
        "ans": ["s/foo/bar/g", "sed 's/foo/bar/g'"],
        "hint": "Uses 's/old/new/g'."
    },

    # 38. awk
    {
        "q": "Level 75: What powerful text processing pattern-matching command uses '{print $1}' blocks?",
        "ans": ["awk"],
        "hint": "Named after authors Aho, Weinberger, and Kernighan."
    },
    {
        "q": "Level 76: What flag sets a custom field delimiter character in 'awk'?",
        "ans": ["awk -F"],
        "hint": "Flag '-F' followed by delimiter (e.g., -F':')."
    },

    # 39. uname
    {
        "q": "Level 77: What command prints system and OS kernel information?",
        "ans": ["uname"],
        "hint": "Unix Name."
    },
    {
        "q": "Level 78: What flag tells 'uname' to output ALL available system information?",
        "ans": ["uname -a"],
        "hint": "Flag '-a' stands for all."
    },

    # 40. whoami
    {
        "q": "Level 79: What command prints the effective username of the currently logged-in user?",
        "ans": ["whoami"],
        "hint": "Literal phrase 'who am i'."
    },
    {
        "q": "Level 80: What alternative command displays logged-in user ID, group IDs, and memberships?",
        "ans": ["id"],
        "hint": "Two-letter command showing UID and GIDs."
    },

    # 41. uptime
    {
        "q": "Level 81: What command reports how long the system has been running alongside load averages?",
        "ans": ["uptime"],
        "hint": "Measures continuous operating time."
    },
    {
        "q": "Level 82: What flag displays uptime in a pretty, human-friendly format?",
        "ans": ["uptime -p"],
        "hint": "Flag '-p' stands for pretty."
    },

    # 42. free
    {
        "q": "Level 83: What utility displays total, used, and available system RAM memory?",
        "ans": ["free"],
        "hint": "Shows memory state."
    },
    {
        "q": "Level 84: What flag renders 'free' memory metrics in human-readable output (MB/GB)?",
        "ans": ["free -h"],
        "hint": "Flag '-h' for human-readable."
    },

    # 43. cron / crontab
    {
        "q": "Level 85: What command edits the scheduled task table for the current user?",
        "ans": ["crontab -e"],
        "hint": "Uses 'crontab' with edit flag '-e'."
    },
    {
        "q": "Level 86: In crontab schedule syntax (* * * * *), how many field asterisks are present?",
        "ans": ["5"],
        "hint": "Minute, Hour, Day-of-month, Month, Day-of-week."
    },

    # 44. ln
    {
        "q": "Level 87: What command creates links between files?",
        "ans": ["ln"],
        "hint": "Short for 'link'."
    },
    {
        "q": "Level 88: What flag creates a symbolic (soft) link instead of a hard link?",
        "ans": ["ln -s"],
        "hint": "Flag '-s' stands for symbolic."
    },

    # 45. diff
    {
        "q": "Level 89: What command compares two files line-by-line and highlights differences?",
        "ans": ["diff"],
        "hint": "Short for 'difference'."
    },
    {
        "q": "Level 90: What flag produces unified context output format in 'diff'?",
        "ans": ["diff -u"],
        "hint": "Flag '-u' stands for unified."
    },

    # 46. hostname
    {
        "q": "Level 91: What command displays or sets the system host network name?",
        "ans": ["hostname"],
        "hint": "Prints device network name."
    },
    {
        "q": "Level 92: What flag displays all IP addresses assigned to the host?",
        "ans": ["hostname -I", "hostname -i"],
        "hint": "Capital or lowercase '-I'."
    },

    # 47. env
    {
        "q": "Level 93: What command prints all exported environment variables or runs a program in a modified environment?",
        "ans": ["env", "printenv"],
        "hint": "Short for 'environment'."
    },
    {
        "q": "Level 94: Which environment variable stores search paths for executable commands?",
        "ans": ["PATH", "$PATH"],
        "hint": "Capital word PATH."
    },

    # 48. lsof
    {
        "q": "Level 95: What utility command lists open files and the processes that opened them?",
        "ans": ["lsof"],
        "hint": "List Open Files."
    },
    {
        "q": "Level 96: What flag combination with 'lsof' finds processes listening on port 80?",
        "ans": ["lsof -i :80", "lsof -i:80"],
        "hint": "Flag '-i' followed by ':80'."
    },

    # 49. nslookup / dig
    {
        "q": "Level 97: What DNS lookup command utility performs domain name queries (e.g. dig or nslookup)?",
        "ans": ["dig", "nslookup"],
        "hint": "Domain Information Groper ('dig') or 'nslookup'."
    },
    {
        "q": "Level 98: In 'dig', what query type argument requests MX (Mail Exchange) records?",
        "ans": ["MX", "mx", "dig mx"],
        "hint": "Two letter code for mail servers."
    },

    # 50. reboot / shutdown
    {
        "q": "Level 99: What immediate command safely restarts or powers down the system?",
        "ans": ["reboot", "shutdown"],
        "hint": "Restarts operating system."
    },
    {
        "q": "Level 100: What flag/argument used with 'shutdown' powers down the machine immediately?",
        "ans": ["shutdown -h now", "shutdown now", "-h now", "now"],
        "hint": "Uses 'now' as time argument."
    }
]

def matrix_rain_surprise():
    """Fun Surprise: Terminal Matrix Code Rain animation on game completion!"""
    sys.stdout.write("\033[2J\033[1;1H") # Clear screen
    print(f"{CYAN}{BOLD}=====================================================")
    print("      CONGRATULATIONS! YOU BEAT ALL 100 LEVELS!      ")
    print(f"====================================================={RESET}\n")
    time.sleep(1.5)
    print(f"{YELLOW}Initiating superuser terminal override sequence...{RESET}\n")
    time.sleep(2)

    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$&%*@!"
    width = 60
    
    print(GREEN)
    for _ in range(80):  # Matrix rain effect
        line = "".join(random.choice(symbols) if random.random() > 0.4 else " " for _ in range(width))
        print(f"   {line}")
        time.sleep(0.04)

    print(RESET)
    time.sleep(0.5)

    print(f"{CYAN}{BOLD}")
    print(r"  ____  _   _ ____   ____ _____ ____ ____  ")
    print(r" / ___|| | | / ___| / ___| ____/ ___/ ___| ")
    print(r" \___ \| | | \___ \| |  _|  _| \___ \___ \ ")
    print(r"  ___) | |_| |___) | |_| | |___ ___) |__) |")
    print(r" |____/ \___/|____/ \____|_____|____/____/ ")
    print(f"{RESET}")
    print(f"{YELLOW}{BOLD}    YOU ARE OFFICIALLY A LINUX TERMINAL MASTER!{RESET}\n")
    print("   🎁 SURPRISE: You unlocked Root Access to the Universe!")
    print("   Run `sudo rm -rf /` in real life? Never! You know better now.\n")

def run_quiz():
    sys.stdout.write("\033[2J\033[1;1H")
    print(f"{BOLD}{CYAN}=======================================================")
    print("   🐧 THE ULTIMATE 100-LEVEL LINUX COMMAND CHALLENGE 🐧  ")
    print(f"======================================================={RESET}")
    print("Test your command-line mastery across 50 essential Linux tools.")
    print("Type 'hint' at any prompt for help. Type 'exit' to quit.\n")
    
    score = 0
    total_levels = len(LEVELS)

    for i, level in enumerate(LEVELS):
        print(f"\n{BOLD}--- Question {i+1} / {total_levels} ---{RESET}")
        print(f"{CYAN}{level['q']}{RESET}")

        while True:
            user_input = input(f"{BOLD}Your Answer > {RESET}").strip()

            if user_input.lower() == "exit":
                print(f"\n{YELLOW}Quiz exited early. Final Score: {score}/{i}{RESET}")
                return

            if user_input.lower() == "hint":
                print(f"{YELLOW}💡 HINT: {level['hint']}{RESET}")
                continue

            # Check if answer matches any acceptable answers
            if any(user_input.lower() == valid_ans.lower() for valid_ans in level["ans"]):
                print(f"{GREEN}✓ Correct!{RESET}")
                score += 1
                break
            else:
                print(f"{RED}✗ Incorrect.{RESET} Acceptable answer: {GREEN}{level['ans'][0]}{RESET}")
                break

    # Completed all 100 levels
    matrix_rain_surprise()

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz cancelled.")
