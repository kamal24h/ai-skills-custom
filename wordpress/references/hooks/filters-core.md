# WordPress Filters: Core / Options / i18n / Cron

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### locale
**Params:** string $locale
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the locale ID of the WordPress installation.

### query_vars
**Params:** string[] $public_query_vars
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the query variables allowed before processing. Allows (publicly allowed) query vars to be added, removed, or changed prior to executing the query. Needed to allow custom rewrite rules using your own arguments to work, or any other custom query variables you want to be publicly available.

### xmlrpc_methods
**Params:** string[] $methods
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the methods exposed by the XML-RPC server. This filter can be used to add new methods, and remove built-in methods.

### attribute_escape
**Params:** string $safe_text, string $text
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a string cleaned and escaped for output in an HTML attribute. Text passed to esc_attr() is stripped of invalid or special characters before output.

### gettext
**Params:** string $translation, string $text, string $domain
**Since:** 2.0.11 | **Tags:** #Legacy
Filters text with its translation.

### js_escape
**Params:** string $safe_text, string $text
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a string cleaned and escaped for output in JavaScript. Text passed to esc_js() is stripped of invalid or special characters, and properly slashed for output.

### query
**Params:** string $query
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the database query. Some queries are made before the plugins have been loaded, and thus cannot be filtered with this method.

### cron_schedules
**Params:** array $new_schedules
**Since:** 2.1 | **Tags:** #Legacy
Filters the non-default cron schedules.

### request
**Params:** array $query_vars
**Since:** 2.1 | **Tags:** #Legacy
Filters the array of parsed query variables.

### wp_redirect
**Params:** string $location, int $status
**Since:** 2.1 | **Tags:** #Legacy
Filters the redirect location.

### ngettext
**Params:** string $translation, string $single, string $plural, int $number, string $domain
**Since:** 2.2 | **Tags:** #Legacy
Filters the singular or plural form of a string.

### wp_mail
**Params:** array $args
**Since:** 2.2 | **Tags:** #Legacy
Filters the wp_mail() arguments.

### wp_mail_from
**Params:** string $from_email
**Since:** 2.2 | **Tags:** #Legacy
Filters the email address to send from.

### xmlrpc_text_filters
**Params:** array $filters
**Since:** 2.2 | **Tags:** #Legacy
Filters the MoveableType text filters list for XML-RPC.

### allowed_redirect_hosts
**Params:** string[] $hosts, string $host
**Since:** 2.3 | **Tags:** #Legacy
Filters the list of allowed hosts to redirect to.

### clean_url
**Params:** string $good_protocol_url, string $original_url, string $_context
**Since:** 2.3 | **Tags:** #Legacy
Filters a string cleaned and escaped for output as a URL.

### pre_kses
**Params:** string $content, array[]|string $allowed_html, string[] $allowed_protocols
**Since:** 2.3 | **Tags:** #Legacy
Filters content to be run through KSES.

### redirect_canonical
**Params:** string $redirect_url, string $requested_url
**Since:** 2.3 | **Tags:** #Legacy
Filters the canonical redirect URL. Returning false to this filter will cancel the redirect.

### sanitize_option_{$option}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### wp_mail_charset
**Params:** string $charset
**Since:** 2.3 | **Tags:** #Legacy
Filters the default wp_mail() charset.

### wp_mail_content_type
**Params:** string $content_type
**Since:** 2.3 | **Tags:** #Legacy
Filters the wp_mail() content type.

### wp_mail_from_name
**Params:** string $from_name
**Since:** 2.3 | **Tags:** #Legacy
Filters the name to associate with the "from" email address.

### wp_parse_str
**Params:** array $result
**Since:** 2.3 | **Tags:** #Legacy
Filters the array of variables derived from a parsed string.

### default_feed
**Params:** string $feed_type
**Since:** 2.5 | **Tags:** #Legacy
Filters the default feed type.

### deprecated_file_trigger_error
**Params:** bool $trigger
**Since:** 2.5 | **Tags:** #Legacy
Filters whether to trigger an error for deprecated files.

### deprecated_function_trigger_error
**Params:** bool $trigger
**Since:** 2.5 | **Tags:** #Legacy
Filters whether to trigger an error for deprecated functions.

### got_rewrite
**Params:** bool $got_rewrite
**Since:** 2.5 | **Tags:** #Legacy
Filters whether Apache and mod_rewrite are present. This filter was previously used to force URL rewriting for other servers, like nginx. Use the {@see 'got_url_rewrite'} filter in got_url_rewrite() instead.

### pre_remote_source
**Params:** string $remote_source, string $pagelinkedto
**Since:** 2.5 | **Tags:** #Legacy
Filters the pingback remote source.

### salt
**Params:** string $cached_salt, string $scheme
**Since:** 2.5 | **Tags:** #Legacy
Filters the WordPress salt.

### wp_redirect_status
**Params:** int $status, string $location
**Since:** 2.5 | **Tags:** #Legacy
Filters the redirect HTTP response status code to use.

### wp_sprintf
**Params:** string $fragment, string $arg
**Since:** 2.5 | **Tags:** #Legacy
Filters a fragment from the pattern passed to wp_sprintf(). If the fragment is unchanged, then sprintf() will be run on the fragment.

### wp_sprintf_l
**Params:** array $delimiters
**Since:** 2.5 | **Tags:** #Legacy
Filters the translated delimiters used by wp_sprintf_l(). Placeholders (%s) are included to assist translators and then removed before the array of strings reaches the filter. Please note: Ampersands and entities should be avoided here.

### xmlrpc_blog_options
**Params:** array $blog_options
**Since:** 2.6 | **Tags:** #Legacy
Filters the XML-RPC blog options property.

### http_headers_useragent
**Since:** 2.7 | **Tags:** #Legacy

### http_request_args
**Params:** array $parsed_args, string $url
**Since:** 2.7 | **Tags:** #Legacy
Filters the arguments used in an HTTP request.

### http_request_redirection_count
**Since:** 2.7 | **Tags:** #Legacy

### http_request_timeout
**Since:** 2.7 | **Tags:** #Legacy

### http_request_version
**Since:** 2.7 | **Tags:** #Legacy

### site_url
**Params:** string $url, string $path, string|null $scheme, int|null $blog_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the site URL.

### use_curl_transport
**Params:** bool $use_class, array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters whether cURL can be used as a transport for retrieving a URL.

### use_streams_transport
**Params:** bool $use_class, array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters whether streams can be used as a transport for retrieving a URL.

### xmlrpc_allow_anonymous_comments
**Params:** bool $allow
**Since:** 2.7 | **Tags:** #Legacy
Filters whether to allow anonymous comments over XML-RPC.

### block_local_requests
**Params:** bool $block
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to block local HTTP API requests. A local request is one to `localhost` or to the same host as the site itself.

### core_version_check_locale
**Params:** string $locale
**Since:** 2.8 | **Tags:** #Legacy
Filters the locale requested for WordPress core translations.

### esc_html
**Params:** string $safe_text, string $text
**Since:** 2.8 | **Tags:** #Legacy
Filters a string cleaned and escaped for output in HTML. Text passed to esc_html() is stripped of invalid or special characters before output.

### feed_content_type
**Params:** string $content_type, string $type
**Since:** 2.8 | **Tags:** #Legacy
Filters the content type for a specific feed type.

### gettext_with_context
**Params:** string $translation, string $text, string $context, string $domain
**Since:** 2.8 | **Tags:** #Legacy
Filters text with its translation based on context information.

### https_local_ssl_verify
**Params:** bool|string $ssl_verify, string $url
**Since:** 2.8 | **Tags:** #Legacy
Filters whether SSL should be verified for local HTTP API requests.

### https_ssl_verify
**Since:** 2.8 | **Tags:** #Legacy

### iis7_supports_permalinks
**Params:** bool $supports_permalinks
**Since:** 2.8 | **Tags:** #Legacy
Filters whether IIS 7+ supports pretty permalinks.

### includes_url
**Params:** string $url, string $path, string|null $scheme
**Since:** 2.8 | **Tags:** #Legacy
Filters the URL to the includes directory.

### ngettext_with_context
**Params:** string $translation, string $single, string $plural, int $number, string $context, string $domain
**Since:** 2.8 | **Tags:** #Legacy
Filters the singular or plural form of a string with gettext context.

### nocache_headers
**Params:** array $headers
**Since:** 2.8 | **Tags:** #Legacy
Filters the cache-controlling HTTP headers that are used to prevent caching.

### no_texturize_shortcodes
**Params:** string[] $default_no_texturize_shortcodes
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of shortcodes not to texturize.

### no_texturize_tags
**Params:** string[] $default_no_texturize_tags
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of HTML elements not to texturize.

### pre_transient_{$transient}
**Since:** 2.8 | **Tags:** #Variable #Legacy

### sanitize_email
**Params:** string $sanitized_email, string $email, string|null $message
**Since:** 2.8 | **Tags:** #Legacy
Filters a sanitized email address. This filter is evaluated under several contexts, including 'email_too_short', 'email_no_at', 'local_invalid_chars', 'domain_period_sequence', 'domain_period_limits', 'domain_no_periods', 'domain_no_valid_subs', or no context.

### sanitize_file_name
**Params:** string $filename, string $filename_raw
**Since:** 2.8 | **Tags:** #Legacy
Filters a sanitized filename string.

### sanitize_file_name_chars
**Params:** string[] $special_chars, string $filename_raw
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of characters to remove from a filename.

### sanitize_html_class
**Params:** string $sanitized, string $classname, string $fallback
**Since:** 2.8 | **Tags:** #Legacy
Filters a sanitized HTML class string.

### transient_{$transient}
**Since:** 2.8 | **Tags:** #Variable #Legacy

### wp_headers
**Params:** string[] $headers, WP $wp
**Since:** 2.8 | **Tags:** #Legacy
Filters the HTTP headers before they're sent to the browser.

### wp_mail_original_content
**Params:** string $content
**Since:** 2.8 | **Tags:** #Legacy
Filters the original content of the email. Give Post-By-Email extending plugins full access to the content, either the raw content, or the content of the last quoted-printable section.

### extra_{$context}_headers
**Since:** 2.9 | **Tags:** #Variable #Legacy

### http_response
**Params:** array $response, array $parsed_args, string $url
**Since:** 2.9 | **Tags:** #Legacy
Filters a successful HTTP API response immediately before the response is returned.

### load_textdomain_mofile
**Params:** string $mofile, string $domain
**Since:** 2.9 | **Tags:** #Legacy
Filters MO file path for loading translations for a specific text domain.

### override_load_textdomain
**Params:** bool $override, string $domain, string $mofile, string|null $locale
**Since:** 2.9 | **Tags:** #Legacy
Filters whether to override the .mo file loading.

### pre_http_request
**Params:** false|array|WP_Error $response, array $parsed_args, string $url
**Since:** 2.9 | **Tags:** #Legacy
Filters the preemptive return value of an HTTP request. Returning a non-false value from the filter will short-circuit the HTTP request and return early with that value. A filter should return one of: - An array containing 'headers', 'body', 'response', 'cookies', and 'filename' elements - A WP_Error instance - Boolean false to avoid short-circuiting the response Returning any other value may result in unexpected behavior.

### safe_style_css
**Params:** string[] $attr
**Since:** 2.9 | **Tags:** #Legacy
Filters the list of allowed CSS attributes.

### sanitize_text_field
**Params:** string $filtered, string $str
**Since:** 2.9 | **Tags:** #Legacy
Filters a sanitized text field string.

### smilies_src
**Params:** string $smiley_url, string $img, string $site_url
**Since:** 2.9 | **Tags:** #Legacy
Filters the Smiley image URL before it's used in the image element.

### {$option}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### deprecated_argument_trigger_error
**Params:** bool $trigger
**Since:** 3.0 | **Tags:** #Modern
Filters whether to trigger an error for deprecated arguments.

### home_url
**Params:** string $url, string $path, string|null $orig_scheme, int|null $blog_id
**Since:** 3.0 | **Tags:** #Modern
Filters the home URL.

### kses_allowed_protocols
**Params:** string[] $protocols
**Since:** 3.0 | **Tags:** #Modern
Filters the list of protocols allowed in HTML attributes.

