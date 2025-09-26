# Universal Document

This document demonstrates the core features of the `.mdu` format, including embedded media.

## Local Images

Standard Markdown for local images is automatically handled. The image is encoded and embedded directly into the file.

![Markdown Logo](markdown_logo.png)

## Local Audio

Here is an audio file directly embedded in the document.

@[audio](sample_audio.mp3)

## Local Video

And here is a local video. Be aware that this can make the `.mdu` file quite large!

@[video](sample_video.mp4)

*(Note: The local audio and video samples used in this document were sourced from open-source datasets on Hugging Face.)*

## External Video (YouTube)

Embedding external videos like YouTube is also very simple. An internet connection is required to view it.

@[youtube](mPZkdNFkNps)

---

## Code Blocks

The copy-to-clipboard feature for code blocks works great.

```python
def hello_mdu():
    print("The .mdu format is really flexible!")

hello_mdu()
```