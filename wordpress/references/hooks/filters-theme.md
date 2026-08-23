# WordPress Filters: Theme / Customizer / Widgets / Scripts

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### stylesheet
**Params:** string $stylesheet
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the name of current stylesheet.

### stylesheet_directory
**Params:** string $stylesheet_dir, string $stylesheet, string $theme_root
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the stylesheet directory path for the active theme.

### stylesheet_directory_uri
**Params:** string $stylesheet_dir_uri, string $stylesheet, string $theme_root_uri
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the stylesheet directory URI.

### stylesheet_uri
**Params:** string $stylesheet_uri, string $stylesheet_dir_uri
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the URI of the active theme stylesheet.

### template
**Params:** string $template
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the name of the active theme.

### template_directory
**Params:** string $template_dir, string $template, string $theme_root
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the active theme directory path.

### template_directory_uri
**Params:** string $template_dir_uri, string $template, string $theme_root_uri
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the active theme directory URI.

### theme_root
**Params:** string $theme_root
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the absolute path to the themes directory.

### theme_root_uri
**Params:** string $theme_root_uri, string $siteurl, string $stylesheet_or_template
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the URI for themes directory.

### {$type}_template
**Since:** 1.5.2 | **Tags:** #Variable #Legacy

### mce_buttons
**Params:** array $mce_buttons, string $editor_id
**Since:** 2.0 | **Tags:** #Legacy
Filters the first-row list of TinyMCE buttons (Visual tab).

### mce_buttons_2
**Params:** array $mce_buttons_2, string $editor_id
**Since:** 2.0 | **Tags:** #Legacy
Filters the second-row list of TinyMCE buttons (Visual tab).

### mce_buttons_3
**Params:** array $mce_buttons_3, string $editor_id
**Since:** 2.0 | **Tags:** #Legacy
Filters the third-row list of TinyMCE buttons (Visual tab).

### richedit_pre
**Params:** string $output
**Since:** 2.0 | **Tags:** #Legacy
Filters text returned for the rich text editor. This filter is first evaluated, and the value returned, if an empty string is passed to wp_richedit_pre(). If an empty string is passed, it results in a break tag and line feed. If a non-empty string is passed, the filter is evaluated on the wp_richedit_pre() return after being formatted.

### locale_stylesheet_uri
**Params:** string $stylesheet_uri, string $stylesheet_dir_uri
**Since:** 2.1 | **Tags:** #Legacy
Filters the localized stylesheet URI.

### mce_css
**Params:** string $stylesheets
**Since:** 2.1 | **Tags:** #Legacy
Filters the comma-delimited list of stylesheets to load in TinyMCE.

### the_editor
**Params:** string $output
**Since:** 2.1 | **Tags:** #Legacy
Filters the HTML markup output that displays the editor.

### the_editor_content
**Params:** string $content, string $default_editor
**Since:** 2.1 | **Tags:** #Legacy
Filters the default editor content.

### script_loader_src
**Params:** string $src, string $handle
**Since:** 2.2 | **Tags:** #Legacy
Filters the script loader source.

### theme_mod_{$name}
**Since:** 2.2 | **Tags:** #Variable #Legacy

### print_scripts_array
**Params:** string[] $to_do
**Since:** 2.3 | **Tags:** #Legacy
Filters the list of script dependencies left to print.

### widget_text
**Params:** string $text, array $instance, WP_Widget_Text|WP_Widget_Custom_HTML $widget
**Since:** 2.3 | **Tags:** #Legacy
Filters the content of the Text widget.

### wp_admin_css
**Params:** string $stylesheet_link, string $file
**Since:** 2.3 | **Tags:** #Legacy
Filters the stylesheet link to the specified CSS file. If the site is set to display right-to-left, the RTL stylesheet link will be used instead.

### wp_admin_css_uri
**Params:** string $_file, string $file
**Since:** 2.3 | **Tags:** #Legacy
Filters the URI of a WordPress admin CSS file.

### dynamic_sidebar_params
**Params:** array $params
**Since:** 2.5 | **Tags:** #Legacy
Filters the parameters passed to a widget's display callback. Note: The filter is evaluated on both the front end and back end, including for the Inactive Widgets sidebar on the Widgets screen.

### language_attributes
**Params:** string $output, string $doctype
**Since:** 2.5 | **Tags:** #Legacy
Filters the language attributes for display in the 'html' tag.

### mce_buttons_4
**Params:** array $mce_buttons_4, string $editor_id
**Since:** 2.5 | **Tags:** #Legacy
Filters the fourth-row list of TinyMCE buttons (Visual tab).

