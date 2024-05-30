import os
from gtts import gTTS
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


class ExtractHeadersAndContent(Treeprocessor):
    def run(self, doc):
        sections = []
        current_header = None
        current_content = []

        for child in doc:
            if child.tag in ['h1', 'h2'] and child.text is not None:
                if current_header is not None:
                    sections.append((current_header, ' '.join(current_content).strip()))
                current_header = child.text.strip()
                current_content = []
            if child.tail:
                current_content.append(child.tail.strip())
            if child.tag == 'p':
                current_content.append(child.text.strip())
                
        if current_header is not None:
            sections.append((current_header, ' '.join(current_content).strip()))

        self.sections = sections
        return doc

class ExtractHeadersAndContentExtension(Extension):
    def extendMarkdown(self, md):
        ext = ExtractHeadersAndContent(md)
        md.treeprocessors.register(ext, 'extractheadersandcontent', 35)
        md.extractheadersandcontent = ext

# Load the markdown file
file_path = 'C:\\Users\\ahm_e\\Documents\\PROJECTs-other\\Pres.Ren\\Audio\\scriptnew.md'
with open(file_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

# Parse the markdown file to extract headers and their content
md = markdown.Markdown(extensions=[ExtractHeadersAndContentExtension()])
md.convert(md_text)
sections = md.extractheadersandcontent.sections

# Convert each section's content to speech and save as a separate mp3 file
for i, (header, content) in enumerate(sections):
    if content:  # Ensure there is content to convert
        tts = gTTS(text=content, lang='ar', slow=False)
        filename = f"section_{i}.mp3"
        tts.save(filename)
        print(f"Saved {filename}")


# from gtts import gTTS
# import os

# # the text that you want to convert to audio
# mytext = 'مرحبا بك في العالم العربي'

# # language in which you want to convert
# language = 'ar'

# # Passing the text and language to the engine
# myobj = gTTS(text=mytext, lang=language, slow=False)

# # Saving the converted audio in a mp3 file named 'welcome' 
# myobj.save("welcome.mp3")

# # Playing the converted file
# os.system("welcome.mp3")
 