# WordPress Filters: Admin / Backend / Dashboard

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### manage_posts_columns
**Params:** string[] $posts_columns, string $post_type
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the columns displayed in the Posts list table.

### admin_body_class
**Params:** string $classes
**Since:** 2.3 | **Tags:** #Legacy
Filters the CSS classes for the body tag in the admin. This filter differs from the {@see 'post_class'} and {@see 'body_class'} filters in two important ways: 1. `$classes` is a space-separated string of class names instead of an array. 2. Not all core admin classes are filterable, notably: wp-admin, wp-core-ui, and no-js cannot be removed.

### dashboard_primary_feed
**Since:** 2.3 | **Tags:** #Legacy

### dashboard_primary_title
**Since:** 2.3 | **Tags:** #Legacy

### dashboard_secondary_feed
**Since:** 2.3 | **Tags:** #Legacy

### dashboard_secondary_link
**Since:** 2.3 | **Tags:** #Legacy

### dashboard_secondary_title
**Since:** 2.3 | **Tags:** #Legacy

### update_footer
**Params:** string $content
**Since:** 2.3 | **Tags:** #Legacy
Filters the version/update text displayed in the admin footer. WordPress prints the current version and update information, using core_update_footer() at priority 10.

### async_upload_{$type}
**Since:** 2.5 | **Tags:** #Variable #Legacy

### dashboard_primary_link
**Since:** 2.5 | **Tags:** #Legacy

### manage_media_columns
**Params:** string[] $posts_columns, bool $detached
**Since:** 2.5 | **Tags:** #Legacy
Filters the Media list table columns.

### manage_pages_columns
**Params:** string[] $posts_columns
**Since:** 2.5 | **Tags:** #Legacy
Filters the columns displayed in the Pages list table.

### plugin_action_links
**Params:** string[] $actions, string $plugin_file, array $plugin_data, string $context
**Since:** 2.5 | **Tags:** #Legacy
Filters the action links displayed for each plugin in the Plugins list table.

### request_filesystem_credentials
**Params:** mixed $credentials, string $form_post, string $type, bool|WP_Error $error, string $context, array $extra_fields, bool $allow_relaxed_file_ownership
**Since:** 2.5 | **Tags:** #Legacy
Filters the filesystem credentials. Returning anything other than an empty string will effectively short-circuit output of the filesystem credentials form, returning that value instead. A filter should return true if no filesystem credentials are required, false if they are required but have not been provided, or an array of credentials if they are required and have been provided.

### wp_check_post_lock_window
**Params:** int $interval
**Since:** 2.5 | **Tags:** #Legacy
Filters the post lock window duration.

### wp_dashboard_widgets
**Params:** string[] $dashboard_widgets
**Since:** 2.5 | **Tags:** #Legacy
Filters the list of widgets to load for the admin dashboard.

### filesystem_method
**Params:** string $method, array $args, string $context, bool $allow_relaxed_file_ownership
**Since:** 2.6 | **Tags:** #Legacy
Filters the filesystem method to use.

### filesystem_method_file
**Params:** string $path, string $method
**Since:** 2.6 | **Tags:** #Legacy
Filters the path for a specific filesystem method class file.

### post_date_column_time
**Params:** string $t_time, WP_Post $post, string $column_name, string $mode
**Since:** 2.6 | **Tags:** #Legacy
Filters the published, scheduled, or unpublished time of the post.

### shortcut_link
**Params:** string $link
**Since:** 2.6 | **Tags:** #Legacy
Filters the Press This bookmarklet link.

### add_menu_classes
**Params:** array $menu
**Since:** 2.7 | **Tags:** #Legacy
Filters administration menu array with classes added for top-level items.

### admin_comment_types_dropdown
**Params:** string[] $comment_types
**Since:** 2.7 | **Tags:** #Legacy
Filters the comment types shown in the drop-down menu on the Comments list table.

