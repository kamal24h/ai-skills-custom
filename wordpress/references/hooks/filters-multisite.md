# WordPress Filters: Multisite / Network

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### pre_site_transient_{$transient}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### site_transient_{$transient}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### add_signup_meta
**Params:** array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the new default site meta variables.

### allowed_themes
**Params:** string[] $allowed_themes
**Since:** 3.0 | **Tags:** #Modern
Filters the array of themes allowed on the network.

### allow_subdirectory_install
**Params:** bool $allow
**Since:** 3.0 | **Tags:** #Modern
Filters whether to enable the subdirectory installation feature in Multisite.

### blog_redirect_404
**Params:** string $no_blog_redirect
**Since:** 3.0 | **Tags:** #Modern
Filters the redirect URL for 404s on the main site. The filter is only evaluated if the NOBLOGREDIRECT constant is defined.

### delete_site_email_content
**Params:** string $content
**Since:** 3.0 | **Tags:** #Modern
Filters the text for the email sent to the site admin when a request to delete a site in a Multisite network is submitted. The following strings have a special meaning and will get replaced dynamically: - `###USERNAME###`   The current user's username. - `###URL_DELETE###` The link to click on to confirm the site deletion. - `###SITENAME###`   The name of the site. - `###SITEURL###`    The URL to the site.

### do_mu_upgrade
**Params:** bool $do_mu_upgrade
**Since:** 3.0 | **Tags:** #Modern
Filters whether to attempt to perform the multisite DB upgrade routine. In single site, the user would be redirected to wp-admin/upgrade.php. In multisite, the DB upgrade routine is automatically fired, but only when this filter returns true. If the network is 50 sites or less, it will run every time. Otherwise, it will throttle itself to reduce load.

### enable_update_services_configuration
**Params:** bool $enable
**Since:** 3.0 | **Tags:** #Modern
Filters whether to enable the Update Services section in the Writing settings screen.

### graceful_fail
**Since:** 3.0 | **Tags:** #Modern

### graceful_fail_template
**Since:** 3.0 | **Tags:** #Modern

### lang_codes
**Params:** string[] $lang_codes, string $code
**Since:** 3.0 | **Tags:** #Modern
Filters the language codes.

### ms_site_check
**Params:** bool|null $check
**Since:** 3.0 | **Tags:** #Modern
Filters checking the status of the current blog.

### mu_dropdown_languages
**Params:** string[] $output, string[] $lang_files, string $current
**Since:** 3.0 | **Tags:** #Modern
Filters the languages available in the dropdown.

### mu_menu_items
**Params:** string[] $admin_menus
**Since:** 3.0 | **Tags:** #Modern
Filters available network-wide administration menu options. Options returned to this filter are output as individual checkboxes that, when selected, enable site administrator access to the specified administration menu in certain contexts. Adding options for specific menus here hinges on the appropriate checks and capabilities being in place in the site dashboard on the other side. For instance, when the single default option, 'plugins' is enabled, site administrators are granted access to the Plugins screen in their individual sites' dashboards.

### myblogs_blog_actions
**Params:** string $actions, object $user_blog
**Since:** 3.0 | **Tags:** #Modern
Filters the row links displayed for each site on the My Sites screen.

### myblogs_options
**Params:** string $settings_html, string $context
**Since:** 3.0 | **Tags:** #Modern
Filters the settings HTML markup in the Global Settings section on the My Sites screen. By default, the Global Settings section is hidden. Passing a non-empty string to this filter will enable the section, and allow new settings to be added, either globally or for specific sites.

### network_admin_url
**Params:** string $url, string $path, string|null $scheme
**Since:** 3.0 | **Tags:** #Modern
Filters the network admin URL.

### network_home_url
**Params:** string $url, string $path, string|null $orig_scheme
**Since:** 3.0 | **Tags:** #Modern
Filters the network home URL.

### network_site_url
**Params:** string $url, string $path, string|null $scheme
**Since:** 3.0 | **Tags:** #Modern
Filters the network site URL.

### newblogname
**Params:** string $blogname
**Since:** 3.0 | **Tags:** #Modern
Filters the new site name during registration. The name is the site's subdomain or the site's subdirectory path depending on the network settings.

### newblog_notify_siteadmin
**Params:** string $msg, int|string $blog_id
**Since:** 3.0 | **Tags:** #Modern
Filters the message body of the new site activation email sent to the network administrator.

