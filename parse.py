import json

def parse_tool_call(response: str):
    try:
        tool_request = json.loads(response)

        if not isinstance(tool_request,dict):
            return None
        
        if "tool" not in tool_request:
            return None

        if not isinstance(tool_request["tool"], str):
            return None

        return tool_request

    except json.JSONDecodeError:
        return None
    
    except Exception:
        pass
    return None
    


if __name__ == "__main__":
    response = """
    {
        "tool": "calculator",
        "expression": "25**2"
    }
    """

    # response = "Hello! how are you?"

    result = parse_tool_call(response)
    print(result)