### mce_external_languages
**Params:** array $translations, string $editor_id
**Since:** 2.5 | **Tags:** #Legacy
Filters the translations loaded for external TinyMCE 3.x plugins. The filter takes an associative array ('plugin_name' => 'path') where 'path' is the include path to the file. The language file should follow the same format as wp_mce_translation(), and should define a variable ($strings) that holds all translated strings.

### mce_external_plugins
**Params:** array $external_plugins, string $editor_id
**Since:** 2.5 | **Tags:** #Legacy
Filters the list of TinyMCE external plugins. The filter takes an associative array of external plugins for TinyMCE in the form 'plugin_name' => 'url'. The url should be absolute, and should include the js filename to be loaded. For example: 'myplugin' => 'http://mysite.com/wp-content/plugins/myfolder/mce_plugin.js'. If the external plugin adds a button, it should be added with one of the 'mce_buttons' filters.

### the_generator
**Params:** string $generator_type, string $type
**Since:** 2.5 | **Tags:** #Legacy
Filters the output of the XHTML generator tag, for display.

### tiny_mce_before_init
**Params:** array $mce_init, string $editor_id
**Since:** 2.5 | **Tags:** #Legacy
Filters the TinyMCE config before init.

### wp_default_editor
**Params:** string $r
**Since:** 2.5 | **Tags:** #Legacy
Filters which editor should be displayed by default.

### wp_generator_type
**Params:** string $generator_type
**Since:** 2.5 | **Tags:** #Legacy
Filters the output of the XHTML generator tag.

### print_styles_array
**Params:** string[] $to_do
**Since:** 2.6 | **Tags:** #Legacy
Filters the array of enqueued styles before processing for output.

### style_loader_src
**Params:** string $src, string $handle
**Since:** 2.6 | **Tags:** #Legacy
Filters an enqueued style's fully-qualified URL.

### style_loader_tag
**Params:** string $tag, string $handle, string $href, string $media
**Since:** 2.6 | **Tags:** #Legacy
Filters the HTML link tag of an enqueued style.

### widget_links_args
**Params:** array $widget_links_args, array $instance
**Since:** 2.6 | **Tags:** #Legacy
Filters the arguments for the Links widget.

### widget_title
**Params:** string $title, array $instance, mixed $id_base
**Since:** 2.6 | **Tags:** #Legacy
Filters the widget title.

### disable_captions
**Params:** bool $bool
**Since:** 2.7 | **Tags:** #Legacy
Filters whether to disable captions. Prevents image captions from being appended to image HTML when inserted into the editor.

### sidebars_widgets
**Params:** array $sidebars_widgets
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of sidebars and their widgets.

### teeny_mce_before_init
**Params:** array $mce_init, string $editor_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the teenyMCE config before init.

### teeny_mce_buttons
**Params:** array $mce_buttons, string $editor_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of teenyMCE buttons (Code tab).

### teeny_mce_plugins
**Params:** array $plugins, string $editor_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of teenyMCE plugins.

### validate_current_theme
**Params:** bool $validate
**Since:** 2.7 | **Tags:** #Legacy
Filters whether to validate the active theme.

### custom_menu_order
**Params:** bool $custom
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to enable custom ordering of the administration menu. See the {@see 'menu_order'} filter for reordering menu items.

### load_default_widgets
**Params:** bool $wp_maybe_load_widgets
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to load the Widgets library. Returning a falsey value from the filter will effectively short-circuit the Widgets library from loading.

### theme_action_links
**Params:** string[] $actions, WP_Theme $theme, string $context
**Since:** 2.8 | **Tags:** #Legacy
Filters the action links displayed for each theme in the Multisite themes list table. The action links displayed are determined by the theme's status, and which Multisite themes list table is being displayed - the Network themes list table (themes.php), which displays all installed themes, or the Site themes list table (site-themes.php), which displays the non-network enabled themes when editing a site in the Network admin. The default action links for the Network themes list table include 'Network Enable', 'Network Disable', and 'Delete'. The default action links for the Site themes list table include 'Enable', and 'Disable'.

### widget_archives_args
**Params:** array $args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the arguments for the Archives widget.

### widget_archives_dropdown_args
**Params:** array $args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the arguments for the Archives widget drop-down.

### widget_categories_args
**Params:** array $cat_args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the arguments for the Categories widget.

### widget_categories_dropdown_args
**Params:** array $cat_args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the arguments for the Categories widget drop-down.

