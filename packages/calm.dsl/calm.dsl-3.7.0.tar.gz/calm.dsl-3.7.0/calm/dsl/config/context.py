import os
import sys

from .env_config import EnvConfig
from .config import get_config_handle
from calm.dsl.log import get_logging_handle
from calm.dsl.constants import DSL_CONFIG

LOG = get_logging_handle(__name__)

DEFAULT_RETRIES_ENABLED = True
DEFAILT_CONNECTION_TIMEOUT = 5
DEFAULT_READ_TIMEOUT = 30


class Context:
    def __init__(self):

        self.initialize_configuration()

    def initialize_configuration(self):
        """initializes the confguration for context
        Priority (Decreases from 1 -> 3):
        1.) Config file passed as param
        2.) Environment Variables
        3.) Config file stored in init.ini
        """

        config_handle = get_config_handle()
        self.server_config = config_handle.get_server_config()
        self.project_config = config_handle.get_project_config()
        self.log_config = config_handle.get_log_config()
        self.categories_config = config_handle.get_categories_config()
        self.policy_config = config_handle.get_policy_config()
        self.approval_policy_config = config_handle.get_approval_policy_config()
        self.stratos_config = config_handle.get_stratos_config()
        self.connection_config = config_handle.get_connection_config()
        # Override with env data
        self.server_config.update(EnvConfig.get_server_config())
        self.project_config.update(EnvConfig.get_project_config())
        self.log_config.update(EnvConfig.get_log_config())

        init_config = config_handle.get_init_config()
        self._CONFIG_FILE = init_config["CONFIG"]["location"]
        self._PROJECT = self.project_config.get("name", "")

    def reset_configuration(self):
        """Resets the configuration"""

        LOG.debug("Resetting configuration in dsl context")
        self.initialize_configuration()

    def validate_init_config(self):
        """validates the init config"""

        config_handle = get_config_handle()
        init_config = config_handle.get_init_config()

        if self._CONFIG_FILE == init_config["CONFIG"]["location"]:
            if not os.path.exists(self._CONFIG_FILE):
                LOG.error("Invalid config file location '{}'".format(self._CONFIG_FILE))
                sys.exit(-1)

    def get_server_config(self):
        """returns server configuration"""

        config = self.server_config
        try:  # if all server variables are present either in env or some other way, not required to validate config file
            if not config.get("pc_ip"):
                LOG.error(
                    "Host IP not found. Please provide it in config file or set environment variable 'CALM_DSL_PC_IP'"
                )
                sys.exit(-1)

            if not config.get("pc_port"):
                LOG.error(
                    "Host Port not found. Please provide it in config file or set environment variable 'CALM_DSL_PC_PORT'"
                )
                sys.exit(-1)

            if not config.get("pc_username"):
                LOG.error(
                    "Host username not found. Please provide it in config file or set environment variable 'CALM_DSL_PC_USERNAME'"
                )
                sys.exit(-1)

            if not config.get("pc_password"):
                LOG.error(
                    "Host password not found. Please provide it in config file or set environment variable 'CALM_DSL_PC_PASSWORD'"
                )
                sys.exit(-1)

        except:  # validate init_config file, if it's contents are valid
            self.validate_init_config()
            raise

        return config

    def get_project_config(self):
        """returns project configuration"""

        config = self.project_config
        if not config.get("name"):
            config["name"] = DSL_CONFIG.EMPTY_PROJECT_NAME

        return config

    def get_connection_config(self):
        """returns connection configuration"""

        config = self.connection_config
        if "retries_enabled" not in config:
            config[
                "retries_enabled"
            ] = DEFAULT_RETRIES_ENABLED  # TODO check boolean is supported by ini
        if "connection_timeout" not in config:
            config["connection_timeout"] = DEFAILT_CONNECTION_TIMEOUT
        if "read_timeout" not in config:
            config["read_timeout"] = DEFAULT_READ_TIMEOUT

        return config

    def get_policy_config(self):
        """returns policy configuration"""
        config = self.policy_config
        if not config.get("policy_status"):
            config["policy_status"] = False

        return config

    def get_approval_policy_config(self):
        """returns approval policy configuration"""
        config = self.approval_policy_config
        if not config.get("approval_policy_status"):
            config["approval_policy_status"] = False

        return config

    def get_stratos_config(self):
        """returns stratos configuration"""
        config = self.stratos_config
        if not config.get("stratos_status"):
            config["stratos_status"] = False

        return config

    def get_log_config(self):
        """returns logging configuration"""

        config = self.log_config
        if not config.get("level"):
            LOG.warning(
                "Default log-level not found in config file or environment('CALM_DSL_LOG_LEVEL'). Setting it to 'INFO' level"
            )
            config["level"] = "INFO"

        return config

    def get_categories_config(self):
        """returns config categories"""

        return self.categories_config

    def get_init_config(self):
        """returns init configuration"""

        config_handle = get_config_handle()
        return config_handle.get_init_config()

    def update_project_context(self, project_name):
        """Overrides the existing project configuration"""

        self._PROJECT = project_name
        LOG.debug("Updating project in dsl context to {}".format(project_name))
        self.project_config["name"] = project_name

    def update_config_file_context(self, config_file):
        """Overrides the existing configuration with passed file configuration"""

        LOG.debug("Updating config file in dsl context to {}".format(config_file))
        self._CONFIG_FILE = config_file
        cxt_config_handle = get_config_handle(self._CONFIG_FILE)
        self.server_config.update(cxt_config_handle.get_server_config())
        self.project_config.update(cxt_config_handle.get_project_config())
        self.log_config.update(cxt_config_handle.get_log_config())
        self.connection_config.update(cxt_config_handle.get_connection_config())

        if cxt_config_handle.get_categories_config():
            self.categories_config = cxt_config_handle.get_categories_config()

    def print_config(self):
        """prints the configuration"""

        server_config = self.get_server_config()
        project_config = self.get_project_config()
        log_config = self.get_log_config()
        policy_config = self.get_policy_config()
        approval_policy_config = self.get_approval_policy_config()
        stratos_status = self.get_stratos_config()
        connection_config = self.get_connection_config()

        ConfigHandle = get_config_handle()
        config_str = ConfigHandle._render_config_template(
            ip=server_config["pc_ip"],
            port=server_config["pc_port"],
            username=server_config["pc_username"],
            password="xxxxxxxx",  # Do not render password
            project_name=project_config["name"],
            log_level=log_config["level"],
            policy_status=policy_config["policy_status"],
            approval_policy_status=approval_policy_config["approval_policy_status"],
            stratos_status=stratos_status["stratos_status"],
            retries_enabled=connection_config["retries_enabled"],
            connection_timeout=connection_config["connection_timeout"],
            read_timeout=connection_config["read_timeout"],
        )

        print(config_str)


_ContextHandle = None


def init_context():

    global _ContextHandle
    _ContextHandle = Context()


def get_context():
    global _ContextHandle
    if not _ContextHandle:
        init_context()

    return _ContextHandle


def get_default_connection_config():
    """Returns default connection config"""

    return {
        "connection_timeout": DEFAILT_CONNECTION_TIMEOUT,
        "read_timeout": DEFAULT_READ_TIMEOUT,
        "retries_enabled": DEFAULT_RETRIES_ENABLED,
    }
