from trashcli.lib.my_input import MyInput
from trashcli.put.describer import Describer


class User:
    def __init__(self,
                 my_input,  # type: MyInput
                 describer,  # type: Describer
                 ):
        self.my_input = my_input
        self.describer = describer

    def ask_user_about_deleting_file(self, program_name, path):
        reply = self.my_input.read_input(
            "%s: trash %s '%s'? " % (program_name,
                                     self.describer.describe(path), path))
        return parse_user_reply(reply)


user_replied_no = "user_replied_no"
user_replied_yes = "user_replied_yes"


def parse_user_reply(reply):
    return {False: user_replied_no,
            True: user_replied_yes}[reply.lower().startswith("y")]
