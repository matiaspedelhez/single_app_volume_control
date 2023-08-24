# single_app_volume_control
This code is used to control the volume of an audio instance using hotkeys. It can target any process that creates an audio instance.
In this case scenario, it is adapted to the process **"Spotify.exe"**, but you can use it with whatever process that creates an audio instance in Windows. Tested in Windows 11 and 10.

## How it works
It uses AudioUtilities library which has direct access to the core Windows audio library.

## Settings and usage
You can edit the file config.json to set the hotkeys you prefer.
```javascript
// config.json
{
  "decrease_volume": "ctrl+1",
  "increase_volume": "ctrl+2"
}
```