### option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### override_unload_textdomain
**Params:** bool $override, string $domain, bool $reloadable
**Since:** 3.0 | **Tags:** #Modern
Filters whether to override the text domain unloading.

### paginate_links
**Params:** string $link
**Since:** 3.0 | **Tags:** #Modern
Filters the paginated links for the given archive pages.

### pre_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### pre_set_transient_{$transient}
**Since:** 3.0 | **Tags:** #Variable #Modern

### pre_update_option_{$option}
**Since:** 3.0 | **Tags:** #Variable #Modern

### robots_txt
**Params:** string $output, bool $public
**Since:** 3.0 | **Tags:** #Modern
Filters the robots.txt output.

### sanitize_key
**Params:** string $sanitized_key, string $key
**Since:** 3.0 | **Tags:** #Modern
Filters a sanitized key string.

### wp_die_handler
**Params:** callable $callback
**Since:** 3.0 | **Tags:** #Modern
Filters the callback for killing WordPress execution for all non-Ajax, non-JSON, non-XML requests.

### add_{$meta_type}_metadata
**Since:** 3.1 | **Tags:** #Variable #Modern

### delete_{$meta_type}_metadata
**Since:** 3.1 | **Tags:** #Variable #Modern

### doing_it_wrong_trigger_error
**Params:** bool $trigger, string $function_name, string $message, string $version
**Since:** 3.1 | **Tags:** #Modern
Filters whether to trigger an error for _doing_it_wrong() calls.

### esc_textarea
**Params:** string $safe_text, string $text
**Since:** 3.1 | **Tags:** #Modern
Filters a string cleaned and escaped for output in a textarea element.

### get_{$meta_type}_metadata
**Since:** 3.1 | **Tags:** #Variable #Modern

### schedule_event
**Params:** object|false $event
**Since:** 3.1 | **Tags:** #Modern
Modify an event before it is scheduled.

### update_{$meta_type}_metadata
**Since:** 3.1 | **Tags:** #Variable #Modern

### wp_xmlrpc_server_class
**Params:** string $class
**Since:** 3.1 | **Tags:** #Modern
Filters the class used for handling XML-RPC requests.

### is_protected_meta
**Params:** bool $protected, string $meta_key, string $meta_type
**Since:** 3.2 | **Tags:** #Modern
Filters whether a meta key is considered protected.

### option_page_capability_{$option_page}
**Since:** 3.2 | **Tags:** #Variable #Modern

### sanitize_mime_type
**Params:** string $sani_mime_type, string $mime_type
**Since:** 3.2 | **Tags:** #Modern
Filters a mime type following sanitization.

### use_google_chrome_frame
**Params:** bool $is_admin
**Since:** 3.2 | **Tags:** #Modern
Filters whether Google Chrome Frame should be used, if available.

### dbdelta_create_queries
**Params:** string[] $cqueries
**Since:** 3.3 | **Tags:** #Modern
Filters the dbDelta SQL queries for creating tables and/or databases. Queries filterable via this hook contain "CREATE TABLE" or "CREATE DATABASE".

### dbdelta_insert_queries
**Params:** string[] $iqueries
**Since:** 3.3 | **Tags:** #Modern
Filters the dbDelta SQL queries for inserting or updating. Queries filterable via this hook contain "INSERT INTO" or "UPDATE".

### dbdelta_queries
**Params:** string[] $queries
**Since:** 3.3 | **Tags:** #Modern
Filters the dbDelta SQL queries.

### pre_ent2ncr
**Params:** string|null $converted_text, string $text
**Since:** 3.3 | **Tags:** #Modern
Filters text before named entities are converted into numbered entities. A non-null string must be returned for the filter to be evaluated.

### allowed_http_origin
**Params:** string $origin, string $origin_arg
**Since:** 3.4 | **Tags:** #Modern
Changes the allowed HTTP origin result.

### allowed_http_origins
**Params:** string[] $allowed_origins
**Since:** 3.4 | **Tags:** #Modern
Changes the origin types allowed for HTTP requests.

### default_option_{$option}
**Since:** 3.4 | **Tags:** #Variable #Modern

### http_origin
**Params:** string $origin
**Since:** 3.4 | **Tags:** #Modern
Changes the origin of an HTTP request.

### sanitize_trackback_urls
**Params:** string $urls_to_ping, string $to_ping
**Since:** 3.4 | **Tags:** #Modern
Filters a list of trackback URLs following sanitization. The string returned here consists of a space or carriage return-delimited list of trackback URLs.

### set_url_scheme
**Params:** string $url, string $scheme, string|null $orig_scheme
**Since:** 3.4 | **Tags:** #Modern
Filters the resulting URL after setting the scheme.

### split_the_query
**Params:** bool $split_the_query, WP_Query $query, string $old_request, string[] $clauses
**Since:** 3.4 | **Tags:** #Modern
Filters whether to split the query. Splitting the query will cause it to fetch just the IDs of the found posts (and then individually fetch each post by ID), rather than fetching every complete row at once. One massive result vs. many small results.

### wp_die_ajax_handler
**Params:** callable $callback
**Since:** 3.4 | **Tags:** #Modern
Filters the callback for killing WordPress execution for Ajax requests.

### wp_die_xmlrpc_handler
**Params:** callable $callback
**Since:** 3.4 | **Tags:** #Modern
Filters the callback for killing WordPress execution for XML-RPC requests.

### wp_http_cookie_value
**Since:** 3.4 | **Tags:** #Modern

### wp_terms_checklist_args
**Params:** array|string $args, int $post_id
**Since:** 3.4 | **Tags:** #Modern
Filters the taxonomy terms checklist arguments.

### xmlrpc_default_posttype_fields
**Params:** array $fields, string $method
**Since:** 3.4 | **Tags:** #Modern
Filters the default post type query fields used by the given XML-RPC method.

### xmlrpc_default_post_fields
**Params:** array $fields, string $method
**Since:** 3.4 | **Tags:** #Modern
Filters the default post query fields used by the given XML-RPC method.

### xmlrpc_default_taxonomy_fields
**Params:** array $fields, string $method
**Since:** 3.4 | **Tags:** #Modern
Filters the default taxonomy query fields used by the given XML-RPC method.

### xmlrpc_prepare_comment
**Params:** array $_comment, WP_Comment $comment
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given comment.

### xmlrpc_prepare_media_item
**Params:** array $_media_item, WP_Post $media_item, string $thumbnail_size
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given media item.

### xmlrpc_prepare_page
**Params:** array $_page, WP_Post $page
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given page.

### xmlrpc_prepare_post
**Params:** array $_post, array $post, array $fields
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared date for the given post.

### xmlrpc_prepare_post_type
**Params:** array $_post_type, WP_Post_Type $post_type
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared date for the given post type.

### xmlrpc_prepare_taxonomy
**Params:** array $_taxonomy, WP_Taxonomy $taxonomy, array $fields
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given taxonomy.

### xmlrpc_prepare_term
**Params:** array $_term, array|object $term
**Since:** 3.4 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given term.

### xmlrpc_wp_insert_post_data
**Params:** array $post_data, array $content_struct
**Since:** 3.4 | **Tags:** #Modern
Filters post data array to be inserted via XML-RPC.

### cron_request
**Params:** array $cron_request_array, string $doing_wp_cron
**Since:** 3.5 | **Tags:** #Modern
Filters the cron request arguments.

### do_parse_request
**Params:** bool $bool, WP $wp, array|string $extra_query_vars
**Since:** 3.5 | **Tags:** #Modern
Filters whether to parse the request.

### exit_on_http_head
**Since:** 3.5 | **Tags:** #Modern

### option_enable_xmlrpc
**Since:** 3.5 | **Tags:** #Modern

### pre_get_space_used
**Params:** int|false $space_used
**Since:** 3.5 | **Tags:** #Modern
Filters the amount of storage space used by the current site, in megabytes.

### pre_http_send_through_proxy
**Params:** bool|null $override, string $uri, array $check, array $home
**Since:** 3.5 | **Tags:** #Modern
Filters whether to preempt sending the request through the proxy. Returning false will bypass the proxy; returning true will send the request through the proxy. Returning null bypasses the filter.

### pre_option_enable_xmlrpc
**Since:** 3.5 | **Tags:** #Modern

### wp_get_update_data
**Params:** array $update_data, array $titles
**Since:** 3.5 | **Tags:** #Modern
Filters the returned array of update data for plugins, themes, and WordPress core.

### wp_kses_allowed_html
**Params:** array[] $html, string $context
**Since:** 3.5 | **Tags:** #Modern
Filters the HTML tags that are allowed for a given context. HTML tags and attribute names are case-insensitive in HTML but must be added to the KSES allow list in lowercase. An item added to the allow list in upper or mixed case will not recognized as permitted by KSES.

### xmlrpc_default_revision_fields
**Params:** array $field, string $method
**Since:** 3.5 | **Tags:** #Modern
Filters the default revision query fields used by the given XML-RPC method.

### xmlrpc_default_user_fields
**Params:** array $fields, string $method
**Since:** 3.5 | **Tags:** #Modern
Filters the default user query fields used by the given XML-RPC method.

### xmlrpc_enabled
**Params:** bool $is_enabled
**Since:** 3.5 | **Tags:** #Modern
Filters whether XML-RPC methods requiring authentication are enabled. Contrary to the way it's named, this filter does not control whether XML-RPC is *fully* enabled, rather, it only controls whether XML-RPC methods requiring authentication - such as for publishing purposes - are enabled. Further, the filter does not control whether pingbacks or other custom endpoints that don't require authentication are enabled. This behavior is expected, and due to how parity was matched with the `enable_xmlrpc` UI option the filter replaced when it was introduced in 3.5. To disable XML-RPC methods that require authentication, use: add_filter( 'xmlrpc_enabled', '__return_false' ); For more granular control over all XML-RPC methods and requests, see the {@see 'xmlrpc_methods'} and {@see 'xmlrpc_element_limit'} hooks.

### xmlrpc_login_error
**Params:** IXR_Error $error, WP_Error $user
**Since:** 3.5 | **Tags:** #Modern
Filters the XML-RPC user login error message.

### xmlrpc_prepare_user
**Params:** array $_user, WP_User $user, array $fields
**Since:** 3.5 | **Tags:** #Modern
Filters XML-RPC-prepared data for the given user.

### http_request_host_is_external
**Params:** bool $external, string $host, string $url
**Since:** 3.6 | **Tags:** #Modern
Checks if HTTP request is external or not. Allows to change and allow external requests for the HTTP request.

### http_request_reject_unsafe_urls
**Since:** 3.6 | **Tags:** #Modern

### shortcode_atts_{$shortcode}
**Since:** 3.6 | **Tags:** #Variable #Modern

### wp_auth_check_load
**Params:** bool $show, WP_Screen $screen
**Since:** 3.6 | **Tags:** #Modern
Filters whether to load the authentication check. Returning a falsey value from the filter will effectively short-circuit loading the authentication check.

### wp_auth_check_same_domain
**Params:** bool $same_domain
**Since:** 3.6 | **Tags:** #Modern
Filters whether the authentication check originated at the same domain.

### wp_embed_handler_audio
**Params:** string $audio, array $attr, string $url, array $rawattr
**Since:** 3.6 | **Tags:** #Modern
Filters the audio embed output.

### wp_embed_handler_video
**Params:** string $video, array $attr, string $url, array $rawattr
**Since:** 3.6 | **Tags:** #Modern
Filters the video embed output.

### wp_http_accept_encoding
**Params:** string[] $type, string $url, array $args
**Since:** 3.6 | **Tags:** #Modern
Filters the allowed encoding types.

### wp_login_errors
**Params:** WP_Error $errors, string $redirect_to
**Since:** 3.6 | **Tags:** #Modern
Filters the login page errors.

### wp_mediaelement_fallback
**Params:** string $output, string $url
**Since:** 3.6 | **Tags:** #Modern
Filters the MediaElement fallback output for no-JS.

### wp_nav_locations_listed_per_menu
**Params:** int $locations
**Since:** 3.6 | **Tags:** #Modern
Filters the number of locations listed per menu in the drop-down select.

### wp_revisions_to_keep
**Params:** int $num, WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters the number of revisions to save for the given post. Overrides the value of WP_POST_REVISIONS.

