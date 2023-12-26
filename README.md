# Houdini Config

This is the houdini config repository of omoolab.

## Getting Started

### Dependencies

- Python >= 3.9
- Houdini >= 19.5

Pull this repository.

```bash
$ git clone https://github.com/OmooLab/HoudiniConfig.git
```

Add it to houdini
Create a env file in packages houdiniX.Y/packages/env.json

```json
{
  "env": [
    { "OMOOLAB_NAS": "O:" },
    { "OMOOLAB_CREATOR": "YourName" }
  ],
  "package_path": [
    "Path/to/HoudiniConfig/Packages"
  ]
}
```
