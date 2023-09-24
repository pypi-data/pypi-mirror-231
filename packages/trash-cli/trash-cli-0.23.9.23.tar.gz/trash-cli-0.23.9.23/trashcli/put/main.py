import os
import random
import sys

from trashcli.fstab.volume_of import RealVolumeOf
from trashcli.lib.my_input import MyInput
from trashcli.put.clock import RealClock
from trashcli.put.describer import Describer
from trashcli.put.dir_maker import DirMaker
from trashcli.put.file_trasher import FileTrasher
from trashcli.put.fs.parent_realpath import ParentRealpath
from trashcli.put.fs.real_fs import RealFs
from trashcli.put.fs.volume_of_parent import VolumeOfParent
from trashcli.put.gate import ClosedGate, HomeFallbackGate, SameVolumeGate
from trashcli.put.gate_impl import ClosedGateImpl, HomeFallbackGateImpl, \
    SameVolumeGateImpl
from trashcli.put.info_dir import InfoDir
from trashcli.put.my_logger import MyLogger
from trashcli.put.original_location import OriginalLocation
from trashcli.put.path_maker import PathMaker
from trashcli.put.reporter import TrashPutReporter
from trashcli.put.suffix import Suffix
from trashcli.put.trash_all import TrashAll
from trashcli.put.trash_dir_volume_reader import TrashDirVolumeReader
from trashcli.put.trash_directories_finder import TrashDirectoriesFinder
from trashcli.put.trash_directory_for_put import TrashDirectoryForPut
from trashcli.put.trash_file_in import TrashFileIn
from trashcli.put.trash_put_cmd import TrashPutCmd
from trashcli.put.trasher import Trasher
from trashcli.put.trashing_checker import TrashingChecker
from trashcli.put.user import User


def main():
    cmd = make_cmd(clock=RealClock(), fs=RealFs(),
                   my_input=MyInput(), randint=random.randint,
                   stderr=sys.stderr, volumes=RealVolumeOf())
    return cmd.run(sys.argv, os.environ, os.getuid())


def make_cmd(clock,
             fs,
             my_input, # type: MyInput
             randint,
             stderr,
             volumes):
    logger = MyLogger(stderr)
    describer = Describer(fs)
    reporter = TrashPutReporter(logger, describer)
    suffix = Suffix(randint)
    dir_maker = DirMaker(fs)
    info_dir = InfoDir(fs, logger, suffix)
    path_maker = PathMaker()
    parent_realpath = ParentRealpath(fs)
    original_location = OriginalLocation(parent_realpath, path_maker)
    trash_dir = TrashDirectoryForPut(fs,
                                     info_dir,
                                     original_location,
                                     clock)
    trash_dir_volume = TrashDirVolumeReader(volumes, fs)
    trashing_checker = TrashingChecker({
        ClosedGate: ClosedGateImpl(),
        HomeFallbackGate: HomeFallbackGateImpl(fs),
        SameVolumeGate: SameVolumeGateImpl(trash_dir_volume),
    })
    trash_file_in = TrashFileIn(fs,
                                reporter,
                                trash_dir,
                                trashing_checker,
                                dir_maker)
    volume_of_parent = VolumeOfParent(volumes, parent_realpath)
    file_trasher = FileTrasher(volumes,
                               TrashDirectoriesFinder(volumes),
                               parent_realpath,
                               logger,
                               reporter,
                               trash_file_in,
                               volume_of_parent)
    user = User(my_input, describer)
    trasher = Trasher(file_trasher, user, reporter, fs)
    trash_all = TrashAll(logger, trasher)
    return TrashPutCmd(trash_all, reporter)