### install_plugins_nonmenu_tabs
**Params:** string[] $nonmenu_tabs
**Since:** 2.7 | **Tags:** #Legacy
Filters tabs not associated with a menu item on the Add Plugins screen.

### install_plugins_tabs
**Params:** string[] $tabs
**Since:** 2.7 | **Tags:** #Legacy
Filters the tabs shown on the Add Plugins screen.

### install_plugin_complete_actions
**Params:** string[] $install_actions, object $api, string $plugin_file
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of action links available following a single plugin installation.

### plugins_api
**Params:** false|object|array $result, string $action, object $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the response for the current WordPress.org Plugin Installation API request. Returning a non-false value will effectively short-circuit the WordPress.org API request. If `$action` is 'query_plugins' or 'plugin_information', an object MUST be passed. If `$action` is 'hot_tags', an array should be passed.

### plugins_api_args
**Params:** object $args, string $action
**Since:** 2.7 | **Tags:** #Legacy
Filters the WordPress.org Plugin Installation API arguments. Important: An object MUST be returned to this filter.

### plugins_api_result
**Params:** object|WP_Error $res, string $action, object $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the Plugin Installation API response results.

### plugin_action_links_{$plugin_file}
**Since:** 2.7 | **Tags:** #Variable #Legacy

### plugin_install_action_links
**Params:** string[] $action_links, array $plugin
**Since:** 2.7 | **Tags:** #Legacy
Filters the install action links for a plugin.

### quick_edit_dropdown_pages_args
**Params:** array $dropdown_args, bool $bulk
**Since:** 2.7 | **Tags:** #Legacy
Filters the arguments used to generate the Quick Edit page-parent drop-down.

### update_plugin_complete_actions
**Params:** string[] $update_actions, string $plugin
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of action links available following a single plugin update.

### admin_footer_text
**Params:** string $text
**Since:** 2.8 | **Tags:** #Legacy
Filters the "Thank you" text displayed in the admin footer.

### admin_url
**Params:** string $url, string $path, int|null $blog_id, string|null $scheme
**Since:** 2.8 | **Tags:** #Legacy
Filters the admin area URL.

### display_post_states
**Params:** WP_Post $post
**Since:** 2.8 | **Tags:** #Legacy
Filters the default post display states used in the posts list table.

### documentation_ignore_functions
**Params:** string[] $ignore_functions
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of functions and classes to be ignored from the documentation lookup.

### edit_categories_per_page
**Params:** int $tags_per_page
**Since:** 2.8 | **Tags:** #Legacy
Filters the number of terms displayed per page for the Categories list table.

### edit_posts_per_page
**Params:** int $posts_per_page, string $post_type
**Since:** 2.8 | **Tags:** #Legacy
Filters the number of posts displayed per page when specifically listing "posts".

### edit_tags_per_page
**Params:** int $tags_per_page
**Since:** 2.8 | **Tags:** #Legacy
Filters the number of terms displayed per page for the Tags list table.

### install_themes_nonmenu_tabs
**Params:** string[] $nonmenu_tabs
**Since:** 2.8 | **Tags:** #Legacy
Filters tabs not associated with a menu item on the Install Themes screen.

### install_themes_tabs
**Params:** string[] $tabs
**Since:** 2.8 | **Tags:** #Legacy
Filters the tabs shown on the Add Themes screen. This filter is for backward compatibility only, for the suppression of the upload tab.

### install_theme_complete_actions
**Params:** string[] $install_actions, object $api, string $stylesheet, WP_Theme $theme_info
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of action links available following a single theme installation.

### manage_users_custom_column
**Params:** string $output, string $column_name, int $user_id
**Since:** 2.8 | **Tags:** #Legacy
Filters the display output of custom columns in the Users list table.

### menu_order
**Params:** array $menu_order
**Since:** 2.8 | **Tags:** #Legacy
Filters the order of administration menu items. A truthy value must first be passed to the {@see 'custom_menu_order'} filter for this filter to work. Use the following to enable custom menu ordering: add_filter( 'custom_menu_order', '__return_true' );

