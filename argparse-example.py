#!/usr/bin/env python3
import argparse


class ChangelogPlaybookArguments(object):
    def __init__(self):
        self.playbook = 'changelog'

    def add_arguments_to_parser(self, parser, subparsers):
        # boilerplate, could be abstracted away into a 'PackagePlaybookArguments' class
        changelog_subparser = subparsers.add_parser(self.playbook, help=self.get_help())
        changelog_subparser.add_argument('package',
                                         metavar='package',
                                         choices=['some', 'choices'],
                                         nargs='+',
                                         help="The package to add a changelog entry for")
        # end boilerplate


        changelog_subparser.add_argument('--changelog', help="The text for the changelog entry")

    def get_help(self):
        return "The '" + self.playbook + "' command writes a RPM changelog entry for the current version and release."




class SetupArguments(object):
    def __init__(self):
        self.playbook = 'setup'

    def add_arguments_to_parser(self, parser, subparsers):
        # boilerplate, could be abstracted away into a 'PlaybookArguments' class
        subparsers.add_parser(self.playbook, help=self.get_help())

    def get_help(self):
        return "The '" + self.playbook + "' command installs packages required for a successful workflow."


class Program(object):
    def run(self, cliargs=None):
        parser = argparse.ArgumentParser()
        ## Add initial obal arguents, blah blah
        subparsers = parser.add_subparsers(dest='action', help="Which action to execute")

        ChangelogPlaybookArguments().add_arguments_to_parser(parser, subparsers)
        SetupArguments().add_arguments_to_parser(parser, subparsers)

        args = parser.parse_args(cliargs)




if __name__ == "__main__":
    Program().run()
