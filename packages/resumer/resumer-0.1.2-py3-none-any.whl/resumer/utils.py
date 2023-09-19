
import logging
import os
import subprocess

def rough_check_drill_string(string :str):
    if "{" not in string:
        return False
    
    if "}" not in string:
        return False
    
    if ":" not in string:
        return False

    return True

def get_drill_vars(string : str, logger : logging.Logger = None):
    var_details : dict = {}
    raw_string = ""
    
    temp_key  =""
    temp_value = ""
    pass_colon = False
    bracket_open = False
    for c in string:
        match c:
            case "{" if bracket_open:
                logger.error("Found { within {")
                return None
            case "}" if not bracket_open:
                logger.error("Found } within {")
                return None
            case "{":
                bracket_open = True
                raw_string += c
            case "}" if not pass_colon:
                logger.error("didnt find :")
                return None
            case "}":
                bracket_open = False
                var_details[temp_key] = temp_value
                temp_key = ""
                temp_value = ""
                pass_colon = False
            case ":":
                pass_colon = True
                raw_string += temp_key + "}"    
            case str(c) if not pass_colon and bracket_open:
                temp_key += c
            case str(c) if pass_colon and bracket_open:
                temp_value += c
            case _:
                raw_string += c

    return var_details, raw_string


def check_invalid_cmdlet(response : bytes):
    if b"invalid cmdlet" in response:
        return True
    if b"is not recognized as an internal or external command" in response:
        return True
    return False

def check_installed(app : str, use_version : bool = True) -> bool:
    args = [app]
    if use_version:
        args += ["--version"]
    try:
        # block output
        response = subprocess.check_output(args, stderr=subprocess.STDOUT)
        if check_invalid_cmdlet(response):
            return False
        
        return True
    except: #noqa
        return False
    
def rename_bkup(path : str):
    if not os.path.exists(path):
        return
    
    try:
        os.rename(path, path + ".bak")
    except: # noqa
        os.remove(path + ".bak")
        os.rename(path, path + ".bak")