### wp_save_post_revision_check_for_changes
**Params:** bool $check_for_changes, WP_Post $latest_revision, WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters whether the post has changed since the latest revision. By default a revision is saved only if one of the revisioned fields has changed. This filter can override that so a revision is saved even if nothing has changed.

### xmlrpc_pingback_error
**Params:** IXR_Error $error
**Since:** 3.6 | **Tags:** #Modern
Filters the XML-RPC pingback error return.

### allow_dev_auto_core_updates
**Params:** bool $upgrade_dev
**Since:** 3.7 | **Tags:** #Modern
Filters whether to enable automatic core updates for development versions.

### allow_major_auto_core_updates
**Params:** bool $upgrade_major
**Since:** 3.7 | **Tags:** #Modern
Filters whether to enable major automatic core updates.

### allow_minor_auto_core_updates
**Params:** bool $upgrade_minor
**Since:** 3.7 | **Tags:** #Modern
Filters whether to enable minor automatic core updates.

### automatic_updater_disabled
**Params:** bool $disabled
**Since:** 3.7 | **Tags:** #Modern
Filters whether to entirely disable background updates. There are more fine-grained filters and controls for selective disabling. This filter parallels the AUTOMATIC_UPDATER_DISABLED constant in name. This also disables update notification emails. That may change in the future.

### automatic_updates_is_vcs_checkout
**Params:** bool $checkout, string $context
**Since:** 3.7 | **Tags:** #Modern
Filters whether the automatic updater should consider a filesystem location to be potentially managed by a version control system.

### automatic_updates_send_debug_email
**Params:** bool $development_version
**Since:** 3.7 | **Tags:** #Modern
Filters whether to send a debugging email for each automatic background update.

### auto_core_update_email
**Params:** array $email, string $type, object $core_update, mixed $result
**Since:** 3.7 | **Tags:** #Modern
Filters the email sent following an automatic background core update.

### auto_core_update_send_email
**Since:** 3.7 | **Tags:** #Modern

### auto_update_{$type}
**Since:** 3.7 | **Tags:** #Variable #Modern

### date_query_valid_columns
**Params:** string[] $valid_columns
**Since:** 3.7 | **Tags:** #Modern
Filters the list of valid date query columns.

### flush_rewrite_rules_hard
**Params:** bool $hard
**Since:** 3.7 | **Tags:** #Modern
Filters whether a "hard" rewrite rule flush should be performed when requested. A "hard" flush updates .htaccess (Apache) or web.config (IIS).

### get_date_sql
**Params:** string $where, WP_Date_Query $query
**Since:** 3.7 | **Tags:** #Modern
Filters the date query WHERE clause.

### get_space_allowed
**Params:** int $space_allowed
**Since:** 3.7 | **Tags:** #Modern
Filters the upload quota for the current site.

### got_url_rewrite
**Params:** bool $got_url_rewrite
**Since:** 3.7 | **Tags:** #Modern
Filters whether URL rewriting is available.

### send_core_update_notification_email
**Params:** bool $notify, object $item
**Since:** 3.7 | **Tags:** #Modern
Filters whether to notify the site administrator of a new core update. By default, administrators are notified when the update offer received from WordPress.org sets a particular flag. This allows some discretion in if and when to notify. This filter is only evaluated once per release. If the same email address was already notified of the same new version, WordPress won't repeatedly email the administrator. This filter is also used on about.php to check if a plugin has disabled these notifications.

### themes_update_check_locales
**Params:** string[] $locales
**Since:** 3.7 | **Tags:** #Modern
Filters the locales requested for theme translations.

### update_translations_complete_actions
**Params:** string[] $update_actions
**Since:** 3.7 | **Tags:** #Modern
Filters the list of action links available following a translations update.

### wp_count_attachments
**Params:** stdClass $counts, string|string[] $mime_type
**Since:** 3.7 | **Tags:** #Modern
Filters the attachment counts by mime type.

### wp_count_posts
**Params:** stdClass $counts, string $type, string $perm
**Since:** 3.7 | **Tags:** #Modern
Filters the post counts by status for the current post type.

### wp_link_query
**Params:** array $results, array $query
**Since:** 3.7 | **Tags:** #Modern
Filters the link query results. Allows modification of the returned link query results.

### wp_link_query_args
**Params:** array $query
**Since:** 3.7 | **Tags:** #Modern
Filters the link query arguments. Allows modification of the link query arguments before querying.

### wp_search_stopwords
**Params:** string[] $stopwords
**Since:** 3.7 | **Tags:** #Modern
Filters stopwords used when parsing search terms.

### automatic_updates_debug_email
**Params:** array $email, int $failures, mixed $results
**Since:** 3.8 | **Tags:** #Modern
Filters the debug email that can be sent following an automatic background core update.

### wp_prepare_themes_for_js
**Params:** array $prepared_themes
**Since:** 3.8 | **Tags:** #Modern
Filters the themes prepared for JavaScript, for themes.php. Could be useful for changing the order, which is by name by default.

### incompatible_sql_modes
**Params:** array $incompatible_modes
**Since:** 3.9 | **Tags:** #Modern
Filters the list of incompatible SQL modes to exclude.

### option_{$option_name}
**Since:** 3.9 | **Tags:** #Variable #Modern

### pre_update_option
**Params:** mixed $value, string $option, mixed $old_value
**Since:** 3.9 | **Tags:** #Modern
Filters an option before its value is (maybe) serialized and updated.

### wp_header_image_attachment_metadata
**Params:** array $metadata
**Since:** 3.9 | **Tags:** #Modern
Filters the header image attachment metadata.

### wp_insert_attachment_data
**Params:** array $data, array $postarr, array $unsanitized_postarr, bool $update
**Since:** 3.9 | **Tags:** #Modern
Filters attachment post data before it is updated in or added to the database.

### wp_mce_translation
**Params:** array $mce_translation, string $mce_locale
**Since:** 3.9 | **Tags:** #Modern
Filters translated strings prepared for TinyMCE.

### async_update_translation
**Params:** bool $update, object $language_update
**Since:** 4.0 | **Tags:** #Modern
Filters whether to asynchronously update translation for core, a plugin, or a theme.

### attach_session_information
**Params:** array $session, int $user_id
**Since:** 4.0 | **Tags:** #Modern
Filters the information attached to the newly created session. Can be used to attach further information to a session.

### human_time_diff
**Params:** string $since, int $diff, int $from, int $to
**Since:** 4.0 | **Tags:** #Modern
Filters the human-readable difference between two timestamps.

### run_wptexturize
**Params:** bool $run_texturize
**Since:** 4.0 | **Tags:** #Modern
Filters whether to skip running wptexturize(). Returning false from the filter will effectively short-circuit wptexturize() and return the original text passed to the function instead. The filter runs only once, the first time wptexturize() is called.

### session_token_manager
**Params:** string $session
**Since:** 4.0 | **Tags:** #Modern
Filters the class name for the session token manager.

### translations_api
**Params:** false|array $result, string $type, object $args
**Since:** 4.0 | **Tags:** #Modern
Allows a plugin to override the WordPress.org Translation Installation API entirely.

### translations_api_result
**Params:** array|WP_Error $res, string $type, object $args
**Since:** 4.0 | **Tags:** #Modern
Filters the Translation Installation API response results.

### wp_embed_handler_youtube
**Params:** string $embed, array $attr, string $url, array $rawattr
**Since:** 4.0 | **Tags:** #Modern
Filters the YouTube embed output.

### wp_spaces_regexp
**Params:** string $spaces
**Since:** 4.0 | **Tags:** #Modern
Filters the regexp for common whitespace characters. This string is substituted for the \s sequence as needed in regular expressions. For websites not written in English, different characters may represent whitespace. For websites not encoded in UTF-8, the 0xC2 0xA0 sequence may not be in use.

### xmlrpc_element_limit
**Params:** int $element_limit
**Since:** 4.0 | **Tags:** #Modern
Filters the number of elements to parse in an XML-RPC response.

### meta_query_find_compatible_table_alias
**Params:** string|false $alias, array $clause, array $parent_query, WP_Meta_Query $query
**Since:** 4.1 | **Tags:** #Modern
Filters the table alias identified as compatible with the current clause.

### process_text_diff_html
**Params:** string $processed_line, string $line, string $context
**Since:** 4.1 | **Tags:** #Modern
Contextually filters a diffed line. Filters TextDiff processing of diffed line. By default, diffs are processed with htmlspecialchars. Use this filter to remove or change the processing. Passes a context indicating if the line is added, deleted or unchanged.

### revision_text_diff_options
**Params:** array $args, string $field, WP_Post $compare_from, WP_Post $compare_to
**Since:** 4.1 | **Tags:** #Modern
Filters revisions text diff options. Filters the options passed to wp_text_diff() when viewing a post revision.

### wp_constrain_dimensions
**Params:** int[] $dimensions, int $current_width, int $current_height, int $max_width, int $max_height
**Since:** 4.1 | **Tags:** #Modern
Filters dimensions to constrain down-sampled images to.

### wp_get_revision_ui_diff
**Params:** array[] $return, WP_Post $compare_from, WP_Post $compare_to
**Since:** 4.1 | **Tags:** #Modern
Filters the fields displayed in the post revision diff UI.

### wp_save_post_revision_post_has_changed
**Params:** bool $post_has_changed, WP_Post $latest_revision, WP_Post $post
**Since:** 4.1 | **Tags:** #Modern
Filters whether a post has changed. By default a revision is saved only if one of the revisioned fields has changed. This filter allows for additional checks to determine if there were changes.

### pre_get_col_charset
**Params:** string|null|false|WP_Error $charset, string $table, string $column
**Since:** 4.2 | **Tags:** #Modern
Filters the column charset value before the DB is checked. Passing a non-null value to the filter will short-circuit checking the DB for the charset, returning that value instead.

### pre_get_table_charset
**Params:** string|WP_Error|null $charset, string $table
**Since:** 4.2 | **Tags:** #Modern
Filters the table charset value before the DB is checked. Returning a non-null value from the filter will effectively short-circuit checking the DB for the charset, returning that value instead.

### deprecated_constructor_trigger_error
**Params:** bool $trigger
**Since:** 4.3 | **Tags:** #Modern
Filters whether to trigger an error for deprecated functions. `WP_DEBUG` must be true in addition to the filter evaluating to true.

### format_for_editor
**Params:** string $text, string $default_editor
**Since:** 4.3 | **Tags:** #Modern
Filters the text after it is formatted for the editor.

### wp_ajax_cropped_attachment_id
**Params:** int $attachment_id, string $context
**Since:** 4.3 | **Tags:** #Modern
Filters the attachment ID for a cropped image.

### wp_ajax_cropped_attachment_metadata
**Params:** array $metadata
**Since:** 4.3 | **Tags:** #Modern
Filters the cropped image attachment metadata.

### wp_refresh_nonces
**Params:** array $response, array $data, string $screen_id
**Since:** 4.3 | **Tags:** #Modern
Filters the nonces to send to the New/Edit Post screen.

### wp_safe_redirect_fallback
**Params:** string $fallback_url, int $status
**Since:** 4.3 | **Tags:** #Modern
Filters the redirect fallback URL for when the provided redirect is not safe (local).

### wp_should_upgrade_global_tables
**Params:** bool $should_upgrade
**Since:** 4.3 | **Tags:** #Modern
Filters if upgrade routines should be run on global tables.

### wp_unique_term_slug
**Params:** string $slug, object $term, string $original_slug
**Since:** 4.3 | **Tags:** #Modern
Filters the unique term slug.

### wp_unique_term_slug_is_bad_slug
**Params:** bool $needs_suffix, string $slug, object $term
**Since:** 4.3 | **Tags:** #Modern
Filters whether the proposed unique term slug is bad.

### expiration_of_site_transient_{$transient}
**Since:** 4.4 | **Tags:** #Variable #Modern

### expiration_of_transient_{$transient}
**Since:** 4.4 | **Tags:** #Variable #Modern

### wp_calculate_image_sizes
**Params:** string $sizes, string|int[] $size, string|null $image_src, array|null $image_meta, int $attachment_id
**Since:** 4.4 | **Tags:** #Modern
Filters the output of wp_calculate_image_sizes().

