from io import StringIO

from typing import IO, Callable, List


class LogData:
    def __init__(self, program_name, verbose):
        self.program_name = program_name
        self.verbose = verbose


class MyLogger:
    def __init__(self,
                 stderr,  # type: IO[str]
                 ):  # type: (...) -> None
        self.stderr = stderr

    def debug(self,
              message,  # type: str
              log_data,  # type: LogData
              ):  # type: (...) -> None
        if log_data.verbose > 1:
            self.stderr.write("%s: %s\n" % (log_data.program_name, message))

    def debug_func_result(self,
                          messages_func,  # type: Callable[[], List[str]]
                          log_data,  # type: LogData
                          ):
        if log_data.verbose > 1:
            for line in messages_func():
                self.stderr.write("%s: %s\n" % (log_data.program_name, line))

    def info(self,
             message,  # type: str
             log_data,  # type: LogData
             ):  # type: (...) -> None
        if log_data.verbose > 0:
            self.stderr.write("%s: %s\n" % (log_data.program_name, message))

    def warning2(self, message, program_name):
        self.stderr.write("%s: %s\n" % (program_name, message))