### page_row_actions
**Params:** string[] $actions, WP_Post $post
**Since:** 2.8 | **Tags:** #Legacy
Filters the array of row action links on the Pages list table. The filter is evaluated only for hierarchical post types.

### plugins_url
**Params:** string $url, string $path, string $plugin
**Since:** 2.8 | **Tags:** #Legacy
Filters the URL to the plugins directory.

### plugin_row_meta
**Since:** 2.8 | **Tags:** #Legacy

### post_row_actions
**Params:** string[] $actions, WP_Post $post
**Since:** 2.8 | **Tags:** #Legacy
Filters the array of row action links on the Posts list table. The filter is evaluated only for non-hierarchical post types.

### print_admin_styles
**Params:** bool $print
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to print the admin styles.

### print_footer_scripts
**Params:** bool $print
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to print the footer scripts.

### print_head_scripts
**Params:** bool $print
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to print the head scripts.

### screen_layout_columns
**Params:** array $empty_columns, string $screen_id, WP_Screen $screen
**Since:** 2.8 | **Tags:** #Legacy
Filters the array of screen layout columns. This hook provides back-compat for plugins using the back-compat Filters instead of add_screen_option().

### set-screen-option
**Params:** mixed $screen_option, string $option, int $value
**Since:** 2.8 | **Tags:** #Legacy
Filters a screen option value before it is set. The filter can also be used to modify non-standard `[items]_per_page` settings. See the parent function for a full list of standard options. Returning false from the filter will skip saving the current option.

### tag_row_actions
**Params:** string[] $actions, WP_Term $tag
**Since:** 2.8 | **Tags:** #Legacy
Filters the action links displayed for each term in the Tags list table.

### themes_api
**Params:** false|object|array $override, string $action, object $args
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to override the WordPress.org Themes API. Returning a non-false value will effectively short-circuit the WordPress.org API request. If `$action` is 'query_themes', 'theme_information', or 'feature_list', an object MUST be passed. If `$action` is 'hot_tags', an array should be passed.

### themes_api_args
**Params:** object $args, string $action
**Since:** 2.8 | **Tags:** #Legacy
Filters arguments used to query for installer pages from the WordPress.org Themes API. Important: An object MUST be returned to this filter.

### themes_api_result
**Params:** array|stdClass|WP_Error $res, string $action, stdClass $args
**Since:** 2.8 | **Tags:** #Legacy
Filters the returned WordPress.org Themes API response.

### update_theme_complete_actions
**Params:** string[] $update_actions, string $theme
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of action links available following a single theme update.

### upgrader_clear_destination
**Params:** true|WP_Error $removed, string $local_destination, string $remote_destination, array $hook_extra
**Since:** 2.8 | **Tags:** #Legacy
Filters whether the upgrader cleared the destination.

### upgrader_post_install
**Params:** bool $response, array $hook_extra, array $result
**Since:** 2.8 | **Tags:** #Legacy
Filters the installation response after the installation has finished.

### upgrader_pre_install
**Params:** bool|WP_Error $response, array $hook_extra
**Since:** 2.8 | **Tags:** #Legacy
Filters the installation response before the installation has started. Returning a value that could be evaluated as a `WP_Error` will effectively short-circuit the installation, returning that value instead.

### upgrader_source_selection
**Params:** string|WP_Error $source, string $remote_source, WP_Upgrader $upgrader, array $hook_extra
**Since:** 2.8 | **Tags:** #Legacy
Filters the source file location for the upgrade package.

### admin_post_thumbnail_html
**Params:** string $content, int $post_id, int|null $thumbnail_id
**Since:** 2.9 | **Tags:** #Legacy
Filters the admin post thumbnail HTML markup to return.

