# Your first Claude Code mod: count tool calls beside the spinner

> **Official companion for [Claude Code mods for beginners: how they work, real examples, and safety tips](https://analyticsmadesimple.com/tutorials/claude-code-mods-what-they-are-examples/)**
> Mod folder: [`05_first_mod/`](./05_first_mod/)

A mod is a Claude Code plugin with event handlers that run inside Claude Code. This one counts how many tools Claude uses and shows the count after the spinner word while Claude works, as in `Thinking · tool calls: 3…`. It is the first example from Anthropic's [Create a mod](https://code.claude.com/docs/en/plugins/mods/create) guide. Mods need Claude Code 2.1.287 or later.

## The three files

```text
05_first_mod/
├── .claude-plugin/
│   └── plugin.json
└── hooks/
    ├── hooks.json
    └── register.js
```

### `.claude-plugin/plugin.json`: names the plugin

```json
{
  "name": "first-mod",
  "version": "0.1.0",
  "description": "Counts Claude's tool calls and shows the count beside the spinner"
}
```

### `hooks/hooks.json`: points to the code

```json
{
  "description": "The first-mod hooks module",
  "modules": ["./register.js"]
}
```

The `modules` line is what turns an ordinary plugin into a mod.

### `hooks/register.js`: the code

```javascript
// Analytics Made Simple (analyticsmadesimple.com)
// Tutorial: Claude Code mods for beginners (https://analyticsmadesimple.com/tutorials/claude-code-mods-what-they-are-examples/)
// License: MIT. Based on the first example in Anthropic's "Create a mod" guide.

// The count, shared by the two hooks below
let calls = 0

// Claude Code calls this once when the mod loads
export function register(on) {
  // Runs each time Claude is about to use a tool
  on('tool.call', async ($, e, next) => {
    calls += 1
    // Ask Claude Code to draw the interface again, so the new count shows
    $.ui.invalidate('ui.render')
    // Let the tool run as usual
    return next(e)
  })

  // Runs each time Claude Code draws the spinner
  on('ui.render', { component: 'Spinner' }, async ($, e, next) => {
    // Keep Claude Code's spinner, with the count added after its word
    return next({ ...e, props: { ...e.props, suffix: ' · tool calls: ' + calls + '…' } })
  })
}
```

## What each part does

1. **`calls`** is a plain variable. Both hooks can read it because they live in the same file.
2. **`register(on)`** runs once when the mod loads. Each `on(...)` call asks Claude Code to run a function when an event happens.
3. **The `tool.call` hook** runs each time Claude is about to use a tool. It adds one to the count, asks for a redraw with `$.ui.invalidate`, and returns `next(e)` so the tool runs as usual.
4. **The `ui.render` hook** runs only for the spinner (the `{ component: 'Spinner' }` matcher). It passes Claude Code's own spinner on with a `suffix` that holds the count.

## Check it before you load it

```bash
claude plugin validate ./05_first_mod
```

Expected output on Claude Code 2.1.295:

```text
  ❯ ./register.js hooks: tool.call, ui.render{component=Spinner}
  ❯ ./register.js gating hook without .catch: tool.call
  ❯ ./register.js calls: $.ui.invalidate

✔ Validation passed with warnings
```

The `hooks:` line lists the events the mod listens to and `calls:` lists what it asks Claude Code to do. The warning means the tool-call hook could block a tool and has no `.catch` error handler, which is fine for a counter.

## How to run

```bash
claude --plugin-dir ./05_first_mod
```

Ask Claude something that takes a few tool calls, such as "list the files here and read the README", and watch the spinner. Edit `register.js` while the session is open and Claude Code reloads the mod.

## Next

- [Back to the Claude Code module](./README.md)
