# Orchestrator prompt for breaking down shopping tasks
ORCHESTRATOR_PROMPT = """
Analyze this shopping query and break it down into 2-3 subtasks:

Query: {task}

Return your response in this format:

<analysis>
Explain the reasoning behind the task breakdown and the purpose of each subtask.
</analysis>

<tasks>
    <task>
    <type>product_matching</type>
    <description>Identify products that match the user's criteria</description>
    </task>
    <task>
    <type>price_optimization</type>
    <description>Optimize product selections to stay within budget</description>
    </task>
    <task>
    <type>style_recommendation</type>
    <description>Provide style recommendations based on user preferences</description>
    </task>
</tasks>
"""

# Worker prompt for handling each subtask
WORKER_PROMPT = """
Handle the following shopping task:
Original Query: {original_task}
Task Type: {task_type}
Guidelines: {task_description}

Return your response in this format:

<response>
Provide the results specific to the task type and fully address the guidelines.
</response>
"""