### fs_ftp_connection_types
**Params:** string[] $types, array $credentials, string $type, bool|WP_Error $error, string $context
**Since:** 2.9 | **Tags:** #Legacy
Filters the connection types to output to the filesystem credentials form.

### admin_memory_limit
**Params:** int|string $filtered_limit
**Since:** 3.0 | **Tags:** #Modern
Filters the maximum memory limit available for administration screens. This only applies to administrators, who may require more memory for tasks like updates. Memory limits when processing images (uploaded or edited by users of any role) are handled separately. The `WP_MAX_MEMORY_LIMIT` constant specifically defines the maximum memory limit available when in the administration back end. The default is 256M (256 megabytes of memory) or the original `memory_limit` php.ini value if this is higher.

### all_plugins
**Params:** array $all_plugins
**Since:** 3.0 | **Tags:** #Modern
Filters the full array of plugins to list in the Plugins list table.

### current_screen
**Params:** WP_Screen $current_screen
**Since:** 3.0 | **Tags:** #Modern
Fires after the current screen has been set.

### manage_{$post_type}_posts_columns
**Since:** 3.0 | **Tags:** #Variable #Modern

### manage_{$screen->id}_columns
**Since:** 3.0 | **Tags:** #Variable #Modern

### parent_file
**Params:** string $parent_file
**Since:** 3.0 | **Tags:** #Modern
Filters the parent file of an admin menu sub-menu item. Allows plugins to move sub-menu items around.

### post_updated_messages
**Params:** array[] $messages
**Since:** 3.0 | **Tags:** #Modern
Filters the post updated messages.

### privacy_on_link_text
**Params:** string $content
**Since:** 3.0 | **Tags:** #Modern
Filters the link label for the 'Search engines discouraged' message displayed in the 'At a Glance' dashboard widget. Prior to 3.8.0, the widget was named 'Right Now'.

### privacy_on_link_title
**Params:** string $title
**Since:** 3.0 | **Tags:** #Modern
Filters the link title attribute for the 'Search engines discouraged' message displayed in the 'At a Glance' dashboard widget. Prior to 3.8.0, the widget was named 'Right Now'.

### screen_settings
**Params:** string $screen_settings, WP_Screen $screen
**Since:** 3.0 | **Tags:** #Modern
Filters the screen settings text displayed in the Screen Options tab.

### show_advanced_plugins
**Params:** bool $show, string $type
**Since:** 3.0 | **Tags:** #Modern
Filters whether to display the advanced plugins list table. There are two types of advanced plugins - must-use and drop-ins - which can be used in a single site or Multisite network. The $type parameter allows you to differentiate between the type of advanced plugins to filter the display of. Contexts include 'mustuse' and 'dropins'.

### update_bulk_plugins_complete_actions
**Params:** string[] $update_actions, array $plugin_info
**Since:** 3.0 | **Tags:** #Modern
Filters the list of action links available following bulk plugin updates.

### update_bulk_theme_complete_actions
**Params:** string[] $update_actions, WP_Theme $theme_info
**Since:** 3.0 | **Tags:** #Modern
Filters the list of action links available following bulk theme updates.

### admin_title
**Params:** string $admin_title, string $title
**Since:** 3.1 | **Tags:** #Modern
Filters the title tag content for an admin page.

### all_themes
**Since:** 3.1 | **Tags:** #Modern

### default_hidden_meta_boxes
**Params:** string[] $hidden, WP_Screen $screen
**Since:** 3.1 | **Tags:** #Modern
Filters the default list of hidden meta boxes.

### enter_title_here
**Params:** string $text, WP_Post $post
**Since:** 3.1 | **Tags:** #Modern
Filters the title field placeholder text.

### force_filtered_html_on_import
**Params:** bool $force
**Since:** 3.1 | **Tags:** #Modern
Filters whether to filter imported data through kses on import. Multisite uses this hook to filter all data through kses by default, as a super administrator may be assisting an untrusted user.

