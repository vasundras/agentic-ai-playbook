# Instantiate the orchestrator with prompts
orchestrator = ShoppingAgentOrchestrator(
    orchestrator_prompt=ORCHESTRATOR_PROMPT,
    worker_prompt=WORKER_PROMPT,
)

# Process a shopping query
results = orchestrator.process(
    task="Find a business casual wardrobe under $500",
    context={
        "budget": 500,
        "style": "business casual",
        "inventory_check": True,
        "user_preferences": {"colors": ["navy", "gray"], "fit": "slim"}
    }
)

# Display results
print("\n=== FINAL OUTPUT ===")
for result in results['worker_results']:
    print(f"Task Type: {result['type']}")
    print(f"Description: {result['description']}")
    print(f"Result: {result['result']}\n")
