# -*- coding: utf-8 -*-
"""
from tempfile import NamedTemporaryFile
"""

import argparse
import sys

from . import __version__
from .base import Base
from .config import Config
from .ican import Ican
from .log import logger
from .exceptions import IcanException
from .exceptions import PipelineNotFound


# ===============================
#
#  CLI Class
#
# ===============================


class CLI(Base):

    RESERVED = ['ican', 'git', 'config', 'version']
    usage = """ican <COMMAND> [<ARGS>]

commands:
  bump [PART]        increment version [minor, major, patch, prerelease, build]
  init               initialize a config in the current directory
  list               list available user-defined pipelines
  pre [TOKEN]        set the prerelease string [alpha, beta, rc, dev]
  run [PIPELINE]     run the specified PIPELINE
  rollback           restore the previous version
  show [STYLE]       show version [semantic, public, pep440, git]
"""

    def __init__(self):
        """
        """
        self._register_excepthook()
        # self._arg_pop()
        self.config = Config()

        parser = argparse.ArgumentParser(usage=CLI.usage, prog="ican")
        parser.add_argument("command", help=argparse.SUPPRESS)
        parser.add_argument(
            "--version",
            action="version",
            help="display ican version",
            version=f"ican v{__version__}",
        )

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            # Unknown, look for pipelines with this name (alias)
            try:
                self.run(args.command)
            except PipelineNotFound:
                logger.error("Unrecognized command")
                parser.print_help()
                exit(1)
            except Exception as e:
                raise(e)
        elif args.command in self.RESERVED:
            parser.print_help()
            exit(1)
        else:
            getattr(self, args.command)()
            return

    def _register_excepthook(self):
        """Register our custom exception handler"""

        self._original_excepthook = sys.excepthook
        sys.excepthook = self._excepthook
        return

    def _excepthook(self, type, value, tracekback, debug=False):
        """Custom exception handler"""

        if isinstance(value, IcanException):
            if value.msg:
                value.output_method(value.msg)
            if value.e:
                for line in value.e:
                    value.output_method(line)
            if debug:
                self._original_excepthook(type, value, tracekback)
            exit_code = value.exit_code
            sys.exit(exit_code)
        else:
            self._original_excepthook(type, value, tracekback)

    def _arg_pop(self):
        """Here we will pop --verbose and --dry_run out asap,
        that way logging can be setup before we parse the config
        file, etc.
        """

        verbose = False
        dry_run = False
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "--verbose":
                verbose = True
                sys.argv.pop(i)
                break
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "--dry_run":
                dry_run = True
                sys.argv.pop(i)
                break
        logger.setup(verbose, dry_run)
        return

    def command_prep(self, parser, alias=None, user_args=False):
        # self._arg_pop()
        self.config.pre_parse()

        parser.add_argument(
            "--dry_run", help="do not write any files", action="store_true"
        )
        parser.add_argument(
            "--verbose", help="display debug information", action="store_true"
        )

        argv = sys.argv[2:]
        if alias:
            argv.insert(0, alias)

        args = parser.parse_args(argv)
        logger.setup(args.verbose, args.dry_run)
        return args

    def bump(self):
        """dispatched here with command bump"""

        parser = argparse.ArgumentParser(
            description="PART choices [major, minor, patch, [pre]release, build]",
            usage="ican bump [PART]",
        )
        parser.add_argument(
            "part",
            nargs="?",
            default="build",
            choices=[
                "major",
                "minor",
                "patch",
                "prerelease",
                "build",
                "pre",
                "beta",
                "alpha",
                "dev",
                "rc",
            ],
            help=argparse.SUPPRESS,
        )
        args = self.command_prep(parser)

        self.ican = Ican()
        self.ican.bump(args.part.lower())
        logger.verbose("bump() COMPLETE")
        return

    def list(self):
        """dispatched here with command list"""
        parser = argparse.ArgumentParser(usage="ican list")
        self.command_prep(parser)

        self.ican = Ican()
        self.ican.list()
        return

    def show(self):
        """dispatched here with command show"""

        parser = argparse.ArgumentParser(
            description="STYLE choices [semantic, public, pep440, git]",
            usage="ican show [STYLE]",
        )
        parser.add_argument(
            "style",
            nargs="?",
            default="semantic",
            choices=["semantic", "public", "pep440", "git"],
            help=argparse.SUPPRESS,
        )
        args = self.command_prep(parser)

        self.ican = Ican(only_pre_parse=True)
        self.ican.show(args.style)
        return

    def pre(self):
        """Sets the prerelease token to [alpha, beta, dev, rc]
        At the same time prerelease mode is enabled for the
        version.
        """

        parser = argparse.ArgumentParser(
            description="set the prerelease TOKEN to one of "
            "[alpha, beta, rc, dev]",
            usage="ican pre [TOKEN]",
        )
        parser.add_argument(
            "token",
            nargs="?",
            default="beta",
            choices=["alpha", "beta", "rc", "dev"],
            help=argparse.SUPPRESS,
        )
        args = self.command_prep(parser)

        self.ican = Ican(only_pre_parse=True)
        self.ican.pre(args.token)
        return

    def rollback(self):
        """in case of emergency, restore the previously
        persisted version.
        """

        parser = argparse.ArgumentParser(usage="ican rollback")
        self.command_prep(parser)

        self.ican = Ican()
        self.ican.rollback()
        logger.verbose("rollback() COMPLETE")
        return

    def init(self):
        """dispatched here with command init"""

        parser = argparse.ArgumentParser(usage="ican init")
        self.command_prep(parser)

        self.config = Config(init=True).parse()
        logger.info("init COMPLETE")

        return

    def run(self, alias=None):
        """dispatched here with command init"""

        parser = argparse.ArgumentParser(
            description="PIPELINE can be any pipeline defined in your .ican file.",
            usage="ican run [PIPELINE]",
        )
        parser.add_argument("pipeline", help=argparse.SUPPRESS)
        parser.add_argument(
            'user_args',
            nargs="*",
            help=argparse.SUPPRESS
        )
        args = self.command_prep(parser, alias)

        self.ican = Ican()
        self.ican.run_pipeline(args.pipeline, args.user_args)
        logger.info(f"+FINISHED pipeline.{args.pipeline.upper()}")

    def test2(self):
        """dispatched here with command test"""

        parser = argparse.ArgumentParser(usage="ican test [ARGS]")
        # parser.add_argument("dynamic_args", nargs="*", help=argparse.SUPPRESS)
        parser.add_argument(
            'user_args',
            nargs=argparse.REMAINDER,
            help=argparse.SUPPRESS)
        args = self.command_prep(parser)

        logger.verbose("verbose")
        print(f"10-4 with arg {args.dynamic_args}")


def entry():
    CLI()
