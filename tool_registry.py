from tools import calculate
from time_tool import execute as time_tool
from weather import execute as weather
from news import execute as news
from stock import execute as stock
from email_tool import execute as email_tool

def calculator(arguments: dict):
    expression = arguments.get("expression")

    if expression is None:
        return "Calculator Error: expression is required."

    return calculate(expression)


TOOLS = {
    "calculator": calculator,
    "time": time_tool,
    "weather": weather,
    "news": news,
    "stock": stock,
    "email": email_tool,
}


def execute_tool(tool_name: str, arguments: dict):
    tool = TOOLS.get(tool_name)

    if tool is None:
        return f"Unknown tool: {tool_name}"

    return tool(arguments)


def list_tools():
    return list(TOOLS.keys())


if __name__ == "__main__":
    print("Registered Tools:")
    print(list_tools())

    print("\nCalculator Test:")
    print(
        execute_tool(
            "calculator",
            {
                "expression": "25*18"
            }
        )
    )

    print("\nTime Test:")
    print(
        execute_tool(
            "time",
            {}
        )
    )

    print("\nWeather Test:")
    print(
        execute_tool(
            "weather",
            {
                "city": "Delhi"
            }
        )
    )