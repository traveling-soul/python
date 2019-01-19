import os
import uuid


def do_file_name(file_name):
    return str(uuid.uuid1()) + os.path.splitext(file_name)[1]