### widget_display_callback
**Params:** array $instance, WP_Widget $widget, array $args
**Since:** 2.8 | **Tags:** #Legacy
Filters the settings for a particular widget instance. Returning false will effectively short-circuit display of the widget.

### widget_form_callback
**Params:** array $instance, WP_Widget $widget
**Since:** 2.8 | **Tags:** #Legacy
Filters the widget instance's settings before displaying the control form. Returning false effectively short-circuits display of the control form.

### widget_pages_args
**Params:** array $args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the arguments for the Pages widget.

### widget_tag_cloud_args
**Params:** array $args, array $instance
**Since:** 2.8 | **Tags:** #Legacy
Filters the taxonomy used in the Tag Cloud widget.

### widget_update_callback
**Params:** array $instance, array $new_instance, array $old_instance, WP_Widget $widget
**Since:** 2.8 | **Tags:** #Legacy
Filters a widget's settings before saving. Returning false will effectively short-circuit the widget's ability to update settings.

### load_default_embeds
**Params:** bool $maybe_load_embeds
**Since:** 2.9 | **Tags:** #Legacy
Filters whether to load the default embed handlers. Returning a falsey value will prevent loading the default embed handlers.

### template_include
**Params:** string $template
**Since:** 3.0 | **Tags:** #Modern
Filters the path of the current template before including it.

### theme_row_meta
**Params:** string[] $theme_meta, string $stylesheet, WP_Theme $theme, string $status
**Since:** 3.1 | **Tags:** #Modern
Filters the array of row meta for each theme in the Multisite themes list table.

### quicktags_settings
**Params:** array $qt_init, string $editor_id
**Since:** 3.3 | **Tags:** #Modern
Filters the Quicktags settings.

### tiny_mce_plugins
**Params:** array $plugins, string $editor_id
**Since:** 3.3 | **Tags:** #Modern
Filters the list of default TinyMCE plugins. The filter specifies which of the default plugins included in WordPress should be added to the TinyMCE instance.

### current_theme_supports-{$feature}
**Since:** 3.4 | **Tags:** #Variable #Modern

### customize_allowed_urls
**Params:** string[] $allowed_urls
**Since:** 3.4 | **Tags:** #Modern
Filters the list of URLs allowed to be clicked and followed in the Customizer preview.

### customize_sanitize_js_{$this->id}
**Since:** 3.4 | **Tags:** #Variable #Modern

### customize_sanitize_{$this->id}
**Since:** 3.4 | **Tags:** #Variable #Modern

### extra_theme_headers
**Since:** 3.4 | **Tags:** #Modern

### theme_install_actions
**Params:** string[] $actions, stdClass $theme
**Since:** 3.4 | **Tags:** #Modern
Filters the install action links for a theme in the Install Themes list table.

### widget_comments_args
**Params:** array $comment_args, array $instance
**Since:** 3.4 | **Tags:** #Modern
Filters the arguments for the Recent Comments widget.

### widget_posts_args
**Params:** array $args, array $instance
**Since:** 3.4 | **Tags:** #Modern
Filters the arguments for the Recent Posts widget.

### theme_action_links_{$stylesheet}
**Since:** 3.5 | **Tags:** #Variable #Modern

### widget_meta_poweredby
**Params:** string $html, array $instance
**Since:** 3.6 | **Tags:** #Modern
Filters the "WordPress.org" list item HTML in the Meta widget.

### customizer_widgets_section_args
**Params:** array $section_args, string $section_id, int|string $sidebar_id
**Since:** 3.9 | **Tags:** #Modern
Filters Customizer widget section arguments for a given sidebar.

### dynamic_sidebar_has_widgets
**Params:** bool $did_one, int|string $index
**Since:** 3.9 | **Tags:** #Modern
Filters whether a sidebar has widgets. Note: The filter is also evaluated for empty sidebars, and on both the front end and back end, including the Inactive Widgets sidebar on the Widgets screen.

### is_active_sidebar
**Params:** bool $is_active_sidebar, int|string $index
**Since:** 3.9 | **Tags:** #Modern
Filters whether a dynamic sidebar is considered "active".

### is_wide_widget_in_customizer
**Params:** bool $is_wide, string $widget_id
**Since:** 3.9 | **Tags:** #Modern
Filters whether the given widget is considered "wide".

### pre_set_theme_mod_{$name}
**Since:** 3.9 | **Tags:** #Variable #Modern

