"""
Analytics Made Simple (analyticsmadesimple.com)
Tutorial: Grok Imagine Visual Prompt Engineering
Series: Grok Imagine Tutorial
License: MIT
"""

def compile_imagine_prompt(topic: str, background_palette: str, focal_object: str, lettering: str) -> str:
    """Compiles a high-contrast editorial prompt optimized for Grok Imagine text rendering."""
    return f"""A clean, high-contrast editorial still representing {topic}.
Setting: Solid matte {background_palette} background with subtle studio shadows.
Hero Object: A tangible, wordless {focal_object} placed neatly in center-right third.
Typography: Bold, clean sans-serif text clearly displaying: "{lettering}".
Lighting: Diffuse softbox lighting, crisp edges, minimal noise, publication-grade finish.
No cluttered desks, no generic laptops, no misspelled lettering.
"""

if __name__ == "__main__":
    p = compile_imagine_prompt(
        topic="Database Indexing and B-Tree Search",
        background_palette="warm cream (#FBF9F5)",
        focal_object="golden brass magnifying glass focusing on an engraved circuit path",
        lettering="INDEX SCAN"
    )
    print("=== Grok Imagine Prompt ===")
    print(p)