### show_recent_comments_widget_style
**Since:** 3.1 | **Tags:** #Modern

### wp_admin_bar_class
**Params:** string $wp_admin_bar_class
**Since:** 3.1 | **Tags:** #Modern
Filters the admin bar class to instantiate.

### wp_network_dashboard_widgets
**Params:** string[] $dashboard_widgets
**Since:** 3.1 | **Tags:** #Modern
Filters the list of widgets to load for the Network Admin dashboard.

### wp_user_dashboard_widgets
**Params:** string[] $dashboard_widgets
**Since:** 3.1 | **Tags:** #Modern
Filters the list of widgets to load for the User Admin dashboard.

### browse-happy-notice
**Params:** string $notice, array|false $response
**Since:** 3.2 | **Tags:** #Modern
Filters the notice output for the 'Browse Happy' nag meta box.

### screen_options_show_screen
**Params:** bool $show_screen, WP_Screen $screen
**Since:** 3.2 | **Tags:** #Modern
Filters whether to show the Screen Options tab.

### hidden_meta_boxes
**Params:** string[] $hidden, WP_Screen $screen, bool $use_defaults
**Since:** 3.3 | **Tags:** #Modern
Filters the list of hidden meta boxes.

### page_attributes_dropdown_pages_args
**Params:** array $dropdown_args, WP_Post $post
**Since:** 3.3 | **Tags:** #Modern
Filters the arguments used to generate a Pages drop-down element.

### print_late_styles
**Params:** bool $print
**Since:** 3.3 | **Tags:** #Modern
Filters whether to print the styles queued too late for the HTML head.

### bulk_actions-{$this->screen->id}
**Since:** 3.5 | **Tags:** #Variable #Modern

### manage_taxonomies_for_{$post_type}_columns
**Since:** 3.5 | **Tags:** #Variable #Modern

### manage_{$this->screen->id}_sortable_columns
**Since:** 3.5 | **Tags:** #Variable #Modern

### manage_{$this->screen->taxonomy}_custom_column
**Since:** 3.5 | **Tags:** #Variable #Modern

### views_{$this->screen->id}
**Since:** 3.5 | **Tags:** #Variable #Modern

### heartbeat_nopriv_received
**Params:** array $response, array $data, string $screen_id
**Since:** 3.6 | **Tags:** #Modern
Filters Heartbeat Ajax response in no-privilege environments.

### heartbeat_nopriv_send
**Params:** array $response, string $screen_id
**Since:** 3.6 | **Tags:** #Modern
Filters Heartbeat Ajax response in no-privilege environments when no data is passed.

### heartbeat_received
**Params:** array $response, array $data, string $screen_id
**Since:** 3.6 | **Tags:** #Modern
Filters the Heartbeat response received.

### heartbeat_send
**Params:** array $response, string $screen_id
**Since:** 3.6 | **Tags:** #Modern
Filters the Heartbeat response sent.

### heartbeat_settings
**Params:** array $settings
**Since:** 3.6 | **Tags:** #Modern
Filters the Heartbeat settings.

### override_post_lock
**Params:** bool $override, WP_Post $post, WP_User $user
**Since:** 3.6 | **Tags:** #Modern
Filters whether to allow the post lock to be overridden. Returning false from the filter will disable the ability to override the post lock.

### show_post_locked_dialog
**Params:** bool $display, WP_Post $post, WP_User $user
**Since:** 3.6 | **Tags:** #Modern
Filters whether to show the post locked dialog. Returning false from the filter will prevent the dialog from being displayed.

### ajax_query_attachments_args
**Params:** array $query
**Since:** 3.7 | **Tags:** #Modern
Filters the arguments passed to WP_Query during an Ajax call for querying attachments.

### audio_submitbox_misc_sections
**Params:** array $fields, WP_Post $post
**Since:** 3.7 | **Tags:** #Modern
Filters the audio attachment metadata fields to be shown in the publish meta box. The key for each item in the array should correspond to an attachment metadata key, and the value should be the desired label.

