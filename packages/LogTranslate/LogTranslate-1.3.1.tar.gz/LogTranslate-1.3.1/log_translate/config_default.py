from log_translate.business.AndroidCrashPattern_translator import CrashPatternTranslator
from log_translate.business.bluetooth_translator import BluetoothTranslator
from log_translate.globals import remember_dict
from log_translate.log_translator import SysLogTranslator

remember_dict["packages"]=["com.heytap.health.international","com.heytap.health:transport","com.example.myapplication"]
translators = [SysLogTranslator(tag_translators=[BluetoothTranslator(), CrashPatternTranslator()])]