### wp_calculate_image_srcset
**Params:** array $sources, array $size_array, string $image_src, array $image_meta, int $attachment_id
**Since:** 4.4 | **Tags:** #Modern
Filters an image's 'srcset' sources.

### wp_http_ixr_client_headers
**Since:** 4.4 | **Tags:** #Modern

### wp_post_revision_title_expanded
**Params:** string $revision_date_author, WP_Post $revision, bool $link
**Since:** 4.4 | **Tags:** #Modern
Filters the formatted author and date for a revision.

### wp_prepare_revision_for_js
**Params:** array $revisions_data, WP_Post $revision, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the array of revisions used on the revisions screen.

### wp_theme_editor_filetypes
**Params:** string[] $default_types, WP_Theme $theme
**Since:** 4.4 | **Tags:** #Modern
Filters the list of file types allowed for editing in the theme file editor.

### xmlrpc_chunk_parsing_size
**Params:** int $chunk_size
**Since:** 4.4 | **Tags:** #Modern
Filters the chunk size that can be used to parse an XML-RPC response message.

### wp_calculate_image_srcset_meta
**Params:** array $image_meta, int[] $size_array, string $image_src, int $attachment_id
**Since:** 4.5 | **Tags:** #Modern
Pre-filters the image meta to be able to fix inconsistencies in the stored data.

### wp_get_comment_fields_max_lengths
**Params:** int[] $lengths
**Since:** 4.5 | **Tags:** #Modern
Filters the lengths for the comment form fields.

### wp_unique_filename
**Params:** string $filename, string $ext, string $dir, callable|null $unique_filename_callback, string[] $alt_filenames, int|string $number
**Since:** 4.5 | **Tags:** #Modern
Filters the result when generating a unique file name.

### deprecated_hook_trigger_error
**Params:** bool $trigger
**Since:** 4.6 | **Tags:** #Modern
Filters whether to trigger deprecated hook errors.

### enable_maintenance_mode
**Params:** bool $enable_checks, int $upgrading
**Since:** 4.6 | **Tags:** #Modern
Filters whether to enable maintenance mode. This filter runs before it can be used by plugins. It is designed for non-web runtimes. If this filter returns true, maintenance mode will be active and the request will end. If false, the request will be allowed to continue processing even if maintenance mode should be active.

### enable_wp_debug_mode_checks
**Params:** bool $enable_debug_mode
**Since:** 4.6 | **Tags:** #Modern
Filters whether to allow the debug mode check to occur. This filter runs before it can be used by plugins. It is designed for non-web runtimes. Returning false causes the `WP_DEBUG` and related constants to not be checked and the default PHP values for errors will be used unless you take care to update them yourself. To use this filter you must define a `$wp_filter` global before WordPress loads, usually in `wp-config.php`. Example: $GLOBALS['wp_filter'] = array( 'enable_wp_debug_mode_checks' => array( 10 => array( array( 'accepted_args' => 0, 'function'      => function() { return false; }, ), ), ), );

### sanitize_{$object_type}_meta_{$meta_key}
**Since:** 4.6 | **Tags:** #Variable #Modern

### wp_resource_hints
**Params:** array $urls, string $relation_type
**Since:** 4.6 | **Tags:** #Modern
Filters domains and URLs for resource hints of the given relation type.

### {$context}_memory_limit
**Since:** 4.6 | **Tags:** #Variable #Modern

### do_shortcode_tag
**Params:** string $output, string $tag, array $attr, array $m
**Since:** 4.7 | **Tags:** #Modern
Filters the output created by a shortcode callback.

### get_available_languages
**Params:** string[] $languages, string $dir
**Since:** 4.7 | **Tags:** #Modern
Filters the list of available language codes.

### pre_do_shortcode_tag
**Params:** false|string $output, string $tag, array $attr, array $m
**Since:** 4.7 | **Tags:** #Modern
Filters whether to call a shortcode callback. Returning a non-false value from filter will short-circuit the shortcode generation process, returning that value instead.

### sanitize_textarea_field
**Params:** string $filtered, string $str
**Since:** 4.7 | **Tags:** #Modern
Filters a sanitized textarea field string.

### strip_shortcodes_tagnames
**Params:** array $tags_to_remove, string $content
**Since:** 4.7 | **Tags:** #Modern
Filters the list of shortcode tags to remove from the content.

### wp_doing_ajax
**Params:** bool $wp_doing_ajax
**Since:** 4.7 | **Tags:** #Modern
Filters whether the current request is a WordPress Ajax request.

### wp_get_custom_css
**Params:** string $css, string $stylesheet
**Since:** 4.7 | **Tags:** #Modern
Filters the custom CSS output into the head element.

### wp_insert_term_data
**Params:** array $data, string $taxonomy, array $args
**Since:** 4.7 | **Tags:** #Modern
Filters term data before it is inserted into the database.

### wp_is_comment_flood
**Params:** bool $is_flood, string $comment_author_ip, string $comment_author_email, string $comment_date_gmt, bool $wp_error
**Since:** 4.7 | **Tags:** #Modern
Filters whether a comment is part of a comment flood. The default check is wp_check_comment_flood(). See check_comment_flood_db().

### wp_query_search_exclusion_prefix
**Params:** string $exclusion_prefix
**Since:** 4.7 | **Tags:** #Modern
Filters the prefix that indicates that a search term should be excluded from results.

### wp_update_comment_data
**Params:** array|WP_Error $data, array $comment, array $commentarr
**Since:** 4.7 | **Tags:** #Modern
Filters the comment data immediately before it is updated in the database. Note: data being passed to the filter is already unslashed.

### {$args[0]}
**Since:** 4.7 | **Tags:** #Variable #Modern

### {$value}
**Since:** 4.7 | **Tags:** #Variable #Modern

### file_mod_allowed
**Params:** bool $file_mod_allowed, string $context
**Since:** 4.8 | **Tags:** #Modern
Filters whether file modifications are allowed.

### send_auth_cookies
**Params:** bool $send, int $expire, int $expiration, int $user_id, string $scheme, string $token
**Since:** 4.8 | **Tags:** #Modern
Allows preventing auth cookies from actually being sent to the client.

### wp_doing_cron
**Params:** bool $wp_doing_cron
**Since:** 4.8 | **Tags:** #Modern
Filters whether the current request is a WordPress cron request.

### alloptions
**Params:** array $alloptions
**Since:** 4.9 | **Tags:** #Modern
Filters all options after retrieving them.

### available_permalink_structure_tags
**Params:** string[] $available_tags
**Since:** 4.9 | **Tags:** #Modern
Filters the list of available permalink structure tags on the Permalinks settings page.

### core_version_check_query_args
**Params:** array $query
**Since:** 4.9 | **Tags:** #Modern
Filters the query arguments sent as part of the core version check. WARNING: Changing this data may result in your site not receiving security updates. Please exercise extreme caution.

### pre_cache_alloptions
**Params:** array $alloptions
**Since:** 4.9 | **Tags:** #Modern
Filters all options before caching them.

### self_admin_url
**Params:** string $url, string $path, string $scheme
**Since:** 4.9 | **Tags:** #Modern
Filters the admin URL for the current site or network depending on context.

### wp_code_editor_settings
**Params:** array $settings, array $args
**Since:** 4.9 | **Tags:** #Modern
Filters settings that are passed into the code editor. Returning a falsey value will disable the syntax-highlighting code editor.

### wp_is_mobile
**Params:** bool $is_mobile
**Since:** 4.9 | **Tags:** #Modern
Filters whether the request should be treated as coming from a mobile device or not.

### wp_new_user_notification_email
**Params:** array $wp_new_user_notification_email, WP_User $user, string $blogname
**Since:** 4.9 | **Tags:** #Modern
Filters the contents of the new user notification email sent to the new user.

### wp_new_user_notification_email_admin
**Params:** array $wp_new_user_notification_email_admin, WP_User $user, string $blogname
**Since:** 4.9 | **Tags:** #Modern
Filters the contents of the new user notification email sent to the site admin.

### wp_password_change_notification_email
**Params:** array $wp_password_change_notification_email, WP_User $user, string $blogname
**Since:** 4.9 | **Tags:** #Modern
Filters the contents of the password change notification email sent to the site admin.

### wp_pre_insert_user_data
**Params:** array $data, bool $update, int|null $user_id, array $userdata
**Since:** 4.9 | **Tags:** #Modern
Filters user data before the record is created or updated. It only includes data in the users table, not any user metadata.

### wp_read_video_metadata
**Params:** array $metadata, string $file, string|null $file_format, array $data
**Since:** 4.9 | **Tags:** #Modern
Filters the array of metadata retrieved from a video. In core, usually this selection is what is stored. More complete data can be parsed from the `$data` parameter.

### block_parser_class
**Params:** string $parser_class
**Since:** 5.0 | **Tags:** #Recent
Filter to allow plugins to replace the server-side block parser.

### delete_{$meta_type}_metadata_by_mid
**Since:** 5.0 | **Tags:** #Variable #Recent

### determine_locale
**Params:** string $determined_locale
**Since:** 5.0 | **Tags:** #Recent
Filters the locale for the current request.

### get_object_subtype_{$object_type}
**Since:** 5.0 | **Tags:** #Variable #Recent

### get_{$meta_type}_metadata_by_mid
**Since:** 5.0 | **Tags:** #Variable #Recent

### pre_determine_locale
**Params:** string|null $locale
**Since:** 5.0 | **Tags:** #Recent
Filters the locale for the current request prior to the default determination process. Using this filter allows to override the default logic, effectively short-circuiting the function.

### sanitize_{$object_type}_meta_{$meta_key}_for_{$object_subtype}
**Since:** 5.0 | **Tags:** #Variable #Recent

### update_{$meta_type}_metadata_by_mid
**Since:** 5.0 | **Tags:** #Variable #Recent

### update_{$meta_type}_metadata_cache
**Since:** 5.0 | **Tags:** #Variable #Recent

### wp_anonymize_comment
**Params:** bool|string $anon_message, WP_Comment $comment, array $anonymized_comment
**Since:** 5.0 | **Tags:** #Recent
Filters whether to anonymize the comment.

### wp_privacy_anonymize_data
**Params:** string $anonymous, string $type, string $data
**Since:** 5.0 | **Tags:** #Recent
Filters the anonymous data for each type.

### wp_privacy_exports_dir
**Params:** string $exports_dir
**Since:** 5.0 | **Tags:** #Recent
Filters the directory used to store personal data export files.

### wp_privacy_exports_url
**Params:** string $exports_url
**Since:** 5.0 | **Tags:** #Recent
Filters the URL of the directory used to store personal data export files.

### wp_privacy_export_expiration
**Params:** int $expiration
**Since:** 5.0 | **Tags:** #Recent
Filters the lifetime, in seconds, of a personal data export file. By default, the lifetime is 3 days. Once the file reaches that age, it will automatically be deleted by a cron job.

### wp_privacy_personal_data_email_content
**Params:** string $email_text, int $request_id, array $email_data
**Since:** 5.0 | **Tags:** #Recent
Filters the text of the email sent with a personal data export file. The following strings have a special meaning and will get replaced dynamically: - `###EXPIRATION###` The date when the URL will be automatically deleted. - `###LINK###`       URL of the personal data export file for the user. - `###SITENAME###`   The name of the site. - `###SITEURL###`    The URL to the site.

### wp_privacy_personal_data_erasers
**Params:** array $args
**Since:** 5.0 | **Tags:** #Recent
Filters the array of personal data eraser callbacks.

### wp_privacy_personal_data_erasure_page
**Params:** array $response, int $eraser_index, string $email_address, int $page, int $request_id, string $eraser_key
**Since:** 5.0 | **Tags:** #Recent
Filters a page of personal data eraser data. Allows the erasure response to be consumed by destinations in addition to Ajax.

### wp_privacy_personal_data_exporters
**Params:** array $args
**Since:** 5.0 | **Tags:** #Recent
Filters the array of exporter callbacks.

### wp_privacy_personal_data_export_page
**Params:** array $response, int $exporter_index, string $email_address, int $page, int $request_id, bool $send_as_email, string $exporter_key
**Since:** 5.0 | **Tags:** #Recent
Filters a page of personal data exporter data. Used to build the export report. Allows the export response to be consumed by destinations in addition to Ajax.