### newuser_notify_siteadmin
**Params:** string $msg, WP_User $user
**Since:** 3.0 | **Tags:** #Modern
Filters the message body of the new user activation email sent to the network administrator.

### new_admin_email_content
**Params:** string $email_text, array $new_admin_email
**Since:** 3.0 | **Tags:** #Modern
Filters the text of the email sent when a change of site admin email address is attempted. The following strings have a special meaning and will get replaced dynamically: - `###USERNAME###`  The current user's username. - `###ADMIN_URL###` The link to click on to confirm the email change. - `###EMAIL###`     The proposed new site admin email address. - `###SITENAME###`  The name of the site. - `###SITEURL###`   The URL to the site.

### new_user_email_content
**Params:** string $email_text, array $new_user_email
**Since:** 3.0 | **Tags:** #Modern
Filters the text of the email sent when a change of user email address is attempted. The following strings have a special meaning and will get replaced dynamically: - `###USERNAME###`  The current user's username. - `###ADMIN_URL###` The link to click on to confirm the email change. - `###EMAIL###`     The new email. - `###SITENAME###`  The name of the site. - `###SITEURL###`   The URL to the site.

### pre_add_site_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### pre_set_site_transient_{$transient}
**Since:** 3.0 | **Tags:** #Variable #Modern

### pre_site_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### pre_update_site_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### signup_another_blog_init
**Params:** array $signup_defaults
**Since:** 3.0 | **Tags:** #Modern
Filters the default site sign-up variables.

### signup_blog_init
**Params:** array $signup_blog_defaults
**Since:** 3.0 | **Tags:** #Modern
Filters the default site creation variables for the site sign-up form.

### signup_user_init
**Params:** array $signup_user_defaults
**Since:** 3.0 | **Tags:** #Modern
Filters the default user variables used on the user sign-up form.

### site_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### subdirectory_reserved_names
**Params:** string[] $subdirectory_reserved_names
**Since:** 3.0 | **Tags:** #Modern
Filters reserved site names on a sub-directory Multisite installation.

### tables_to_repair
**Params:** string[] $tables
**Since:** 3.0 | **Tags:** #Modern
Filters additional database tables to repair.

### update_welcome_email
**Params:** string $welcome_email, int $blog_id, int $user_id, string $password, string $title, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the content of the welcome email sent to the site administrator after site activation. Content should be formatted for transmission via wp_mail().

### update_welcome_subject
**Params:** string $subject
**Since:** 3.0 | **Tags:** #Modern
Filters the subject of the welcome email sent to the site administrator after site activation.

### update_welcome_user_email
**Params:** string $welcome_email, int $user_id, string $password, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the content of the welcome email after user activation. Content should be formatted for transmission via wp_mail().

### update_welcome_user_subject
**Params:** string $subject
**Since:** 3.0 | **Tags:** #Modern
Filters the subject of the welcome email after user activation.

### wpmu_active_signup
**Params:** string $active_signup
**Since:** 3.0 | **Tags:** #Modern
Filters the type of site sign-up.

### wpmu_blogs_columns
**Params:** string[] $sites_columns
**Since:** 3.0 | **Tags:** #Modern
Filters the displayed site columns in Sites list table.

### wpmu_delete_blog_upload_dir
**Params:** string $basedir, int $site_id
**Since:** 3.0 | **Tags:** #Modern
Filters the upload base directory to delete when the site is deleted.

### wpmu_drop_tables
**Params:** string[] $tables, int $site_id
**Since:** 3.0 | **Tags:** #Modern
Filters the tables to drop when the site is deleted.

### wpmu_signup_blog_notification
**Params:** string|false $domain, string $path, string $title, string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters whether to bypass the new site email notification.

### wpmu_signup_blog_notification_email
**Params:** string $content, string $domain, string $path, string $title, string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the message content of the new blog notification email. Content should be formatted for transmission via wp_mail().

### wpmu_signup_blog_notification_subject
**Params:** string $subject, string $domain, string $path, string $title, string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the subject of the new blog notification email.

### wpmu_signup_user_notification
**Params:** string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters whether to bypass the email notification for new user sign-up.