### widget_customizer_setting_args
**Params:** array $args, string $id
**Since:** 3.9 | **Tags:** #Modern
Filters the common arguments supplied when constructing a Customizer setting.

### customize_control_active
**Params:** bool $active, WP_Customize_Control $control
**Since:** 4.0 | **Tags:** #Modern
Filters response of WP_Customize_Control::active().

### customize_panel_active
**Params:** bool $active, WP_Customize_Panel $panel
**Since:** 4.1 | **Tags:** #Modern
Filters response of WP_Customize_Panel::active().

### customize_section_active
**Params:** bool $active, WP_Customize_Section $section
**Since:** 4.1 | **Tags:** #Modern
Filters response of WP_Customize_Section::active().

### script_loader_tag
**Params:** string $tag, string $handle, string $src
**Since:** 4.1 | **Tags:** #Modern
Filters the HTML script tag of an enqueued script.

### customize_dynamic_setting_args
**Params:** false|array $setting_args, string $setting_id
**Since:** 4.2 | **Tags:** #Modern
Filters a dynamic setting's constructor args. For a dynamic setting to be registered, this filter must be employed to override the default false value with an array of args to pass to the WP_Customize_Setting constructor.

### customize_dynamic_setting_class
**Params:** string $setting_class, string $setting_id, array $setting_args
**Since:** 4.2 | **Tags:** #Modern
Allow non-statically created settings to be constructed with custom WP_Customize_Setting subclass.

### customize_refresh_nonces
**Params:** string[] $nonces, WP_Customize_Manager $manager
**Since:** 4.2 | **Tags:** #Modern
Filters nonces for Customizer.

### customize_save_response
**Params:** array $response, WP_Customize_Manager $manager
**Since:** 4.2 | **Tags:** #Modern
Filters response data for a successful customize_save Ajax request. This filter does not apply if there was a nonce or authentication failure.

### widget_nav_menu_args
**Params:** array $nav_menu_args, WP_Term $nav_menu, array $args, array $instance
**Since:** 4.2 | **Tags:** #Modern
Filters the arguments for the Navigation Menu widget.

### customize_nav_menu_available_items
**Params:** array $items, string $object_type, string $object_name, int $page
**Since:** 4.3 | **Tags:** #Modern
Filters the available menu items.

### customize_nav_menu_available_item_types
**Params:** array $item_types
**Since:** 4.3 | **Tags:** #Modern
Filters the available menu item types.

### customize_loaded_components
**Params:** string[] $components, WP_Customize_Manager $manager
**Since:** 4.4 | **Tags:** #Modern
Filters the core Customizer components to load. This allows Core components to be excluded from being instantiated by filtering them out of the array. Note that this filter generally runs during the {@see 'plugins_loaded'} action, so it cannot be added in a theme.

### customize_value_{$id_base}
**Since:** 4.4 | **Tags:** #Variable #Modern

### navigation_markup_template
**Params:** string $template, string $css_class
**Since:** 4.4 | **Tags:** #Modern
Filters the navigation markup template. Note: The filtered template HTML must contain specifiers for the navigation class (%1$s), the screen-reader-text value (%2$s), placement of the navigation links (%3$s), and ARIA label text if screen-reader-text does not fit that (%4$s): <nav class="navigation %1$s" aria-label="%4$s"> <h2 class="screen-reader-text">%2$s</h2> <div class="nav-links">%3$s</div> </nav>

### customize_dynamic_partial_args
**Params:** false|array $partial_args, string $partial_id
**Since:** 4.5 | **Tags:** #Modern
Filters a dynamic partial's constructor arguments. For a dynamic partial to be registered, this filter must be employed to override the default false value with an array of args to pass to the WP_Customize_Partial constructor.

### customize_dynamic_partial_class
**Params:** string $partial_class, string $partial_id, array $partial_args
**Since:** 4.5 | **Tags:** #Modern
Filters the class used to construct partials. Allow non-statically created partials to be constructed with custom WP_Customize_Partial subclass.

### customize_nav_menu_searched_items
**Params:** array $items, array $args
**Since:** 4.5 | **Tags:** #Modern
Filters the available menu items during a search request.

### customize_partial_render
**Params:** string|array|false $rendered, WP_Customize_Partial $partial, array $container_context
**Since:** 4.5 | **Tags:** #Modern
Filters partial rendering.

### customize_partial_render_{$partial->id}
**Since:** 4.5 | **Tags:** #Variable #Modern