### download_url_error_max_body_size
**Params:** int $size
**Since:** 5.1 | **Tags:** #Recent
Filters the maximum error response body size in `download_url()`.

### get_schedule
**Params:** string|false $schedule, string $hook, array $args
**Since:** 5.1 | **Tags:** #Recent
Filters the schedule name for a hook.

### load_script_textdomain_relative_path
**Params:** string|false $relative, string $src, bool $is_module
**Since:** 5.1 | **Tags:** #Recent
Filters the relative path of scripts used for finding translation files.

### load_script_translations
**Params:** string $translations, string $file, string $handle, string $domain
**Since:** 5.1 | **Tags:** #Recent
Filters script translations for the given file, script handle and text domain.

### load_script_translation_file
**Params:** string|false $file, string $handle, string $domain
**Since:** 5.1 | **Tags:** #Recent
Filters the file path for loading script translations for the given script handle and text domain.

### pre_clear_scheduled_hook
**Params:** null|int|false|WP_Error $pre, string $hook, array $args, bool $wp_error
**Since:** 5.1 | **Tags:** #Recent
Filter to override clearing a scheduled hook. Returning a non-null value will short-circuit the normal unscheduling process, causing the function to return the filtered value instead. For plugins replacing wp-cron, return the number of events successfully unscheduled (zero if no events were registered with the hook) or false or a WP_Error if unscheduling one or more events fails.

### pre_get_ready_cron_jobs
**Params:** null|array[] $pre
**Since:** 5.1 | **Tags:** #Recent
Filter to override retrieving ready cron jobs. Returning an array will short-circuit the normal retrieval of ready cron jobs, causing the function to return the filtered value instead.

### pre_get_scheduled_event
**Params:** null|false|object $pre, string $hook, array $args, int|null $timestamp
**Since:** 5.1 | **Tags:** #Recent
Filter to override retrieving a scheduled event. Returning a non-null value will short-circuit the normal process, returning the filtered value instead. Return false if the event does not exist, otherwise an event object should be returned.

### pre_load_script_translations
**Params:** string|false|null $translations, string|false $file, string $handle, string $domain
**Since:** 5.1 | **Tags:** #Recent
Pre-filters script translations for the given file, script handle and text domain. Returning a non-null value allows to override the default logic, effectively short-circuiting the function.

### pre_reschedule_event
**Params:** null|bool|WP_Error $pre, object $event, bool $wp_error
**Since:** 5.1 | **Tags:** #Recent
Filter to override rescheduling of a recurring event. Returning a non-null value will short-circuit the normal rescheduling process, causing the function to return the filtered value instead. For plugins replacing wp-cron, return true if the event was successfully rescheduled, false or a WP_Error if not.

### pre_schedule_event
**Params:** null|bool|WP_Error $result, object $event, bool $wp_error
**Since:** 5.1 | **Tags:** #Recent
Filter to override scheduling an event. Returning a non-null value will short-circuit adding the event to the cron array, causing the function to return the filtered value instead. Both single events and recurring events are passed through this filter; single events have `$event->schedule` as false, whereas recurring events have this set to a recurrence from wp_get_schedules(). Recurring events also have the integer recurrence interval set as `$event->interval`. For plugins replacing wp-cron, it is recommended you check for an identical event within ten minutes and apply the {@see 'schedule_event'} filter to check if another plugin has disallowed the event before scheduling. Return true if the event was scheduled, false or a WP_Error if not.

### pre_unschedule_event
**Params:** null|bool|WP_Error $pre, int $timestamp, string $hook, array $args, bool $wp_error
**Since:** 5.1 | **Tags:** #Recent
Filter to override unscheduling of events. Returning a non-null value will short-circuit the normal unscheduling process, causing the function to return the filtered value instead. For plugins replacing wp-cron, return true if the event was successfully unscheduled, false or a WP_Error if not.

### pre_unschedule_hook
**Params:** null|int|false|WP_Error $pre, string $hook, bool $wp_error
**Since:** 5.1 | **Tags:** #Recent
Filter to override clearing all events attached to the hook. Returning a non-null value will short-circuit the normal unscheduling process, causing the function to return the filtered value instead. For plugins replacing wp-cron, return the number of events successfully unscheduled (zero if no events were registered with the hook). If unscheduling one or more events fails then return either a WP_Error object or false depending on the value of the `$wp_error` parameter.

### wp_die_json_handler
**Params:** callable $callback
**Since:** 5.1 | **Tags:** #Recent
Filters the callback for killing WordPress execution for JSON requests.

### wp_initialize_site_args
**Params:** array $args, WP_Site $site, WP_Network $network
**Since:** 5.1 | **Tags:** #Recent
Filters the arguments for initializing a site.

### wp_insert_term_duplicate_term_check
**Params:** object $duplicate_term, string $term, string $taxonomy, array $args, int $tt_id
**Since:** 5.1 | **Tags:** #Recent
Filters the duplicate term check that takes place during term creation. Term parent + taxonomy + slug combinations are meant to be unique, and wp_insert_term() performs a last-minute confirmation of this uniqueness before allowing a new term to be created. Plugins with different uniqueness requirements may use this filter to bypass or modify the duplicate-term check.

### wp_kses_uri_attributes
**Params:** string[] $uri_attributes
**Since:** 5.1 | **Tags:** #Recent
Filters the list of attributes that are required to contain a URL. Use this filter to add any `data-` attributes that are required to be validated as a URL.

### wp_targeted_link_rel
**Params:** string $rel, string $link_html
**Since:** 5.1 | **Tags:** #Recent
Filters the rel values that are added to links with `target` attribute.

### wp_update_php_url
**Params:** string $update_url
**Since:** 5.1 | **Tags:** #Recent
Filters the URL to learn more about updating the PHP version the site is running on. Providing an empty string is not allowed and will result in the default URL being used. Furthermore the page the URL links to should preferably be localized in the site language.

### wp_using_themes
**Params:** bool $wp_using_themes
**Since:** 5.1 | **Tags:** #Recent
Filters whether the current request should use themes.

### x_redirect_by
**Params:** string|false $x_redirect_by, int $status, string $location
**Since:** 5.1 | **Tags:** #Recent
Filters the value of the `X-Redirect-By` HTTP header. Allows applications to identify themselves when they're doing a redirect.

### debug_information
**Since:** 5.2 | **Tags:** #Recent

### is_protected_endpoint
**Params:** bool $is_protected_endpoint
**Since:** 5.2 | **Tags:** #Recent
Filters whether the current request is against a protected endpoint. This filter is only fired when an endpoint is requested which is not already protected by WordPress core. As such, it exclusively allows providing further protected endpoints in addition to the admin backend, login pages and protected Ajax actions.

### recovery_email_support_info
**Params:** string $message
**Since:** 5.2 | **Tags:** #Recent
Filters the support message sent with the the fatal error protection email.

### recovery_mode_begin_url
**Params:** string $url, string $token, string $key
**Since:** 5.2 | **Tags:** #Recent
Filters the URL to begin recovery mode.

### recovery_mode_cookie_length
**Params:** int $length
**Since:** 5.2 | **Tags:** #Recent
Filters the length of time a Recovery Mode cookie is valid for.

### recovery_mode_email
**Params:** array $email, string $url
**Since:** 5.2 | **Tags:** #Recent
Filters the contents of the Recovery Mode email.

### recovery_mode_email_link_ttl
**Params:** int $valid_for
**Since:** 5.2 | **Tags:** #Recent
Filters the amount of time the recovery mode email link is valid for. The ttl must be at least as long as the email rate limit.

### recovery_mode_email_rate_limit
**Params:** int $rate_limit
**Since:** 5.2 | **Tags:** #Recent
Filters the rate limit between sending new recovery mode email links.

### site_status_tests
**Params:** array[] $tests
**Since:** 5.2 | **Tags:** #Recent
Filters which site status tests are run on a site. The site health is determined by a set of tests based on best practices from both the WordPress Hosting Team and web standards in general. Some sites may not have the same requirements, for example the automatic update checks may be handled by a host, and are therefore disabled in core. Or maybe you want to introduce a new test, is caching enabled/disabled/stale for example. Tests may be added either as direct, or asynchronous ones. Any test that may require some time to complete should run asynchronously, to avoid extended loading periods within wp-admin.

### site_status_test_php_modules
**Params:** array $modules
**Since:** 5.2 | **Tags:** #Recent
Filters the array representing all the modules we wish to test for.

### wp_die_jsonp_handler
**Params:** callable $callback
**Since:** 5.2 | **Tags:** #Recent
Filters the callback for killing WordPress execution for JSONP REST requests.

### wp_die_xml_handler
**Params:** callable $callback
**Since:** 5.2 | **Tags:** #Recent
Filters the callback for killing WordPress execution for XML requests.

### wp_direct_php_update_url
**Params:** string $direct_update_url
**Since:** 5.2 | **Tags:** #Recent
Filters the URL for directly updating the PHP version the site is running on from the host.

### wp_fatal_error_handler_enabled
**Params:** bool $enabled
**Since:** 5.2 | **Tags:** #Recent
Filters whether the fatal error handler is enabled. **Important:** This filter runs before it can be used by plugins. It cannot be used by plugins, mu-plugins, or themes. To use this filter you must define a `$wp_filter` global before WordPress loads, usually in `wp-config.php`. Example: $GLOBALS['wp_filter'] = array( 'wp_fatal_error_handler_enabled' => array( 10 => array( array( 'accepted_args' => 0, 'function'      => function() { return false; }, ), ), ), ); Alternatively you can use the `WP_DISABLE_FATAL_ERROR_HANDLER` constant.

### wp_is_php_version_acceptable
**Since:** 5.2 | **Tags:** #Recent

### wp_php_error_args
**Params:** array $args, array $error
**Since:** 5.2 | **Tags:** #Recent
Filters the arguments passed to {@see wp_die()} for the default PHP error template.

### wp_php_error_message
**Params:** string $message, array $error
**Since:** 5.2 | **Tags:** #Recent
Filters the message that the default PHP error template displays.

### wp_protected_ajax_actions
**Params:** string[] $actions_to_protect
**Since:** 5.2 | **Tags:** #Recent
Filters the array of protected Ajax actions. This filter is only fired when doing Ajax and the Ajax request has an 'action' property.

### wp_should_handle_php_error
**Params:** bool $should_handle_error, array $error
**Since:** 5.2 | **Tags:** #Recent
Filters whether a given thrown error should be handled by the fatal error handler. This filter is only fired if the error is not already configured to be handled by WordPress core. As such, it exclusively allows adding further rules for which errors should be handled, but not removing existing ones.

### wp_signature_hosts
**Params:** string[] $hostnames
**Since:** 5.2 | **Tags:** #Recent
Filters the list of hosts which should have Signature Verification attempted on.

### wp_signature_softfail
**Params:** bool $signature_softfail, string $url
**Since:** 5.2 | **Tags:** #Recent
Filters whether Signature Verification failures should be allowed to soft fail. WARNING: This may be removed from a future release.

### wp_signature_url
**Params:** false|string $signature_url, string $url
**Since:** 5.2 | **Tags:** #Recent
Filters the URL where the signature for a file is located.

### wp_trusted_keys
**Params:** string[] $trusted_keys
**Since:** 5.2 | **Tags:** #Recent
Filters the valid signing keys used to verify the contents of files.

### log_query_custom_data
**Params:** array $query_data, string $query, float $query_time, string $query_callstack, float $query_start
**Since:** 5.3 | **Tags:** #Recent
Filters the custom data to log alongside a query. Caution should be used when modifying any of this data, it is recommended that any additional information you need to store about a query be added as a new associative array element.

### make_clickable_rel
**Params:** string $rel, string $url
**Since:** 5.3 | **Tags:** #Recent
Filters the rel value that is added to URL matches converted to links.

### recovery_email_debug_info
**Params:** array $message
**Since:** 5.3 | **Tags:** #Recent
Filters the debug information included in the fatal error protection email.

### site_status_test_result
**Params:** array $test_result
**Since:** 5.3 | **Tags:** #Recent
Filters the output of a finished Site Health test.

