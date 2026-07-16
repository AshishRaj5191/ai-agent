from main import chat
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT
from parse import parse_tool_call
from tool_registry import execute_tool


class Agent:
    def run(self, user_input: str):

        # Load previous conversation
        memory = load_memory()

        # Prepare messages
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Add memory
        messages.extend(memory)

        # Add current user message
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Get LLM response
        llm_response = chat(messages)

        # Check whether LLM wants to use a tool
        tool_request = parse_tool_call(llm_response)

        # -------------------------
        # No Tool Required
        # -------------------------
        if tool_request is None:

            memory.append({
                "role": "user",
                "content": user_input
            })

            memory.append({
                "role": "assistant",
                "content": llm_response
            })

            save_memory(memory)

            return llm_response

        # -------------------------
        # Tool Required
        # -------------------------
        tool_name = tool_request.get("tool")

        arguments = tool_request.copy()
        arguments.pop("tool", None)

        print("\n========== TOOL ==========")
        print("Tool :", tool_name)
        print("Arguments :", arguments)

        # Execute Tool
        tool_result = execute_tool(tool_name, arguments)

        print("Observation :", tool_result)
        print("==========================\n")

        # Give tool result back to LLM
        messages.append({
            "role": "assistant",
            "content": llm_response
        })

        messages.append({
            "role": "user",
            "content": f"""
Tool Result:

{tool_result}

Now answer the user's original question in a natural and helpful way.
"""
        })

        # Final response from LLM
        final_response = chat(messages)

        # Save memory
        memory.append({
            "role": "user",
            "content": user_input
        })

        memory.append({
            "role": "assistant",
            "content": final_response
        })

        save_memory(memory)

        return final_response