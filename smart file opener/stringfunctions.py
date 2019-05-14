
def prepare_string(inputString: str) -> str:
    outputString = inputString.lower().strip()
    outputString.replace(" ", "_")
    return outputString