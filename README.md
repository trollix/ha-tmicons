# ha-tmicons

Home assistant More icons

![More icons](https://img.shields.io/github/v/release/trollix/ha-tmicons)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=flat)](https://github.com/custom-components/hacs)

Additional vector icons for Home Assistant, this repo add more icons custom vectors created specifically by the author of typeicons:

## Typicons

Typeicons are free-to-use vector icons embedded in a webfont for use in your user interfaces, whether it be on the web or in a native application.
The set of icons are available on Github, with everything included from the source files in SVG format to the minifed CSS. You can even use this project to build your own custom version of Typicons.This version greatly improves Typicons, with the addition on 220 icons with solid and outline styles and Github hosting of the source content. Combine HTTP requests with a retina ready, resolution independent webfont.

[Typeicons](https://www.s-ings.com/typicons/)

## Installation

HA-tmicons has not been already accepted into the [Home Assistant Community Store (HACS)](https://hacs.xyz).

### HACS (Recommended)

This is the recommended way to install hass-hue-icons. Hass-hue-icons is a default repository for HACS. To install:

- Open HACS (installation instructions are [here](https://hacs.xyz/docs/installation/installation/)).
- Go to "Frontend" section
- Click button with "+" icon
- Search for "hass hue icons" and install it.
- Add the following to your configuration.yaml, save and restart HA.

```yaml

frontend:
  extra_module_url:
    - /hacsfiles/ha-tmicons/ha-tmicons.js
```

### Manual

- Copy `dist/ha-tmicons.js` into your `config/www` folder.
- Go to Configuration -> Lovelace Dashboards -> Resources -> Add Resource
- set url as `/local/ha-tmicons.js` and Resource Type as `Javascript Module`.
- Add the following to your configuration.yaml, save and restart HA.

```yaml
frontend:
  extra_module_url:
    - /local/ha-tmicons.js
```

- Save, restart Home Assistant.

## Usage

- In your entity editor, specify an icon as `tmi:icon-name`
- If you set `state_color: true` in your card, you'll see the icons get colorised based upon the current RGB setting.

### Example

```yaml
title: My Room
state_color: true
type: entities
entities:
  - entity: light.my_wall_light
    name: My Wall Light
    icon: tmi:wall-spot
```

## Icons

![Image of HA-TMICONS](https://github.com/trollix/ha-tmicons/blob/main/icons_combined_with_names.png?raw=true)

## Typeicons

[Typeicons](https://www.s-ings.com/typicons/)