### wpmu_signup_user_notification_email
**Params:** string $content, string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the content of the notification email for new user sign-up. Content should be formatted for transmission via wp_mail().

### wpmu_signup_user_notification_subject
**Params:** string $subject, string $user_login, string $user_email, string $key, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters the subject of the notification email of new user signup.

### wpmu_users_columns
**Params:** string[] $users_columns
**Since:** 3.0 | **Tags:** #Modern
Filters the columns displayed in the Network Admin Users list table.

### wpmu_validate_blog_signup
**Params:** array $result
**Since:** 3.0 | **Tags:** #Modern
Filters site details and error messages following registration.

### wpmu_validate_user_signup
**Params:** array $result
**Since:** 3.0 | **Tags:** #Modern
Filters the validated user registration details. This does not allow you to override the username or email of the user during registration. The values are solely used for validation and error handling.

### wpmu_welcome_notification
**Params:** int|false $blog_id, int $user_id, string $password, string $title, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters whether to bypass the welcome email sent to the site administrator after site activation. Returning false disables the welcome email.

### wpmu_welcome_user_notification
**Params:** int $user_id, string $password, array $meta
**Since:** 3.0 | **Tags:** #Modern
Filters whether to bypass the welcome email after user activation. Returning false disables the welcome email.

### wp_signup_location
**Params:** string $sign_up_url
**Since:** 3.0 | **Tags:** #Modern
Filters the Multisite sign up URL.

### can_edit_network
**Params:** bool $result, int $network_id
**Since:** 3.1 | **Tags:** #Modern
Filters whether this network can be edited from this page.

### manage_sites_action_links
**Params:** string[] $actions, int $blog_id, string $blogname
**Since:** 3.1 | **Tags:** #Modern
Filters the action links displayed for each site in the Sites list table. The 'Edit', 'Dashboard', 'Delete Permanently', and 'Visit' links are displayed by default for each site. The site's status determines whether to show the 'Remove Deletion Flag' or 'Flag for Deletion' link, 'Unarchive' or 'Archive' links, and 'Not Spam' or 'Spam' link for each site.

### ms_user_list_site_actions
**Params:** string[] $actions, int $userblog_id
**Since:** 3.1 | **Tags:** #Modern
Filters the action links displayed next the sites a user belongs to in the Network Admin Users list table.

### network_sites_updated_message_{$action}
**Since:** 3.1 | **Tags:** #Variable #Modern

### show_network_site_users_add_existing_form
**Since:** 3.1 | **Tags:** #Modern

### show_network_site_users_add_new_form
**Since:** 3.1 | **Tags:** #Modern

### ms_user_row_actions
**Params:** string[] $actions, WP_User $user
**Since:** 3.2 | **Tags:** #Modern
Filters the action links displayed under each user in the Network Admin Users list table.

### redirect_network_admin_request
**Params:** bool $redirect_network_admin_request
**Since:** 3.2 | **Tags:** #Modern
Filters whether to redirect the request to the Network Admin.

### wp_is_large_network
**Params:** bool $is_large_network, string $component, int $count, int $network_id
**Since:** 3.3 | **Tags:** #Modern
Filters whether the network is considered large.

### default_site_option_{$option}
**Since:** 3.4 | **Tags:** #Variable #Modern

### blog_option_{$option}
**Since:** 3.5 | **Tags:** #Variable #Modern

### domain_exists
**Params:** int|null $result, string $domain, string $path, int $network_id
**Since:** 3.5 | **Tags:** #Modern
Filters whether a site name is taken. The name is the site's subdomain or the site's subdirectory path depending on the network settings.

### is_email_address_unsafe
**Params:** bool $is_email_address_unsafe, string $user_email
**Since:** 3.5 | **Tags:** #Modern
Filters whether an email address is unsafe.

### enable_live_network_counts
**Params:** bool $small_network, string $context
**Since:** 3.7 | **Tags:** #Modern
Filters whether to update network site or user counts when a new site is created.

### populate_network_meta
**Params:** array $sitemeta, int $network_id
**Since:** 3.7 | **Tags:** #Modern
Filters meta for a network on creation.

### network_by_path_segments_count
**Params:** int|null $segments, string $domain, string $path
**Since:** 3.9 | **Tags:** #Modern
Filters the number of path segments to consider when searching for a site.

