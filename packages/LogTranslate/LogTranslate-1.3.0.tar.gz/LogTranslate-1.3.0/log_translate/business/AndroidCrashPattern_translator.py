import re
from typing import List, Dict

from log_translate.data_struct import Log, Level, log_o
from log_translate.globals import remember_dict, remember_current_pid, remember_list
from log_translate.log_translator import TagPatternTranslator


class CrashPatternTranslator(TagPatternTranslator):
    def __init__(self):
        super().__init__({
            r"AndroidRuntime|System.err.*|DEBUG.?": CrashLogMsgTranslator()
        })


class CrashLogMsgTranslator:
    def translate(self, tag, msg):
        # DEBUG   : Process name is com.heytap.health:transport, not key_process
        if "Process name is " in msg:
            remember_list("crash_pids", remember_current_pid())
            result = re.search("is (.*), ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=" %s 𓆣 %s " % (tag, msg), level=Level.e)
        # AndroidRuntime: Process: com.heytap.health, PID: 30260
        if "Process: " in msg:
            remember_list("crash_pids", remember_current_pid())
            # 开始需要收集日志
            result = re.search("Process: (.*), ", msg)
            if result:
                if result.group(1) in remember_dict["packages"]:
                    return Log(translated=" %s 𓆣 %s " % (tag, msg), level=Level.e)
        if remember_current_pid() in remember_list("crash_pids"):
            return Log(translated=" %s 𓆣 %s " % (tag, msg), level=Level.e)
        if tag.startswith("System.err") and remember_current_pid() in remember_list("pids"):
            # system.err不会导致奔溃，在能解析日志的进程有此日志都打印
            return Log(translated=" %s ⚠ %s " % (tag, msg), level=Level.w)
        return None


def process_dict(my_dict: Dict[str, int]):
    # 对字典进行操作
    for key, value in my_dict.items():
        print(key, value)


if __name__ == '__main__':
    print(re.compile(".*Task").match("aaTas8km"))
    print(CrashPatternTranslator().translate("FATAL EION", "你好"))