### wp_date
**Params:** string $date, string $format, int $timestamp, DateTimeZone $timezone
**Since:** 5.3 | **Tags:** #Recent
Filters the date formatted based on the locale.

### wp_get_original_image_path
**Params:** string $original_image, int $attachment_id
**Since:** 5.3 | **Tags:** #Recent
Filters the path to the original image.

### wp_get_original_image_url
**Params:** string $original_image_url, int $attachment_id
**Since:** 5.3 | **Tags:** #Recent
Filters the URL to the original attachment image.

### wp_privacy_personal_data_email_subject
**Params:** string $subject, string $sitename, array $email_data
**Since:** 5.3 | **Tags:** #Recent
Filters the subject of the email sent when an export request is completed.

### wp_privacy_personal_data_email_to
**Params:** string $request_email, WP_User_Request $request
**Since:** 5.3 | **Tags:** #Recent
Filters the recipient of the personal data export email notification. Should be used with great caution to avoid sending the data export link to the wrong email.

### wp_privacy_additional_user_profile_data
**Params:** array $additional_user_profile_data, WP_User $user, string[] $reserved_names
**Since:** 5.4 | **Tags:** #Recent
Filters the user's profile data for the privacy exporter.

### wp_privacy_personal_data_email_headers
**Params:** string|array $headers, string $subject, string $content, int $request_id, array $email_data
**Since:** 5.4 | **Tags:** #Recent
Filters the headers of the email sent with a personal data export file.

### allowed_options
**Params:** array $allowed_options
**Since:** 5.5 | **Tags:** #Recent
Filters the allowed options list.

### auto_plugin_theme_update_email
**Params:** array $email, string $type, array $successful_updates, array $failed_updates
**Since:** 5.5 | **Tags:** #Recent
Filters the email sent following an automatic background update for plugins and themes.

### auto_plugin_update_send_email
**Params:** bool $enabled, array $update_results
**Since:** 5.5 | **Tags:** #Recent
Filters whether to send an email following an automatic background plugin update.

### auto_theme_update_send_email
**Params:** bool $enabled, array $update_results
**Since:** 5.5 | **Tags:** #Recent
Filters whether to send an email following an automatic background theme update.

### default_{$meta_type}_metadata
**Since:** 5.5 | **Tags:** #Variable #Recent

### esc_xml
**Params:** string $safe_text, string $text
**Since:** 5.5 | **Tags:** #Recent
Filters a string cleaned and escaped for output in XML. Text passed to esc_xml() is stripped of invalid or special characters before output. HTML named character references are converted to their equivalent code points.

### gettext_with_context_{$domain}
**Since:** 5.5 | **Tags:** #Variable #Recent

### gettext_{$domain}
**Since:** 5.5 | **Tags:** #Variable #Recent

### ngettext_with_context_{$domain}
**Since:** 5.5 | **Tags:** #Variable #Recent

### ngettext_{$domain}
**Since:** 5.5 | **Tags:** #Variable #Recent

### themes_auto_update_enabled
**Params:** bool $enabled
**Since:** 5.5 | **Tags:** #Recent
Filters whether themes auto-update is enabled.

### wp_edited_image_metadata
**Params:** array $new_image_meta, int $new_attachment_id, int $attachment_id
**Since:** 5.5 | **Tags:** #Recent
Filters the meta data for the new image created by editing an existing image.

### wp_img_tag_add_loading_attr
**Params:** string|bool $value, string $image, string $context
**Since:** 5.5 | **Tags:** #Recent
Filters the `loading` attribute value to add to an image. Default 'lazy'. Returning `false` or an empty string will not add the attribute. Returning `true` will add the default value.

### wp_img_tag_add_srcset_and_sizes_attr
**Params:** bool $value, string $image, string $context, int $attachment_id
**Since:** 5.5 | **Tags:** #Recent
Filters whether to add the `srcset` and `sizes` HTML attributes to the img tag. Default `true`. Returning anything else than `true` will not add the attributes.

### wp_img_tag_add_width_and_height_attr
**Params:** bool $value, string $image, string $context, int $attachment_id
**Since:** 5.5 | **Tags:** #Recent
Filters whether to add the missing `width` and `height` HTML attributes to the img tag. Default `true`. Returning anything else than `true` will not add the attributes.

### wp_lazy_loading_enabled
**Params:** bool $default, string $tag_name, string $context
**Since:** 5.5 | **Tags:** #Recent
Filters whether to add the `loading` attribute to the specified tag in the specified context.

### wp_opcache_invalidate_file
**Params:** bool $will_invalidate, string $filepath
**Since:** 5.5 | **Tags:** #Recent
Filters whether to invalidate a file from the opcode cache.

### wp_sitemaps_add_provider
**Params:** WP_Sitemaps_Provider $provider, string $name
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap provider before it is added.

### wp_sitemaps_enabled
**Params:** bool $is_enabled
**Since:** 5.5 | **Tags:** #Recent
Filters whether XML Sitemaps are enabled or not. When XML Sitemaps are disabled via this filter, rewrite rules are still in place to ensure a 404 is returned.

### wp_sitemaps_index_entry
**Params:** array $sitemap_entry, string $object_type, string $object_subtype, int $page
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap entry for the sitemap index.

### wp_sitemaps_max_urls
**Params:** int $max_urls, string $object_type
**Since:** 5.5 | **Tags:** #Recent
Filters the maximum number of URLs displayed on a sitemap.

### wp_sitemaps_posts_entry
**Params:** array $sitemap_entry, WP_Post $post, string $post_type
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap entry for an individual post.

### wp_sitemaps_posts_pre_max_num_pages
**Params:** int|null $max_num_pages, string $post_type
**Since:** 5.5 | **Tags:** #Recent
Filters the max number of pages before it is generated. Passing a non-null value will short-circuit the generation, returning that value instead.

### wp_sitemaps_posts_pre_url_list
**Params:** array[]|null $url_list, string $post_type, int $page_num
**Since:** 5.5 | **Tags:** #Recent
Filters the posts URL list before it is generated. Returning a non-null value will effectively short-circuit the generation, returning that value instead.

### wp_sitemaps_posts_query_args
**Params:** array $args, string $post_type
**Since:** 5.5 | **Tags:** #Recent
Filters the query arguments for post type sitemap queries.

### wp_sitemaps_posts_show_on_front_entry
**Params:** array $sitemap_entry
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap entry for the home page when the 'show_on_front' option equals 'posts'.

### wp_sitemaps_post_types
**Params:** WP_Post_Type[] $post_types
**Since:** 5.5 | **Tags:** #Recent
Filters the list of post object sub types available within the sitemap.

### wp_sitemaps_stylesheet_content
**Params:** string $xsl_content
**Since:** 5.5 | **Tags:** #Recent
Filters the content of the sitemap stylesheet.

### wp_sitemaps_stylesheet_css
**Params:** string $css
**Since:** 5.5 | **Tags:** #Recent
Filters the CSS only for the sitemap stylesheet.

### wp_sitemaps_stylesheet_index_content
**Params:** string $xsl_content
**Since:** 5.5 | **Tags:** #Recent
Filters the content of the sitemap index stylesheet.

### wp_sitemaps_stylesheet_index_url
**Params:** string $sitemap_url
**Since:** 5.5 | **Tags:** #Recent
Filters the URL for the sitemap index stylesheet. If a falsey value is returned, no stylesheet will be used and the "raw" XML of the sitemap index will be displayed.

### wp_sitemaps_stylesheet_url
**Params:** string $sitemap_url
**Since:** 5.5 | **Tags:** #Recent
Filters the URL for the sitemap stylesheet. If a falsey value is returned, no stylesheet will be used and the "raw" XML of the sitemap will be displayed.

### wp_sitemaps_taxonomies
**Params:** WP_Taxonomy[] $taxonomies
**Since:** 5.5 | **Tags:** #Recent
Filters the list of taxonomy object subtypes available within the sitemap.

### wp_sitemaps_taxonomies_entry
**Params:** array $sitemap_entry, int $term_id, string $taxonomy, WP_Term $term
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap entry for an individual term.

### wp_sitemaps_taxonomies_pre_max_num_pages
**Params:** int|null $max_num_pages, string $taxonomy
**Since:** 5.5 | **Tags:** #Recent
Filters the max number of pages for a taxonomy sitemap before it is generated. Passing a non-null value will short-circuit the generation, returning that value instead.

### wp_sitemaps_taxonomies_pre_url_list
**Params:** array[]|null $url_list, string $taxonomy, int $page_num
**Since:** 5.5 | **Tags:** #Recent
Filters the taxonomies URL list before it is generated. Returning a non-null value will effectively short-circuit the generation, returning that value instead.

### wp_sitemaps_taxonomies_query_args
**Params:** array $args, string $taxonomy
**Since:** 5.5 | **Tags:** #Recent
Filters the taxonomy terms query arguments. Allows modification of the taxonomy query arguments before querying.

### wp_sitemaps_users_entry
**Params:** array $sitemap_entry, WP_User $user
**Since:** 5.5 | **Tags:** #Recent
Filters the sitemap entry for an individual user.

### wp_sitemaps_users_pre_max_num_pages
**Params:** int|null $max_num_pages
**Since:** 5.5 | **Tags:** #Recent
Filters the max number of pages for a user sitemap before it is generated. Returning a non-null value will effectively short-circuit the generation, returning that value instead.

### wp_sitemaps_users_pre_url_list
**Params:** array[]|null $url_list, int $page_num
**Since:** 5.5 | **Tags:** #Recent
Filters the users URL list before it is generated. Returning a non-null value will effectively short-circuit the generation, returning that value instead.

### wp_sitemaps_users_query_args
**Params:** array $args
**Since:** 5.5 | **Tags:** #Recent
Filters the query arguments for authors with public posts. Allows modification of the authors query arguments before querying.

### wp_update_comment_type_batch_size
**Params:** int $comment_batch_size
**Since:** 5.5 | **Tags:** #Recent
Filters the comment batch size for updating the comment type.

### pre_recurse_dirsize
**Params:** int|false $space_used, string $directory, string|string[]|null $exclude, int $max_execution_time, array $directory_cache
**Since:** 5.6 | **Tags:** #Recent
Filters the amount of storage space used by one directory and all its children, in megabytes. Return the actual used space to short-circuit the recursive PHP file size calculation and use something else, like a CDN API or native operating system tools for better performance.

### wp_installed_email
**Params:** array $installed_email, WP_User $user, string $blog_title, string $blog_url, string $password
**Since:** 5.6 | **Tags:** #Recent
Filters the contents of the email sent to the site administrator when WordPress is installed.

### wp_is_application_passwords_available
**Params:** bool $available
**Since:** 5.6 | **Tags:** #Recent
Filters whether Application Passwords is available.

### wp_is_application_passwords_available_for_user
**Params:** bool $available, WP_User $user
**Since:** 5.6 | **Tags:** #Recent
Filters whether Application Passwords is available for a specific user.

### wp_untrash_post_status
**Params:** string $new_status, int $post_id, string $previous_status
**Since:** 5.6 | **Tags:** #Recent
Filters the status that a post gets assigned when it is restored from the trash (untrashed). By default posts that are restored will be assigned a status of 'draft'. Return the value of `$previous_status` in order to assign the status that the post had before it was trashed. The `wp_untrash_post_set_previous_status()` function is available for this. Prior to WordPress 5.6.0, restored posts were always assigned their original status.

### paginate_links_output
**Params:** string $r, array $args
**Since:** 5.7 | **Tags:** #Recent
Filters the HTML output of paginated links for archives.

### pre_wp_mail
**Params:** null|bool $return, array $atts
**Since:** 5.7 | **Tags:** #Recent
Filters whether to preempt sending an email. Returning a non-null value will short-circuit {@see wp_mail()}, returning that value instead. A boolean return value should be used to indicate whether the email was successfully sent.

### pre_wp_update_https_detection_errors
**Params:** null|WP_Error $pre
**Since:** 5.7 | **Tags:** #Recent
Short-circuits the process of detecting errors related to HTTPS support. Returning a `WP_Error` from the filter will effectively short-circuit the default logic of trying a remote request to the site over HTTPS, storing the errors array from the returned `WP_Error` instead.

### wp_direct_update_https_url
**Params:** string $direct_update_url
**Since:** 5.7 | **Tags:** #Recent
Filters the URL for directly updating the PHP version the site is running on from the host.

