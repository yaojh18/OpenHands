from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

from openhands.agenthub.codeact_agent.tools.prompt import refine_prompt
from openhands.llm.tool_names import PLAYWRIGHT_TEST_TOOL_NAME

_PLAYWRIGHT_DESCRIPTION = """Create and run Playwright tests for visual/UI testing and image validation.

Use this tool to:
* Generate Playwright test files for UI interactions and visual regression testing
* Run existing Playwright tests with screenshot/image comparison
* Validate visual elements and image-based functionality

The tool will create test files following Playwright conventions and execute them with visual assertions."""

PlaywrightTool: ChatCompletionToolParam = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name=PLAYWRIGHT_TEST_TOOL_NAME,
        description=refine_prompt(_PLAYWRIGHT_DESCRIPTION),
        parameters={
            'type': 'object',
            'properties': {
                'action': {
                    'type': 'string',
                    'description': 'Action to perform: "create" to generate a test file, "run" to execute tests',
                    'enum': ['create', 'run'],
                },
                'file_path': {
                    'type': 'string',
                    'description': 'Path to the test file to create or run',
                },
                'test_content': {
                    'type': 'string',
                    'description': 'Playwright test code content (required when action is "create")',
                },
            },
            'required': ['action', 'file_path'],
        },
    ),
)
