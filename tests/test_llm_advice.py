import yaml
from ..app.services.llm_service import LLMService

# Step 1: Call LLMService with admission advice prompt
llm = LLMService()
response_text = llm.run_prompt("admission_advice", {
    "country": "Canada",
    "user_profile": "BSc in Engineering, IELTS 6.5, budget $15,000, looking to do a Master's in Renewable Energy"
})

# Step 2: Print raw output from LLM
print("\n🔍 Raw LLM Output:\n", response_text)

# Step 3: Extract YAML block
try:
    yaml_block = response_text.split("```yaml")[1].split("```")[0]
except IndexError:
    raise ValueError("YAML block not found in LLM response!")

# Step 4: Parse YAML
try:
    parsed = yaml.safe_load(yaml_block)
except yaml.YAMLError as e:
    raise ValueError(f"YAML parsing failed: {e}")

# Step 5: Print parsed result (you can use this to power UI or store in DB)
print("\n✅ Parsed YAML:\n")
for uni in parsed.get("universities", []):
    print(f"- {uni['name']} (${uni['tuition']}) starts {uni['start_date']}")
    print(f"  Requirements: {', '.join(uni['requirements'])}\n")

print(f"📌 Recommendation: {parsed.get('recommendation')}")
print(f"📝 Advice: {parsed.get('advice')}")
