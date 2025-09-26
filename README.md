# Universal Markdown Viewer (.mdu)

**Universal Markdown Viewer** is a project aimed at creating a modern, flexible, and universal alternative to the PDF format. We introduce the `.mdu` (Markdown Universal) file format, designed for the web and rich media integration.

## The Vision: Beyond PDF

PDF is a fantastic format for static, print-oriented documents. However, in an increasingly interactive digital world, it feels rigid. Embedding videos, audio, or interactive scripts is often cumbersome or impossible.

The `.mdu` format solves this by leveraging the power of web technologies. An `.mdu` file is a single, self-contained HTML file that can be opened in any modern web browser, on any device, without requiring special software.

## Key Features

-   **Truly Universal**: If you have a web browser, you can open an `.mdu` file. No plugins or viewers needed.
-   **Rich Media Support**: Easily embed local audio and video files, or embed content from services like YouTube and Vimeo directly into your document.
-   **Self-Contained**: All assets (CSS, JavaScript, images, audio, video) are encoded and embedded into a single file, making it incredibly portable.
-   **Easy to Create**: Write your content in simple Markdown, use our custom syntax for media, and let the Python script handle the rest.
-   **Lightweight & Flexible**: Based on clean HTML, CSS, and JS, `.mdu` files are more flexible and often lighter than complex PDFs.
-   **Interactive**: Includes features like a "Copy to Clipboard" button for code blocks.

## How It Works

The project consists of a Python script (`main.py`) that acts as a compiler. It takes a standard Markdown file (`.md`) as input and performs the following steps:
1.  **Parses Custom Tags**: It looks for special tags like `@[type](source)` to handle media.
2.  **Encodes Local Assets**: All local files referenced (images, audio, video) are read and encoded into Base64.
3.  **Converts Markdown to HTML**: The Markdown content is converted into standard HTML.
4.  **Bundles Everything**: The generated HTML, all CSS styles, JavaScript functionalities, and the Base64-encoded assets are bundled together into a single `.mdu` file.

The result is a standalone document that contains everything it needs to be rendered perfectly.

## Usage

### 1. Project Setup
- Clone this repository.
- Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Create Your Content
- Write your content in the `convert_markdown/document.md` file.
- Place any local media files (images, mp3, mp4) in the same `convert_markdown/` directory.

### 3. Use the Custom Syntax

#### Local Images
Use standard Markdown syntax. The script will automatically find local images and embed them.
```markdown
![A description of the image](my-image.png)
```

#### Rich Media (`@` syntax)
Use the `@[type](source)` syntax to embed media.

-   **Local Audio:**
    ```markdown
    @[audio](my-song.mp3)
    ```

-   **Local Video:**
    ```markdown
    @[video](my-presentation.mp4)
    ```

-   **YouTube Video:**
    Use the video ID from the YouTube URL.
    ```markdown
    @[youtube](dQw4w9WgXcQ)
    ```

-   **Vimeo Video:**
    Use the video ID from the Vimeo URL.
    ```markdown
    @[vimeo](123456789)
    ```

### 4. Build the `.mdu` file
Run the main script from the root of the project:
```bash
python main.py
```
This will generate the `document.mdu` file in the project's root directory. You can now open this file in any web browser.

## Project Structure
```
.
├── convert_markdown/   # Your source files go here
│   ├── document.md
│   └── (your media files like my-image.png)
├── docs/               # Documentation assets (like the icon)
├── src/                # CSS and JS source files
│   ├── script.js
│   └── style.css
├── main.py             # The compiler script
├── requirements.txt
└── README.md
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the GPL-3.0 License.