# WordPress Naming Conventions

From the official WordPress Coding Standards (PHP). WordPress predates PSR and deliberately diverges — do **not** apply PSR casing inside WP core conventions. Everything escaping into global scope carries a unique plugin/theme prefix.

## Element table

| Element | Convention | Example |
|---|---|---|
| Prefix | Unique 3+ char prefix for ALL globals your code creates | `myplugin_` / `wc_` |
| Function | lowercase_snake_case, prefixed | `myplugin_render_invoice_row()` |
| Class | Snake_Case with capitalised words | `MyPlugin_Invoice_Renderer` |
| Class file | `class-myplugin-invoice-renderer.php` (lowercase-hyphens, `class-` prefix) | — |
| Method / property | snake_case inside Snake_Case classes | `$invoice->get_total()` |
| Hook (action/filter) | prefixed, lowercase, dot-free, `{prefix}_{noun}_{verb}` | `myplugin_before_invoice_save` |
| Dynamic hook | full variable part: `myplugin_save_{$post->post_type}` | see `variable-hooks.md` in the wordpress skill |
| Option name | prefixed snake_case | `myplugin_settings` |
| Constant | PREFIXED_UPPER_SNAKE | `MYPLUGIN_API_VERSION` |
| Custom DB table | `$wpdb->prefix` + prefixed snake_case | `wp_myplugin_invoices` |
| Nonce action | prefixed snake_case | `myplugin_save_invoice` |
| Text domain | matches plugin slug | `my-plugin` |
| Regular file | lowercase, hyphens | `admin/invoice-list.php` |

## Rules worth remembering

- If two plugins define `render_footer()` both crash — the prefix is the namespace. Never ship a bare function/hook/option name.
- Hook names document *when* they fire: `{$prefix}_before_…`, `{$prefix}_after_…`.
- Third-party callbacks registered against someone else's hooks stay unprefixed (you don't own the name you're listening to).

## Sources

- [WordPress PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/)
- [WordPress Naming Conventions section](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/#naming-conventions)
