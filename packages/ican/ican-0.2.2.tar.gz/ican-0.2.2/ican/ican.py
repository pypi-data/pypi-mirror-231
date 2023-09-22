# -*- coding: utf-8 -*-

from .base import Base
from .version import Version
from .git import Git
from .log import logger
from .exceptions import GitDescribeError
from .exceptions import NoConfigFound
from .exceptions import RollbackNotPossible
from .exceptions import PipelineNotFound


#######################################
#
#   Bump Class
#
#######################################


class Ican(Base):
    """
    Object which will orchestrate entire program
    """

    def __init__(self, only_pre_parse=False):
        """Typically ican will be instantiated by cli with a half parsed
        config.  We pre-parse so logging can begin.
        """
        self.ready = False

        # Make sure the config is fully parsed
        if only_pre_parse:
            pass
        # This if statement should be for init() cases only
        elif not self.config.parsed:
            self.config.parse()

        # Here if still config not ready, it will never be ready
        if not self.config.config_file:
            raise NoConfigFound()

        # Now config is parsed.  We can parse from config
        self.version = Version.parse(self.config.current_version)
        logger.verbose(f"discovered {self.version.semantic} @ CONFIG.version")

        # Git init
        self.git = Git()

        try:
            self.version._git_metadata = self.git.describe()
        except GitDescribeError as e:
            logger.verbose(e)
            logger.verbose("Git-versions are disabled. Does this repo have a tag?")
            self.git.disable()
        else:
            logger.verbose(f"Discovered {self.version.git} @ GIT.version")
        return

    def pre(self, token):
        """Set the prerelease token"""

        logger.verbose(f"Setting prerelease string to {token}")
        self.version.set_token(token)

        # Save the new version, config will check for dry_run
        self.config.persist_version(self.version.semantic)

        # Display message to user
        logger.info(f"prerelease token set: {self.version.semantic}")
        return self

    def show(self, style="semantic"):
        """
        Show the <STYLE> version
        """

        v = None
        if hasattr(self.version, style):
            v = getattr(self.version, style)
        if v is None:
            logger.error(f"Version.Style not available: {style}")
        # Display message to user
        logger.info(f"Current {style} version: {v}")
        return self

    def rollback(self):
        """When all else fails, this should bring the version back
        to your prior saved version.  It will also update all source
        files you have configured.
        """
        if not self.config.previous_version:
            raise RollbackNotPossible()

        # delete old, create new self.version
        del self.version
        self.version = Version.parse(self.config.previous_version)

        # Update the source files
        for file in self.config.source_files:
            file.update(self.version)

        # Now that everything else is finished, persist version
        self.config.persist_version(self.config.previous_version)

        # Display message to user
        logger.info(f"Rollback: {self.version.semantic}")
        return self

    def list(self):
        """
        """

        pipelines = self.config.pipelines.values()
        lines = "\n".join([p.describe_self() for p in pipelines])

        if lines:
            logger.info("\nAvailable Commands  ")
            logger.info("══════════════════\n")
            logger.info(lines)
            logger.info("\n")
        else:
            logger.info("\nNo Pipelines Defined  ")

    def bump(self, part="build"):
        """This is pretty much the full process"""

        # Little magic here to turn `bump pre` into `bump prerelease`
        logger.verbose(f"Beginning bump of <{part.upper()}>")

        self.version.bump(part)

        # Update the user's files with new version
        for file in self.config.source_files:
            file.update(self.version)

        # Once all else is successful, persist the new version
        self.config.persist_version(self.version.semantic)

        # Display message to user
        logger.info(f"Version: {self.ican.version.semantic}")
        return self

    def run_pipeline(self, pipeline, user_args=[]):
        # Pipeline
        if self.config.pipelines.get(pipeline) is None:
            # Pipeline is not defined
            raise PipelineNotFound(f'pipeline.{pipeline.upper()} not found')

        pl = self.config.pipelines.get(pipeline)
        pl.run(user_args)
        return self
