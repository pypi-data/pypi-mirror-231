
from config_parser.action_config_parser import ActionConfigModel
from config_parser.application_config_model import ApplicationConfigModel
from config_parser.base_config_model import BaseConfigModel
from config_parser.chat_app_config_model import ChatAppConfigModel
from config_parser.config_parser_enums.parameter_names import ParameterNames
from config_parser.flow_config_model import FlowConfigModel
from config_parser.training_data_config_model import TrainingDataConfigModel


class PackageConfigModel(BaseConfigModel):
    def __init__(self, yaml_object: dict, source_path: str = None):
        super().__init__(yaml_object=yaml_object)
        self.source_path = source_path

    def get_required_params(self):
        return {
            ParameterNames.name: self.set_name,
            ParameterNames.version: self.set_version,
        }

    def get_optional_params(self):
        return {
            ParameterNames.display_name: self.set_display_name,
            ParameterNames.description: self.set_description,
            ParameterNames.state: self.set_state,
            ParameterNames.actions: self.set_actions,
            ParameterNames.authors: self.set_authors,
            ParameterNames.flows: self.set_flows,
            ParameterNames.applications: self.set_applications,
            ParameterNames.training_data: self.set_training_data,
            ParameterNames.chat_apps: self.set_chat_apps,
        }

# Required Parameter Setters

    def set_name(self, value):
        assert isinstance(value, str)
        self.name = value

    def set_version(self, value):
        assert isinstance(value, float)
        self.version = value

# Optional Parameter Setters

    def set_display_name(self, value):
        if value is None:
            value = self.name
        assert isinstance(value, str)
        self.display_name = value

    def set_description(self, value):
        if value is None:
            value = self.display_name
        assert isinstance(value, str)
        self.description = value

    def set_state(self, value):
        if value is None:
            value = 'draft'
        assert isinstance(value, str), f"For Application:`{self.name}`: `state` must be string but it's passed as {value}."
        allowed_state = ["draft", "published"]
        assert value in allowed_state, f"For Application:`{self.name}`: `state` is passed as `{value}` but must be {allowed_state}."
        self.state = value

    def set_actions(self, value):
        if value is None:
            value = []
        assert isinstance(value, list)
        actions = []
        for action in value:
            action_model = ActionConfigModel(action)
            if action_model is None:
                raise ValueError(f"Action model parse failed for action: {action}")
            actions.append(action_model)
        self.actions = actions

    def set_authors(self, value):
        if value is None:
            value = []
        assert isinstance(value, list)
        self.authors = value

    def set_flows(self, value):
        if value is None:
            value = []
        assert isinstance(value, list), "Flows must be a list"
        flows = []
        for flow in value:
            flow_model = FlowConfigModel(flow)
            flows.append(flow_model)
        self.flows = flows

    def set_applications(self, value):
        if value is None:
            value = []

        assert isinstance(value, list), "Applications must be a list"
        applications = []
        for item in value:
            applications.append(ApplicationConfigModel(item))

        self.applications = applications

    def set_training_data(self, value):
        if value is None:
            value = []

        assert isinstance(value, list), "Training data must be a list"
        training_data = []
        for item in value:
            training_data.append(TrainingDataConfigModel(item))

        self.training_data = training_data

    def set_chat_apps(self, value):
        if value is None:
            value = []

        assert isinstance(value, list), "Chat apps must be a list"
        chat_apps = []
        for item in value:
            chat_apps.append(ChatAppConfigModel(item))

        self.chat_apps = chat_apps