### bulk_post_updated_messages
**Params:** array[] $bulk_messages, int[] $bulk_counts
**Since:** 3.7 | **Tags:** #Modern
Filters the bulk action updated messages. By default, custom post types use the messages for the 'post' post type.

### install_plugins_table_api_args_{$tab}
**Since:** 3.7 | **Tags:** #Variable #Modern

### install_themes_table_api_args_{$tab}
**Since:** 3.7 | **Tags:** #Variable #Modern

### months_dropdown_results
**Params:** object[] $months, string $post_type
**Since:** 3.7 | **Tags:** #Modern
Filters the 'Months' drop-down results.

### plugins_update_check_locales
**Params:** string[] $locales
**Since:** 3.7 | **Tags:** #Modern
Filters the locales requested for plugin translations.

### upgrader_pre_download
**Params:** false|string|WP_Error $reply, string $package, WP_Upgrader $upgrader, array $hook_extra
**Since:** 3.7 | **Tags:** #Modern
Filters whether to download a package for a WordPress core, plugin, theme, or translation upgrade. Return a non-false value to short-circuit the download and return that value instead.

### dashboard_glance_items
**Params:** string[] $items
**Since:** 3.8 | **Tags:** #Modern
Filters the array of extra elements to list in the 'At a Glance' dashboard widget. Prior to 3.8.0, the widget was named 'Right Now'. Each element is wrapped in list-item tags on output.

### install_themes_table_api_args_{$old_filter}
**Since:** 3.9 | **Tags:** #Variable #Modern

### {$action}_prefilter
**Since:** 4.0 | **Tags:** #Variable #Modern

### dashboard_recent_posts_query_args
**Params:** array $query_args
**Since:** 4.2 | **Tags:** #Modern
Filters the query arguments used for the Recent Posts widget.

### disable_months_dropdown
**Params:** bool $disable, string $post_type
**Since:** 4.2 | **Tags:** #Modern
Filters whether to remove the 'Months' drop-down from the post list table.

### pre_prepare_themes_for_js
**Params:** array $prepared_themes, WP_Theme[]|null $themes, string $current_theme
**Since:** 4.2 | **Tags:** #Modern
Filters theme data before it is prepared for JavaScript. Passing a non-empty array will result in wp_prepare_themes_for_js() returning early with that value instead.

### quick_edit_show_taxonomy
**Params:** bool $show_in_quick_edit, string $taxonomy_name, string $post_type
**Since:** 4.2 | **Tags:** #Modern
Filters whether the current taxonomy should be shown in the Quick Edit panel.

### removable_query_args
**Params:** string[] $removable_query_args
**Since:** 4.2 | **Tags:** #Modern
Filters the list of query variable names to remove.

### list_table_primary_column
**Params:** string $default, string $context
**Since:** 4.3 | **Tags:** #Modern
Filters the name of the primary column for the current list table.

### upgrader_package_options
**Params:** array $options
**Since:** 4.3 | **Tags:** #Modern
Filters the package options before running an update. See also {@see 'upgrader_process_complete'}.

### admin_post_thumbnail_size
**Params:** string|int[] $size, int $thumbnail_id, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the size used to display the post thumbnail image in the 'Featured image' meta box. Note: When a theme adds 'post-thumbnail' support, a special 'post-thumbnail' image size is registered, which differs from the 'thumbnail' image size managed via the Settings > Media screen.

### dashboard_recent_drafts_query_args
**Params:** array $query_args
**Since:** 4.4 | **Tags:** #Modern
Filters the post query arguments for the 'Recent Drafts' dashboard widget.

### dashboard_secondary_items
**Since:** 4.4 | **Tags:** #Modern

### default_hidden_columns
**Params:** string[] $hidden, WP_Screen $screen
**Since:** 4.4 | **Tags:** #Modern
Filters the default list of hidden columns.

