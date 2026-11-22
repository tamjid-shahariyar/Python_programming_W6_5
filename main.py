SEPARATOR = ";"


def readValues(Filename: str) -> str:
    Values: str = ""
    with open(Filename, "r", encoding="UTF-8") as File:
        for Row in File:
            Row = Row.strip()
            if Row == "":
                continue
            if Values != "":
                Values += SEPARATOR
            Values += Row
    return Values


def analyseValues(Values: str) -> str:
    Numbers = [int(Value) for Value in Values.split(SEPARATOR) if Value != ""]
    Count = len(Numbers)
    Total = sum(Numbers)
    Greatest = max(Numbers) if Count > 0 else 0
    Average = Total / Count if Count > 0 else 0.0
    Result = "Count;Sum;Greatest;Average\n"
    Result += f"{Count};{Total};{Greatest};{Average:.2f}\n"
    return Result


def displayResults(Filename: str, Results: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{Filename}" results:')
    print(Results)
    print("#### Number analysis - END ####")
    return None


def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    Values = readValues(Filename)
    Results = analyseValues(Values)
    displayResults(Filename, Results)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
