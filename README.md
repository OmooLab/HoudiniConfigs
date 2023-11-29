# Houdini Config

This is the houdini config repository of omoolab.

## Getting Started

### Dependencies

- Python >= 3.9
- Houdini >= 19.5

Create python virtualenv for houdini.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

Install dependencies.

```bash
$ pip install -r requirements.txt
```

### Add packages to houdini

Copy the directory `packages` to `$HOME/houdiniX.Y/`, e.g. `C:/Users/{UserName}/Documents/houdini19.5`.

Edit `packages/omoolab.json`

```json
// omoolab.json
{
  ...
  "env": [
    { "OMOOLAB_CREATOR": "YourName" }, // change to your name.
    ...
    // change to this repository path
    { "OMOOLAB_CONFIG": "$OMOOLAB_RESOUCES/Configs/Houdini" },
    ...
  ]
}
```
