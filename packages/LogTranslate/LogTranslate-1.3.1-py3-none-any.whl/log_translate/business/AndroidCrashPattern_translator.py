import re
from typing import List, Dict

from log_translate.data_struct import Log, Level, log_o
from log_translate.globals import remember_dict, remember_current_pid, remember_list
from log_translate.log_translator import TagPatternTranslator

anr_patten = (r" *(PID|Reason|Parent|Frozen|Load):.*|CPU usage from.*| *\d+% \d+/.*"
              r"| *\d+% TOTAL:.*|.*?Output from /.*| *(some|full) avg.*")


class CrashPatternTranslator(TagPatternTranslator):
    def __init__(self):
        super().__init__({
            r"AndroidRuntime|System.err.*|DEBUG.?": CrashLogMsgTranslator(),
            "ActivityManager": ActivityManager(),
            r"am_anr|am_kill|am_proc_start": event_crash
        })


def event_crash(tag, msg):
    if "am_proc_start" == tag:
        # am_proc_start: [0,12735,10003,com.example.myapplication,next-top-activity,{com.example.myapplication/com.example.myapplication.MainActivity}]
        result = re.search("\d+,\d+,\d+,(.*?\..*?),", msg)
        if result:
            if result.group(1) in remember_dict["packages"]:
                return Log(translated=f" {tag} 𓆣 {msg} ", level=Level.i)
        return None
    #  [0,12735,com.example.myapplication,900,remove task]
    result = re.search("\d+,\d+,(.*?\..*?),", msg)
    if result:
        if result.group(1) in remember_dict["packages"]:
            return Log(translated=f" {tag} 𓆣 {msg} ", level=Level.e)
    return None


class ActivityManager:
    def __init__(self):
        self.msg_check = None

    def translate(self, tag, msg):
        if "ANR in" in msg:
            #     ActivityManager: ANR in com.example.myapplication (com.example.myapplication/.MainActivity)
            result = re.search("in (.*?) ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    self.msg_check = lambda x: True if re.match(anr_patten, x, re.IGNORECASE) else False
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
                else:
                    self.msg_check = None
                    return None
        if "Start proc" in msg:
            self.msg_check = None
            #     ActivityManager: Killing 12939:com.example.myapplication/u0a3 (adj 700): stop com.example.myapplicati
            result = re.search(":(.*?)/", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if "Process" in msg and "has died" in msg:
            self.msg_check = None
            # Process com.example.myapplication (pid 12383) has died
            result = re.search(r"Process (.*?) \(", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if "Killing" in msg:
            self.msg_check = None
            # Killing 14058:com.example.myapplication/u0a3 (adj 905): remove task
            result = re.search(":(.*?)/", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if "Force stopping" in msg:
            self.msg_check = None
            # 应用详情中强制停止
            # Force stopping com.example.myapplication appid=10003 user=0: from pid 2276|40|F|M:0,0
            result = re.search("stopping (.*?) ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if self.msg_check:
            if self.msg_check(msg):
                return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
            # else:
            #     self.msg_check = None
        return None


class CrashLogMsgTranslator:
    def translate(self, tag, msg):
        # DEBUG   : Process name is com.heytap.health:transport, not key_process
        if "Process name is " in msg:
            result = re.search("is (.*), ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    remember_list("crash_pids", remember_current_pid())
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        # AndroidRuntime: Process: com.heytap.health, PID: 30260
        if "Process: " in msg:
            # 开始需要收集日志
            result = re.search("Process: (.*), ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    remember_list("crash_pids", remember_current_pid())
                    return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if remember_current_pid() in remember_list("crash_pids"):
            return Log(translated=f"{tag} 𓆣 {msg} ", level=Level.e)
        if tag.startswith("System.err") and remember_current_pid() in remember_list("sys_err_pids"):
            # system.err不会导致奔溃，在能解析日志的进程有此日志都打印
            return Log(translated=" %s ⚠ %s " % (tag, msg), level=Level.w)
        return None


def process_dict(my_dict: Dict[str, int]):
    # 对字典进行操作
    for key, value in my_dict.items():
        print(key, value)


def remember_system_err_pid():
    remember_list("sys_err_pids", remember_current_pid())


if __name__ == '__main__':
    print(ActivityManager().msg_check(" Reason: 12485"))
    print(ActivityManager().msg_check("   33% 2276/system_server: 20% user + 12% kernel / faults: 39485 minor 9 m"))
    print(ActivityManager().msg_check(" 27% TOTAL: 13% user + 11% kernel + 0.3% iowait + 1.4% irq + 0.2% softi"))
    print(re.compile(".*Task").match("aaTas8km"))
    print(CrashPatternTranslator().translate("FATAL EION", "你好"))
