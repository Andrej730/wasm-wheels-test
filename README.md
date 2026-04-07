# WASM Wheels

Emscripten-compiled Python wheels for use with [Pyodide](https://pyodide.org/).

**[View available wheels](https://andrej730.github.io/wasm-wheels-test/)**

## Usage

Serve the wheels locally:

```bash
python -m http.server 8000
```

In a Pyodide environment, install a wheel using `micropip`:

```python
import micropip
await micropip.install("http://localhost:8000/wheel-name.whl")
```

## Available Wheels

- `ifcopenshell` - Building Information Modeling (BIM) library with IFC file support

Open `index.html` in your browser to see the full list of available wheels.

## References

- [Pyodide Documentation](https://pyodide.org/)
- [Emscripten](https://emscripten.org/)
- [IfcOpenShell WASM Demo](http://wasm.ifcopenshell.org)
