import platform, os


def is_available() -> bool:
    kind = platform.system()
    one_api = ...
    if kind == "Windows":
        program_files = os.environ.get("ProgramFiles(x86)")
        one_api = f"{program_files}\\Intel\\oneAPI"
    elif kind == "Linux":
        one_api = "/opt/intel/oneapi"
    else:
        raise AssertionError("Unexpected branch!")

# Extremely naive check if Intel oneAPI is installed or not
    return os.path.exists(one_api)