### customize_previewable_devices
**Params:** array $devices
**Since:** 4.5 | **Tags:** #Modern
Filters the available devices to allow previewing in the Customizer.

### customize_render_partials_response
**Params:** array $response, WP_Customize_Selective_Refresh $refresh, array $partials
**Since:** 4.5 | **Tags:** #Modern
Filters the response from rendering the partials. Plugins may use this filter to inject `$scripts` and `$styles`, which are dependencies for the partials being rendered. The response data will be available to the client via the `render-partials-response` JS event, so the client can then inject the scripts and styles into the DOM if they have not already been enqueued there. If plugins do this, they'll need to take care for any scripts that do `document.write()` and make sure that these are not injected, or else to override the function to no-op, or else the page will be destroyed. Plugins should be aware that `$scripts` and `$styles` may eventually be included by default in the response.

### customize_validate_{$this->id}
**Since:** 4.6 | **Tags:** #Variable #Modern

### customize_changeset_save_data
**Params:** array $data, array $context
**Since:** 4.7 | **Tags:** #Modern
Filters the settings' data that will be persisted into the changeset. Plugins may amend additional data (such as additional meta for settings) into the changeset with this filter.

### customize_validate_{$setting->id}
**Since:** 4.7 | **Tags:** #Variable #Modern

### get_theme_starter_content
**Params:** array $content, array $config
**Since:** 4.7 | **Tags:** #Modern
Filters the expanded array of starter content.

### parent_theme_file_path
**Params:** string $path, string $file
**Since:** 4.7 | **Tags:** #Modern
Filters the path to a file in the parent theme.

### parent_theme_file_uri
**Params:** string $url, string $file
**Since:** 4.7 | **Tags:** #Modern
Filters the URL to a file in the parent theme.

### theme_file_path
**Params:** string $path, string $file
**Since:** 4.7 | **Tags:** #Modern
Filters the path to a file in the theme.

### theme_file_uri
**Params:** string $url, string $file
**Since:** 4.7 | **Tags:** #Modern
Filters the URL to a file in the theme.

### theme_{$post_type}_templates
**Since:** 4.7 | **Tags:** #Variable #Modern

### update_custom_css_data
**Params:** array $data, array $args
**Since:** 4.7 | **Tags:** #Modern
Filters the `css` (`post_content`) and `preprocessed` (`post_content_filtered`) args for a `custom_css` post being updated. This filter can be used by plugin that offer CSS pre-processors, to store the original pre-processed CSS in `post_content_filtered` and then store processed CSS in `post_content`. When used in this way, the `post_content_filtered` should be supplied as the setting value instead of `post_content` via a the `customize_value_custom_css` filter, for example: <code> add_filter( 'customize_value_custom_css', function( $value, $setting ) { $post = wp_get_custom_css_post( $setting->stylesheet ); if ( $post && ! empty( $post->post_content_filtered ) ) { $css = $post->post_content_filtered; } return $css; }, 10, 2 ); </code>

### {$type}_template_hierarchy
**Since:** 4.7 | **Tags:** #Variable #Modern

### page_menu_link_attributes
**Params:** array $atts, WP_Post $page, int $depth, array $args, int $current_page_id
**Since:** 4.8 | **Tags:** #Modern
Filters the HTML attributes applied to a page menu item's anchor element.

### theme_scandir_exclusions
**Params:** string[] $exclusions
**Since:** 4.8 | **Tags:** #Modern
Filters the array of excluded directories and files while scanning theme folder.

### widget_text_content
**Params:** string $text, array $instance, WP_Widget_Text $widget
**Since:** 4.8 | **Tags:** #Modern
Filters the content of the Text widget to apply changes expected from the visual (TinyMCE) editor. By default a subset of the_content filters are applied, including wpautop and wptexturize.

### widget_{$this->id_base}_instance
**Since:** 4.8 | **Tags:** #Variable #Modern

### customize_changeset_branching
**Params:** bool $allow_branching, WP_Customize_Manager $wp_customize
**Since:** 4.9 | **Tags:** #Modern
Filters whether or not changeset branching is allowed. By default in core, when changeset branching is not allowed, changesets will operate linearly in that only one saved changeset will exist at a time (with a 'draft' or 'future' status). This makes the Customizer operate in a way that is similar to going to "edit" to one existing post: all users will be making changes to the same post, and autosave revisions will be made for that post. By contrast, when changeset branching is allowed, then the model is like users going to "add new" for a page and each user makes changes independently of each other since they are all operating on their own separate pages, each getting their own separate initial auto-drafts and then once initially saved, autosave revisions on top of that user's specific post. Since linear changesets are deemed to be more suitable for the majority of WordPress users, they are the default. For WordPress sites that have heavy site management in the Customizer by multiple users then branching changesets should be enabled by means of this filter.

