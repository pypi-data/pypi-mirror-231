"""
Most of the functions here are standalone
"""
import os as _os
import re as _re
from typing import (
    List as _List,
    Tuple as _Tuple,
)


def same_ext_for_all_dir_files(dir_path:str, extension:str) -> bool:
    """
    Check whether all files in `dir_path` have the same `extension`.
    Return `True` if they are all the same, and `False` if not.

    ### Conditions
    - All items in folder `dir_path` are files only; no subfolders.

    ### Params
    - `dir_path`: absolute path to the directory
    - `extension`: file type (including the dot), example: `'.txt'`, `'.py'`.

    ### Exceptions
    - `NotADirectoryError`: if `dir_path` is not a folder
    - `ValueError`: if `extension` doesn't match the regex
    - `AssertionError`: if an item in the folder is not a file

    ### Docs
    - Will return `True` when `dir_path` is empty
    - Will ignore case: `.json` matches `.JSON`, `.TxT` matches `.Txt`, and so on.
    """
    if not _os.path.isdir(dir_path): raise NotADirectoryError(f'Not a dir: {repr(dir_path)}.')
    if not _re.match(r'^\.\w+$', extension): raise ValueError(f'Invalid extension: {repr(extension)}.')
    for file in _os.listdir(dir_path):
        pth = _os.path.join(dir_path, file)
        if not _os.path.isfile(pth): raise AssertionError(f'Not a file: {repr(pth)}.')
        if not file.lower().endswith(extension.lower()): return False
    return True


def list_dir(dir_path:str, /) -> _List[_Tuple[str, str]]:
    """
    The extended version of `os.listdir`.

    @param `dir_path`: absolute path
    @returns: List of pairs of item names and the items' absolute paths,
              e.g., `[(file_name, file_abspath), (subdir_name, subdir_abspath), ...]`

    ### Exceptions
    - `NotADirectoryError`: if `dir_path` not a folder

    ### Demo
    ```
    for file_name, file_path in list_dir('/dir/abs/path'):
        pass
    for item, abspth in list_dir('/dir/abs/path'):
        pass
    for name, pth in list_dir('/dir/abs/path'):  # my favorite  ~Nicholas
        pass
    ```
    """
    if not _os.path.isdir(dir_path): raise NotADirectoryError(f'Not a dir: {repr(dir_path)}.')
    out = []
    for name in _os.listdir(dir_path):
        pth = _os.path.join(dir_path, name)
        out.append((name, pth))
    return out


def remove_all_specific_files_in(dir_path:str, file_pattern:str, recursive:bool=False) -> _List[str]:
    """
    Delete certain files within the `dir_path` folder.

    ---

    ## Params
    - `dir_path`: Absolute path to the folder
    - `file_pattern`: Regex pattern to match the files that you want to delete.
    - `recursive`: If `False`, just delete the files inside `dir_path`.

    ## Returns
    - List of deleted files' absolute paths.

    ## Docs
    - Please review the code for this function before using it.
    """
    deleted = []
    def run(pth):
        for stuff in _os.listdir(pth):
            stuff_pth = _os.path.join(pth, stuff)
            if _os.path.isdir(stuff_pth):
                if recursive: run(stuff_pth)
            else:
                if _re.match(file_pattern, stuff):
                    _os.remove(stuff_pth)
                    deleted.append(stuff_pth)
    run(dir_path)
    return deleted