### wp_iframe_tag_add_loading_attr
**Params:** string|bool $value, string $iframe, string $context
**Since:** 5.7 | **Tags:** #Recent
Filters the `loading` attribute value to add to an iframe. Default 'lazy'. Returning `false` or an empty string will not add the attribute. Returning `true` will add the default value.

### wp_inline_script_attributes
**Params:** string $data
**Since:** 5.7 | **Tags:** #Recent
Filters attributes to be added to a script tag.

### wp_is_site_protected_by_basic_auth
**Params:** bool $is_protected, string $context
**Since:** 5.7 | **Tags:** #Recent
Filters whether a site is protected by HTTP Basic Auth.

### wp_robots
**Params:** array $robots
**Since:** 5.7 | **Tags:** #Recent
Filters the directives to be included in the 'robots' meta tag. The meta tag will only be included as necessary.

### wp_script_attributes
**Params:** array $attributes
**Since:** 5.7 | **Tags:** #Recent
Filters attributes to be added to a script tag.

### wp_should_replace_insecure_home_url
**Params:** bool $should_replace_insecure_home_url
**Since:** 5.7 | **Tags:** #Recent
Filters whether WordPress should replace old HTTP URLs to the site with their HTTPS counterpart. If a WordPress site had its URL changed from HTTP to HTTPS, by default this will return `true`. This filter can be used to disable that behavior, e.g. after having replaced URLs manually in the database.

### wp_update_https_url
**Params:** string $update_url
**Since:** 5.7 | **Tags:** #Recent
Filters the URL to learn more about updating the HTTPS version the site is running on. Providing an empty string is not allowed and will result in the default URL being used. Furthermore the page the URL links to should preferably be localized in the site language.

### {$action}_overrides
**Since:** 5.7 | **Tags:** #Variable #Recent

### enable_loading_object_cache_dropin
**Params:** bool $enable_object_cache
**Since:** 5.8 | **Tags:** #Recent
Filters whether to enable loading of the object-cache.php drop-in. This filter runs before it can be used by plugins. It is designed for non-web runtimes. If false is returned, object-cache.php will never be loaded.

### site_health_navigation_tabs
**Params:** string[] $tabs
**Since:** 5.8 | **Tags:** #Recent
Filters the extra tabs for the Site Health navigation bar. Add a custom page to the Site Health screen, based on a tab slug and label. The label you provide will also be used as part of the site title.

### styles_inline_size_limit
**Params:** int $total_inline_limit
**Since:** 5.8 | **Tags:** #Recent
The maximum size of inlined styles in bytes.

### update_plugins_{$hostname}
**Since:** 5.8 | **Tags:** #Variable #Recent

### wp_{$post->post_type}_revisions_to_keep
**Since:** 5.8 | **Tags:** #Variable #Recent

### {$hook_name}
**Since:** 5.8 | **Tags:** #Variable #Recent

### http_allowed_safe_ports
**Params:** int[] $allowed_ports, string $host, string $url
**Since:** 5.9 | **Tags:** #Recent
Controls the list of ports considered safe in HTTP API. Allows to change and allow external requests for the HTTP request.

### is_post_status_viewable
**Params:** bool $is_viewable, stdClass $post_status
**Since:** 5.9 | **Tags:** #Recent
Filters whether a post status is considered "viewable". The returned filtered value must be a boolean type to ensure `is_post_status_viewable()` only returns a boolean. This strictness is by design to maintain backwards-compatibility and guard against potential type errors in PHP 8.1+. Non-boolean values (even falsey and truthy values) will result in the function returning false.

### is_post_type_viewable
**Params:** bool $is_viewable, WP_Post_Type $post_type
**Since:** 5.9 | **Tags:** #Recent
Filters whether a post type is considered "viewable". The returned filtered value must be a boolean type to ensure `is_post_type_viewable()` only returns a boolean. This strictness is by design to maintain backwards-compatibility and guard against potential type errors in PHP 8.1+. Non-boolean values (even falsey and truthy values) will result in the function returning false.

### wp_omit_loading_attr_threshold
**Params:** int $omit_threshold
**Since:** 5.9 | **Tags:** #Recent
Filters the threshold for how many of the first content media elements to not lazy-load. For these first content media elements, the `loading` attribute will be omitted. By default, this is the case for only the very first content media element.

### wp_admin_bar_show_site_icons
**Params:** bool $show_site_icons
**Since:** 6.0 | **Tags:** #Recent
Filters whether to show the site icons in toolbar. Returning false to this hook is the recommended way to hide site icons in the toolbar. A truthy return may have negative performance impact on large multisites.

### wp_content_img_tag
**Params:** string $filtered_image, string $context, int $attachment_id
**Since:** 6.0 | **Tags:** #Recent
Filters an img tag within the content for a given context.

### wp_filesize
**Params:** int $size, string $path
**Since:** 6.0 | **Tags:** #Recent
Filters the size of the file.

### wp_is_large_user_count
**Params:** bool $is_large_user_count, int $count, int|null $network_id
**Since:** 6.0 | **Tags:** #Recent
Filters whether the site is considered large, based on its number of users.

### pre_option
**Params:** mixed $pre_option, string $option, mixed $default_value
**Since:** 6.1 | **Tags:** #Recent
Filters the value of any existing option before it is retrieved. Returning a value other than false from the filter will short-circuit retrieval and return that value instead.

### query_loop_block_query_vars
**Params:** array $query, WP_Block $block, int $page
**Since:** 6.1 | **Tags:** #Recent
Filters the arguments which will be passed to `WP_Query` for the Query Loop Block. Anything to this filter should be compatible with the `WP_Query` API to form the query context which will be passed down to the Query Loop Block's children. This can help, for example, to include additional settings or meta queries not directly supported by the core Query Loop Block, and extend its capabilities. Please note that this will only influence the query that will be rendered on the front-end. The editor preview is not affected by this filter. Also, worth noting that the editor preview uses the REST API, so, ideally, one should aim to provide attributes which are also compatible with the REST API, in order to be able to implement identical queries on both sides.

### site_status_available_object_cache_services
**Params:** string[] $services
**Since:** 6.1 | **Tags:** #Recent
Filters the persistent object cache services available to the user. This can be useful to hide or add services not included in the defaults.

### site_status_good_response_time_threshold
**Params:** int $threshold
**Since:** 6.1 | **Tags:** #Recent
Filters the threshold below which a response time is considered good. The default is based on https://web.dev/time-to-first-byte/.

### site_status_page_cache_supported_cache_headers
**Since:** 6.1 | **Tags:** #Recent
Filters the list of cache headers supported by core. This list indicates how each of the specified headers will be checked to indicate if a page cache is enabled or not. WordPress checks for each of the headers in the returned array. If the callback is provided, it will be passed the value for the corresponding header and return a boolean value indicating if the header suggests that a cache is active. If the value is `null` for the header, then WordPress will assume that a cache is active if the header is present, regardless of its value.

### site_status_persistent_object_cache_notes
**Params:** string $notes, string[] $available_services
**Since:** 6.1 | **Tags:** #Recent
Filters the second paragraph of the health check's description when suggesting the use of a persistent object cache. Hosts may want to replace the notes to recommend their preferred object caching solution. Plugin authors may want to append notes (not replace) on why object caching is recommended for their plugin.

### site_status_persistent_object_cache_thresholds
**Params:** int[] $thresholds
**Since:** 6.1 | **Tags:** #Recent
Filters the thresholds used to determine whether to suggest the use of a persistent object cache.

### site_status_persistent_object_cache_url
**Params:** string $action_url
**Since:** 6.1 | **Tags:** #Recent
Filters the action URL for the persistent object cache health check.

### site_status_should_suggest_persistent_object_cache
**Params:** bool|null $suggest
**Since:** 6.1 | **Tags:** #Recent
Filters whether to suggest use of a persistent object cache and bypass default threshold checks. Using this filter allows to override the default logic, effectively short-circuiting the method.

### update_themes_{$hostname}
**Since:** 6.1 | **Tags:** #Variable #Recent

### wp_allow_query_attachment_by_filename
**Params:** bool $allow_query_attachment_by_filename
**Since:** 6.1 | **Tags:** #Recent
Filters whether an attachment query should include filenames or not.

### wp_img_tag_add_decoding_attr
**Params:** string|false|null $value, string $image, string $context
**Since:** 6.1 | **Tags:** #Recent
Filters the `decoding` attribute value to add to an image. Default 'async'. Returning a falsey value will omit the attribute.

### wp_preload_resources
**Params:** array $preload_resources
**Since:** 6.1 | **Tags:** #Recent
Filters domains and URLs for resource preloads.

### wp_read_audio_metadata
**Params:** array $metadata, string $file, string|null $file_format, array $data
**Since:** 6.1 | **Tags:** #Recent
Filters the array of metadata retrieved from an audio file. In core, usually this selection is what is stored. More complete data can be parsed from the `$data` parameter.

### wp_required_field_indicator
**Params:** string $indicator
**Since:** 6.1 | **Tags:** #Recent
Filters the markup for a visual indicator of required form fields.

### wp_required_field_message
**Params:** string $message
**Since:** 6.1 | **Tags:** #Recent
Filters the message to explain required form fields.

### wp_send_new_user_notification_to_admin
**Params:** bool $send, WP_User $user
**Since:** 6.1 | **Tags:** #Recent
Filters whether the admin is notified of a new user registration.

### wp_send_new_user_notification_to_user
**Params:** bool $send, WP_User $user
**Since:** 6.1 | **Tags:** #Recent
Filters whether the user is notified of their new user registration.

### wp_theme_json_data_blocks
**Params:** WP_Theme_JSON_Data $theme_json
**Since:** 6.1 | **Tags:** #Recent
Filters the data provided by the blocks for global styles & settings.

### wp_theme_json_data_default
**Params:** WP_Theme_JSON_Data $theme_json
**Since:** 6.1 | **Tags:** #Recent
Filters the default data provided by WordPress for global styles & settings.

### wp_theme_json_data_theme
**Params:** WP_Theme_JSON_Data $theme_json
**Since:** 6.1 | **Tags:** #Recent
Filters the data provided by the theme for global styles and settings.

### wp_theme_json_data_user
**Params:** WP_Theme_JSON_Data $theme_json
**Since:** 6.1 | **Tags:** #Recent
Filters the data provided by the user for global styles & settings.

### wp_theme_json_get_style_nodes
**Params:** array $nodes
**Since:** 6.1 | **Tags:** #Recent
Filters the list of style nodes with metadata. This allows for things like loading block CSS independently.

### pre_wp_load_alloptions
**Params:** array|null $alloptions, bool $force_cache
**Since:** 6.2 | **Tags:** #Recent
Filters the array of alloptions before it is populated. Returning an array from the filter will effectively short circuit wp_load_alloptions(), returning that value instead.

### wp_internal_hosts
**Params:** string[] $internal_hosts
**Since:** 6.2 | **Tags:** #Recent
Filters the array of URL hosts which are considered internal.

### wp_save_post_revision_revisions_before_deletion
**Params:** WP_Post[] $revisions, int $post_id
**Since:** 6.2 | **Tags:** #Recent
Filters the revisions to be considered for deletion.

### cron_memory_limit
**Params:** int|string $filtered_limit
**Since:** 6.3 | **Tags:** #Recent
Filters the memory limit allocated for WP-Cron event processing.

### pre_load_textdomain
**Params:** bool|null $loaded, string $domain, string $mofile, string|null $locale
**Since:** 6.3 | **Tags:** #Recent
Filters whether to short-circuit loading .mo file. Returning a non-null value from the filter will effectively short-circuit the loading, returning the passed value instead.

### sanitize_locale_name
**Params:** string $sanitized, string $locale_name
**Since:** 6.3 | **Tags:** #Recent
Filters a sanitized locale name string.

### wp_min_priority_img_pixels
**Params:** int $threshold
**Since:** 6.3 | **Tags:** #Recent
Filters the minimum square-pixels threshold for an image to be eligible as the high-priority image.

### wp_navigation_should_create_fallback
**Params:** bool $create
**Since:** 6.3 | **Tags:** #Recent
Filters whether or not a fallback should be created.

