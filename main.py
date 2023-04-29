from tkinter import Tk, filedialog
from tika import parser


def openFilePicker() -> str:
    file_picker = Tk()
    file_picker.withdraw()
    file = filedialog.askopenfilename()
    return file


def extractRawText(file_path: str) -> str:
    with open(file_path, "rb") as input_file:
        raw_text = parser.from_file(input_file)
    return raw_text["content"]


def formatRawText(raw_text: str) -> str:
    text = raw_text
    text = text.strip()
    text = text.replace("\t", "")
    text = text.replace("\n\n\n", "\n\n")
    text = text.replace("  ", " ")
    return text


def writeTextToFile(text: str, output_file: str) -> None:
    with open(output_file, "w+", encoding="utf-8") as output:
        output.write(text)


def main() -> None:
    file = openFilePicker()

    if not file:
        raise Exception("No file supplied")

    raw_text = extractRawText(file)
    formatted_text = formatRawText(raw_text)
    writeTextToFile(formatted_text, "pdf_content.txt")


if __name__ == "__main__":
    main()
