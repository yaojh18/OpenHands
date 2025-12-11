from litellm import ChatCompletionToolParam, ChatCompletionToolParamFunctionChunk

from openhands.agenthub.codeact_agent.tools.security_utils import (
    RISK_LEVELS,
    SECURITY_RISK_DESC,
)

CRITIC_TOOL_NAME = 'invoke_critic_agent'

_CRITIC_DESCRIPTION= """Trigger a specialized Critic Agent to verify the task completion.

### When to use
* Use this tool ONLY when you believe you have completed the requested task or fixed the bug.
* Do NOT use this tool for intermediate testing. Use other tools for that.
* This tool initiates a rigorous review process including visual verification and logic testing.

### Workflow
* Calling this tool will pause your current session.
* The Critic Agent will take over the shared environment to run independent verification scripts.
* You will receive a feedback message starting with "VERDICT: PASS" or "VERDICT: FAIL".
* If FAIL, you must fix the issues reported and call this tool again.
* If PASS, you can then proceed to use the `finish` tool.

### Best Practices
* Provide a clear and concise `summary_of_changes`. The Critic relies on this to know what to test.
* If the task involves visual elements, explicitly mention them in `verification_instructions`.
"""


CriticTool = ChatCompletionToolParam(
    type='function',
    function=ChatCompletionToolParamFunctionChunk(
        name=CRITIC_TOOL_NAME,
        description=_CRITIC_DESCRIPTION,
        parameters={
            'type': 'object',
            'properties': {
                'summary_of_changes': {
                    'type': 'string',
                    'description': 'A detailed summary of the files modified and the logic changes implemented. This helps the Critic Agent understand the scope of the fix.',
                },
                'verification_instructions': {
                    'type': 'string',
                    'description': 'Optional specific instructions for the Critic Agent. E.g., "Check if the red line in plot.png is now solid instead of dashed" or "Verify edge case where input is None".',
                },
                'security_risk': {
                    'type': 'string',
                    'description': SECURITY_RISK_DESC,
                    'enum': RISK_LEVELS,
                },
            },
            'required': ['summary_of_changes', 'security_risk'],
        },
    ),
)