### pre_get_network_by_path
**Params:** null|false|WP_Network $network, string $domain, string $path, int|null $segments, string[] $paths
**Since:** 3.9 | **Tags:** #Modern
Determines a network by its domain and path. This allows one to short-circuit the default logic, perhaps by replacing it with a routine that is more optimal for your setup. Return null to avoid the short-circuit. Return false if no network can be found at the requested domain and path. Otherwise, return an object from wp_get_network().

### pre_get_site_by_path
**Params:** null|false|WP_Site $site, string $domain, string $path, int|null $segments, string[] $paths
**Since:** 3.9 | **Tags:** #Modern
Determines a site by its domain and path. This allows one to short-circuit the default logic, perhaps by replacing it with a routine that is more optimal for your setup. Return null to avoid the short-circuit. Return false if no site can be found at the requested domain and path. Otherwise, return a site object.

### site_by_path_segments_count
**Params:** int|null $segments, string $domain, string $path
**Since:** 3.9 | **Tags:** #Modern
Filters the number of path segments to consider when searching for a site.

### get_main_network_id
**Params:** int $main_network_id
**Since:** 4.3 | **Tags:** #Modern
Filters the main network ID.

### get_site_icon_url
**Params:** string $url, int $size, int $blog_id
**Since:** 4.4 | **Tags:** #Modern
Filters the site icon URL.

### network_admin_plugin_action_links
**Params:** string[] $actions, string $plugin_file, array $plugin_data, string $context
**Since:** 4.4 | **Tags:** #Modern
Filters the action links displayed for each plugin in the Network Admin Plugins list table.

### network_admin_plugin_action_links_{$plugin_file}
**Since:** 4.4 | **Tags:** #Variable #Modern

### signup_get_available_languages
**Params:** string[] $languages
**Since:** 4.4 | **Tags:** #Modern
Filters the list of available languages for front-end site sign-ups. Passing an empty array to this hook will disable output of the setting on the sign-up form, and the default language will be used when creating the site. Languages not already installed will be stripped.

### network_allowed_themes
**Params:** string[] $allowed_themes, int $blog_id
**Since:** 4.5 | **Tags:** #Modern
Filters the array of themes allowed on the network. Site is provided as context so that a list of network allowed themes can be filtered further.

### site_allowed_themes
**Params:** string[] $allowed_themes, int $blog_id
**Since:** 4.5 | **Tags:** #Modern
Filters the array of themes allowed on the site.

### enable_loading_advanced_cache_dropin
**Since:** 4.6 | **Tags:** #Modern

### found_networks_query
**Params:** string $found_networks_query, WP_Network_Query $network_query
**Since:** 4.6 | **Tags:** #Modern
Filters the query used to retrieve found network count.

### found_sites_query
**Params:** string $found_sites_query, WP_Site_Query $site_query
**Since:** 4.6 | **Tags:** #Modern
Filters the query used to retrieve found site count.

### get_network
**Params:** WP_Network $_network
**Since:** 4.6 | **Tags:** #Modern
Fires after a network is retrieved.

### get_site
**Params:** WP_Site $_site
**Since:** 4.6 | **Tags:** #Modern
Fires after a site is retrieved.

### ms_sites_list_table_query_args
**Params:** array $args
**Since:** 4.6 | **Tags:** #Modern
Filters the arguments for the site query in the sites list table.

### networks_clauses
**Since:** 4.6 | **Tags:** #Modern

### network_edit_site_nav_links
**Params:** array $links
**Since:** 4.6 | **Tags:** #Modern
Filters the links that appear on site-editing network pages. Default links: 'site-info', 'site-users', 'site-themes', and 'site-settings'.

### pre_get_blogs_of_user
**Params:** null|object[] $sites, int $user_id, bool $all
**Since:** 4.6 | **Tags:** #Modern
Filters the list of a user's sites before it is populated. Returning a non-null value from the filter will effectively short circuit get_blogs_of_user(), returning that value instead.

### sites_clauses
**Since:** 4.6 | **Tags:** #Modern

### site_details
**Params:** stdClass $details
**Since:** 4.6 | **Tags:** #Modern
Filters a site's extended properties.

### site_search_columns
**Params:** string[] $search_columns, string $search, WP_Site_Query $query
**Since:** 4.6 | **Tags:** #Modern
Filters the columns to search in a WP_Site_Query search. The default columns include 'domain' and 'path.

