#!/usr/bin/env python3
"""
Usage: mrs-marc.py [--no-highlight] <file.mrc> [--output <output.mrc>]

Options:
    -n --no-highlight   do not highlight console output
    -o --output <file>  output identified records to file
    -h --help           show this text
    -v --version        print program version
"""
from docopt import docopt
from mrs import mrs
from pymarc import MARCReader

# highlight console output
def highlight(target, text):
    # if we're not on the CLI for some reason, don't do anything
    if __name__ != "__main__":
        return text
    else:
        return text.replace(target, '\033[44;33m{}\033[m'.format(target))


def main(arguments):
    output = []

    with open(arguments['<file.mrc>'], 'rb') as fh:
        reader = MARCReader(fh)
        # iterate over records & then over meaningful fields in those records
        for record in reader:
            for field in [f for f in record.fields if not f.is_control_field()]:
                # see mrs documentation - https://github.com/ngeraci/mrs
                # iterate over name entities, check for problems
                data = mrs.Text(field.format_field())
                for entity in data.mrs_names:
                    name = mrs.Name(entity)
                    if name.format == "first_last":
                        if name.gender_guess not in ["female", "mostly_female"]:
                            # build list of records with potential problems
                            if arguments.get('--output') is not None:
                                output.append(record)

                            print(record.title())

                            # highlight name in context
                            if arguments.get('--no-highlight') is not None:
                                print(str(field) + '\n')
                            else:
                                print(highlight('Mrs. ' + name.text, str(field)) + '\n')

    # write output file
    if arguments.get('--output') is not None:
        with open(arguments['--output'], 'wb') as fh:
            for record in output:
                fh.write(record.as_marc())


if __name__ == '__main__':
    arguments = docopt(__doc__, version='mrs-marc 1.0.0')
    main(arguments)
