import re
import yaml
import markdown
from pathlib import Path

def extract_code_snippets(markdown_text):
    code_blocks = re.findall(r'```[a-zA-Z]*\n(.*?)\n```', markdown_text, re.DOTALL)
    return code_blocks

def main():
    readme_path = Path('README.md')
    if not readme_path.exists():
        raise FileNotFoundError("README.md not found")

    with open(readme_path, 'r') as file:
        markdown_text = file.read()

    snippets = extract_code_snippets(markdown_text)
    snippets_paths = []

    for i, snippet in enumerate(snippets):
        snippet_path = Path(f'.github/snippets/snippet_{i}.txt')
        snippet_path.parent.mkdir(parents=True, exist_ok=True)
        snippet_path.write_text(snippet)
        snippets_paths.append(str(snippet_path))

    print(f"::set-output name=snippets::{','.join(snippets_paths)}")

if __name__ == "__main__":
    main()