### customize_load_themes
**Params:** array|stdClass $themes, array $args, WP_Customize_Manager $manager
**Since:** 4.9 | **Tags:** #Modern
Filters the theme data loaded in the customizer. This allows theme data to be loading from an external source, or modification of data loaded from `wp_prepare_themes_for_js()` or WordPress.org via `themes_api()`.

### widget_custom_html_content
**Params:** string $content, array $instance, WP_Widget_Custom_HTML $widget
**Since:** 4.9 | **Tags:** #Modern
Filters the content of the Custom HTML widget.

### widget_{$this->id_base}_instance_schema
**Since:** 4.9 | **Tags:** #Variable #Modern

### theme_templates
**Params:** string[] $post_templates, WP_Theme $theme, WP_Post|null $post, string $post_type
**Since:** 5.0 | **Tags:** #Recent
Filters list of page templates for a theme.

### get_custom_logo_image_attributes
**Params:** array $custom_logo_attr, int $custom_logo_id, int $blog_id
**Since:** 5.5 | **Tags:** #Recent
Filters the list of custom logo image attributes.

### navigation_widgets_format
**Params:** string $format
**Since:** 5.5 | **Tags:** #Recent
Filters the HTML format of widgets with navigation links.

### theme_auto_update_debug_string
**Params:** string $auto_updates_string, WP_Theme $theme, bool $enabled
**Since:** 5.5 | **Tags:** #Recent
Filters the text string of the auto-updates setting for each theme in the Site Health debug data.

### theme_auto_update_setting_html
**Params:** string $html, string $stylesheet, WP_Theme $theme
**Since:** 5.5 | **Tags:** #Recent
Filters the HTML of the auto-updates setting for each theme in the Themes list table.

### theme_auto_update_setting_template
**Params:** string $template
**Since:** 5.5 | **Tags:** #Recent
Filters the JavaScript template used to display the auto-update setting for a theme (in the overlay). See {@see wp_prepare_themes_for_js()} for the properties of the `data` object.

### should_load_remote_block_patterns
**Params:** bool $should_load_remote
**Since:** 5.8 | **Tags:** #Recent
Filter to disable remote block patterns.

### should_load_separate_core_block_assets
**Params:** bool $load_separate_assets
**Since:** 5.8 | **Tags:** #Recent
Filters whether block styles should be loaded separately. Returning false loads all core block assets, regardless of whether they are rendered in a page or not. Returning true loads core block assets only when they are rendered.

### use_widgets_block_editor
**Params:** bool $use_widgets_block_editor
**Since:** 5.8 | **Tags:** #Recent
Filters whether to use the block editor to manage widgets.

### widget_block_content
**Params:** string $content, array $instance, WP_Widget_Block $widget
**Since:** 5.8 | **Tags:** #Recent
Filters the content of the Block widget before output.

### widget_block_dynamic_classname
**Params:** string $classname, string $block_name
**Since:** 5.8 | **Tags:** #Recent
The classname used in the block widget's container HTML. This can be set according to the name of the block contained by the block widget.

### widget_types_to_hide_from_legacy_widget_block
**Since:** 5.8 | **Tags:** #Recent

### activate_tinymce_for_media_description
**Since:** 6.6 | **Tags:** #Recent

### frontpage_template_hierarchy
**Since:** 6.6 | **Tags:** #Recent

### index_template_hierarchy
**Since:** 6.6 | **Tags:** #Recent

### page_template_hierarchy
**Since:** 6.6 | **Tags:** #Recent

### {$template_type}_template_hierarchy
**Since:** 6.6 | **Tags:** #Variable #Recent

### should_load_block_assets_on_demand
**Params:** bool $load_assets_on_demand
**Since:** 6.8 | **Tags:** #Recent
Filters whether block styles should be loaded on demand. Returning false loads all block assets, regardless of whether they are rendered in a page or not. Returning true loads block assets only when they are rendered. The default value of the filter depends on the result of {@see wp_should_load_separate_core_block_assets()}, which controls whether Core block stylesheets should be loaded separately or via a combined 'wp-block-library' stylesheet.

### theme_block_pattern_files
**Params:** array $files, string $dirpath
**Since:** 6.8 | **Tags:** #Recent
Filters list of block pattern files for a theme.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
