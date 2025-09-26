import markdown
import os
import re
import base64

# --- Path Configuration ---
SRC_DIR = "src"
DOCS_DIR = "docs"
MARKDOWN_DIR = "convert_markdown"
INPUT_MD_FILE = os.path.join(MARKDOWN_DIR, "document.md")
OUTPUT_MDU_FILE = "document.mdu"

STYLE_FILE = os.path.join(SRC_DIR, "style.css")
SCRIPT_FILE = os.path.join(SRC_DIR, "script.js")
ICON_FILE = os.path.join(DOCS_DIR, "mdu_icon.ico")

# --- Encoding Functions ---

def get_mime_type(filepath):
    """Determines the MIME type based on the file extension."""
    ext = filepath.lower().split('.')[-1]
    types = {
        # Images
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'ico': 'image/x-icon',
        'svg': 'image/svg+xml',
        # Audio
        'mp3': 'audio/mpeg',
        'ogg': 'audio/ogg',
        'wav': 'audio/wav',
        # Video
        'mp4': 'video/mp4',
        'webm': 'video/webm',
        'ogv': 'video/ogg',
    }
    return types.get(ext, 'application/octet-stream')

def file_to_base64(filepath):
    """Encodes any file to Base64."""
    try:
        with open(filepath, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
        mime_type = get_mime_type(filepath)
        return f"data:{mime_type};base64,{encoded_string}"
    except FileNotFoundError:
        print(f"Warning: File not found: {filepath}")
        return None

# --- Markdown Processing Functions ---

def process_markdown_images(md_content, base_path):
    """Finds local images ![alt](path) and converts them to Base64."""
    pattern = r'!\[(.*?)\]\((?!https?:\/\/)(.*?)\)'
    
    def replacer(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        full_img_path = os.path.join(base_path, img_path)
        base64_data = file_to_base64(full_img_path)
        return f'![{alt_text}]({base64_data})' if base64_data else match.group(0)

    return re.sub(pattern, replacer, md_content)

def process_media_tags(md_content, base_path):
    """Processes our custom syntax @[type](source) for audio, video, etc."""
    pattern = r'@\[(audio|video|youtube|vimeo)\]\((.*?)\)'
    
    def replacer(match):
        media_type = match.group(1)
        source = match.group(2)
        
        if media_type == 'audio':
            full_path = os.path.join(base_path, source)
            base64_data = file_to_base64(full_path)
            if base64_data:
                return f'<audio controls src="{base64_data}">Your browser does not support the audio element.</audio>'
        
        elif media_type == 'video':
            full_path = os.path.join(base_path, source)
            base64_data = file_to_base64(full_path)
            if base64_data:
                return f'<video controls width="100%" src="{base64_data}">Your browser does not support the video element.</video>'
        
        elif media_type == 'youtube':
            return f'''<div class="video-container">
<iframe src="https://www.youtube.com/embed/{source}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>'''
            
        elif media_type == 'vimeo':
            return f'''<div class="video-container">
<iframe src="https://player.vimeo.com/video/{source}" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
</div>'''

        # If the file is not found or the type is unknown, we don't replace anything
        return match.group(0)

    # We replace media tags before Markdown conversion to inject pure HTML
    return re.sub(pattern, replacer, md_content)


def main():
    """Main function to generate the .mdu file."""
    print("Starting conversion (v2)...")

    # 1. Read the source files
    try:
        with open(STYLE_FILE, "r", encoding="utf-8") as f:
            css_content = f.read()
        with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
            js_content = f.read()
        with open(INPUT_MD_FILE, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError as e:
        print(f"Error: A source file is missing: {e}")
        return

    # 2. Process custom media tags @[]() BEFORE everything else
    processed_md = process_media_tags(md_content, MARKDOWN_DIR)

    # 3. Process local images ![]()
    processed_md = process_markdown_images(processed_md, MARKDOWN_DIR)

    # 4. Convert the remaining Markdown to HTML
    # `fenced_code`: for ``` code blocks
    # `codehilite`: for syntax highlighting
    # The HTML content we injected will not be modified by the converter.
    html_content = markdown.markdown(processed_md, extensions=['fenced_code', 'codehilite'])
    
    # 5. Encode the icon
    icon_base64 = file_to_base64(ICON_FILE) if os.path.exists(ICON_FILE) else ""

    # 6. Create the final HTML document
    final_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MDU Document</title>
    <link rel="icon" type="image/x-icon" href="{icon_base64}">
    <style>
        {css_content}
    </style>
</head>
<body>
    <main>
        {html_content}
    </main>
    <script>
        {js_content}
    </script>
</body>
</html>
"""

    # 7. Write the output .mdu file
    with open(OUTPUT_MDU_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Conversion finished! File '{OUTPUT_MDU_FILE}' successfully updated.")

if __name__ == "__main__":
    main()