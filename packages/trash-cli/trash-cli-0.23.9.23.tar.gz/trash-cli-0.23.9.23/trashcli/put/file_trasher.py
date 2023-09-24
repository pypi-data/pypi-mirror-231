# Copyright (C) 2007-2023 Andrea Francia Trivolzio(PV) Italy
from typing import Dict

from trashcli.fstab.volume_of import VolumeOf
from trashcli.put.fs.parent_realpath import ParentRealpath
from trashcli.put.fs.volume_of_parent import VolumeOfParent
from trashcli.put.my_logger import MyLogger, LogData
from trashcli.put.reporter import TrashPutReporter
from trashcli.put.trash_directories_finder import TrashDirectoriesFinder
from trashcli.put.trash_file_in import TrashFileIn
from trashcli.put.trash_result import TrashResult
from trashcli.put.trashee import Trashee


class FileTrasher:

    def __init__(self,
                 volumes,  # type: VolumeOf
                 trash_directories_finder,  # type: TrashDirectoriesFinder
                 parent_realpath,  # type: ParentRealpath
                 logger,  # type: MyLogger
                 reporter,  # type: TrashPutReporter
                 trash_file_in,  # type: TrashFileIn
                 volume_of_parent,  # type: VolumeOfParent
                 ):  # type: (...) -> None
        self.volumes = volumes
        self.trash_directories_finder = trash_directories_finder
        self.parent_realpath = parent_realpath
        self.logger = logger
        self.reporter = reporter
        self.trash_file_in = trash_file_in
        self.volume_of_parent = volume_of_parent or volume_of_parent

    def trash_file(self,
                   path,  # type: str
                   forced_volume,
                   user_trash_dir,
                   home_fallback,
                   result,  # type: TrashResult
                   environ,  # type: Dict[str, str]
                   uid,  # type: int
                   log_data,  # type: LogData
                   ):
        volume_of_file_to_be_trashed = forced_volume or \
                                       self.volume_of_parent.volume_of_parent(
                                           path)
        file_be_trashed = Trashee(path, volume_of_file_to_be_trashed)
        candidates = self.trash_directories_finder. \
            possible_trash_directories_for(volume_of_file_to_be_trashed,
                                           user_trash_dir, environ, uid,
                                           home_fallback)
        self.reporter.volume_of_file(volume_of_file_to_be_trashed, log_data)
        file_has_been_trashed = False
        for candidate in candidates:
            file_has_been_trashed = file_has_been_trashed or \
                                    self.trash_file_in.trash_file_in(candidate,
                                                                     log_data,
                                                                     environ,
                                                                     file_be_trashed)
            if file_has_been_trashed: break

        if not file_has_been_trashed:
            result = result.mark_unable_to_trash_file()
            self.reporter.unable_to_trash_file(path, log_data)

        return result
