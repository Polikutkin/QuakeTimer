Quake Timer
===========
[![Build and Deploy](https://github.com/Polikutkin/QuakeTimer/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/Polikutkin/QuakeTimer/actions/workflows/build.yml)

This small app was developed for those quake players who strugle with remembring timings for major items and powerups.
All timer settings can be found and changed for your convenience.
To show timer on top of the game, choose `Borderless` or `Windowed` option in video game settings.


Configuration Options
---------------------

### Common Options

These options apply to all configurations.

| Config Name                    | Type    | Example    | Description                                                                                |
|--------------------------------|---------|------------|--------------------------------------------------------------------------------------------|
| exit_key                       | string  | ctrl+q     | Key combination to exit the application                                                    |
| window\_x\_y\_position\_pixels | string  | +0+300     | Position of the application window in pixels                                               |
| text_size                      | integer | 60         | Font size of the timer                                                                     |
| bold_text                      | boolean | true       | Whether to use bold text                                                                   |
| font                           | string  | DS-Digital | Font family to use. Cool timer font can be found in folder `fonts/` and installed manually |
| visibility                     | float   | 0.8        | The visibility of the application window. 0 - invisible, 1 - fully opaque, step - 0.1      |
| transparent_bg                 | boolean | true       | Whether to use a transparent background                                                    |
| enable\_sound\_alarm           | boolean | true       | Whether to enable the sound alarm                                                          |
| sound\_alarm\_timeout_seconds  | integer | 10         | Timeout in seconds for the sound alarm                                                     |

### Mega / Heavy Configuration

These options can be applied independently for each major item.

| Config Name                 | Type    | Example   | Description                                |
|-----------------------------|---------|-----------|--------------------------------------------|
| timeout_seconds             | integer | 29        | Timeout in seconds for the timer           |
| text_color                  | string  | white     | Color of the timer text                    |
| bg_color                    | string  | "#0246b3" | Background color of the timer              |
| attention\_timeout\_seconds | integer | 10        | Timeout in seconds for the attention phaze |
| attention\_text\_color      | string  | yellow    | Color of the attention phaze text          |
| attention\_bg\_color        | string  | "#0246b3" | Background color of the attention phaze    |
| warning\_timeout\_seconds   | integer | 5         | Timeout in seconds for the warning phaze   |
| warning\_text\_color        | string  | red       | Color of the warning phaze text            |
| warning\_bg\_color          | string  | "#0246b3" | Background color of the warning phaze      |
| start_key                   | string  | alt       | Keyboard key to start the timer            |

Future plans
---------------------
- Add different types of alarms (e.g. `beep`, `beep-till-end`)
- Implement automatic timer start based on the item pickup sound pattern
- Implement automatic timer start based on voice commands