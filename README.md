Sublime Castling
================

## Summary
This plugin allows you to replace two parts of code you have selected in your sublime editor.

## Install

#### Git Clone
Clone this repository in to the Sublime Text "Packages" directory, which is located where ever the
"Preferences" -> "Browse Packages" option in sublime takes you.

## Key Binding

The default key binding is "ctrl+shift+q"

## Key Binding Conflicts

Unfortunately there are other plugins that use "ctrl+shift+q", this is a hard problem to solve. If sublimecastling works
OK via the command palette but does nothing when you use the "ctrl+shift+q" shortcut, you have two options:

1. Add ```{"keys": ["ctrl+shift+q"],  "command": "sublimeCastling"}``` to your user keybindings file. This will override anything specifid by a plugin.
2. Find the offending plugin, and change the shortcut in its sublime-keymap file (will revert on updates)


## Usage

First you need to select first part then the second one! The selections will be replaced after you press "ctrl+shift+q" and will replace back if you press the combination again.

---
