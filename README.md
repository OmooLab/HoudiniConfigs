# Houdini Config

This is the houdini config repository of omoolab.

## Getting Started

### Dependencies

- Python >= 3.9
- Houdini >= 19.5

Pull this repository.

```bash
$ git clone https://github.com/OmooLab/HoudiniConfig.git
$ cd HoudiniConfig
```

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

Copy the directory `packages` to `C:/Users/{UserName}/houdiniX.Y/`, e.g. `C:/Users/{UserName}/Documents/houdini19.5`.

Edit `packages/omoolab_env.json`

```json
// omoolab_env.json
{
  "env": [
    { "OMOOLAB_NAS": "O:" }, 
    { "OMOOLAB_CREATOR": "YourName" }, // change to your name
    { "OMOOLAB_CONFIG": "C:/Users/{UserName}/HoudiniConfig" }  // change to this repository path
  ]
}
```