### the_networks
**Since:** 4.6 | **Tags:** #Modern

### the_sites
**Since:** 4.6 | **Tags:** #Modern

### minimum_site_name_length
**Params:** int $length
**Since:** 4.8 | **Tags:** #Modern
Filters the minimum site name length required when validating a site signup.

### signup_site_meta
**Params:** array $meta, string $domain, string $path, string $title, string $user, string $user_email, string $key
**Since:** 4.8 | **Tags:** #Modern
Filters the metadata for a site signup. The metadata will be serialized prior to storing it in the database.

### signup_user_meta
**Params:** array $meta, string $user, string $user_email, string $key
**Since:** 4.8 | **Tags:** #Modern
Filters the metadata for a user signup. The metadata will be serialized prior to storing it in the database.

### can_add_user_to_blog
**Params:** true|WP_Error $retval, int $user_id, string $role, int $blog_id
**Since:** 4.9 | **Tags:** #Modern
Filters whether a user should be added to a site.

### network_admin_email_change_email
**Params:** array $email_change_email, string $old_email, string $new_email, int $network_id
**Since:** 4.9 | **Tags:** #Modern
Filters the contents of the email notification sent when the network admin email address is changed.

### new_network_admin_email_content
**Params:** string $email_text, array $new_admin_email
**Since:** 4.9 | **Tags:** #Modern
Filters the text of the email sent when a change of network admin email address is attempted. The following strings have a special meaning and will get replaced dynamically: - `###USERNAME###`  The current user's username. - `###ADMIN_URL###` The link to click on to confirm the email change. - `###EMAIL###`     The proposed new network admin email address. - `###SITENAME###`  The name of the network. - `###SITEURL###`   The URL to the network.

### pre_get_main_site_id
**Params:** int|null $main_site_id, WP_Network $network
**Since:** 4.9 | **Tags:** #Modern
Filters the main site ID. Returning a positive integer will effectively short-circuit the function.

### send_network_admin_email_change_email
**Params:** bool $send, string $old_email, string $new_email, int $network_id
**Since:** 4.9 | **Tags:** #Modern
Filters whether to send the network admin email change notification email.

### send_site_admin_email_change_email
**Params:** bool $send, string $old_email, string $new_email
**Since:** 4.9 | **Tags:** #Modern
Filters whether to send the site admin email change notification email.

### site_admin_email_change_email
**Params:** array $email_change_email, string $old_email, string $new_email
**Since:** 4.9 | **Tags:** #Modern
Filters the contents of the email notification sent when the site admin email address is changed.

### pre_wp_is_site_initialized
**Params:** bool|null $pre, int $site_id
**Since:** 5.1 | **Tags:** #Recent
Filters the check for whether a site is initialized before the database is accessed. Returning a non-null value will effectively short-circuit the function, returning that value instead.

### wp_normalize_site_data
**Params:** array $data
**Since:** 5.1 | **Tags:** #Recent
Filters passed site data in order to normalize it.

### ms_user_list_site_class
**Params:** string[] $site_classes, int $site_id, int $network_id, WP_User $user
**Since:** 5.2 | **Tags:** #Recent
Filters the span class for a site listing on the multisite user list table.

### networks_pre_query
**Since:** 5.2 | **Tags:** #Recent

### populate_site_meta
**Params:** array $meta, int $site_id
**Since:** 5.2 | **Tags:** #Recent
Filters meta for a site on creation.

### sites_pre_query
**Since:** 5.2 | **Tags:** #Recent

### new_site_email
**Params:** array $new_site_email, WP_Site $site, WP_User $user
**Since:** 5.6 | **Tags:** #Recent
Filters the content of the email sent to the Multisite network administrator when a new site is created. Content should be formatted for transmission via wp_mail().

### send_new_site_email
**Params:** bool $send, WP_Site $site, WP_User $user
**Since:** 5.6 | **Tags:** #Recent
Filters whether to send an email to the Multisite network administrator when a new site is created. Return false to disable sending the email.

### pre_site_option
**Params:** mixed $pre_option, string $option, int $network_id, mixed $default_value
**Since:** 6.9 | **Tags:** #Recent
Filters the value of any existing network option before it is retrieved. Returning a value other than false from the filter will short-circuit retrieval and return that value instead.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
