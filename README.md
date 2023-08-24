# single_app_volume_control
This code is designed to control the volume of an audio instance using keyboard shortcuts (hotkeys). It can target any application that plays audio on your system. In this example, it is configured for the **'Spotify.exe'** process, but you can adapt it for any application that creates an audio instance in Windows. It has been tested on both Windows 11 and 10.

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
