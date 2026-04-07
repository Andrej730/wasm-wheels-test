import glob
import os

# Generate index.html listing all .whl files

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WASM Wheels</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
            border-bottom: 2px solid #007acc;
            padding-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .wheel-name {
            font-family: monospace;
            font-size: 0.9em;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <h1>Available WASM Wheels</h1>
    <p>Emscripten-compiled Python wheels for use with <a href="https://pyodide.org/">Pyodide</a>.</p>

    <h2>Install</h2>
    <pre><code>import micropip
await micropip.install("https://Andrej730.github.io/wasm-wheels-test/wheel-name.whl")</code></pre>

    <h2>Wheels</h2>
    <ul>
"""

# Find all .whl files in root, sorted descending
whl_files = sorted(glob.glob("*.whl"), reverse=True)

# Debug: list all files if no wheels found
if not whl_files:
    import sys
    all_files = os.listdir(".")
    print(f"DEBUG: No .whl files found. Files in directory: {all_files}", file=sys.stderr)

if whl_files:
    for whl_file in whl_files:
        filename = os.path.basename(whl_file)
        html_content += f'        <li><div class="wheel-name"><a href="{filename}">{filename}</a></div></li>\n'
else:
    html_content += '        <li>No wheels found</li>\n'

html_content += """    </ul>
</body>
</html>
"""

print(html_content)
