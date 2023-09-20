import os
import sys
# TODO(Pavel): Не забыть поставить точку
from .parse import extract_includes, insert_includes
from .settings import CPP_STD_LIBS, FLAGS


def sort_all(includes):
    res_includes = {key: [] for key in CPP_STD_LIBS}
    for include in includes:
        is_appended = False
        for lib_type in CPP_STD_LIBS:
            if include[0] == '"':
                res_includes['Local'].append(include)
                is_appended = True
                break
            elif include[1:-1] in CPP_STD_LIBS[lib_type]:
                res_includes[lib_type].append(include)
                is_appended = True
                break
        if not is_appended:
            res_includes['External'].append(include)
    for key in res_includes:
        res_includes[key] = list(set(res_includes[key]))
        res_includes[key].sort()
    return res_includes


def get_files(directory: str = '.',
              flags: "list | None" = None,
              files: "list | None" = None) -> list:
    if flags is None:
        flags = []
    if files is None:
        files = []

    for file in os.listdir(directory):
        path = f"{directory}/{file}"
        if os.path.isdir(path) and '-r' in flags or '--recursive' in flags:
            get_files(path, flags, files)
        elif file.split('.')[-1] in ('c', 'cpp', 'h', 'hpp'):
            if '-ls' in flags:
                print(f'Add to cisorting list {path}')
            files.append(path)
    return files


def is_correct_flags(flags: list) -> bool:
    for flag in flags:
        if flag not in FLAGS:
            print(
                f'Flag "{flag}" is incorrect!\n'
                f'Try:\n\tcisort --help'
            )
            return False
    return True


def cisort():
    args = sys.argv[1:]

    if '-h' in args or '--help' in args:
        print(
            'Using:\n\n'
            '\tcisort [flags] [path]\n\n'
            'Flags:\n'
            '\t-r --recursive - recursive searching C/C++ files\n'
            '\t-c --comments - add comments to sorted blocks\n'
            '\t-ls - show info about sorted files\n'
            '\t-h --help - to get help\n'
        )
        return

    if sys.argv[-1][0] == '-' or not args:
        print('Start cisearching...')
        files = get_files(flags=args)
    elif is_correct_flags(args[:-1]):
        print('Start cisearching...')
        files = get_files(directory=args[-1], flags=args[:-1])
    else:
        return

    print('Start cisorting...')
    for file in files:
        if '-ls' in args:
            print(f'Cisorting {file}')
        insert_includes(sort_all(extract_includes(file)), file, args)
    print(f'{len(files)} files are cisorted!')


if __name__ == '__main__':
    cisort()
