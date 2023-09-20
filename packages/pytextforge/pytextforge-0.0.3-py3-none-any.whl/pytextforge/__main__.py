import argparse
import os
import sys

from .file import read_file, write_file
from .forge import generate_output
from .inputs import load_data, load_json, process_data
from .messages import MessageManager

VERSION = 'v0.0.1'
MM = MessageManager()

def validate_output(outputpath: str, force: bool) -> str:
    if os.path.exists(path=outputpath):
        if force:
            os.remove(path=outputpath)
        else:
            return f'The output path[{outputpath}] already exists, use --force to force the deletion'
    try:
        f = open(file=outputpath, mode='w')
        f.close()
    except:
        return f'Cannot create the output file[{outputpath}]'
    return None

def validate_file(value: str) -> str:
    if not os.path.isfile(path=value):
        raise argparse.ArgumentTypeError(f"The template path[{value}] doesn't exist or is not a file")
    return os.path.realpath(path=value)

def __validate(value: str, load: any) -> dict:
    id, data, err = load(string=value)
    if err:
        raise argparse.ArgumentTypeError(err)
    return {'id': id, 'data': data}

def validate_data(value: str) -> dict:
    return __validate(value=value, load=load_data)

def validate_json(value: str) -> dict:
    return __validate(value=value, load=load_json)

def parse_arguments(args: list) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='TODO')
    parser.add_argument('--version', action='version', version=VERSION, \
                        help='TODO')
    parser.add_argument('--template', dest='template', type=validate_file, \
                        required=True, help='TODO')
    parser.add_argument('--output', dest='output', type=str, \
                        required=True, help='TODO')
    parser.add_argument('-d', '--data', action='append', dest='data', type=validate_data, \
                        help='TODO')
    parser.add_argument('-j', '--json', action='append', dest='data', type=validate_json, \
                        help='TODO')
    parser.add_argument('-f', '--force', action='store_true', dest='force', \
                        help='TODO')
    parser.add_argument('-v', '--verbose', action='count', default=0, dest='verbose', \
                        help='TODO')
    return parser.parse_args(args=args)

def exit_script(errorcode: int) -> None:
    if errorcode == 0:
        MM.show_success()
    else:
        MM.show_failure()
    MM.show_line()
    sys.exit(errorcode)

def main():
    args = parse_arguments(args=sys.argv[1:])
    MM.verbose = args.verbose
    err = validate_output(outputpath=args.output, force=args.force)
    if err:
        MM.show_error(msg=f'Error: {err}')
        exit_script(1)
    MM.show_title_line(title='')
    MM.show_banner(version=VERSION)
    MM.show_title_line(title='Process data')
    MM.show_verbose(msg=f'Data array: {args.data}', level=2)
    data = process_data(data=args.data)
    MM.show_verbose(msg=f'Data dict: {data}', level=2)
    MM.show_success()
    MM.show_title_line(title='Reading template')
    content, err = read_file(path=args.template)
    if err:
        MM.show_error(msg=f'Error: {err}')
        exit_script(1)
    MM.show_verbose(msg=f'Template content: {content}', level=3)
    MM.show_success()
    MM.show_title_line(title='Generate output')
    output, err = generate_output(data=data, content=content)
    if err:
        MM.show_error(msg=f'Error: {err}')
        exit_script(1)
    MM.show_verbose(msg=f'Output: {output}', level=3)
    MM.show_success()
    MM.show_title_line(title='Writing output')
    err = write_file(content=output, path=args.output)
    if err:
        MM.show_error(msg=f'Error: {err}')
        exit_script(1)
    exit_script(0)

if __name__ == '__main__':
    main()