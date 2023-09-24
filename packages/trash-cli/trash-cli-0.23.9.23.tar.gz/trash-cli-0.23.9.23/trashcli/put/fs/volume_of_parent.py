from trashcli.fstab.volume_of import VolumeOf
from trashcli.put.fs.parent_realpath import ParentRealpath


class VolumeOfParent:
    def __init__(self,
                 volumes,  # type: VolumeOf
                 parent_realpath,  # type: ParentRealpath
                 ):
        self.volumes = volumes
        self.parent_realpath = parent_realpath

    def volume_of_parent(self, path):
        parent_realpath = self.parent_realpath.parent_realpath(path)
        return self.volumes.volume_of(parent_realpath)
