import traceback
import time
import sys
import config
import os
from datetime import datetime

logfile = "logs/" + time.strftime("%Y-%m") + config.logfile
logfile_encoding = config.logfile_encoding

try:
        os.mkdir("logs/")

except FileExistsError:
        pass

def now():
        return datetime.utcnow().__str__()

def debug(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 6:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                        lf.write(f"[{timestamp}] [D] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 6:
                    sys.stdout.write(f"[{timestamp}] [D] {message}\n")
                    sys.stdout.flush()

        except Exception as e:
                pass
def msg(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is none else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 5:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                        lf.write(f"[{timestamp} [M] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 5:
                        sys.stdout.write(f"[{timestamp}] [M] {message}\n")
                        sys.stdout.flush()

        except Exception as e:
                pass

def info(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 4:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                        lf.write(f"[{timestamp}] [I] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 4:
                    sys.stdout.write(f"[{timestamp}] [I] {message}\n")
                    sys.stdout.flush()
        except Exception as e:
                pass

def warn(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 3:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                        lf.write(f"[{timestamp}] [W] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 3:
                    if config.exc_to_stderr:
                            sys.stderr.write(f"[{timestamp}] [W] {message}\n")
                            sys.stderr.flush()
                    else:
                            sys.stdout.write(f"[{timestamp}] [W] {message}\n")
                            sys.stdout.flush()
        except Exception as e:
                pass

warning = warn

def error(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 2:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                    lf.write(f"[{timestamp}] [E] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 2:
                        if config.exc_to_stderr:
                                sys.stderr.write(f"[{timestamp}] [E] {message}\n")
                                sys.stderr.flush()
                        else:
                                sys.stdout.write(f"[{timestamp}] [E] {message}\n")
                                sys.stdout.flush()
        except Exception as e:
                pass

def critical(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 1:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                    lf.write(f"[{timestamp}] [C] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 1:
                        if config.exc_to_stderr:
                                sys.stderr.write(f"[{timestamp}] [C] {message}\n")
                                sys.stderr.flush()
                        else:
                                sys.stdout.write(f"[{timestamp}] [C] {message}\n")
                                sys.stdout.flush()
        except Exception as e:
                pass

crit = critical

def fatal(message: str, ts: datetime = None, include_exception: bool = False) -> None:
        try:
                timestamp = now() if ts is None else ts.__str__()
                if include_exception and (sys.exc_info()[2] is not None):
                        message += "\n" + traceback.format_exc()
                if config.file_loglevel >= 0:
                        try:
                                with open(logfile, "a", encoding=logfile_encoding) as lf:
                                    lf.write(f"[{timestamp}] [F] {message}\n")
                        except:
                                pass
                if config.terminal_loglevel >= 0:
                        if config.exc_to_stderr:
                                sys.stderr.write(f"[{timestamp}] [F] {message}\n")
                                sys.stderr.flush()
                        else:
                                sys.stdout.write(f"[{timestamp}] [F] {message}\n")
                                sys.stdout.flush()
        except Exception as e:
                pass
