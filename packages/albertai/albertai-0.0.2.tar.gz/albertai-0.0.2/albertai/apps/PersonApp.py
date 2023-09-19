from string import Template

from embedchain.apps.App import App
from embedchain.apps.OpenSourceApp import OpenSourceApp
from embedchain.config import ChatConfig, QueryConfig
from embedchain.config.apps.BaseAppConfig import BaseAppConfig
from embedchain.config.QueryConfig import (DEFAULT_PROMPT,
                                           DEFAULT_PROMPT_WITH_HISTORY)


class EmbedChainPersonApp:
    """
    Base class to create a person bot.
    This bot behaves and speaks like a person.

    :param person: name of the person, better if its a well known person.
    :param config: BaseAppConfig instance to load as configuration.
    """

    def __init__(self, person, config: BaseAppConfig = None):
        self.person = person
        self.person_prompt = f"You are {person}. Whatever you say, you will always say in {person} style."  # noqa:E501
        super().__init__(config)

    def add_person_template_to_config(self, default_prompt: str, config: ChatConfig = None):
        """
        This method checks if the config object contains a prompt template
        if yes it adds the person prompt to it and return the updated config
        else it creates a config object with the default prompt added to the person prompt

        :param default_prompt: it is the default prompt for query or chat methods
        :param config: Optional. The `ChatConfig` instance to use as
        configuration options.
        """
        template = Template(self.person_prompt + " " + default_prompt)

        if config:
            if config.template:
                # Add person prompt to custom user template
                config.template = Template(self.person_prompt + " " + config.template.template)
            else:
                # If no user template is present, use person prompt with the default template
                config.template = template
        else:
            # if no config is present at all, initialize the config with person prompt and default template
            config = QueryConfig(
                template=template,
            )

        return config


class PersonApp(EmbedChainPersonApp, App):
    """
    The Person app.
    Extends functionality from EmbedChainPersonApp and App
    """

    def query(self, input_query, config: QueryConfig = None, dry_run=False):
        config = self.add_person_template_to_config(DEFAULT_PROMPT, config)
        return super().query(input_query, config, dry_run)

    def chat(self, input_query, config: ChatConfig = None, dry_run=False):
        config = self.add_person_template_to_config(DEFAULT_PROMPT_WITH_HISTORY, config)
        return super().chat(input_query, config, dry_run)


class PersonOpenSourceApp(EmbedChainPersonApp, OpenSourceApp):
    """
    The Person app.
    Extends functionality from EmbedChainPersonApp and OpenSourceApp
    """

    def query(self, input_query, config: QueryConfig = None, dry_run=False):
        config = self.add_person_template_to_config(DEFAULT_PROMPT, config)
        return super().query(input_query, config, dry_run)

    def chat(self, input_query, config: ChatConfig = None, dry_run=False):
        config = self.add_person_template_to_config(DEFAULT_PROMPT_WITH_HISTORY, config)
        return super().chat(input_query, config, dry_run)
