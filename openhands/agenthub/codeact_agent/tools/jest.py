from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

from openhands.agenthub.codeact_agent.tools.prompt import refine_prompt
from openhands.llm.tool_names import JEST_TEST_TOOL_NAME

_JEST_DESCRIPTION = """Create and run Jest tests for JavaScript/TypeScript code.

Use this tool to:
* Generate Jest test files for JavaScript/TypeScript functions and modules
* Run existing Jest tests
* Validate JavaScript code behavior through unit tests

The tool will create test files following Jest conventions and execute them."""

JestTool: ChatCompletionToolParam = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name=JEST_TEST_TOOL_NAME,
        description=refine_prompt(_JEST_DESCRIPTION),
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
                    'description': 'Path to the source file to test (for create) or test file to run (for run)',
                },
                'test_content': {
                    'type': 'string',
                    'description': 'Jest test code content (required when action is "create")',
                },
            },
            'required': ['action', 'file_path'],
        },
    ),
)