### hidden_columns
**Params:** string[] $hidden, WP_Screen $screen, bool $use_defaults
**Since:** 4.4 | **Tags:** #Modern
Filters the list of hidden columns.

### screen_options_show_submit
**Params:** bool $show_button, WP_Screen $screen
**Since:** 4.4 | **Tags:** #Modern
Filters whether to show the Screen Options submit button.

### show_network_active_plugins
**Params:** bool $show
**Since:** 4.4 | **Tags:** #Modern
Filters whether to display network-active plugins alongside plugins active for the current site. This also controls the display of inactive network-only plugins (plugins with "Network: true" in the plugin header). Plugins cannot be network-activated or network-deactivated from this screen.

### submenu_file
**Params:** string $submenu_file, string $parent_file
**Since:** 4.4 | **Tags:** #Modern
Filters the file of an admin menu sub-menu item.

### update_right_now_text
**Params:** string $content
**Since:** 4.4 | **Tags:** #Modern
Filters the text displayed in the 'At a Glance' dashboard widget. Prior to 3.8.0, the widget was named 'Right Now'.

### users_list_table_query_args
**Params:** array $args
**Since:** 4.4 | **Tags:** #Modern
Filters the query arguments used to retrieve users for the current users list table.

### view_mode_post_types
**Params:** string[] $view_mode_post_types
**Since:** 4.4 | **Tags:** #Modern
Filters the post types that have different view mode options.

### disable_categories_dropdown
**Params:** bool $disable, string $post_type
**Since:** 4.6 | **Tags:** #Modern
Filters whether to remove the 'Categories' drop-down from the post list table.

### handle_network_bulk_actions->id}
**Since:** 4.7 | **Tags:** #Modern

### enable_login_autofocus
**Params:** bool $print
**Since:** 4.8 | **Tags:** #Modern
Filters whether to print the call to `wp_attempt_focus()` on the login screen.

### handle_bulk_actions-{$screen}
**Since:** 4.8 | **Tags:** #Variable #Modern

### handle_network_bulk_actions-{$screen}
**Since:** 4.8 | **Tags:** #Variable #Modern

### admin_referrer_policy
**Params:** string $policy
**Since:** 4.9 | **Tags:** #Modern
Filters the admin referrer policy header value.

### plugin_files_exclusions
**Params:** string[] $exclusions
**Since:** 4.9 | **Tags:** #Modern
Filters the array of excluded directories and files while scanning the folder.

### write_your_story
**Params:** string $text, WP_Post $post
**Since:** 5.0 | **Tags:** #Recent
Filters the body placeholder text.

### disable_formats_dropdown
**Params:** bool $disable, string $post_type
**Since:** 5.2 | **Tags:** #Recent
Filters whether to remove the 'Formats' drop-down from the post list table.

### postbox_classes_{$screen_id}_{$box_id}
**Since:** 5.2 | **Tags:** #Variable #Recent

### admin_email_check_interval
**Params:** int $interval
**Since:** 5.3 | **Tags:** #Recent
Filters the interval for redirecting the user to the admin email confirmation screen. If `0` (zero) is returned, the user will not be redirected.

### display_site_states
**Params:** string[] $site_states, WP_Site $site
**Since:** 5.3 | **Tags:** #Recent
Filters the default site display states for items in the Sites list table.

### admin_email_remind_interval
**Params:** int $interval
**Since:** 5.4 | **Tags:** #Recent
Filters the interval for dismissing the admin email confirmation screen. If `0` (zero) is returned, the "Remind me later" link will not be displayed.

### admin_viewport_meta
**Params:** string $viewport_meta
**Since:** 5.5 | **Tags:** #Recent
Filters the viewport meta in the admin.