### deprecated_class_trigger_error
**Params:** bool $trigger
**Since:** 6.4 | **Tags:** #Recent
Filters whether to trigger an error for a deprecated class.

### pre_wp_get_https_detection_errors
**Params:** null|WP_Error $pre
**Since:** 6.4 | **Tags:** #Recent
Short-circuits the process of detecting errors related to HTTPS support. Returning a `WP_Error` from the filter will effectively short-circuit the default logic of trying a remote request to the site over HTTPS, storing the errors array from the returned `WP_Error` instead.

### pre_wp_get_loading_optimization_attributes
**Params:** array|false $loading_attrs, string $tag_name, array $attr, string $context
**Since:** 6.4 | **Tags:** #Recent
Filters whether to short-circuit loading optimization attributes. Returning an array from the filter will effectively short-circuit the loading of optimization attributes, returning that value instead.

### wp_admin_notice_args
**Params:** array $args, string $message
**Since:** 6.4 | **Tags:** #Recent
Filters the arguments for an admin notice.

### wp_admin_notice_markup
**Params:** string $markup, string $message, array $args
**Since:** 6.4 | **Tags:** #Recent
Filters the markup for an admin notice.

### wp_authorize_application_redirect_url_invalid_protocols
**Params:** string[] $bad_protocols, string $url
**Since:** 6.4 | **Tags:** #Recent
Filters the list of invalid protocols used in applications redirect URLs.

### wp_get_loading_optimization_attributes
**Params:** array $loading_attrs, string $tag_name, array $attr, string $context
**Since:** 6.4 | **Tags:** #Recent
Filters the loading optimization attributes.

### wp_loading_optimization_force_header_contexts
**Params:** array $default_header_enforced_contexts
**Since:** 6.4 | **Tags:** #Recent
Filters the header-specific contexts.

### wp_post_revision_meta_keys
**Params:** array $keys, string $post_type
**Since:** 6.4 | **Tags:** #Recent
Filter the list of post meta keys to be revisioned.

### load_translation_file
**Params:** string $file, string $domain, string $locale
**Since:** 6.5 | **Tags:** #Recent
Filters the file path for loading translations for the given text domain. Similar to the {@see 'load_textdomain_mofile'} filter with the difference that the file path could be for an MO or PHP file.

### pre_get_language_files_from_path
**Params:** null|array $files, string $path
**Since:** 6.5 | **Tags:** #Recent
Filters the translation files retrieved from a specified path before the actual lookup. Returning a non-null value from the filter will effectively short-circuit the MO files lookup, returning that value instead. This can be useful in situations where the directory contains a large number of files and the default glob() function becomes expensive in terms of performance.

### script_module_loader_src
**Params:** string $src, string $id
**Since:** 6.5 | **Tags:** #Recent
Filters the script module source.

### translation_file_format
**Params:** string $preferred_format, string $domain
**Since:** 6.5 | **Tags:** #Recent
Filters the preferred file format for translation files. Can be used to disable the use of PHP files for translations.

### wp_admin_canonical_url
**Params:** string $filtered_url
**Since:** 6.5 | **Tags:** #Recent
Filters the admin canonical URL value.

### wp_plugin_dependencies_slug
**Params:** string $slug
**Since:** 6.5 | **Tags:** #Recent
Filters a plugin dependency's slug before matching to the WordPress.org slug format. Can be used to switch between free and premium plugin slugs, for example.

### lang_dir_for_domain
**Params:** string|false $path, string $domain, string $locale
**Since:** 6.6 | **Tags:** #Recent
Filters the determined languages directory path for a specific domain and locale.

### site_status_autoloaded_options_action_to_perform
**Since:** 6.6 | **Tags:** #Recent

### site_status_autoloaded_options_limit_description
**Since:** 6.6 | **Tags:** #Recent

### site_status_autoloaded_options_size_limit
**Params:** int $limit
**Since:** 6.6 | **Tags:** #Recent
Filters max bytes threshold to trigger warning in Site Health.

### wp_autoload_values_to_autoload
**Params:** string[] $autoload_values
**Since:** 6.6 | **Tags:** #Recent
Filters the autoload values that should be considered for autoloading from the options table. The filter can only be used to remove autoload values from the default list.

### wp_default_autoload_value
**Params:** bool|null $autoload, string $option, mixed $value, mixed $serialized_value
**Since:** 6.6 | **Tags:** #Recent
Allows to determine the default autoload value for an option where no explicit value is passed.

### wp_max_autoloaded_option_size
**Params:** int $max_option_size, string $option
**Since:** 6.6 | **Tags:** #Recent
Filters the maximum size of option value in bytes.

### wp_theme_files_cache_ttl
**Params:** int $cache_expiration, string $cache_type
**Since:** 6.6 | **Tags:** #Recent
Filters the cache expiration time for theme files.

### script_module_data_{$module_id}
**Since:** 6.7 | **Tags:** #Variable #Recent

### pre_count_many_users_posts
**Params:** string[]|null $count, int[] $users, string|string[] $post_type, bool $public_only
**Since:** 6.8 | **Tags:** #Recent
Filters whether to short-circuit performing the post counts. When filtering, return an array of posts counts as strings, keyed by the user ID.

### wp_allowed_block_metadata_collection_roots
**Params:** string[] $collection_roots
**Since:** 6.8 | **Tags:** #Recent
Filters the root directory paths for block metadata collections. Any block metadata collection that is registered must not use any of these paths, or any parent directory path of them. Most commonly, block metadata collections should reside within one of these paths, though in some scenarios they may also reside in entirely different directories (e.g. in case of symlinked plugins). Example: * It is allowed to register a collection with path `WP_PLUGIN_DIR . '/my-plugin'`. * It is not allowed to register a collection with path `WP_PLUGIN_DIR`. * It is not allowed to register a collection with path `dirname( WP_PLUGIN_DIR )`. The default list encompasses the `wp-includes` directory, as well as the root directories for plugins, must-use plugins, and themes. This filter can be used to expand the list, e.g. to custom directories that contain symlinked plugins, so that these root directories cannot be used themselves for a block metadata collection either.

### wp_hash_password_algorithm
**Params:** string $algorithm
**Since:** 6.8 | **Tags:** #Recent
Filters the hashing algorithm to use in the password_hash() and password_needs_rehash() functions. The default is the value of the `PASSWORD_BCRYPT` constant which means bcrypt is used. **Important:** The only password hashing algorithm that is guaranteed to be available across PHP installations is bcrypt. If you use any other algorithm you must make sure that it is available on the server. The `password_algos()` function can be used to check which hashing algorithms are available. The hashing options can be controlled via the {@see 'wp_hash_password_options'} filter. Other available constants include: - `PASSWORD_ARGON2I` - `PASSWORD_ARGON2ID` - `PASSWORD_DEFAULT`

### wp_hash_password_options
**Params:** array $options, string $algorithm
**Since:** 6.8 | **Tags:** #Recent
Filters the options passed to the password_hash() and password_needs_rehash() functions. The default hashing algorithm is bcrypt, but this can be changed via the {@see 'wp_hash_password_algorithm'} filter. You must ensure that the options are appropriate for the algorithm in use.

### wp_img_tag_add_auto_sizes
**Params:** boolean $enabled
**Since:** 6.8 | **Tags:** #Recent
Filters whether auto-sizes for lazy loaded images is enabled.

### wp_next_scheduled
**Params:** int $timestamp, object $next_event, string $hook, array $args
**Since:** 6.8 | **Tags:** #Recent
Filters the timestamp of the next scheduled event for the given hook.

### wp_prevent_unsupported_mime_type_uploads
**Params:** bool $check_mime, string|null $mime_type
**Since:** 6.8 | **Tags:** #Recent
Filter whether the server should prevent uploads for image types it doesn't support. Default true. Developers can use this filter to enable uploads of certain image types. By default image types that are not supported by the server are prevented from being uploaded.

### wp_speculation_rules_configuration
**Since:** 6.8 | **Tags:** #Recent
Filters the way that speculation rules are configured. The Speculation Rules API is a web API that allows to automatically prefetch or prerender certain URLs on the page, which can lead to near-instant page load times. This is also referred to as speculative loading. There are two aspects to the configuration: * The "mode" (whether to "prefetch" or "prerender" URLs). * The "eagerness" (whether to speculatively load URLs in an "eager", "moderate", or "conservative" way). By default, the speculation rules configuration is decided by WordPress Core ("auto"). This filter can be used to force a certain configuration, which could for instance load URLs more or less eagerly. For logged-in users or for sites that are not configured to use pretty permalinks, the default value is `null`, indicating that speculative loading is entirely disabled.

### wp_speculation_rules_href_exclude_paths
**Params:** string[] $href_exclude_paths, string $mode
**Since:** 6.8 | **Tags:** #Recent
Filters the paths for which speculative loading should be disabled. All paths should start in a forward slash, relative to the root document. The `*` can be used as a wildcard. If the WordPress site is in a subdirectory, the exclude paths will automatically be prefixed as necessary. Note that WordPress always excludes certain path patterns such as `/wp-login.php` and `/wp-admin/*`, and those cannot be modified using the filter.

### validate_plugin_requirements
**Params:** bool|WP_Error $met_requirements, string $plugin
**Since:** 6.9 | **Tags:** #Recent
Filters the plugin requirement validation response. If a plugin fails due to a Core-provided validation (incompatible WP, PHP versions), this filter will not fire. A WP_Error response will already be returned. This filter is intended to add additional validation steps by site administrators.

### validate_theme_requirements
**Params:** bool|WP_Error $met_requirements, string $stylesheet
**Since:** 6.9 | **Tags:** #Recent
Filters the theme requirement validation response. If a theme fails due to a Core-provided validation (incompatible WP, PHP versions), this filter will not fire. A WP_Error response will already be returned. This filter is intended to add additional validation steps by site administrators.

### wp_ajax_menu_quick_search_args
**Params:** array $args
**Since:** 6.9 | **Tags:** #Recent
Filter the menu quick search arguments.

### wp_mail_embed_args
**Params:** array $args
**Since:** 6.9 | **Tags:** #Recent
Filters the arguments for PHPMailer's addEmbeddedImage() method.

### wp_register_ability_args
**Params:** string $name
**Since:** 6.9 | **Tags:** #Recent
Filters the ability arguments before they are validated and used to instantiate the ability.

### wp_register_ability_category_args
**Params:** string $slug
**Since:** 6.9 | **Tags:** #Recent
Filters the ability category arguments before they are validated and used to instantiate the ability category.

### wp_should_output_buffer_template_for_enhancement
**Params:** bool $use_output_buffer
**Since:** 6.9 | **Tags:** #Recent
Filters whether the template should be output-buffered for enhancement. By default, an output buffer is only started if a {@see 'wp_template_enhancement_output_buffer'} filter has been added or if a plugin has added a {@see 'wp_finalized_template_enhancement_output_buffer'} action. For this default to apply, either of the hooks must be added by the time the template is included at the {@see 'wp_before_include_template'} action. This allows template responses to be streamed unless the there is code which depends on an output buffer being opened. This filter allows a site to opt in to adding such template enhancement filters later during the rendering of the template.

### wp_template_enhancement_output_buffer
**Params:** string $filtered_output, string $output
**Since:** 6.9 | **Tags:** #Recent
Filters the template enhancement output buffer prior to sending to the client. This filter only applies the HTML output of an included template. This filter is a progressive enhancement intended for applications such as optimizing markup to improve frontend page load performance. Sites must not depend on this filter applying since they may opt to stream the responses instead. Callbacks for this filter are highly discouraged from using regular expressions to do any kind of replacement on the output. Use the HTML API (either `WP_HTML_Tag_Processor` or `WP_HTML_Processor`), or else use {@see DOM\HtmlDocument} as of PHP 8.4 which fully supports HTML5. Do not print any output during this filter. While filters normally don't print anything, this is especially important since this applies during an output buffer callback. Prior to PHP 8.5, the output will be silently omitted, whereas afterward a deprecation notice will be emitted. Important: Because this filter is applied inside an output buffer callback (i.e. display handler), any callbacks added to the filter must not attempt to start their own output buffers. Otherwise, PHP will raise a fatal error: "Cannot use output buffering in output buffering display handlers."

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
