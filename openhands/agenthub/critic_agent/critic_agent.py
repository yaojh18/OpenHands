import os
import sys
from typing import TYPE_CHECKING

from openhands.llm.llm_registry import LLMRegistry

if TYPE_CHECKING:
    from litellm import ChatCompletionToolParam

    from openhands.events.action import Action
    from openhands.llm.llm import ModelResponse

from openhands.agenthub.codeact_agent import CodeActAgent
from openhands.core.config import AgentConfig
from openhands.utils.prompt import PromptManager


class CriticAgent(CodeActAgent):
    VERSION = '1.0'
    """
    An agent dedicated to multimodal critic debugging quality, including visual verification, unit test generation, etc.
    """

    def __init__(self, config: AgentConfig, llm_registry: LLMRegistry) -> None:
        super().__init__(config, llm_registry)
        # TODO: customize tools and prompts for critic agent

    @property
    def prompt_manager(self) -> PromptManager:
        if self._prompt_manager is None:
            self._prompt_manager = PromptManager(
                prompt_dir=os.path.join(os.path.dirname(__file__), 'prompts'),
                system_prompt_filename='system_prompt.j2',
            )

        return self._prompt_manager