### install_plugin_overwrite_actions
**Params:** string[] $install_actions, object $api, array $new_plugin_data
**Since:** 5.5 | **Tags:** #Recent
Filters the list of action links available following a single plugin installation failure when overwriting is allowed.

### install_plugin_overwrite_comparison
**Params:** string $table, array $current_plugin_data, array $new_plugin_data
**Since:** 5.5 | **Tags:** #Recent
Filters the compare table output for overwriting a plugin package on upload.

### install_theme_overwrite_actions
**Params:** string[] $install_actions, object $api, array $new_theme_data
**Since:** 5.5 | **Tags:** #Recent
Filters the list of action links available following a single theme installation failure when overwriting is allowed.

### install_theme_overwrite_comparison
**Params:** string $table, WP_Theme $current_theme_data, array $new_theme_data
**Since:** 5.5 | **Tags:** #Recent
Filters the compare table output for overwriting a theme package on upload.

### plugins_auto_update_enabled
**Params:** bool $enabled
**Since:** 5.5 | **Tags:** #Recent
Filters whether plugins auto-update is enabled.

### plugin_auto_update_debug_string
**Params:** string $auto_updates_string, string $plugin_path, array $plugin, bool $enabled
**Since:** 5.5 | **Tags:** #Recent
Filters the text string of the auto-updates setting for each plugin in the Site Health debug data.

### plugin_auto_update_setting_html
**Params:** string $html, string $plugin_file, array $plugin_data
**Since:** 5.5 | **Tags:** #Recent
Filters the HTML of the auto-updates setting for each plugin in the Plugins list table.

### set_screen_option_{$option}
**Since:** 5.5 | **Tags:** #Variable #Recent

### quick_edit_dropdown_authors_args
**Params:** array $users_opt, bool $bulk
**Since:** 5.6 | **Tags:** #Recent
Filters the arguments used to generate the Quick Edit authors drop-down.

### pre_months_dropdown_query
**Params:** object[]|false $months, string $post_type
**Since:** 5.7 | **Tags:** #Recent
Filters whether to short-circuit performing the months dropdown query.

### upgrader_install_package_result
**Params:** array|WP_Error $result, array $hook_extra
**Since:** 5.7 | **Tags:** #Recent
Filters the result of WP_Upgrader::install_package().

### plugin_install_description
**Params:** string $description, array $plugin
**Since:** 6.0 | **Tags:** #Recent
Filters the plugin card description on the Add Plugins screen.

### ajax_term_search_results
**Params:** string[] $results, WP_Taxonomy $taxonomy_object, string $search
**Since:** 6.1 | **Tags:** #Recent
Filters the Ajax term search results.

### plugins_list
**Params:** array[] $plugins
**Since:** 6.3 | **Tags:** #Recent
Filters the array of plugins for the list table.

### pre_get_available_post_mime_types
**Params:** string[]|null $mime_types, string $type
**Since:** 6.4 | **Tags:** #Recent
Filters the list of available post MIME types for the given post type.

### quick_edit_enabled_for_post_type
**Params:** bool $enable, string $post_type
**Since:** 6.4 | **Tags:** #Recent
Filters whether Quick Edit should be enabled for the given post type.

### quick_edit_enabled_for_taxonomy
**Params:** bool $enable, string $taxonomy
**Since:** 6.4 | **Tags:** #Recent
Filters whether Quick Edit should be enabled for the given taxonomy.

### manage_users-network_custom_column
**Params:** string $output, string $column_name, int $user_id
**Since:** 6.8 | **Tags:** #Recent
Filters the display output of custom columns in the Network Users list table.

### bulk_action_observer_ids
**Params:** array $bulk_action_observer_ids
**Since:** 6.9 | **Tags:** #Recent
Filters the array of field name attributes for bulk actions.

### quick_edit_statuses
**Params:** string $post_type, bool $bulk, bool $can_publish
**Since:** 6.9 | **Tags:** #Recent
Filters the statuses available in the Quick Edit and Bulk Edit UI.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
